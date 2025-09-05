###############################################################################################################
#   Autor: Vitória Maria Oliveira dos Santos                                                                  #
#   Data: 04/09/2024                                                                                          #                                      
#                                                                                                          #                  
###############################################################################################################


import networkx as nx
from networkx.algorithms import community

class User:
    def __init__(self, user_id, data):
        self._user_id = user_id
        self._data = data

    def get_id(self):
        return self._user_id

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data


class SocialNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_user(self, user_id, user_data):
        self.graph.add_node(user_id, data=user_data)

    def remove_user(self, user_id):
        self.graph.remove_node(user_id)

    def connect_users(self, user1_id, user2_id):
        self.graph.add_edge(user1_id, user2_id)

    def disconnect_users(self, user1_id, user2_id):
        self.graph.remove_edge(user1_id, user2_id)

    def find_communities(self):
        communities = community.greedy_modularity_communities(self.graph)
        return [list(c) for c in communities]

    def user_centralities(self, method='degree'):
        if method == 'degree':
            return nx.degree_centrality(self.graph)
        elif method == 'betweenness':
            return nx.betweenness_centrality(self.graph)
        elif method == 'closeness':
            return nx.closeness_centrality(self.graph)
        else:
            raise ValueError("Método de centralidade não reconhecido.")

    def analyze_subgraph(self, user_ids):
        subgraph = self.graph.subgraph(user_ids)
        return {
            "nodes": subgraph.nodes(data=True),
            "edges": subgraph.edges(),
            "density": nx.density(subgraph),
            "average_clustering": nx.average_clustering(subgraph)
        }
streamer1 = User("vava_queen", {"nome": "Luna", "interesses": ["FPS competitivo", "ranked", "coaching"]})
streamer2 = User("clutch_master", {"nome": "Rafa", "interesses": ["jogadas épicas", "clutch", "montagens"]})
streamer3 = User("valorant_tips", {"nome": "Gui", "interesses": ["tutorial", "educacional", "novatos"]})
streamer4 = User("chill_vibes", {"nome": "Nina", "interesses": ["gameplay casual", "chat interativo", "variedades"]})
streamer5 = User("duo_god", {"nome": "Leo", "interesses": ["duo ranked", "comunidade", "discord"]})

rede = SocialNetwork()
for streamer in [streamer1, streamer2, streamer3, streamer4, streamer5]:
    rede.add_user(streamer.get_id(), streamer.get_data())

rede.connect_users("vava_queen", "clutch_master")
rede.connect_users("valorant_tips", "vava_queen")
rede.connect_users("chill_vibes", "duo_god")
rede.connect_users("duo_god", "clutch_master")
rede.connect_users("valorant_tips", "chill_vibes")

comunidades = rede.find_communities()
print("Comunidades detectadas:")
for i, grupo in enumerate(comunidades):
    print(f"Grupo {i+1}: {grupo}")

centralidade = rede.user_centralities(method='degree')
print("\n Centralidade (grau):")
for user_id, score in centralidade.items():
    print(f"{user_id}: {score:.2f}")

subgrafo_info = rede.analyze_subgraph(["vava_queen", "clutch_master", "valorant_tips"])
print("\n Subgrafo (Luna, Rafa, Gui):")
print("Nós:", list(subgrafo_info["nodes"]))
print("Conexões:", list(subgrafo_info["edges"]))
print("Densidade:", f"{subgrafo_info['density']:.2f}")
print("Agrupamento médio:", f"{subgrafo_info['average_clustering']:.2f}")
