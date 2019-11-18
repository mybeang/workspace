import unittest

loader = unittest.TestLoader()
tc = loader.loadTestsFromName("evt_db_comm.test.TestBase.test_test001")
suite = unittest.TestSuite()
suite.addTests(tc)
runner = unittest.TextTestRunner()
runner.run(suite)