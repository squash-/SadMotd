#!/usr/bin/python

import twitter
import lsb_release
from random import randint

osID = lsb_release.get_distro_information()['ID']

if (osID == 'Ubuntu') or (osID == 'Debian'):
        f = open("/etc/motd.tail", 'w')
elif (osID == 'CentOS'):
        f = open("/etc/motd", 'w')

f.truncate()

c_key='<replace with consumer key>'
c_secret='<replace with consumer secret>'
axx_token='<replace with access token key>'
axx_secret='<replace with access token secret>'
 
twitter_user="sadserver"

t = twitter.Api(consumer_key=c_key,
		consumer_secret=c_secret,
		access_token_key=axx_token,
		access_token_secret=axx_secret)

rand_tweet = randint(0,99)

status=t.GetUserTimeline(screen_name=twitter_user, count=100)
latest_status = status[rand_tweet].text

f.write("SadServer Says: ")
f.write(latest_status)
f.write("\n")
f.write("\n")

f.close()
