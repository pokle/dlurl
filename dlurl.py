#!/usr/bin/env python
#
# Helps you download files from a website that follow a numeric pattern.


import sys
import re

class UserError(Exception):
	pass

class URLDownloader:

	def __init__(self, url_pattern): 
		self.url_pattern = url_pattern

	# Converts the pattern "{01..20}" to the tuple ('01','20')
	def extract_range(self, s):
		range_pattern = re.compile('\{(\d+)\.\.(\d+)\}')
		range_match = range_pattern.search(s)
	
		if range_match == None:
			raise UserError("Couldn't find a numeric range in the URL. Examples: {1..20}, {001..020}")
		else:
			return (range_match.group(1), range_match.group(2))

 	# Determine the right padding format to be used with sprintf
	def determine_sprintf_pattern(self, r):
		(a,b) = r

		# Extract leading padding zeros from a
		leading_zeros_match = re.compile('^(0+)').match(a)
		if leading_zeros_match:
			return '%0' + str(len(a)) + 'd'
		else:
			return '%d' # No padding

	def build_url(self, url_pat, sprintf_pat, index):
		p = re.compile('\{[^\}]*\}')
		return p.sub(sprintf_pat % index, url_pat)

	def split_url(self, url):
		p = re.compile('^(.*/)([^/]*)$')
		m = p.search(url)
		if m:
			return (m.group(1), m.group(2))
		else:
			raise "Not a URL: " + url

	# Generates a list of commands that can be used to download the generated URLS
	def commands(self):
		
		r = self.extract_range(self.url_pattern)

		sprintf_pat = self.determine_sprintf_pattern(r)

		result = []
		for index in xrange(int(r[0]), int(r[1])+1):
			url = self.build_url(self.url_pattern, sprintf_pat, index)
			(url_base,url_file) = self.split_url(url)
			cmd = ("curl " + url_base + url_file + " > " + url_file)
			result.append(cmd)
			
		return result


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "arg len is", len(sys.argv)
		print "Helps you download files from a website that follow a numeric pattern"
		print "usage: " + sys.argv[0] + " http://host/filename-{01..10}.jpg | bash\n"
		sys.exit(1)

	try:
		dl = URLDownloader(sys.argv[1])
		for command in dl.commands():
			print command
	except UserError, e:
		print e.message
