import socket
import time
import base64
import zlib


def decode_string(string):
    string_bytes = base64.b64decode(string)
    decompressed_string = zlib.decompress(string_bytes)
    return decompressed_string.decode('utf-8')


SERVER = "irc.root-me.org"
PORT = 6667

# set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((SERVER, PORT))

# send user information
s.send(b"NICK user6\r\n")
time.sleep(0.1)
s.send(b"USER user6 irc.root-me.org root-me :MyBot5\r\n")
time.sleep(0.1)
s.send(b"JOIN #root-me_challenge\r\n")
time.sleep(0.3)

# send privmsg
s.send(b"PRIVMSG candy :!ep4\r\n")
time.sleep(1.5)

# receive the message
msg = s.recv(7000).decode("utf-8")

# extract the message
result = decode_string(msg[msg.rfind(":") - 1:len(msg)])

# send the result
s.send(b"PRIVMSG candy :!ep4 -rep " + str(result).encode() + b"\r\n")

# receive the message
print(s.recv(7000).decode("utf-8"))
