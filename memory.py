'''
Memory Class
Detail: Simulator Memory
Date: 24/11/2014
Autor: Pongsakorn Sommalai
'''

class memory:
  #Constructor
  def __init__(self , n=65536, ins=[]):
    self.mem = [0] * n
    c = 0
    for i in ins:
      self.mem[c] = int(i)
      c+=1

  #Method set memory
  def set(self, index, value):
    self.mem[index] = value

  #Method get memory
  def get(self, index):
    return self.mem[index]

  #Method get All mem
  def getAll(self):
    return self.mem
