from veiculo import Veiculo

class Drone(Veiculo):

  def __init__(self, marca, modelo, helices):
    super().__init__(marca, modelo)
    self._helices = helices
  
  def imprimirInformacoes(self):
    super().imprimirInformacoes()
    print(f"Hélices: {self._helices}")
  
  def __repr__(self):
    return f"Marca: {self.marca}\nModelo: {self.modelo}\nHélices: {self._helices}"