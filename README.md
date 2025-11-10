# Rota Inteligente: Otimização de Entregas com Algoritmos de IA


## Descrição do Problema
A empresa **Sabor Express** atua com delivery de alimentos na região central da cidade. Durante horários de pico, os entregadores enfrentam atrasos, percursos ineficientes e aumento do custo de combustível, afetando a satisfação dos clientes.  

O desafio é criar uma solução baseada em **Inteligência Artificial** para:
- Sugerir as **melhores rotas** para os entregadores.
- Agrupar pedidos próximos para otimizar a entrega.

---

## Objetivos do Projeto
1. Representar a cidade como um **grafo**, onde:
   - **Nós:** bairros ou pontos de entrega
   - **Arestas:** ruas com peso baseado em distância ou tempo estimado
2. Implementar algoritmos de **busca de menor caminho** para otimizar rotas:
   - A* (A-star)
   - Dijkstra
   - BFS/DFS (quando necessário)
3. Implementar **algoritmos de clustering** para agrupar entregas próximas:
   - K-Means
4. Avaliar soluções usando métricas como:
   - Tempo total de entrega
   - Distância percorrida
   - Número de entregas por rota
   - Eficiência do agrupamento

---

## Abordagem
1. **Representação da cidade como grafo:**  
   Cada bairro/ponto de entrega é um nó. Cada rua é uma aresta com peso baseado em distância ou tempo.

2. **Cálculo de rotas ótimas:**  
   Para cada entregador, o algoritmo sugere a rota que minimiza o tempo ou distância total.  

3. **Agrupamento de pedidos (clustering):**  
   Para horários de pico, pedidos próximos são agrupados em clusters, permitindo que um entregador faça várias entregas em uma mesma região.

4. **Integração e otimização:**  
   - Clusteriza os pedidos
   - Calcula rotas dentro de cada cluster
   - Gera rotas otimizadas para cada entregador

---

## Algoritmos Utilizados
- **A\***: Busca de menor caminho considerando heurística (distância euclidiana estimada)
- **Dijkstra**: Busca de menor caminho considerando pesos das arestas
- **BFS/DFS**: Para exploração do grafo e casos simples
- **K-Means**: Agrupamento de entregas por proximidade geográfica

---

## Diagrama do Grafo de Entregas

O grafo abaixo mostra os bairros e ruas da cidade, com o tempo estimado de viagem em cada aresta:

<img width="660" height="499" alt="grafo_demo" src="https://github.com/user-attachments/assets/dd8aeb0a-45d5-40be-ac03-ef13a77555cd" />

---

## Resultados Obtidos

O sistema gera rotas otimizadas do restaurante até cada cliente.
Clientes são agrupados em clusters geográficos, permitindo distribuir entregas entre múltiplos entregadores.
O projeto produz um relatório CSV com rota, distância e cluster de cada cliente, e um gráfico do grafo com rotas coloridas por cluster.

- **Eficiência da Solução:** 
Agrupar clientes por cluster reduz o deslocamento total dos entregadores.
O uso do algoritmo Dijkstra garante caminhos de menor distância entre pontos do grafo.
Permite planejar entregas simultâneas para diferentes clusters, aumentando a eficiência operacional.

- **Limitações Encontradas:** 
Coordenadas de clientes são simuladas; em situações reais seria necessário dados GPS reais.
O roteamento dentro de cada cluster não considera a sequência ótima de entregas (não resolve totalmente o problema do Caixeiro Viajante – TSP).
Rotas não consideram variáveis como tráfego, horário de pico ou tempo de preparo do pedido.

- **Sugestões de Melhoria:** 
Implementar TSP dentro de cada cluster para otimizar a ordem de entrega.
Integrar dados de tráfego e GPS em tempo real.
Automatizar a alocação de entregadores com base na capacidade de carga e tempo de entrega estimado.
Expandir a visualização do grafo para incluir mapas reais da cidade.





