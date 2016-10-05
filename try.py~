from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy

#consumer key, consumer secret, access token, access secret.
ckey="PlO8d5fGDyKPkA3GMOdImljTz"
csecret="u5944xZy9GPsg5A3OIySMjeSZ6qIFRkMbG9d9NcBpEjeovB07i"
atoken="1586345078-a1mPtaK8oL8VZRgN5mp0E1c9YxP2ro8mzg67yju"
asecret="9U1DB5Ic12T2Qx4RkeWrdenPuqi6Fo3LmdIiw2e1ASfTh"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)
api.update_status('#rejigthesystem bribe was taken at x !')
#twitterStream = Stream(auth, listener())
#twitterStream.filter(track=["car"])
		
