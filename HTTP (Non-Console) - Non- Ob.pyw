#!/usr/bin/env python

#---------------------------------------------------------------------#
# Project : Simple HTTP Server                                        #
# Script  : Base HTTP Server                                          #
# Author  : Mrinal Wahal                                              #
# Website : http://www.dynacrux.de.vu/                                #
#---------------------------------------------------------------------#

print "-"*60
print "Dyna HTTP Server"
print "-"*60

import SimpleHTTPServer, BaseHTTPServer, sys

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"

if sys.argv[1:]: port = int(sys.argv[1])
else: port = 8080

server_addr = ("0.0.0.0",port)

Handler.Protocol = Protocol
httpd = Server(server_addr,Handler)

s = httpd.socket.getsockname()

print "Serving HTTP on", s[0], "Port ", s[1], "..."
httpd.serve_forever()
