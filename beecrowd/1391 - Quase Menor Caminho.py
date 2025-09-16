import heapq
from collections import deque

def dijkstra(vertices, origem, destino, lista_adjacencia, removed_edges):
    # Inicializa as distâncias e a fila de prioridade
    INF = float('inf')
    distancia = [INF] * vertices
    distancia[origem] = 0
    prev = [[] for _ in range(vertices)]
    # Min-heap para o próximo vértice a ser processado
    min_heap = [(0, origem)]
    visitado = [False] * vertices

    # Processa os vértices na ordem de distância
    while min_heap:
        # Retira o vértice com a menor distância
        distancia_atual, vertice_atual = heapq.heappop(min_heap)
        
        # Se já foi visitado, pula
        if visitado[vertice_atual]:
            continue
        
        # Marca como visitado
        visitado[vertice_atual] = True
        
        for vizinho, peso in lista_adjacencia[vertice_atual]:
            # Ignora arestas removidas
            if (vertice_atual, vizinho, peso) in removed_edges:
                continue
            
            # Calcula a nova distância
            nova_distancia = distancia_atual + peso
            
            # Atualiza a distância se for menor
            if nova_distancia < distancia[vizinho]:
                distancia[vizinho] = nova_distancia
                prev[vizinho] = [vertice_atual]
                heapq.heappush(min_heap, (nova_distancia, vizinho))
            
            # Se for igual, adiciona o predecessor
            elif nova_distancia == distancia[vizinho]:
                prev[vizinho].append(vertice_atual)
    return distancia, prev

def mark_all_shortest_path_edges(destino, prev, lista_adjacencia, distancia, removed_edges):
    # Marca todas as arestas que fazem parte de qualquer caminho mais curto
    queue = deque([destino])
    visited = [False] * len(prev)
     
    # BFS reverso para marcar todas as arestas do caminho mais curto
    while queue:
        # Retira o vértice da fila
        u = queue.popleft()
        if visited[u]:
            continue
        visited[u] = True

        # Para cada predecessor, verifica se a aresta faz parte do caminho mais curto
        for v in prev[u]:
            for w, p in lista_adjacencia[v]:
                if w == u and distancia[v] + p == distancia[u]:
                    removed_edges.add((v, w, p))
            queue.append(v)

def main():
    while True:
        vertices, arestas = map(int, input().split())
        if vertices == 0 and arestas == 0:
            break
        origem, destino = map(int, input().split())
        lista_adjacencia = [[] for _ in range(vertices)]
        for _ in range(arestas):
            u, v, p = map(int, input().split())
            lista_adjacencia[u].append((v, p))

        removed_edges = set()
        distancia, prev = dijkstra(vertices, origem, destino, lista_adjacencia, removed_edges)
        if distancia[destino] == float('inf'):
            print("-1")
            continue

        mark_all_shortest_path_edges(destino, prev, lista_adjacencia, distancia, removed_edges)

        distancia2, _ = dijkstra(vertices, origem, destino, lista_adjacencia, removed_edges)
        print("-1" if distancia2[destino] == float('inf') else distancia2[destino])

if __name__ == "__main__":
    main()