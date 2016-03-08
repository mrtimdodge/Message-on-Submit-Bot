# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:34:48 2016

@author: DapperDodger

Change test
"""
import praw
import obot_duel as obot
import time

r = obot.login()
author_name = "DapperDodger"
subreddit_name = "mousehuntcss"
start_word = "lumos"
end_word = "nox"
bot_word = "duelingbot!"
poke_word = "poke"
#keyword = "Hello World"
start_header = "Hello! A Trivia Game you wanted to know about has opened: \n\n"
results_header = "Hello! Trivia Game results you wanted to know about are up: \n\n"

footer = "\n\nI am a bot! If I'm acting up contact /u/" + author_name
open_text = "#COMMENT HERE FOR A POKE WHEN QUIZ IS OPEN"



def comment_parse(s):
    notStop = True
    already_done = set()
    while notStop:
        s.refresh()
        flat_comments = praw.helpers.flatten_tree(s.comments)
        for comment in flat_comments:
            if comment.id not in already_done:
                notStop = check_condition_comments(comment)
            already_done.add(comment.id)
        time.sleep(20)
            
def send_start_messages(s):
    with open('users.txt') as f:
        users = f.readlines()
    for user in users:
        r.send_message(user, s.title + " has started!", start_header + s.shortlink +footer)
    open('users.txt', 'w').close()
    
def send_result_messages(s):
    with open('users.txt') as f:
        users = f.readlines()
    for user in users:
        r.send_message(user, s.title + " results!", results_header + s.shortlink +footer)
    open('users.txt', 'w').close()
    
def add_comment(s,text):
    s.add_comment(text)
    
def check_condition_open(s):
    if s.title == "Game":    
    #if s.link_flair_text == "Game":
            add_comment(s,open_text)
            comment_parse(s)

def check_condition_comments(c):
    authorized = []
    with open('authorized.txt') as fin:
        authorized = fin.readlines()
    if start_word.lower() in c.body.lower() and bot_word.lower() in c.body.lower() and c.author in authorized:
            send_start_messages(c.submission)
            return True
    elif poke_word.lower() in c.body.lower():
        if c.author:
            f = open('users.txt','a')
            f.write(c.author.name + "\n")
            f.close()
            return True
    elif end_word.lower() in c.body.lower() and bot_word.lower() in c.body.lower() and c.author in authorized:
        send_result_messages(c.submission)
        return False
    else:
        return True
    
if __name__=="__main__":
   for s in praw.helpers.submission_stream(r,subreddit_name, 1):
        check_condition_open(s)
        

