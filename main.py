import random, time
import math
from random import shuffle
import re
from collections import defaultdict, deque
import cProfile, pstats, io
from pstats import SortKey
from Annealing import *
from GRASP import *
from VNS import *
from geraGramatica import *

import argparse

tamanho_adj = {}
coloracao_vertice = {}
grafo = {}


#INICIO DA MAIN

def main():
  global grafo
  inicio = time.time()
  parser = argparse.ArgumentParser(description="Processa o arquivo .txt para o grafo.")
  parser.add_argument('arquivo', type=str, help='Nome do arquivo .txt a ser processado')
    
  args = parser.parse_args()
  grammar_file = args.arquivo

  print("Utilizando o", grammar_file, "\n")

  grafo, qtde_cores = read_grammar_file(grammar_file)

  random.seed(1)

  lista_vertices = list(grafo.keys())

  solucao_inicial, qtde_cores_solucao_inicial = gerar_solucao_inicial(lista_vertices, grafo)
  #print("\nA solucao é inicial gerada foi: ", solucao_inicial)
  print("Quantidade de cores da solução inicial: ", qtde_cores_solucao_inicial)

#   pr = cProfile.Profile()
#   pr.enable()
#   pesos = calcular_pesos(grafo)
#   ordem = sorteio_ponderado_sem_repeticao(grafo, pesos)
#   GRASP = gerar_solucao(ordem, grafo)
#   qnt_cores_GRASP = obj(GRASP)

#   print ("Quantidade de cores do GRASP fase de construção gulosa: ", qnt_cores_GRASP)

#   GRASP_busca_local , qnt_cores_GRASP_completo = busca_local(GRASP,grafo, annealing=False, )

#   print ("Quantidade de cores do GRASP após busca local: ", qnt_cores_GRASP_completo)
  
#   print("\n")
#   pr.disable()
#   s = io.StringIO()
#   sortby = SortKey.CUMULATIVE
#   ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#   ps.print_stats()
#   print(s.getvalue())

  pr = cProfile.Profile()
  pr.enable()
  inicio_simulated_annealing = time.time()
  solucao_simulated_annealing, qtde_cores_solucao_simulated_annealing = busca_local(
      solucao_inicial,grafo)
  fim_simulated_annealing = time.time()
  tempo_simulated_annealing = fim_simulated_annealing - inicio_simulated_annealing
  #print("Solução utilizando o simulated annealing: ", solucao_simulated_annealing)
  print("Quantidade de cores do simulated annealing: ",
        qtde_cores_solucao_simulated_annealing)
  print("Tempo gasto no simulated annealing: ", tempo_simulated_annealing,
        "segundos")

  pr.disable()
  s = io.StringIO()
  sortby = SortKey.CUMULATIVE
  ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
  ps.print_stats()
  print(s.getvalue())
  
  with open('Annealing_'+grammar_file, 'w') as f:
        # Substitui o print pelo write
        f.write(str(solucao_simulated_annealing) + "\n")
        f.write("Cores " + str(qtde_cores_solucao_simulated_annealing) + "\n")
        f.write(str(s.getvalue()) + "\n")


  print("\n")

#   inicio_vns = time.time()
#   solucao_vns, qtde_cores_solucao_vns = VNS(solucao_inicial,grafo)
#   fim_vns = time.time()
#   tempo_vns = fim_vns - inicio_vns
#   #print("Solução utilizando o VNS: ", solucao_vns)
#   print("Quantidade de cores do VNS: ", qtde_cores_solucao_vns)
#   print("Tempo gasto no VNS: ", tempo_vns, "segundos")

#   print("\n")

#   inicio_vns_annealing = time.time()
#   solucao_vns_annealing, qtde_cores_solucao_vns_annealing = VNS(
#       solucao_inicial,grafo, annealing=True)
#   fim_vns_annealing = time.time()
#   tempo_vns_annealing = fim_vns_annealing - inicio_vns_annealing
#   #print("Solução utilizando o VNS com o Annealing: ", solucao_vns_annealing)
#   print("Quantidade de cores do VNS com o Annealing: ",
#         qtde_cores_solucao_vns_annealing)
#   print("Tempo gasto no VNS com Annealing: ", tempo_vns_annealing, "segundos")

  print("\n")

  fim = time.time()
  tempo_total = fim - inicio
  print("Tempo de execução total: ", tempo_total, "segundos")


if __name__ == "__main__":
  main()