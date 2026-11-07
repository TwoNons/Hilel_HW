import unittest
from lesson_13 import homework_13

class Test_Login_Event(unittest.TestCase):
    def test_login_success(self):
        with self.assertLogs('log_event', level='INFO') as logs:
            homework_13.log_event('Den', 'success')
        self.assertEqual(logs.output, ["INFO:log_event:Login event - Username: Den, Status: success"])

    def test_login_expired(self):
        with self.assertLogs('log_event', level='WARNING') as logs:
            homework_13.log_event('Den', 'expired')
        self.assertEqual(logs.output, ["WARNING:log_event:Login event - Username: Den, Status: expired"])

    def test_login_failed(self):
        with self.assertLogs('log_event', level='ERROR') as logs:
            homework_13.log_event('Den', 'failed')
        self.assertEqual(logs.output, ["ERROR:log_event:Login event - Username: Den, Status: failed"])

    def test_status_unknown(self):
        with self.assertLogs('log_event', level='ERROR') as logs:
            homework_13.log_event('Den', 'unknown')
        self.assertEqual(logs.output, ["ERROR:log_event:Login event - Username: Den, Status: unknown"])

if __name__ == '__main__': unittest.main()
