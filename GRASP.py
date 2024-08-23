import random, time
import math
from random import shuffle
import re
from collections import defaultdict, deque
import cProfile, pstats, io
from pstats import SortKey
from Annealing import *
from geraGramatica import *
from VNS import *


def calcular_pesos(grafo):
    pesos = {}
    for vertice, vizinhos in grafo.items():
      pesos[vertice] = len(vizinhos)  # O peso é o número de vizinhos (filhos)
    return pesos


  # Função para realizar sorteio ponderado sem repetição
def sorteio_ponderado_sem_repeticao(grafo, pesos):
    vertices = list(grafo.keys())  # Lista de vértices
    ordem_sorteada = []

    while vertices:
      probabilidade = [pesos[v] for v in vertices]  # Probabilidade proporcional aos pesos
      vertice_sorteado = random.choices(vertices, weights=probabilidade, k=1)[0]
      ordem_sorteada.append(vertice_sorteado)
      vertices.remove(vertice_sorteado)  # Remove o vértice sorteado da lista

    return ordem_sorteada
