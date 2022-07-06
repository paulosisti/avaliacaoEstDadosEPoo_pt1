from veiculo import Veiculo

class Carro(Veiculo):

  def __init__(self, marca, modelo, portas):
    super().__init__(marca, modelo)
    self.__portas = portas
  
  def imprimirInformacoes(self):
    super().imprimirInformacoes()
    print(f"Portas: {self.__portas}")
  
  def __repr__(self):
    return f"Marca: {self.marca}\nModelo: {self.modelo}\nPortas: {self.__portas}"