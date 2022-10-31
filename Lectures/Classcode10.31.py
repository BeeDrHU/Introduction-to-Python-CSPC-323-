##########################################
###     Networked Programs             ###
###     Updated: 10/31/2022            ###
##########################################

#####################
# Hypertext Transfer Protocols (HTTP)
# -sockets
#   -networks run off of sockets to make connections between files/programs
#   -a socket is like a file, except a socket provides two-way connection
# between programs.
#   -something written to a socket is sent to the other end app
#   -something read from the socket gives data that has been sent
#
# -protocol
#   -set of precise rules that determine who goes first, what they
# do, and then what the responses are to that messsage, who to send
# next, and so on.
#   -back and forth game of ping pong
#####################

######################
### simplest web browser
######################

import socket

#define the constants
mysock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#establish connection to port 80 of website of interest
mysock.connect(('data.pr4e.org', 80))

#HTTP protocol: requires that we sent a get command followed by
#blank line. We used two blanks line
cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

#send the HTTP command
mysock.send(cmd)

#prints out the data from the socket until there's no more
while True:
    data=mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode(), end='')

#close the socket
mysock.close()

######################
### retrieve an image over HTTP
######################

import socket
import time

#establish connections
HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

#run the website and collect the data
while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

#close connection
mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

######################
### retrieve webpage with urllib
######################

#much simpler way to connect and recieve data. treats www like a file
#handles all HTTP protocol
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#example: using library to retrieve data from file and count freq of
#words in file (Romeo adv.)
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

######################
### retrieve binary file with urllib
######################

#working with non-text files in urllib
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()

#wb opens binary for writing only
fhand = open('cover3.jpg', 'wb')
fhand.write(img)

fhand.close()

#for large files, this program would run out of memory.
#We now will write the program so it retrieves the data in blocks
#and writes that data to disk before retrieving the next block.
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: 
        break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')

fhand.close()

######################
### parsing html w/ beautifulsoup
######################

#beautifulsoup is the most common way of scraping the web (webscraper/webcrawler)
#benefit: really good at dealing with bad HTML
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors, just for this example. Decreases security
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#prompt for url, opens, reads data, and passes to Btflsp
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

####Same code, but parses and prints individual components of tags
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
