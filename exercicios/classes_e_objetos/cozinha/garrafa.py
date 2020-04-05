class Garrafa():
  def __init__(self,nome):
    self.nome = nome
    self.estácheio = False
    self.estálimpo = True
  def encher_garrafa(self):
    self.estácheio = True
    self.estálimpo = False 
  def esvaziar_garrafa(self):
    self.estácheio = False
  def limpar_garrafa(self):
    self.estálimpo = True
  def volume(self,volume):
    self.volume = volume

    
