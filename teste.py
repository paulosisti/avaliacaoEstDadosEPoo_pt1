from veiculo import Veiculo
from carro import Carro
from drone import Drone

#Não podemos instanciar um objeto de uma classe abstrata, erro.
#c1 = Veiculo() 

print("CARROS")
c2 = Carro("Fiat","Uno",4)
c2.imprimirInformacoes()

print("--------------------------")

print("DRONES")
c3 = Drone("Drone","DJ Mini",8)
c3.imprimirInformacoes()