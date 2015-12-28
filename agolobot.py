from inspect import getmembers
from pprint import pprint

import time
import praw

import agoloapi

r = praw.Reddit('Agolo Reddit bot')
r.login(disable_warning=True);

searchWords = ['!tldr', '!tl;dr']
subreddits = ['worldnews', 'android', 'finance', 'nyc']

def is_already_done(comment):
  done = False
  repliesarray = praw.helpers.flatten_tree(comment.submission.comments)
  for repl in repliesarray:
    if repl.author != None and (repl.author.name == 'agolo_bot'):
      #print("%s already done"%comment.id)
      done = True
      continue
  return done

while True:
    try:
      for subreddit_name in subreddits:
        subreddit = r.get_subreddit(subreddit_name)
        for comment in subreddit.get_comments():
            text = comment.body.lower()
            has_word = any(string in text for string in searchWords)

            if has_word and not is_already_done(comment):
              print("replying to %s"%comment.id)
              try:
                comment_reply_text = agoloapi.summarize(comment.submission.url)
                #print(comment_reply_text)
                comment.reply(comment_reply_text)
              except:
                pass
    except:
      pass
    time.sleep(60)
