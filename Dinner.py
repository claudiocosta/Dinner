__author__ = ['Claudio', 'Cristiano']
#
#   Sistemas Operacionais - Jantar dos Filósofos
#   BCC 6S
#
#   Claudio Roberto Costa RA 527033
#   Cristiano Vicente RA 443913
#
# -*- coding: utf-8 -*-

import time, random, threading


def filosofo(f):
    f = int(f)
    while True:
        # garfo da esquerda
        garfo[f].acquire()  # P
        # garfo da direita
        garfo[(f + 1) % n].acquire()  # P
        print("Filósofo %i comendo... :)" % f)
        time.sleep(random.randint(1, 5))
        garfo[f].release()  # V
        garfo[(f + 1) % n].release()  # V
        print("Filósofo %i pensando... :|" % f)
        time.sleep(random.randint(1, 10))


if __name__ == "__main__":

    n = 5

    garfo = [threading.Semaphore(1) for i in range(n)]
    for i in range(n):
        print("Filósofo", i, "morto de fome :x")
        threading._start_new_thread(filosofo, tuple([i]))

    try:
        while True: time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        exit(0)
