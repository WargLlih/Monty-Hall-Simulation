import random
import sys

def zonks(portas, porta_premiada, jogador_escolha):
  open = []
  for p in portas:
    if p == porta_premiada: continue 
    if p == jogador_escolha: continue
    open.append(p) # add para essa lista as porta que podem ser abertas
    return random.choice(open) #escolhe aleatoriamente uma dessas portas


def switch(troca:int, portas, porta_zonk, jogador_escolha):
  for p in portas:
    if p == porta_zonk: continue
    if p == jogador_escolha: continue
    porta_alternativa = p
  if troca:
    return porta_alternativa
  else:
    return jogador_escolha
    

def main(num_testes, troca:int):
  sem_troca = com_troca = 0
  for n in range(num_testes):
    #PREPARACAO PARA O SHOW
    portas = [0, 1, 2]
    porta_premiada = random.choice(portas)

    #ESCOLHA INICIAL DO JOGADOR
    jogador_escolha = random.choice(portas)

    #ABRINDO A PORTA
    porta_zonk = zonks(portas, porta_premiada, jogador_escolha)

    #SEGUNDA ESCOLHA DO JOGADOR
    escolha_final = switch(troca, portas, porta_zonk, jogador_escolha)
    if escolha_final == porta_premiada:
      if troca:
        com_troca += 1
      else:
        sem_troca += 1
  if troca:
    return com_troca
  else:
    return sem_troca



numero_de_testes = int(sys.argv[1])


print('chance de ganhar sem trocar:', main(numero_de_testes, 0)/numero_de_testes)
print('chance de ganhar trocando:', main(numero_de_testes, 1)/numero_de_testes)


