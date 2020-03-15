class Prato():
  def __init__(self,nome,volume):     
    self.nome = nome
    self.volume = volume
    self.estácheio = False
    self.estálimpo = True
  def encher_prato(self):
    self.estácheio = True
    self.estálimpo = False
  def esvaziar_prato(self):
    self.estácheio = False
  def cor(self,cor):
    self.cor = cor
  def limpo(self):
    self.estálimpo = True
  def sujo(self):
    self.estálimpo = False
