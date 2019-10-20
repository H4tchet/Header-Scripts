import requests
import sys
import colored

headers = sys.argv[1]
response = requests.get(headers)
response.headers

#print response.headers
print("\033[1;32;49m")
print "\n Verbose Headers:"

if "Server" in response.headers:
	print("\033[1;31;49m")
	print "Server:"
	print response.headers['Server']

if "X-Powered-By" in response.headers:
	print "X-Powered-By:"
	print response.headers['X-Powered-By']

if "X-AspNet-Version" in response.headers:
	print "X-AspNet-Version"
	print response.headers['X-AspNet-Version']

if "X-AspNetMvc-Version" in response.headers:
	print "X-AspNetMvc-Version"
	print response.headers['X-AspNetMvc-Version']
else:
	print("\033[1;32;49m")
	print "\n [*] Completed - Please enumerate more"
