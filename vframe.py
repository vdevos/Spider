#!/usr/bin/env python

import sys, os, urllib2

def geturl(url, data=None, headers=None, cookiejar=None, maxtries=2):
    """Try to fetch the URL 'url' (default = 'GET')
       If data is set, POST the URL with the data
       Optionally, a CookieJar can be used if supplied"""

    if not headers:
        headers = {}
    if 'User-Agent' not in headers:
        headers[ 'User-Agent' ] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

    req = urllib2.Request(url, data, headers=headers)

    # try to open the webservice
    while maxtries > 0:
        maxtries -= 1
        try:
            ufp = urllib2.urlopen(req)
        except Exception, inst:
            sys.stderr.write("There was an exception trying to open url %s\nError: %s\n" % (url, inst))
        else:
            break
        if maxtries > 0:
            sys.stderr.write("Sleeping for 30 seconds\n")
            time.sleep(30)
    else:
        # hopeless
        sys.stderr.write("Giving up\n")
        return None

    return ufp

def dialog(message, defaultYes=True):
    sys.stderr.write("%s" % message)
    if defaultYes:
        sys.stderr.write(" [Y/n] ")
    else:
        sys.stderr.write(" [y/N] ")
    confirmation = sys.stdin.readline().strip().lower()
    if confirmation == "" or confirmation == "y" or confirmation == "yes":
        return True
    else:
        return False

