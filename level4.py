"""
I would like to thank: http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/

For the mechanize setup code.
"""

import mechanize
import cookielib

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

########### Brute force attack against adjunct ##########
import itertools

variables = ['l1 = ','l2 = ','l3 = ', 'l4 = ', 'l5 = ', 'l6 = ']
values = ['true;', 'false;'] 

br.open('http://ifc-challenge.appspot.com/steps/adjunct')
for comb in list(itertools.product(values, repeat=6)):
	br.select_form(nr=0)
	pgm = "".join("%s%s" % tup for tup in zip(variables, comb))
	br.form['program'] = pgm 
	br.submit()
	html = br.response().read()
	if "Congrats" in html:
		print "Solution program:\n%s" % pgm
		break