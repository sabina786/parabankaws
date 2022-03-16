import unittest
import parabank_app as pb


class ParabankPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_register_account():
        pb.setUp()
        pb.register()
        pb.logout()
        pb.login()
        pb.logout()
        pb.tearDown()