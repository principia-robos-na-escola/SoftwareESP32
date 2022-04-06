import requests
import time
from threading import Thread

# Input sem precisar apertar enter - pip install blessed ou paru -S python-blessed
from blessed import Terminal

term = Terminal()

speed = 0
speed1 = 0
speed2 = 0
dir1 = 1
dir2 = 1

class Send(Thread):
    def run(self):
        while True:
            s = f'http://192.168.4.1/motor?dir1={dir1}&dir2={dir2}&speed1={speed1}&speed2={speed2}'
            r = requests.get(s)
            print(s)
            time.sleep(0.2)

if __name__ == '__main__':
    t = Send()
    t.daemon=True
    t.start()

    while True:
        with term.cbreak():
            c = term.inkey()
            if c == 'w':
                speed += 10
                speed1 = speed
                speed2 = speed
            if c == 's':
                speed -= 10
                speed1 = speed
                speed2 = speed
            if c == 'a':
                speed1 = 0
            if c == 'd':
                speed2 = 0
            if c == ' ':
                speed1 = 0
                speed2 = 0
            if c == 'q':
                exit()
