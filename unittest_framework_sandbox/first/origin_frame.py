import unittest
from unittest.case import SkipTest
import re
import sys


class ExceptionTest(unittest.TestCase):
    def _call_setUpCommon(self):
        if "setUpCommon" in dir(self):
            method = getattr(self, 'setUpCommon')
            try:
                method()
            except AssertionError as e:
                return "FAIL", e
            else:
                return "OK", ""
        else:
            return "OK", ""

    def _call_setUp_test(self):
        name = re.sub(r"test_", "setUp_", self._testMethodName)
        if name in dir(self):
            method = getattr(self, name)
            try:
                method()
            except AssertionError as e:
                return "FAIL", e
            else:
                return "OK", ""
        else:
            return "OK", ""

    def setUp(self, result):
        self.setUp_test_common = True
        c_res, c_res_logs = self._call_setUpCommon()
        if c_res == "OK":
            t_res, t_res_logs = self._call_setUp_test()
            if t_res == "FAIL":
                print("SetUp_{}: [{}] - {}".format(re.sub(r"test_", "setUp_", self._testMethodName),
                                                   t_res, t_res_logs))
                result.addFailure(self, sys.exc_info())
                raise AssertionError(t_res_logs)
        else:
            print("SetUpCommon: [{}] - {}".format(c_res, c_res_logs))
            self.setUp_test_common = False
            raise IOError(c_res_logs)

    def _call_tearDownCommon(self):
        if "tearDownCommon" in dir(self):
            method = getattr(self, 'tearDownCommon')
            try:
                method()
            except AssertionError as e:
                return "FAIL", e
            else:
                return "OK", ""
        else:
            return "OK", ""

    def _call_tearDown_test(self):
        name = re.sub(r"test_", "tearDown_", self._testMethodName)
        if name in dir(self):
            method = getattr(self, name)
            try:
                method()
            except AssertionError as e:
                return "FAIL", e
            else:
                return "OK", ""
        else:
            return "OK", ""

    def tearDown(self, result):
        if hasattr(self, 'setUp_test_common') and self.setUp_test_common:
            t_res, t_res_logs = self._call_tearDown_test()
            if t_res == "FAIL":
                print("TearDown_{}: [{}] - {}".format(re.sub(r"test_", "tearDown_", self._testMethodName),
                                                  t_res, t_res_logs))
                result.addFailure(self, sys.exc_info())
        c_res, c_res_logs = self._call_tearDownCommon()
        if c_res == "FAIL":
            print("TearDownCommon: [{}] - {}".format(c_res, c_res_logs))
            raise IOError(c_res_logs)
        if t_res == "FAIL":
            raise AssertionError(t_res_logs)

    def run(self, result=None):
        orig_result = result
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

        self._resultForDoCleanups = result
        result.startTest(self)

        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or
            getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, skip_why)
            finally:
                result.stopTest(self)
            return
        try:
            success = False
            try:
                self.setUp(result) # add arguments for add result 'fail' on setup_test
            except SkipTest as e:
                self._addSkip(result, str(e))
            except AssertionError: # for not add the result 'error'
                pass
            except KeyboardInterrupt:
                raise
            except:
                result.addError(self, sys.exc_info())
                self.setUp_test_common = False # for skip teardown test
            else:
                try:
                    testMethod()
                except KeyboardInterrupt:
                    raise
                except self.failureException:
                    result.addFailure(self, sys.exc_info())
                # remove the ExpecedFailure and UnexpectSuccess
                except SkipTest as e:
                    self._addSkip(result, str(e))
                except:
                    result.addError(self, sys.exc_info())
                else:
                    success = True
            finally: # add finally
                try:
                    self.tearDown(result) # add arguments for add result 'fail' on teardown_test
                except KeyboardInterrupt:
                    raise
                except AssertionError: # for not add the result 'ok'
                    success = False
                except:
                    result.addError(self, sys.exc_info())
                    success = False

            cleanUpSuccess = self.doCleanups()
            success = success and cleanUpSuccess
            if success:
                result.addSuccess(self)
        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()
            print("\n\n")

class Test001(ExceptionTest):
    """
    NORMAL
    """
    def setUpCommon(self):
        print("")
        print("SETUPCOMMON_Test001")

    def setUp_001(self):
        print("SETUP_001")

    def test_001(self):
        print("TEST_001")

    def tearDown_001(self):
        print("TEARDOWN_001")

    def setUp_002(self):
        print("SETUP_002")

    def test_002(self):
        print("TEST_002")

    def tearDown_002(self):
        print("TEARDOWN_002")

    def tearDownCommon(self):
        print("TEARDOWNCOMMON_Test001")


