import socket
import time
import re
from math import sqrt

SERVER = "irc.root-me.org"
PORT = 6667

# set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((SERVER, PORT))

# send user information
s.send(b"NICK user2\r\n")
time.sleep(0.1)
s.send(b"USER user2 irc.root-me.org root-me :MyBot1\r\n")
time.sleep(0.1)
s.send(b"JOIN #root-me_challenge\r\n")

# send privmsg
s.send(b"PRIVMSG candy :!ep1\r\n")
time.sleep(0.5)

# receive the message
time.sleep(0.5)
msg = s.recv(7000).decode("utf-8")

# extract the message
match = re.search(r'\d+ \/ \d+', msg)

# If a match is found, extract the matched string
if match:
    result = match.group().split(' / ')
    result = [int(x) for x in result]

    # format the result
    final = round(sqrt(result[0]) * result[1], 2)

    # send the result
    s.send(b"PRIVMSG candy :!ep1 -rep " + str(final).encode() + b"\r\n")

    # receive the message
    print(s.recv(7000).decode("utf-8"))
