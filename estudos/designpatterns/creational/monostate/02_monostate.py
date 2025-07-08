"""
Exemplo prático para entender o padrão de projeto Monostate.

Componentes principais:
- Monostate
- Client
"""
import time
import threading


class TaskQueue:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not hasattr(self, "queue"):
            self.queue = []

    def set_task(self, func, *args):
        print(f"Enfileirando tarefa: {func.__name__}({args})")
        self.queue.append((func, args))

    def get_next_task(self):
        if self.queue:
            return self.queue.pop(0)
        return None


def send_email(email):
    print(f"[WORKER] Enviando e-mail para {email}...")
    time.sleep(2)
    print(f"[WORKER] E-mail enviado para {email}!")


def user_register(email):
    queue = TaskQueue()
    queue.set_task(send_email, email)
    print("Cadastro concluído.")


def worker_loop():
    queue = TaskQueue()
    while True:
        task = queue.get_next_task()
        if task:
            func, args = task
            func(*args)
        else:
            print("[WORKER] Nenhuma tarefa. Aguardando...")
            time.sleep(3)


if __name__ == "__main__":
    t = threading.Thread(target=worker_loop, daemon=True)
    t.start()
    user_register("thomas@exemplo.com")
    time.sleep(1)
    user_register("nicholas@exemplo.com")
    time.sleep(1)
    user_register("teste@exemplo.com")

    time.sleep(10)
