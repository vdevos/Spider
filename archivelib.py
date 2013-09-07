#!/usr/bin/env python

import sys, os, time, base64, urllib2, json
from urlparse import urlparse

MAJOR = 1
MINOR = 0
PATCH = 0
VERSION = "%s.%s.%s" % (MAJOR, MINOR, PATCH) 

ARCHIVE_PATH = "/home/vdevos/archive"

def url2safestring(url):
    return base64.urlsafe_b64encode(url)    

# Write a URL with HTML to the archive
# Gets stored as document: archive/<domain.com>/b64encoded(url).html
def writetoarchive(url, html):
    
    urlhash = url2safestring(url)
    domain = urlparse(url).netloc
    archpath = "%s/%s" % (ARCHIVE_PATH, domain)
    archfile = "%s/%s.html" % (archpath, urlhash)
    timestamp = str(int(time.time()))

    document = {
        'url' : url,
        'spiderdate' : timestamp,
        'body' : html,
        'spider-version' : VERSION,
    }
    
    documentstr = json.dumps(document)    

    try:
        if not os.path.exists(archpath):
            os.makedirs(archpath)
        fp = open(archfile,"w")
        try:
            fp.writelines(documentstr)
        finally:
            fp.close()
            return document
    except IOError:
        return False

def getfromarchive(url):
    urlhash = url2safestring(url)
    domain = urlparse(url).netloc
    archpath = "%s/%s" % (ARCHIVE_PATH, domain)
    archfile = "%s/%s.html" % (archpath, urlhash)

    try:
        fp = open(archfile,"r")
        try:
            documentstr = fp.read()
            document = json.loads(documentstr)
            return document
        finally:
            fp.close()
    except IOError:
        return None

