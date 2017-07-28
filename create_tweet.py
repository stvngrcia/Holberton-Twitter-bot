#!/usr/bin/python3
import twitter
import requests
import os

'''
    Simple script that will post a QOD on Tweeter
'''

def qod():
    '''
        Quering api to get random quote
    '''
    url = " http://quotesondesign.com/wp-json/posts?filter[orderby]=rand"
    response = requests.get(url)
    quote = response.json()

    author = quote[0]["title"]
    text = quote[0]["content"]
    # Removing p tags by removing first 3 and last 5 chars
    text = text[3:][:-5]

    # Constructing the message
    message = "{} -{}".format(text, author)
    # Checking if the message is longer than allowed or if it has unwanted char
    if len(message) > 140 or "&#" in message:
        qod()
    else:
        return (message)

def auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    '''
        Getting authorized to post in to twitter as user
    '''
    api = twitter.Api(consumer_key= CONSUMER_KEY,
                  consumer_secret= CONSUMER_SECRET,
                  access_token_key= ACCESS_TOKEN,
                  access_token_secret= ACCESS_TOKEN_SECRET)

    return (api)


def post_status(api, message):
    '''
        Posting message
    '''
    status = api.PostUpdate(message)



if __name__ == "__main__":
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

    MESSAGE = qod()

    api = auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    post_status(api, MESSAGE)
