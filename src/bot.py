'''
scrapes all tweets having #rejigthesystem
'''
__author__ = 'ankit'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import cPickle
from nltk.tag import pos_tag

#consumer key, consumer secret, access token, access secret.
ckey="I7CLI6FuaP5rbTMwVtPoykPfQ"
csecret="5N50wezoVkIZTRXq2WSZFEF1Gm6cPHyOkjA9QxB4sBUASPXPZx"
atoken="740092965926768640-oynCxQYi6liDJ9RlMc61qiEs8NtOl8N"
asecret="ZeeVlbcfGqDZmzJigbIpTNGDYnionoHPhv32Gzw23NeU3"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


api = tweepy.API(auth)
dangerwords=cPickle.load(open('dangerwords.p', 'rb'))
#print str(dangerwords)
badwords=cPickle.load(open('badwords.p', 'rb'))
def ethical(tweet):
	spam=1
	for a in tweet.split():
		
		#print str(a)
		if a in badwords:
    			spam=0
    			break
    		if a in dangerwords:
    			spam=0
    			break
    	
    	tagged_sent = pos_tag(tweet.split())
    	print str(tagged_sent)
# [('Michael', 'NNP'), ('Jackson', 'NNP'), ('likes', 'VBZ'), ('to', 'TO'), ('eat', 'VB'), ('at', 'IN'), ('McDonalds', 'NNP')]
	#print str(spam)
	propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
	print propernouns
	if len(propernouns)>0:
		spam=0
	#print "spam= " +str(spam)
	return spam
#print ethical('Justin Bieber top discussions in India.')
	
for tweet in tweepy.Cursor(api.search,
                           q="#rejigthesystem",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    	try:
    		print tweet.text+"\n\nnewtweet:"
    	except UnicodeEncodeError:
		print ""   		
    	'''
    	if '@' not in tweet.text:
    		if ethical(tweet.text.lower()):
    			if "mumbai" in tweet.text:
    				print "oh yeeeeh"
    				#api.update_status('@CompaProject'+tweet.text)
    	'''
	#if "bribe" in tweet.text:
	#	api.update_status('@CompaProject'+'#rejigthesystem bribe was taken at x !')

