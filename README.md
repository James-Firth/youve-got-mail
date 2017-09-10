Example crontab:

```shell
DISPLAY=:0.0
XAUTHORITY=/$HOME/.Xauthority
*/5 * * * * /$HOME/path/to/ygm_youve_got_mail/ygm/bin/python /$USER/path/to/ygm_youve_got_mail/ygm.py > /tmp/cronlog.txt 2>&1
```

Replace with actual paths
