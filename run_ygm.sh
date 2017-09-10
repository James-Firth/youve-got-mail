#!/bin/bash

# TODO make cronjob or something

working_dir=$(pwd -P)
parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
cd "$parent_path"

export DISPLAY=:0
my_command="source '$parent_path/ygm/bin/activate'; python '$parent_path/ygm.py'; sleep 10"


# CRONTAB EXAMPLE
# DISPLAY=:0.0
# XAUTHORITY=/home/james/.Xauthority
# * * * * * /home/james/projects/personal/ygm_youve_got_mail/ygm/bin/python /home/james/projects/personal/ygm_youve_got_mail/ygm.py > /tmp/cronlog.txt 2>&1
