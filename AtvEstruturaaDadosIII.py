import heapq

class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_aresta(self, origem, destino, peso):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adjacencia[origem].append((destino, peso))

    def dijkstra(self, inicio, fim):
        distancias = {vertice: float('inf') for vertice in self.adjacencia}
        distancias[inicio] = 0
        anteriores = {vertice: None for vertice in self.adjacencia}
        fila = [(0, inicio)]

        while fila:
            distancia_atual, vertice_atual = heapq.heappop(fila)

            if vertice_atual == fim:
                break

            for vizinho, peso in self.adjacencia[vertice_atual]:
                nova_distancia = distancia_atual + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    anteriores[vizinho] = vertice_atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        caminho = []
        atual = fim
        while atual:
            caminho.insert(0, atual)
            atual = anteriores[atual]

        return caminho, distancias[fim]

def main():
    grafo = Grafo()

    # Dados estáticos
    grafo.adicionar_aresta('A', 'B', 2)
    grafo.adicionar_aresta('A', 'C', 5)
    grafo.adicionar_aresta('B', 'C', 1)
    grafo.adicionar_aresta('B', 'D', 4)
    grafo.adicionar_aresta('C', 'D', 2)
    grafo.adicionar_aresta('D', 'E', 1)

    print("Vértices disponíveis: A, B, C, D, E")
    origem = input("Digite o vértice de origem: ").strip().upper()
    destino = input("Digite o vértice de destino: ").strip().upper()

    if origem not in grafo.adjacencia or destino not in grafo.adjacencia:
        print("Vértice inválido. Tente novamente.")
        return

    caminho, custo = grafo.dijkstra(origem, destino)
    print(f"\nCaminho mais curto de {origem} até {destino}: {' -> '.join(caminho)}")
    print(f"Custo total: {custo}")

if __name__ == "__main__":
    main()
