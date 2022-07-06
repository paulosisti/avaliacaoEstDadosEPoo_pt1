from numpy import deprecate_with_doc


class No:
  def __init__(self, dado):
    self.dado = dado
    self.proximo = None