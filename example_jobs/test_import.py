import unittest
import glob
import os
import sys
import logging
from pip._vendor import pkg_resources

"""
This is the test for setup.
Caution! This test does not work in YTest
"""


def extract_ytest_path():
    ypath = ''
    ypath_list = \
        [p.location for p in pkg_resources.working_set if p.key in 'ytest']
    if ypath_list:
        ypath = ypath_list[0]
    return os.path.join(ypath)


def import_with_string(import_string):
    import_string = import_string[6:-3]
    try:
        __import__(import_string)
    except Exception as e:
        if hasattr(e, 'message'):
            return e.message
        else:
            return e
    else:
        return True


def extract_result(path):
    module_list = glob.glob('{}/{}'.format(self.ytest_path, path))
    result_list = []
    for module in module_list:
        module = module[self.ytest_index:].replace('/', '.')
        result_list.append((module, import_with_string(module)))
    false_result_list = []
    false_count = 0
    for result in result_list:
        if isinstance(result[1], str):
            false_count += 1
            false_result_list.append(result)
    return false_count, str(false_result_list).strip('[]').replace("), ",
                                                                   ")\n")


class SetupTest(unittest.TestCase):
    def setUp(self):
        self.ytest_path = '/root/ytest/YTest'
        # self.ytest_path = extract_ytest_path()
        self.ytest_index = self.ytest_path.find('YTest')
        sys.path.append(self.ytest_path)

    def test_top(self):
        top_path = '*.py'
        false_count, fail_log = extract_result(top_path)
        self.assertEqual(false_count, 0, '\n' + fail_log)

    def test_dut(self):
        dut_path = 'Dut/*.py'
        false_count, fail_log = extract_result(dut_path)
        self.assertEqual(false_count, 0, '\n' + fail_log)

    def test_testcase(self):
        testcase_path = 'TestCase/*.py'
        false_count, fail_log = extract_result(testcase_path)
        self.assertEqual(false_count, 0, '\n' + fail_log)

    def test_utiltiy(self):
        utility_path = 'utility/*.py'
        false_count, fail_log = extract_result(utility_path)
        self.assertEqual(false_count, 0, '\n' + fail_log)


if __name__ == '__main__':
    unittest.main(verbosity=2)