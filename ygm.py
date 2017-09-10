#!/bin/python
# TODO Make shebang better for venv
from O365 import *
import json
import os
import sys
import time
import logging
import subprocess
logging.basicConfig(filename='ff.log',level=logging.DEBUG)

log = logging.getLogger('ff')

# CONFIGS
e = 'EMAIL_ADDRESS'
p = 'EMAIL_PASSWORD' # TODO read from file
notify_icon_local = 'mail-unread' #preferrably 32x32


# TODO
# * Add better notification styling
# * Add Slack PM support
def notify(title, body):
    subprocess.Popen(['/usr/bin/notify-send', title, body, '-i', notify_icon_local])
    return

def format_notify_send(message):
    string = ""
    return

print "checking for emails"


auth = (e,p)

i = Inbox( auth, getNow=False) #Email, Password, Delay fetching so I can change the filters.

i.setFilter("IsRead eq false")

i.getMessages()

log.debug("messages: {0}".format(len(i.messages)))

msg_links = []

ygm_list_path = os.path.join('/', 'tmp', 'ygmlist')
if os.path.exists(ygm_list_path):
    with open(ygm_list_path, 'r') as f:
        for line in f:
            msg_links.append(line)

new_msg_counter = 0
if len(i.messages) > 0:
    msg_body = "From:"
    # TODO Cache and compare hashes or timestamps
    for m in i.messages:
        if m.json['WebLink'] not in msg_links:
            new_msg_counter += 1
            msg_body = msg_body + m.json['From']['EmailAddress']['Name'] + "\n"
            with open(ygm_list_path, 'w+') as f:
                f.write(m.json['WebLink'])

            # print(m.json['Subject'])
            # print(m.json['From']['EmailAddress']['Name'])
            # print(m.json['From']['EmailAddress']['Address'])
            # print(m.json['BodyPreview'])
    if new_msg_counter > 0:
        msg_title = "{0} new email(s)".format(new_msg_counter)
        notify(msg_title, msg_body)
    else:
        print("no new messages")
        log.debug("no new messages")
else:
    print("no new messages")
    log.debug("no new messages")
