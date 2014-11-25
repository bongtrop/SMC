'''
Register Class
Detail: Report working of Simulator
Date: 26/11/2014
Autor: Pongsakorn Sommalai
'''

class reportor:
  #Constructor
  def __init__(self, numMemory=0, startSign='@@@', mem=None, reg=None, pc=0):
    for i in range(0, numMemory):
      print "memory[" + str(i) + "]="+str(mem[i])

    self.numMemory = numMemory
    self.mem=mem
    self.reg=reg
    self.startSign = startSign
    self.pc = str(pc)
    self.n = 0

  #Update Memory and Register and pc
  def update(self, mem, reg, pc):
    self.mem = mem
    self.reg = reg
    self.pc = str(pc)
    self.n+=1

  #Report them on stdio
  def report(self):
    print "\n"+self.startSign
    print "state:"
    print "\tpc "+self.pc
    print "\tmemory:"

    for i in range(0, self.numMemory):
      print "\t\tmem[ " + str(i) + " ] " + str(self.mem[i])

    print "\tregisters:"

    for i in range(0, 8):
      print "\t\treg[ " + str(i) + " ] " + str(self.reg[i])

    print "end state"

  #Summary Simulator
  def summary(self):
    print "machine halted"
    print "total of " + str(self.n) + " instructions executed"
    print "final state of machine"

    self.report()
