from abc import ABCMeta, abstractmethod

class Veiculo(metaclass = ABCMeta):

  def __init__(self, marca, modelo):
      self.marca = marca
      self.modelo = modelo

  @abstractmethod
  def imprimirInformacoes(self):
    print(f"Marca: {self.marca}\nModelo: {self.modelo}")
