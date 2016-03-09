# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:34:48 2016

@author: DapperDodger

"""
import praw
import obot_duel as obot
import time

r = obot.login()

author_name = "DapperDodger"
subreddit_name = "mousehuntcss" #subreddit name
start_word = "lumos" #send started messages keyword
end_word = "nox" #send results messages keyword
bot_word = "duelingbot!" #keyword to call bot
poke_word = "poke" #keyword to be added to list
message_word = "results" #word that has to be the message header to post results
#keyword = "Hello World"
start_header = "POKE! A Trivia Game you wanted to know about has opened: \n\n" #This is the header for the starting message
results_header = "POKE! Trivia Game results you wanted to know about are up: \n\n" #This is the header for the results message
footer = "\n\nI am a bot! If I'm acting up contact /u/" + author_name #General footer

open_text = "#COMMENT HERE WITH KEYWORD '"+ poke_word + "' FOR A POKE WHEN QUIZ IS OPEN" #initial comment
results_text = "#COMMENT HERE WITH KEYWORD "+ poke_word + "  FOR A POKE WHEN FULL RESULTS ARE UP" #results comment

wait_time = 60 #time to wait between checking comments/messages in seconds



def comment_parse(s):
    print "Starting to read comments for keyword"
    finalResults = False
    already_done = set()
    while not finalResults:
        print "Reading comments..."
        s.refresh()
        flat_comments = praw.helpers.flatten_tree(s.comments)
        for comment in flat_comments:
            if comment.id not in already_done and comment.author and comment.author.name != "DuelingBot":
                finalResults = check_condition_comments(comment)
            already_done.add(comment.id)
        time.sleep(wait_time)
            
def send_start_messages(s):
    print "Sending game started messages"
    with open('users.txt') as f:
        users = f.readlines()
    for user in users:
        r.send_message(user, s.title + " has started!", start_header + s.permalink +footer)
    open('users.txt', 'w').close()
    
def send_result_messages(s):
    print "Sending results are up messages"
    with open('users.txt') as f:
        users = f.readlines()
    for user in users:
        r.send_message(user, s.title + " results!", results_header + "/r/" + subreddit_name +footer)
    open('users.txt', 'w').close()
    
def add_comment(s,text):
    print "Adding comment to post"
    s.add_comment(text)
    
def check_condition_open(s):
    print "Reading submissions..."
    #if s.title == "Game":    
    if s.link_flair_text and s.link_flair_text == "Game":
            add_comment(s,open_text)
            comment_parse(s)

def check_condition_comments(c):
    print "Checking comment for keywords"
    authorized = []
    with open('authorized.txt') as fin:
        authorized = fin.readlines()
    if start_word.lower() in c.body.lower() and bot_word.lower() in c.body.lower() and c.author.name in authorized:
            send_start_messages(c.submission)
            wait_for_message()
            return False
    elif poke_word.lower() in c.body.lower():
            f = open('users.txt','a')
            f.write(c.author.name + "\n")
            f.close()
            print "Added User: " + c.author.name 
            return False
            
    elif end_word.lower() in c.body.lower() and bot_word.lower() in c.body.lower() and c.author.name in authorized:
        send_result_messages(c.submission)
        return True
    else:
        return False
        
def wait_for_message():
    print "Starting to wait for results message"
    message_received = False
    with open('authorized.txt') as fin:
        authorized = fin.readlines()
    while not message_received:
        print "Waiting for results message..."
        mail = r.get_unread()
        if mail:
            for message in mail:
                if message.subject.lower() == message_word.lower() and message.author and message.author.name in authorized:
                    add_comment(s, message.body + "\n\n" + results_text)
                    message_received = True
                message.mark_as_read()
        time.sleep(wait_time)
if __name__=="__main__":
   open('users.txt', 'w').close()
   print "Starting to check submission flair for keyword"
           
   try:
       for s in praw.helpers.submission_stream(r,subreddit_name, 1):
           check_condition_open(s)
   except:
       print "ERROR PLEASE RESTART BOT"
        

