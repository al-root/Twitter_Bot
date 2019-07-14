# themodelbot

import tweepy as tp
import time
import os


# credentials to login to twitter api
consumer_key = 'mco6jxmRJOQpy50uKSEoAIMu3'
consumer_secret = 'VlbDvZreHLdICm8zSfxCYivGaxqGdtjKv4mgxLVid1d6BppKN1'
access_token = '953746935386726401-fr6NrOeCondBjpzQDZBoTRd6kcVPWF5'
access_secret = 'MqV3HusuyiBQp8WspT2KIURnVzEQsxNEGZK6CLOjcyU2c'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('coolWallpapers')

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(60)
