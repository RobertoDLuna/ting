from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        # list() -> Estrutura para guardar infos da pilha
        self.list = list()
    # Retornar tamanho da lista
    def __len__(self):
        return len(self.list)
    # Adicionar dados
    def enqueue(self, value):
        return self.list.append(value)
    # Remover dados
    def dequeue(self):
        return self.list.pop(0)
    # Buscar dados
    def search(self, index):
        # se o index for < 0 ou maior que o len da lista
        if (index < 0 or index > len(self.list)):
            # Retorna o indexError
            raise IndexError
        return self.list[index]