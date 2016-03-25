from threading import Thread
import time
stop = False

def child():
  while True:
    print 'child'
    time.sleep(1)
  
def parent():
  t = Thread(target=child)
  t.daemon = True
  t.start()

  while not stop:
    print 'parent'
    time.sleep(1)

from threading import Thread
t = Thread(target=parent)
t.daemon = True
t.start()

i=0
while True:
  time.sleep(1)

  i+= 1
  if i == 5:
    stop = True
