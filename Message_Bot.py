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
start_word = "lumos"
end_word = "nox"
#keyword = "Hello World"
keyword = "[Interactive] Dark SOULS"
header = "Hello! " + author_name + " has made a new submission regarding " + keyword + " in /r/" +subreddit_name + " : \n\n"
footer = "\n\nI am a bot! If I'm acting up contact /u/" + author_name
open_text = "#COMMENT HERE FOR A POKE WHEN QUIZ IS OPEN"
def comment_parse():
    for c in praw.helpers.comment_stream(r,subreddit_name, 1):
        check_condition_start(c)     
def send_messages(s):
    with open('users.txt') as f:
        users = f.readlines()
    for user in users:
        r.send_message(user, s.title + " has started!", header + s.shortlink +footer)
def add_comment(s,text):
    s.add_comment(text)
def check_condition_open(s):
    if s.link_flair_text == "Game":
            add_comment(s,open_text)
            comment_parse()
def check_condition_start(c):
    if start_word.lower() in c.body:
            send_messages(c.submission)
            
        
for s in praw.helpers.submission_stream(r,subreddit_name, 1):
    check_condition_open(s)
