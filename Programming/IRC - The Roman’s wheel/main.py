import socket
import time


def rot13_decode(string):
    decoded_str = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                decoded_str += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                decoded_str += chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            decoded_str += char
    return decoded_str


SERVER = "irc.root-me.org"
PORT = 6667

# set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((SERVER, PORT))

# send user information
s.send(b"NICK user5\r\n")
time.sleep(0.1)
s.send(b"USER user5 irc.root-me.org root-me :MyBot5\r\n")
time.sleep(0.1)
s.send(b"JOIN #root-me_challenge\r\n")
time.sleep(0.3)

# send privmsg
s.send(b"PRIVMSG candy :!ep3\r\n")
time.sleep(1.5)

# receive the message
msg = s.recv(7000).decode("utf-8")
print(msg)

# extract the message
result = rot13_decode(msg[msg.rfind(":") - 1:len(msg)]).replace(":", "")

# send the result
s.send(b"PRIVMSG candy :!ep3 -rep" + str(result).encode("utf-8"))

# receive the message
print(s.recv(7000).decode("utf-8"))
