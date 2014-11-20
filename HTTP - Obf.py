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

# Create Request Handler
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# Name Your Server
Server = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"

# If the port is provided in the system argument, recognize it.
if sys.argv[1:]: port = int(sys.argv[1])
else: port = 8080

server_addr = ("0.0.0.0",port)

Handler.Protocol = Protocol
httpd = Server(server_addr,Handler)

s = httpd.socket.getsockname()

print "Serving HTTP on", s[0], "Port ", s[1], "..."
httpd.serve_forever()
