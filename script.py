#!/usr/bin/env python3
"""
License: MIT License
Copyright (c) 2023 Miel Donkers

Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
import urllib
from urllib.parse import urlparse, parse_qs

from hello import Hello
from erreur import Erreur
from route import Route
from render import Render
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

#files
import os
import posixpath
import cgi
import shutil
import mimetypes
import re
import sys
#try:
#    from cStringIO import StringIO #except ImportError:
#    from StringIO import StringIO
ROUTE={"/":"hello#hi"}

class S(BaseHTTPRequestHandler):
    def deal_post_data(self,uploads=False):
        if uploads:
          myuploads={}
          ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
          print(pdict)
          try:
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
          except:
            pdict['boundary'] = bytes("", "utf-8")
          pdict['CONTENT-LENGTH'] = int(self.headers['Content-Length'])
          print(ctype, "type of form")
          if ctype == 'multipart/form-data':
              form = cgi.FieldStorage( fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'], })
              print(type(form), "=====> DEAL_POST_DATA typemyform")
              print(uploads, "===> uploads")

              if uploads:
                for upload in uploads:
                  try:
                      print("check ", upload)

                      try:
                        if form[upload].filename:
                          myuploads[upload]=form[upload]
                        else:
                          print("my name")
                          print(form[upload].value)
                          myuploads[upload]=form[upload].value
                      except Exception as e:
                          print(e)
                          print("this name")

                          myuploads[upload]=form[upload].value
                      finally:
                          print("suivant", myuploads)
                  except IOError:
                          #return (False, "Can't create file to write, do you have permission to write?")
                          return myuploads
          #return (True, "Files uploaded")
          return myuploads

    def _set_response(self,pic=False,js=False,runprogram=False,music=False,redirect=False,css=False,json=False):
        if redirect:
          self.send_response(301)
          self.send_header('Location', redirect) 
          self.send_header('Status', "301 Moved Permanently") 
        else:
          self.send_response(200)
        if pic:
          self.send_header('Content-type', 'image/'+pic)
        elif music:
          self.send_header('Content-type', 'audio/'+music)
        elif json:
          self.send_header('Content-type', 'application/json')
        elif js:
          self.send_header('Content-type', 'text/javascript')
        elif css:
          self.send_header('Content-type', 'text/css')

        else:

          self.send_header('Content-type', 'text/html')

        self.end_headers()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        params=parse_qs(parsed_path.query)
        if parsed_path.path.startswith("/echo"):
           message = '\n'.join([  'CLIENT VALUES:',
           'client_address=%s (%s)' % (self.client_address, self.address_string()),
           'command=%s' % self.command,
           'path=%s' % self.path,
           'real path=%s' % parsed_path.path,
           'query=%s' % parsed_path.query,
           'request_version=%s' % self.request_version,
           '',
           'HEADERS:',
           '%s' % self.headers,])
           self.send_response(200)
           self.end_headers()
           self.wfile.write(message.encode('utf-8'))
        else:
           logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))


           
           print(params)
           print("myparams")
           myProgram=Route().get_route(myroute=self.path.split("?")[0],myparams=params,mydata=False)

           self._set_response(pic=myProgram.get_pic(), js=myProgram.get_js(),music=myProgram.get_music(),redirect=myProgram.get_redirect(),css=myProgram.get_css(),json=myProgram.get_json())
           
           print(myProgram, "y mrograù")
           html=myProgram.get_html()
           #print(html)
           self.wfile.write(bytes(html))

    def do_POST(self):

        parsed_path = urllib.parse.urlparse(self.path)
        #params=parse_qs(parsed_path.query)
        if self.path.startswith("/echo"):
          message = '\n'.join([  'CLIENT VALUES:',
          'client_address=%s (%s)' % (self.client_address, self.address_string()),
          'command=%s' % self.command,
          'path=%s' % self.path,
          'real path=%s' % parsed_path.path,
          'query=%s' % parsed_path.query,
          'request_version=%s' % self.request_version,
          '',
          'HEADERS:',
          '%s' % self.headers,])
          print(message)
          self.send_response(200)
          self.end_headers()
          self.wfile.write(message.encode('utf-8'))
        else:
          content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
          post_data = ""
          parsed_path = urllib.parse.urlparse(self.path)
          #params=parse_qs(post_data)
          logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                 str(self.path), str(self.headers), post_data)
          myProgram=Route().get_route(myroute=self.path.split("?")[0],myparams={},mydata=self.deal_post_data)
          self._set_response(pic=myProgram.get_pic(), js=myProgram.get_js(),music=myProgram.get_music(),redirect=myProgram.get_redirect(),css=myProgram.get_css(),json=myProgram.get_json())
          print(myProgram,post_data, "y mrograù")
          html=myProgram.get_html()
          #print(html)
          self.wfile.write(bytes(html))

def run(server_class=HTTPServer, handler_class=S, port=8081):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
