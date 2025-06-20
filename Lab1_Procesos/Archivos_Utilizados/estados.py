import time
import random

# Estructura para guardar los tiempos de transición
tiempos_transicion = []

# Simulación de procesos con estados Ready y Running
class Proceso:
    def __init__(self, pid):
        self.pid = pid
        self.estado = "Ready"
        self.t_ready_a_running_inicio = None

    def cambiar_a_running(self):
        # Marca el inicio del cambio Ready -> Running
        self.t_ready_a_running_inicio = time.perf_counter()
        self.estado = "Running"

    def inicio_ejecucion(self):
        # Marca el fin del cambio Ready -> Running y calcula el tiempo
        t_fin = time.perf_counter()
        tiempo = (t_fin - self.t_ready_a_running_inicio) * 1000  # Convertir a ms
        tiempos_transicion.append((self.pid, "Ready → Running", tiempo))
        print(f"Proceso {self.pid}: Tiempo Ready→Running = {tiempo:.3f} ms")

# Simulación de varios procesos y sus transiciones
def simular_procesos():
    procesos = [Proceso(pid) for pid in range(1, 6)]

    for p in procesos:
        # Simular un retardo variable en estado Ready
        retardo_ready = random.uniform(0.001, 0.01)  # 1 a 10 ms
        time.sleep(retardo_ready)

        p.cambiar_a_running()

        # Simular que el proceso empieza a ejecutarse después de un retardo pequeño
        retardo_ejecucion = random.uniform(0.001, 0.005)
        time.sleep(retardo_ejecucion)

        p.inicio_ejecucion()

    # Mostrar resumen
    tiempos = [t[2] for t in tiempos_transicion]
    print(f"\nTiempo promedio Ready→Running: {sum(tiempos)/len(tiempos):.3f} ms")

if __name__ == "__main__":
    simular_procesos()
