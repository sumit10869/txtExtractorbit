#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6623083455:AAGjPOWeR5H3qo7_zqz-oHjiu-MnG-x8pmI")
    API_ID = int(os.environ.get("API_ID", "22439323"))
    API_HASH = os.environ.get("API_HASH", "e0e203c8be2c2c58b04d0c59fc82f507")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6090912349")
