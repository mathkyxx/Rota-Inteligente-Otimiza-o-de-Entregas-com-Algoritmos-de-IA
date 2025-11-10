SaborExpress/
│
├── src/
│   ├── main.py            # Script principal
│   ├── routing.py         # Funções de cálculo de rotas
│   ├── visualization.py   # Funções para gerar gráficos e mapas
│   └── utils.py           # Funções auxiliares
│
├── data/
│   ├── mapa.csv            # Grafo das ruas (origem, destino, distância)
│   └── pedidos.csv         # Pontos de entrega (cliente, endereço, coordenadas)
│
├── outputs/
│   ├── rotas.png           # Exemplo de visualização da rota
│   └── relatorio.csv       # Relatório de rotas otimizadas
│
├── docs/
│   └── README.md           # Instruções de execução e explicações
│
└── requirements.txt        # Bibliotecas necessárias


  origem,destino,distancia
A,B,2
A,C,4
B,C,1
B,D,7
C,D,3
C,E,5
D,E,2


  cliente,endereco,x,y
Cliente1,A,0,0
Cliente2,C,2,1
Cliente3,D,4,3
Cliente4,E,5,2


  import heapq

def dijkstra(grafo, inicio):
    fila = [(0, inicio, [])]
    visitados = set()
    
    while fila:
        (custo, vertice, caminho) = heapq.heappop(fila)
        if vertice not in visitados:
            visitados.add(vertice)
            caminho = caminho + [vertice]
            yield (vertice, custo, caminho)
            for prox, peso in grafo.get(vertice, []):
                if prox not in visitados:
                    heapq.heappush(fila, (custo + peso, prox, caminho))

def criar_grafo(mapa_csv):
    import csv
    grafo = {}
    with open(mapa_csv, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            origem, destino, distancia = row['origem'], row['destino'], float(row['distancia'])
            grafo.setdefault(origem, []).append((destino, distancia))
            grafo.setdefault(destino, []).append((origem, distancia))  # Grafo não-direcionado
    return grafo


import matplotlib.pyplot as plt

def plot_rotas(pontos, rotas, arquivo_saida):
    fig, ax = plt.subplots()
    for rota in rotas:
        xs = [pontos[vert]['x'] for vert in rota]
        ys = [pontos[vert]['y'] for vert in rota]
        ax.plot(xs, ys, marker='o')
    for nome, ponto in pontos.items():
        ax.text(ponto['x'], ponto['y'], nome)
    plt.title("Rotas Otimizadas")
    plt.savefig(arquivo_saida)
    plt.close()


import csv
from src.routing import criar_grafo, dijkstra
from src.visualization import plot_rotas

# 1. Criar grafo a partir do CSV
grafo = criar_grafo('data/mapa.csv')

# 2. Carregar pontos de entrega
pontos = {}
with open('data/pedidos.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pontos[row['endereco']] = {'cliente': row['cliente'], 'x': float(row['x']), 'y': float(row['y'])}

# 3. Calcular rotas do depósito (A) para todos os pontos
rotas = []
for vert, custo, caminho in dijkstra(grafo, 'A'):
    if vert in pontos:
        rotas.append(caminho)

# 4. Salvar relatório CSV
with open('outputs/relatorio.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Cliente', 'Rota'])
    for rota in rotas:
        writer.writerow([pontos[rota[-1]]['cliente'], ' -> '.join(rota)])

# 5. Visualizar rotas
plot_rotas(pontos, rotas, 'outputs/rotas.png')

print("Rotas calculadas e visualização gerada!")


matplotlib


networkx
ortools


pip install -r requirements.txt


python src/main.py
