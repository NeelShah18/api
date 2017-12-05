from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="sRfCM1D5RUetDCp3abBzQcS4P"
consumer_secret="z5uACcOznq0sV3rZmowzOe7oibwbRZijM5jWjBY0FQGBk2VhXA"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="765052127873945600-NcssTtt0FkyUcAICXdJQ79quypsONsD"
access_token_secret="ZkgPgWUfv7x0Zx6jrF4llZUjHqzGXd4ZABeXjDsiulMOK"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['trump','python','nips','google'])