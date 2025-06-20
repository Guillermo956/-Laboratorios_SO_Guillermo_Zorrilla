import threading
import time

recurso_a = threading.Lock()
recurso_b = threading.Lock()

def hilo_1():
    print("Hilo 1: intentando bloquear recurso A")
    recurso_a.acquire()
    print("Hilo 1: recurso A bloqueado")
    time.sleep(1)

    print("Hilo 1: intentando bloquear recurso B")
    recurso_b.acquire()
    print("Hilo 1: recurso B bloqueado")

def hilo_2():
    print("Hilo 2: intentando bloquear recurso B")
    recurso_b.acquire()
    print("Hilo 2: recurso B bloqueado")
    time.sleep(1)

    print("Hilo 2: intentando bloquear recurso A")
    recurso_a.acquire()
    print("Hilo 2: recurso A bloqueado")

t1 = threading.Thread(target=hilo_1)
t2 = threading.Thread(target=hilo_2)

t1.start()
t2.start()

t1.join()
t2.join()
