import requests
import sys
import colored

hostname = sys.argv[1]
response = requests.get(hostname)
response.headers

if "X-XSS-Protection" in response.headers:
        print("\033[1;32;49m")
        print "[+]	XSS header is present"
else:
        print("\033[1;31;49m")
        print "[-]	XSS header is not present"

if "x-frame-options" in response.headers:
        print("\033[1;32;49m")
        print "[+]	X-Frame header is present"
else:
        print("\033[1;31;49m")
        print "[-]	X-Frame header is not present"

if "x-content-type" in response.headers:
        print("\033[1;32;49m")
        print "[+]	X-Content-Type header is present"
else:
        print("\033[1;31;49m")
        print "[-]	C-Content-Type header is not present"

if "Public-Key-Pins" in response.headers:
        print("\033[1;32;49m")
        print "[+]	Public-Key-Pins is present"
else:
        print("\033[1;31;49m")
        print "[-]	Public-Key-Pins header is not present"

if "X-Content-Type-Options" in response.headers:
        print("\033[1;32;49m")
       	print "[+]	X-Content-Type-Options is present"
else:
        print("\033[1;31;49m")
        print "[-]	X-Content-Type-Options header is not present"

if "X-Permitted-Cross-Domain-Policies" in response.headers:
        print("\033[1;32;49m")
        print "[+]	X-Permitted-Cross-Domain-Policies is present"
else:
        print("\033[1;31;49m")
       	print "[-]	X-Permitted-Cross-Domain-Policies header is not present"

if "Content-Security-Policy" in response.headers:
        print("\033[1;32;49m")
        print "[+]	Referrer-Policy is present"
else:
        print("\033[1;31;49m")
        print "[-]	Referrer-Policy header is not present"

if "Content-Security-Policy" and "X-Content-Type-Options" not in response.headers:
	print ("\033[1;32;49m")
	print "[!] Site may be vulnerable to Clickjacking"
if "X-XSS-Protection" not in response.headers:
	print "[!] Check site with XSS payloads"
        print("\033[1;31;49m")

print ("\033[1;32;49m")
print ("Completed")
print ("\033[0;0m")
