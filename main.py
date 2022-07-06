from carro import Carro
from drone import Drone
from fila import Fila

filaCarros = Fila()
filaDrones = Fila()

import os
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionarCarro():
  while True:
    carroMarca = input("Digite a marca do carro: ").upper()
    carroModelo = input("Digite o modelo: ").upper()
    carroPortas = input("Digite a quantidade de portas: ").upper()
    limpa_tela()
    if carroMarca:
      newCarro = Carro(carroMarca,carroModelo,carroPortas)
      filaCarros.adicionar(newCarro)
      break

def adicionarDrone():
  while True:
    DroneMarca = input("Digite a marca do drone: ").upper()
    DroneModelo = input("Digite o modelo: ").upper()
    DroneHelices = input("Digite a quantidade de helices: ").upper()
    limpa_tela()
    if DroneMarca:
      newDrone = Drone(DroneMarca,DroneModelo,DroneHelices)
      filaDrones.adicionar(newDrone)
      break

def removerCarro():
  filaCarros.remover()

def removerDrone():
  filaDrones.remover()

def relatorioCarros():
  print(">> Fila Carros <<\n")
  filaCarros.imprimir()

def relatorioDrones():
  print(">> Fila Drones <<\n")
  filaDrones.imprimir()

while True:
    
    print("""             
            MENU
    [0]	Finalizar o Programa
    [1]	Adicionar Carro
    [2]	Adicionar Drone
    [3]	Relatório Carros
    [4] Relatório Drones
    [5]	Remover Carro
    [6] Remover Drone
        """)

    escolha = input("    Escolha uma opção: ")
    limpa_tela()

    if escolha == '0':
      print("Programa Encerrado!")
      break
    if escolha == '1':
      adicionarCarro()
    if escolha == '2':
      adicionarDrone()
    if escolha == '3':
      relatorioCarros()
    if escolha == '4':
      relatorioDrones()
    if escolha == '5':
      removerCarro()
    if escolha == '6':
      removerDrone()    