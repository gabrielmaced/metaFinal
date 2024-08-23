import random, time
import math
from random import shuffle
import re
from collections import defaultdict, deque
import cProfile, pstats, io
from pstats import SortKey

tamanho_adj = {}
coloracao_vertice = {}
grafo = {}

#FUNÇÃO PARA LER O TXT INICIAL
def read_grammar_file(file_path):
  with open(file_path, 'r') as file:
    grammar_text = file.read()
  return parse_grammar(grammar_text)


#FUNÇÃO PARA FAZER O DICIONÁRIO COM VERTICE E SEUS FILHOS
def parse_grammar(grammar_text):
  adj = {}
  tamanho_grafo = 0
  lines = grammar_text.split('\n')
  for line in lines:
    if not line.strip():
      continue
    linha = re.split(r'[,\s]+', line)
    left = linha[0]
    right = linha[1]
    if left not in adj:
      tamanho_grafo += 1
      adj[left] = set()
      tamanho_adj[left] = 0
      coloracao_vertice[left] = set()
      coloracao_vertice[left] = 0
    if right not in adj:
      tamanho_grafo += 1
      adj[right] = set()
      tamanho_adj[right] = 0
      coloracao_vertice[right] = set()
      coloracao_vertice[right] = 0
    adj[left].add(right)
    tamanho_adj[left] += 1
    adj[right].add(left)
    tamanho_adj[right] += 1
  return adj, tamanho_grafo