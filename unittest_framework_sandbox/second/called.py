import unittest
from unittest.case import SkipTest
import re
import sys


SETUPCOMMON = 0
SETUPTEST = 1
RUNTEST = 2
TEARDOWNTEST = 3
TEARDOWNCOMMON = 4
FINISH = -1


class ExceptionTest(unittest.TestCase):
    def run_startTestRun(self, result=None):
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

    def call_setUpCommon(self, result):
        if "setUpCommon" in dir(self):
            method = getattr(self, 'setUpCommon')
            try:
                method()
            except AssertionError:
                result.addFailure(self, sys.exc_info())
                self.stage = TEARDOWNCOMMON
                return False
            except:
                self.stage = TEARDOWNCOMMON
                return False
            else:
                self.stage = SETUPTEST
                return True
        return True

    def call_setUp_test(self, result):
        name = re.sub(r"test_", "setUp_", self._testMethodName)
        if name in dir(self):
            method = getattr(self, name)
            try:
                method()
            except AssertionError:
                result.addFailure(self, sys.exc_info())
                self.stage = TEARDOWNTEST
                return False
            except:
                self.stage = TEARDOWNTEST
                return False
            else:
                self.stage = RUNTEST
                return True
        return True

    def call_test(self, result, testMethod):
        try:
            testMethod()
        except KeyboardInterrupt:
            raise
        except self.failureException:
            result.addFailure(self, sys.exc_info())
            self.stage = TEARDOWNTEST
            return False
        # remove the ExpecedFailure and UnexpectSuccess
        except SkipTest as e:
            self._addSkip(result, str(e))
        except:
            result.addError(self, sys.exc_info())
            self.stage = TEARDOWNTEST
            return False
        else:
            self.stage = TEARDOWNTEST
            return True

    def call_tearDown_test(self, result):
        name = re.sub(r"test_", "tearDown_", self._testMethodName)
        if name in dir(self):
            method = getattr(self, name)
            try:
                method()
            except AssertionError:
                result.addFailure(self, sys.exc_info())
                self.stage = TEARDOWNCOMMON
                return False
            except:
                self.stage = TEARDOWNCOMMON
                return False
            else:
                self.stage = TEARDOWNCOMMON
                return True
        return True

    def call_tearDownCommon(self, result):
        if "tearDownCommon" in dir(self):
            method = getattr(self, 'tearDownCommon')
            try:
                method()
            except AssertionError:
                result.addFailure(self, sys.exc_info())
                self.stage = FINISH
                return False
            except:
                self.stage = FINISH
                return False
            else:
                self.stage = FINISH
                return True
        return True

    def run(self, result=None):
        orig_result = result
        self.run_startTestRun(result)
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
        success = False

        self.stage = 0
        stages = [(self.call_setUpCommon, (result,)),
                  (self.call_setUp_test, (result,)),
                  (self.call_test, (result, testMethod)),
                  (self.call_tearDown_test, (result,)),
                  (self.call_tearDownCommon, (result,))]
        try:
            while self.stage > -1:
                this_stage = stages[self.stage]
                success = this_stage[0](*this_stage[1])
        except:
            result.addError(self, sys.exc_info())
            success = False

        finally:
            cleanUpSuccess = self.doCleanups()
            success = success and cleanUpSuccess
            if success:
                result.addSuccess(self)

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
    tcs = ["called.Test00{}".format(i) for i in range(1, 8)]
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromNames(tcs))
    return suite

if __name__=="__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())