#!/usr/bin/python3
import twitter
import requests
import os
import time

'''
    Simple script that will post a QOD on Tweeter
'''

def qod():
    '''
        Quering api to get random quote
    '''
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    response = requests.get(url)
    quote = response.json()
    author = quote["author"]
    text = quote["quote"]

    # Constructing the message
    message = "{} -{}".format(text, author)
    # Checking if the message is longer than allowed or if it has unwanted char

    if len(message) > 140:
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
    print(message)
    #status = api.PostUpdate(message)



if __name__ == "__main__":
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

    MESSAGE = qod()

    api = auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    post_status(api, MESSAGE)
