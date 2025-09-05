###############################################################################################################
#   Autor: Vitória Maria Oliveira dos Santos                                                                  #
#   Data: 05/09/2024                                                                                          #                                      
#                                                                                                             #
# Descrição:Você foi contratado como um desenvolvedor de software para um novo jogo de Pokémon e recebeu      #
#  a tarefa de implementar um sistema eficiente de gerenciamento de Pokémon utilizando uma Árvore             #
#  AVL. Cada Pokémon no jogo é caracterizado por um nome e um valor de força, que é um número                 #
#  inteiro.                                                                                                   #
#                                                                                                             #                  
###############################################################################################################


class PokemonNode:
    def __init__(self, nome, forca):
        self.nome = nome
        self.forca = forca
        self.left = None
        self.right = None
        self.height = 1

class PokemonAVL:
    
    def __init__(self):
        self.root = None
    def get_height(self, node):
        return node.height if node else 0
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x
    
    # Função de busca para encontrar um Pokémon pelo nome
    def search(self, node, nome):
        if not node:
            return None
        if nome == node.nome:
            return node
        elif nome < node.nome:
            return self.search(node.left, nome)
        else:
            return self.search(node.right, nome)
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Insere cada Pokémon na árvore AVL(Pokedex), rebalanceando
    def insert(self, node, nome, forca):
        if not node:
            return PokemonNode(nome, forca)
        if nome < node.nome:
            node.left = self.insert(node.left, nome, forca)
        elif nome > node.nome:
            node.right = self.insert(node.right, nome, forca)
        else:
            return node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Rebalanceamento
        if balance > 1 and nome < node.left.nome:
            return self.rotate_right(node)
        if balance < -1 and nome > node.right.nome:
            return self.rotate_left(node)
        if balance > 1 and nome > node.left.nome:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and nome < node.right.nome:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def add_pokemon(self, nome, forca):
        self.root = self.insert(self.root, nome, forca)

    def buscar_pokemon(self, nome):
        result = self.search(self.root, nome)
        return (result.nome, result.forca) if result else None

    def listar_decrescente(self):
        pokemons = []
        def inorder(node):
            if node:
                inorder(node.left)
                pokemons.append((node.nome, node.forca))
                inorder(node.right)
        inorder(self.root)
        return sorted(pokemons, key=lambda x: x[1], reverse=True)

    def delete(self, node, nome):
        if not node:
            return node
        if nome < node.nome:
            node.left = self.delete(node.left, nome)
        elif nome > node.nome:
            node.right = self.delete(node.right, nome)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.get_min_value_node(node.right)
            node.nome = temp.nome
            node.forca = temp.forca
            node.right = self.delete(node.right, temp.nome)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def remover_pokemon(self, nome):
        self.root = self.delete(self.root, nome)


#Execução & Teste do código:

if __name__ == "__main__":
    avl = PokemonAVL()
    avl.add_pokemon("Pikachu", 60)
    avl.add_pokemon("Bulbassaur", 60)
    avl.add_pokemon("Jigglypuff", 70)
    avl.add_pokemon("Squirtle", 70)
    avl.add_pokemon("RaiChu", 90)
    avl.add_pokemon("Charizard", 100)
    avl.add_pokemon("Mewtwo", 150)

    print("Pokémons listados em ordem decrescente de força:")
    for nome_lista, forca in avl.listar_decrescente():
        print(f"{nome_lista}: {forca}")

    nome_busca = input("\nDigite o nome do Pokémon a ser buscado: ")
    resultado = avl.buscar_pokemon(nome_busca)
    if resultado:
        print(f"\nPokémon encontrado - Nome: {resultado[0]}, Força: {resultado[1]}")
    else:
        print(f"\nPokémon {nome_busca} não encontrado.")

    nome_remocao = input("\nDigite o nome do Pokémon a ser removido: ")
    avl.remover_pokemon(nome_remocao)

    print(f"\n{nome_remocao} foi removido com sucesso. Os Pokémons disponíveis são:")
    for nome_lista, forca in avl.listar_decrescente():
        print(f"{nome_lista}: {forca}")
