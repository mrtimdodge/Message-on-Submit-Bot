# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:34:48 2016

@author: DapperDodger

Change test
"""
import praw
import obot_jdmg as obot
r = obot.login()
author_name = "DapperDodger"
subreddit_name = "test"
#keyword = "Hello World"
keyword = "[Interactive] Dark SOULS"
header = "Hello! " + author_name + " has made a new submission regarding " + keyword + " in /r/" +subreddit_name + " : \n\n"
footer = "\n\nI am a bot! If I'm acting up contact /u/DapperDodger"
def send_messages(s):
    with open('users.txt') as f:
        users = f.readlines()
    for user in users:
        r.send_message(user, s.author.name + " has made a new submission!", header + s.permalink +footer)
    
def check_condition(s):
    if s.author and s.author.name.lower() == author_name.lower() and keyword in s.title:
            send_messages(s)
        
for s in praw.helpers.submission_stream(r,subreddit_name, 1):
    print s.title
    check_condition(s)
