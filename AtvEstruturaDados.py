
###############################################################################################################
#   Autor: Vitória Maria Oliveira dos Santos                                                                  #
#   Data: 04/09/2024                                                                                          #                                      
#                                                                                                             #
# Descrição:A atividade consiste em implementar uma função chamada count_nodes, que recebe uma lista          #
#   encadeada como parâmetro e retorna o número de nós presentes na lista. A função percorre a lista          #
#   encadeada usando um loop enquanto incrementa um contador. Ao final do percurso, o valor do                #
#   contador é retornado.                                                                                     #
#                                                                                                             #                  
###############################################################################################################



class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None

    def append(self, data):

        item = Node(data)
        item.next = self.head
        self.head = item

    def print_list(self):

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("A lista terminou.")

    
    def count_nodes(self, linked_list):

        count = 0
        current = linked_list.head
        while current:
            count += 1
            current = current.next
        return count
    
#Execução do código
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(100)
    linked_list.append(200)
    linked_list.append(300)

    linked_list.print_list()

    num_nodes = linked_list.count_nodes(linked_list)
    print(f"Número de nós na lista encadeada: {num_nodes}")

