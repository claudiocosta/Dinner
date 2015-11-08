__author__ = 'Claudio'
# -*- coding: utf-8 -*-
import _thread
import time, random
import threading

garfo = list()
for i in range(5):
   garfo.append(threading.Semaphore(1))

def filosofo(f):
   f = int(f)
   while True:
      # garfo da esquerda
      garfo[f].acquire()
      # garfo da direita
      garfo[(f + 1) % 5].acquire()
      print("Filósofo %i comendo..." %f)
      time.sleep(random.randint(1, 5))
      garfo[f].release()
      garfo[(f + 1) % 5].release()
      print ("Filósofo %i pensando..." %f)
      time.sleep(random.randint(1, 10))

for i in range(5):
   print ("Filósofo", i)
   _thread.start_new_thread(filosofo, tuple([i]))

while 1: pass