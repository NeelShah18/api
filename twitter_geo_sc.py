from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import logging as lg
import pymongo
import json

#logging server settings
lg.basicConfig(filename="twiiter_debug_log.log",level=lg.DEBUG)
#MonogDB client connection
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client.twitter

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="3MdQmqPrl83wjW25FluO37n7M"
consumer_secret=" KVmroiqHLBstq0AXEaR8Chwn3RYQ6swsNwDx9WYEws0PPbTy4Y"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="938140566130515974-3YXKcivJ8Vnwr0LKAUmVtYFDK2tpufS"
access_token_secret="1EZFJZkYxcTIQGMLVC3m1Ruft9FGF5TsTpqxHkpSoKDvh"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        get_data = json.loads(data)
        lg.debug("get a tweet")
        writemongo(get_data)
        return True

    def on_error(self, status):
        lg.debug("Error from twitter: "+str(status))
        print("Twitter Error!")

def writemongo(pass_data):
    try:
        db.set7.insert(pass_data)
        lg.info("Tweet inserted to database")
    except:
        lg.info("Error while MonogDB insertion")
        print("Program End- Bcz mongoDB error!")
        exit()


if __name__ == '__main__':
    print("Program started")
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    #word_string="bacon-beef-chicken-cooked-meat-duck-ham-kidneys-lamb-liver-mince-minced-pate-salami-sausages-pork-pork-pie-sausage-roll-turkey-veal-butter-cream-cheese-blue-cottage-goats-creme-fraiche-eggs-free-range-eggs-margarine-milk-full-fat-milk-semi-skimmed-milk-skimmed-milk-sour-cream-yoghurt-apple-apricot-banana-blackberry-blackcurrant-blueberry-cherry-coconut-fig-gooseberry-grape-grape-fruit-kiwi-lemon-lime-mango-melon-orange-peach-pear-pineapple-plum-pomegranate-raspberry-redcurrant-rhubarb-strawberry-bunch-bananas-bunch-grapes-grap-baguette-bread-rolls-brown-white-garlic-pitta-loaf-bread-sliced-cake-Danish-pastry-quiche-sponge-baking-powder-plain-flour-self-raising-cornflour-sugar-brown-icing-pastry-yeast-dried-apricots-prunes-dates-raisins-sultanas-anchovy-cod-haddock-herring-kipper-smoked-fish-usually-herring-mackerel-pilchard-plaice-salmon-sardine-smoked-salmon-sole-trout-tuna-artichoke-asparagus-aubergine-avocado-beansprouts-beetroot-broad-beans-broccoli-Brussels-sprouts-cabbage-carrot-cauliflower-celery-chilli-pepper-courgette-cucumber-French beans-garlic-ginger-leek-lettuce-mushroom-onion-peas-pepper-potato-potatoes-pumpkin-radish-rocket-runner-beans-swede-sweet-potato-sweetcorn-tomato-tomatoes-turnip-spinach-spring-onion-squash-clove-garlic-stick-celery-baked-beans-corned-beef-kidney-beans-soup-tinned-tomatoes-chips-fish-fingers-frozen-peas-frozen-pizza-ice-cream-cooking-oil-olive-stock-cubes-tomato-puree-breakfast-cereal-cornflakes-honey-jam-marmalade-muesli-porridge-toast-noodles-pasta-sauce-pizza-rice-spaghetti-ketchup-mayonnaise-mustard-pepper-salad-dressing-salt-vinaigrette-vinegar-biscuits-chocolate-crisps-hummus-nuts-olives-peanuts-sweets-walnuts-basil-chives-coriander-dill-parsley-rosemary-sage-thyme-chilli-powder-cinnamon-cumin-curry-nutmeg-paprika-saffron-organic-ready-meal-bar-bottle-milk-bear-wine-wisky-takila-shot-alcohol-pepsi-cocola-soda-juce-fruits-vegetables-fruite-veggi-veg-vegetable-rum-carton-eggs-carbohydrate-chanterelle-chow-comestibles-comfort-food-concoction-convenience-food-cordon-bleu-delicacy-diabetic-dietary-fibre-doggy-bag-dry-goods-eats-fare-fast-food-fayre-fibre-food-foodstuff-fruit-fruits-greengrocer-grocer-grocery-grub-health-food-junk-food-morel-morsel-mouthful-munch-non-dairy-nosh-superfood-taste-tidbit-titbit-tuck-tucker-victuals-whole-teasty-yummy-yum-yummm-love-it-loved-fabulous"
    word_string = "watching-tv-movie-runing-dancing-eating-skiing-hiking-running-siting-sitting-laying-walking-treadmill-gym-meditation-yoga-martial-boxing-jumppig-eating"
    stream = Stream(auth, l)
    stream.filter(track=word_string.split("-"))