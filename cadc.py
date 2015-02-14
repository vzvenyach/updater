#!/usr/bin/env python

import requests
from lxml import html
import datetime
import os

url = "http://www.cadc.uscourts.gov/internet/opinions.nsf/OpinionsShowDate?OpenAgent&scode=0"
r = requests.get(url)
d = html.fromstring(r.text)
content = d.get_element_by_id("ViewBody")

if content.text_content() == "No documents found":
	print "No updates as of " + str(datetime.datetime.now())
else:
	payload = {
		"token":os.environ.get("PUSHOVER_TOKEN"),
		"user":os.environ.get("PUSHOVER_USER",
		"message":"New Opinions!",
		"url": url
	}
	requests.post("https://api.pushover.net/1/messages.json",data=payload)
	print "new contents"