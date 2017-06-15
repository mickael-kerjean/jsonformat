import unittest
from jsonformat import Runner


class Logs(unittest.TestCase):
    def test_fail2ban_short(self):
        runner = Runner('$date', '')
        res = runner.process('2017-06-15 03:51:02,043 fail2ban.filter         [1112]: INFO    [sshd] Found 103.207.39.83')
        self.assertEqual(res, {'date': '2017-06-15'})
        
    def test_fail2ban_long(self):
        runner = Runner('$date $hour _ _ _ _ _ $ip', '')
        res = runner.process('2017-06-15 03:51:02,043 fail2ban.filter         [1112]: INFO    [sshd] Found 103.207.39.83')
        self.assertEqual(res, {'date': '2017-06-15', 'hour': '03:51:02,043', 'ip': '103.207.39.83'})
    

def main():
    unittest.main()

if __name__ == "__main__":
    main()
