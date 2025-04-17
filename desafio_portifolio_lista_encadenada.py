""" Olá meu nome é marcio e esse é um exercicio de portifólio proposto pela faculdade,
nele o objeto era criar uma lista encadeada e depois criar uuma função que
retornasse o numero de nós"""

from random import randint

class Node:
    def __init__(self, data):
        self.data = data  # Dado armazenado
        self.next = None  # Referência para o próximo nó
    
    def __repr__(self):
        return "%s => %s" % (self.data, self.next)

class LinkedList:
    def __init__(self):
        self.head = None  # Head é None pois a lista está vazia
    
    def __repr__(self):
        return "%s" % (self.head)
    
    def append(self, data):
        # Criando objeto para armazenar novo item na lista
        item = Node(data)
        # Se a lista está vazia, o novo item se torna o head
        if not self.head:
            self.head = item
        else:
            # Percorre a lista até encontrar o último item
            item_atual = self.head
            while item_atual.next:
                item_atual = item_atual.next
            # Adiciona o novo item no final da lista
            item_atual.next = item
    
    def print_list(self):
        # Imprime os elementos da lista
        no = self.head
        while no:
            print(f'{no.data}', end=" -> ")
            no = no.next
        print("Vazio")
    
    def count_nodes(self):
        # Implementa a função para contar o número de nós na lista encadeada
        contador = 0
        item = self.head
        while item:
            contador += 1
            item = item.next
        return contador

# Testes
if __name__ == "__main__":
    # Criar uma lista encadeada e adicionar alguns elementos
    lista = LinkedList()
    lista.append(randint(1,100))
    lista.append(randint(2,100))
    lista.append(randint(2,100))

    # Imprimir a lista encadeada
    print("Lista Encadeada:")
    lista.print_list()

    # Contar o número de nós na lista encadeada
    num_no = lista.count_nodes()
    print(f"Número de nós na lista: {num_no}")