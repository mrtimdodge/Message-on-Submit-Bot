# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 13:52:01 2016

@author: DapperDodger
"""

app_id = 'DaSCqB8GeabEeQ'
app_secret = 'u08rM1bnKh9GNcg_RCb212sdqj8'
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_ua = 'This is a messaging service developed by /u/DapperDodger to be used by /u/JDmg'
app_scopes = 'privatemessages read'
app_account_code = 'cXO4HJKRr5CP1WWkjNvgv03Q6I4'
app_refresh = '54184954-sJYV9RpRGDnN3CGsVR2rqbQXT3A'

import praw
def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r