from client import Client
import time
from threading import Thread

def update_messages():
    msgs = []
    run = True
    while True:
        time.sleep(0.1)
        new_messages = c1.get_messages()
        
        msgs.extend(new_messages)
        for msg in new_messages:

                print(msg)
                if msg == "{quit}":
                    run = False
                    break

Thread(target=update_messages).start()

c1 = Client("Shpat")
c2 = Client("John")

c1.send_message("Hello")
time.sleep(5)
c2.send_message("What up bro")
time.sleep(5)
c1.send_message("Not rlly anything special, how about u?")
time.sleep(5)
c2.send_message("Chilling")
time.sleep(5)
c1.send_message("nice")
time.sleep(5)
c2.send_message("see ya")
time.sleep(5)

c1.disconnect()
time.sleep(2)
c2.disconnect()


