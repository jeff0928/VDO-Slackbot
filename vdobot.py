#!/usr/bin/env python
import os
import sys
import logging
import logging.config
from slackbot import settings
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import datetime
from datetime import timedelta
import random

@listen_to('middle_finger', re.IGNORECASE)
def middle_finger(message):
    message.reply('https://i.imgur.com/Y4dD2Az.gif')

def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger(
        'requests.packages.urllib3.connectionpool').setLevel(logging.DEBUG)

    Bot().run()

if __name__ == "__main__":
    main()
