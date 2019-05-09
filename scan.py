import socket
import colored

ip_input = raw_input('IP or HOSTNAME:')
port_input = int(raw_input('PORT:'))


s = socket.socket()
s.connect((ip_input,port_input))
s.send(b'GET /\n\n')
result = s.recv(1024)

#print result

print "Results"
if "X-XSS-Protection" in result:
        print("\033[1;32;49m")
        print "         XSS header is present"
else:
        print("\033[1;31;49m")
        print "         XSS header is not present"

if "x-frame-options" in result:
        print("\033[1;32;49m")
        print "         X-Frame header is present"
else:
        print("\033[1;31;49m")
        print "         X-Frame header is not present"

if "x-content-type" in result:
        print("\033[1;32;49m")
        print "         X-Content-Type header is present"
else:
        print("\033[1;31;49m")
        print "         C-Content-Type header is not present"

if "Public-Key-Pins" in result:
        print("\033[1;32;49m")
        print "         Public-Key-Pins is present"
else:
        print("\033[1;31;49m")
        print "         Public-Key-Pins header is not present"

if "X-Content-Type-Options" in result:
        print("\033[1;32;49m")
        print "         X-Content-Type-Options is present"
else:
        print("\033[1;31;49m")
        print "         X-Content-Type-Options header is not present"

if "X-Permitted-Cross-Domain-Policies" in result:
        print("\033[1;32;49m")
        print "         X-Permitted-Cross-Domain-Policies is present"
else:
        print("\033[1;31;49m")
        print "         X-Permitted-Cross-Domain-Policies header is not present"

if "Content-Security-Policy" in result:
        print("\033[1;32;49m")
        print "         Referrer-Policy is present"
else:
        print("\033[1;31;49m")
        print "         Referrer-Policy header is not present"
        

