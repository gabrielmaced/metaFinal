import random, time
import math
from random import shuffle
import re
from collections import defaultdict, deque
import cProfile, pstats, io
from pstats import SortKey
from geraGramatica import *
from GRASP import *
from VNS import *


  # Simulated Annealing - busca_local com o "annealing" como True
def busca_local(solucao_inicial,
                grafo,
                  temp_inicial=1000,
                  temp_final=0.1,
                  alpha=0.9,
                  qtd_vizinhos=100,
                  reaquecimentos=1,
                  annealing=True):

    melhor_solucao = solucao_inicial
    solucao_atual = solucao_inicial

    while reaquecimentos >= 0:
      reaquecimentos -= 1
      temp_atual = temp_inicial
      while temp_atual > temp_final:
        temp_atual *= alpha
        for _ in range(qtd_vizinhos):
          lista_vertices = list(solucao_atual.keys())
          nova_solucao = vizinhanca(lista_vertices,grafo)
          delta = obj(solucao_atual) - obj(nova_solucao)
          if delta > 0:
            solucao_atual = nova_solucao
            delta2 = obj(melhor_solucao) - obj(nova_solucao)
            if delta2 > 0:
              melhor_solucao = nova_solucao
          else:
            if annealing:
              r = random.uniform(0, 1)
              if r <= math.exp(-delta / temp_atual):
                solucao_atual = nova_solucao

    return melhor_solucao, obj(melhor_solucao)
  
def gerar_solucao_inicial(lista_vertices, grafo):
  random.shuffle(lista_vertices)
  solucao_inicial = gerar_solucao(lista_vertices, grafo)
  return solucao_inicial, obj(solucao_inicial)


def gerar_solucao(lista_vertices, grafo):
  dicionario = {vertice: '0' for vertice in lista_vertices}

  for vertice in lista_vertices:
    cores_vizinhos = set()
    for vizinho in grafo[str(vertice)]:
      if dicionario[str(vizinho)] != 0:
        cores_vizinhos.add(dicionario[str(vizinho)])

    cor_atual = 1
    while cor_atual in cores_vizinhos:
      cor_atual += 1

    dicionario[str(vertice)] = cor_atual

  return dicionario


def vizinhanca(lista_vertices, grafo):
  lista_vertices = swap_porcentagem(lista_vertices)
  nova_solucao = gerar_solucao(lista_vertices, grafo)
  return nova_solucao


def obj(solucao):
  return len(set(solucao.values()))

def shift_porcentagem(lista_vertices, porcentagem=5):
  tamanho = len(lista_vertices)
  num_elementos = int(tamanho * (porcentagem / 100))
  if num_elementos == 0:
    return lista_vertices

  deslocamento = random.randint(1, tamanho)
  nova_lista = lista_vertices[deslocamento:] + lista_vertices[:deslocamento]
  return nova_lista


def swap_porcentagem(lista_vertices, porcentagem=5):
  tamanho = len(lista_vertices)
  num_elementos = int(tamanho * (porcentagem / 100))
  if num_elementos < 2:
    return lista_vertices

  for _ in range(num_elementos // 2):
    idx1, idx2 = random.sample(range(tamanho), 2)
    lista_vertices[idx1], lista_vertices[idx2] = lista_vertices[
        idx2], lista_vertices[idx1]
  return lista_vertices