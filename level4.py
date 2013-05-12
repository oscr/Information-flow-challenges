import mechanize
import cookielib

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

########### Bruteforce attack against adjunct ##########

import itertools

variables = ['l1 = ','l2 = ','l3 = ', 'l4 = ', 'l5 = ', 'l6 = ']
values = ['true;', 'false;'] 

comb = list(itertools.product(values, repeat=6))

for c in comb:
	r = br.open('http://ifc-challenge.appspot.com/steps/adjunct')
	html = r.read()
	br.select_form(nr=0)
	pgm = "".join("%s%s" % tup for tup in zip(variables, c))
	br.form['program'] = pgm
	br.submit()
	rhtml = br.response().read()
	if "Congrats" in rhtml:
		print "Solution ", pgm
		break
	
