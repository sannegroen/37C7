import socket
import random

host = '151.217.30.160'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

from PIL import Image
im = Image.open("/Users/san/Desktop/Verve.png")
im = im.resize((400, 200))
rgb_im = im.convert('RGBA')

def pix(x, y, color):
    msg = f'PX {x} {y} {color}\n'
    packet = msg.encode('ascii')
    s.sendall(packet)

while True:
    for j in range(400):
        for k in range(200):
            x = 0 + j
            y = 0 + k

            r, g, b, a = rgb_im.getpixel((x, y))

            if a == 0:
                continue

            color = '%02X%02X%02X%02X' % (r, g, b, a)
            pix(x + 400, y + 80, color)
