# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 13:52:01 2016

@author: DapperDodger
"""

app_id = 'A3Hv1xtB84ftkw'
app_secret = 'FauAU3Mwx7HkvBQJy0bTL13uqMQ'
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_ua = 'This is a messaging service developed by /u/DapperDodger to be used by /r/Dueling'
app_scopes = 'privatemessages read submit'
app_account_code = 'F8YCvX8n5XnZYv-w0hIm9ikTPIg'
app_refresh = '54198900-1vKau5EGCZaVajBkRjrwwbHtszI'

import praw
def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r# -*- coding: utf-8 -*-

