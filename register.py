'''
Register Class
Detail: Simulator Register
Date: 24/11/2014
Autor: Pongsakorn Sommalai
'''

class register:
  #Constructor
  def __init__(self , n=8):
    self.reg = [0] * n

  #Method set register
  def set(self, index, value):
    self.reg[index] = value

  #Method get register
  def get(self, index):
    return self.reg[index]

  #Get All
  def getAll(self):
    return self.reg