class Test002(ExceptionTest):
    """
    FAIL SETUPCOMMON
    """
    def setUpCommon(self):
        print("")
        print("SETUPCOMMON_Test002")
        raise AssertionError("FAIL This")

    def setUp_001(self):
        print("SETUP_001")

    def test_001(self):
        print("TEST_001")

    def tearDown_001(self):
        print("TEARDOWN_001")

    def setUp_002(self):
        print("SETUP_002")

    def test_002(self):
        print("TEST_002")

    def tearDown_002(self):
        print("TEARDOWN_002")

    def tearDownCommon(self):
        print("TEARDOWNCOMMON_Test002")


class Test003(ExceptionTest):
    """
    FAIL EACH STAGE WITHOUT COMMON
    """
    def setUpCommon(self):
        print("")
        print("SETUPCOMMON_Test003")

    def setUp_001(self):
        print("SETUP_001")
        raise AssertionError("FAIL This")

    def test_001(self):
        print("TEST_001")

    def tearDown_001(self):
        print("TEARDOWN_001")

    def setUp_002(self):
        print("SETUP_002")

    def test_002(self):
        print("TEST_002")
        raise AssertionError("FAIL This")

    def tearDown_002(self):
        print("TEARDOWN_002")

    def setUp_003(self):
        print("SETUP_003")

    def test_003(self):
        print("TEST_003")

    def tearDown_003(self):
        print("TEARDOWN_003")
        raise AssertionError("FAIL This")

    def tearDownCommon(self):
        print("TEARDOWNCOMMON_Test003")


class Test004(ExceptionTest):
    """
    FAIL TEARDOWNCOMMON
    """
    def setUpCommon(self):
        print("")
        print("SETUPCOMMON_Test004")

    def setUp_001(self):
        print("SETUP_001")

    def test_001(self):
        print("TEST_001")

    def tearDown_001(self):
        print("TEARDOWN_001")

    def tearDownCommon(self):
        print("TEARDOWNCOMMON_Test004")
        raise AssertionError("Fail This")


class Test005(ExceptionTest):
    """
    ERROR SETUPCOMMON
    """
    def setUpCommon(self):
        print("")
        print("SETUPCOMMON_Test005")
        raise IOError("ERROR This")

    def setUp_001(self):
        print("SETUP_001")

    def test_001(self):
        print("TEST_001")

    def tearDown_001(self):
        print("TEARDOWN_001")

    def setUp_002(self):
        print("SETUP_002")

    def test_002(self):
        print("TEST_002")

    def tearDown_002(self):
        print("TEARDOWN_002")

    def tearDownCommon(self):
        print("TEARDOWNCOMMON_Test005")


class Test006(ExceptionTest):
    """
    ERROR EACH STAGE WITHOUT COMMON
    """
    def setUpCommon(self):
        print("")
        print("SETUPCOMMON_Test006")

    def setUp_001(self):
        print("SETUP_001")
        raise IOError("ERROR This")

    def test_001(self):
        print("TEST_001")

    def tearDown_001(self):
        print("TEARDOWN_001")

    def setUp_002(self):
        print("SETUP_002")

    def test_002(self):
        print("TEST_002")
        raise IOError("ERROR This")

    def tearDown_002(self):
        print("TEARDOWN_002")

    def setUp_003(self):
        print("SETUP_003")

    def test_003(self):
        print("TEST_003")

    def tearDown_003(self):
        print("TEARDOWN_003")
        raise IOError("ERROR This")

    def tearDownCommon(self):
        print("TEARDOWNCOMMON_Test006")


class Test007(ExceptionTest):
    """
    ERROR TEARDOWNCOMMON
    """
    def setUpCommon(self):
        print("")
        print("SETUPCOMMON_Test007")

    def setUp_001(self):
        print("SETUP_001")

    def test_001(self):
        print("TEST_001")

    def tearDown_001(self):
        print("TEARDOWN_001")

    def tearDownCommon(self):
        print("TEARDOWNCOMMON_Test007")
        raise IOError("ERROR This")


def suite():
    tcs = ["origin_frame.Test00{}".format(i) for i in range(1, 8)]
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromNames(tcs))
    return suite

if __name__=="__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())