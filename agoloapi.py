from inspect import getmembers
import requests

api_key = ''
summary_length = 5

def summarize(url):
  payload = {
    'summary_length': summary_length,
    'articles': [{'url': url}]
  }

  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + api_key
  }

  r = requests.post('http://api.agolo.com/v0.1/summarize/', json=payload, headers=headers)
  response_json = r.json()

  comment = ''
  for sentence in response_json['summary'][0]['sentences']:
    comment += '* ' + sentence + "\n\n"

  comment += '*This is a summarized version of the article, checkout /r/agolo for more info*'

  return comment
