###############################################################################################################
#   Autor: Vitória Maria Oliveira dos Santos                                                                  #
#   Data: 04/09/2024                                                                                          #                                      
#                                                                                                          #                  
###############################################################################################################


from AtvEstruturaDadosIV import SocialNetwork, User
rede = SocialNetwork()

streamers = [
    User("vava_queen", {"nome": "Luna", "interesses": ["FPS competitivo", "coaching"]}),
    User("clutch_master", {"nome": "Rafa", "interesses": ["clutch", "montagens"]}),
    User("valorant_tips", {"nome": "Gui", "interesses": ["tutorial", "educacional"]}),
    User("chill_vibes", {"nome": "Nina", "interesses": ["gameplay casual", "chat interativo"]}),
    User("duo_god", {"nome": "Leo", "interesses": ["duo ranked", "comunidade"]})
]

for s in streamers:
    rede.add_user(s.get_id(), s.get_data())

rede.connect_users("vava_queen", "clutch_master")
rede.connect_users("valorant_tips", "vava_queen")
rede.connect_users("chill_vibes", "duo_god")
rede.connect_users("duo_god", "clutch_master")
rede.connect_users("valorant_tips", "chill_vibes")

rede.remove_user("duo_god")  # Leo sai da rede

rede.disconnect_users("valorant_tips", "chill_vibes")

comunidades = rede.find_communities()
print("\n Comunidades detectadas:")
for i, grupo in enumerate(comunidades):
    print(f"Grupo {i+1}: {grupo}")

print("\n Centralidade (grau):")
grau = rede.user_centralities(method='degree')
for user_id, score in grau.items():
    print(f"{user_id}: {score:.2f}")

print("\n Centralidade (intermediação):")
betweenness = rede.user_centralities(method='betweenness')
for user_id, score in betweenness.items():
    print(f"{user_id}: {score:.2f}")

print("\n Centralidade (proximidade):")
closeness = rede.user_centralities(method='closeness')
for user_id, score in closeness.items():
    print(f"{user_id}: {score:.2f}")

subgrafo = rede.analyze_subgraph(["vava_queen", "clutch_master", "valorant_tips"])
print("\n Subgrafo (Luna, Rafa, Gui):")
print("Nós:", list(subgrafo["nodes"]))
print("Conexões:", list(subgrafo["edges"]))
print("Densidade:", f"{subgrafo['density']:.2f}")
print("Agrupamento médio:", f"{subgrafo['average_clustering']:.2f}")
