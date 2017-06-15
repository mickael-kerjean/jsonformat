json format is a small bash utility that can be use to format text in json.

Example with fail2ban:
```
2017-06-15 03:51:02,043 fail2ban.filter         [1112]: INFO    [sshd] Found 103.207.39.83
2017-06-15 03:51:02,335 fail2ban.filter         [1112]: INFO    [sshd] Found 103.207.39.83
2017-06-15 03:51:04,417 fail2ban.filter         [1112]: INFO    [sshd] Found 103.207.39.83
2017-06-15 03:51:15,780 fail2ban.filter         [1112]: INFO    [sshd] Found 103.207.39.83
2017-06-15 03:51:16,118 fail2ban.filter         [1112]: INFO    [sshd] Found 103.207.39.83
2017-06-15 03:51:17,021 fail2ban.actions        [1112]: NOTICE  [sshd] Ban 103.207.39.83
2017-06-15 03:51:18,456 fail2ban.filter         [1112]: INFO    [sshd] Found 103.207.39.83
2017-06-15 03:56:02,100 fail2ban.filter         [1112]: INFO    [sshd] Found 59.61.73.197
2017-06-15 03:56:04,356 fail2ban.filter         [1112]: INFO    [sshd] Found 59.61.73.197
2017-06-15 04:01:17,955 fail2ban.actions        [1112]: NOTICE  [sshd] Unban 103.207.39.83
```

```
cat /var/log/fail2band.log | jsonformat --schema '$date $hour _ _ $level _ _ $ip'
```
will give:
```
{"date": "2017-06-15", "ip": "103.207.39.83", "hour": "03:51:02,043", "level": "INFO"}
{"date": "2017-06-15", "ip": "103.207.39.83", "hour": "03:51:02,335", "level": "INFO"}
{"date": "2017-06-15", "ip": "103.207.39.83", "hour": "03:51:04,417", "level": "INFO"}
{"date": "2017-06-15", "ip": "103.207.39.83", "hour": "03:51:15,780", "level": "INFO"}
{"date": "2017-06-15", "ip": "103.207.39.83", "hour": "03:51:16,118", "level": "INFO"}
{"date": "2017-06-15", "ip": "103.207.39.83", "hour": "03:51:17,021", "level": "NOTICE"}
{"date": "2017-06-15", "ip": "103.207.39.83", "hour": "03:51:18,456", "level": "INFO"}
{"date": "2017-06-15", "ip": "59.61.73.197", "hour": "03:56:02,100", "level": "INFO"}
{"date": "2017-06-15", "ip": "59.61.73.197", "hour": "03:56:04,356", "level": "INFO"}
{"date": "2017-06-15", "ip": "103.207.39.83", "hour": "04:01:17,955", "level": "NOTICE"}
```    
