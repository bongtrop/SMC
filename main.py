'''
Main Class
Detail: Start Simulator
Date: 25/11/2014
Autor: Pongsakorn Sommalai
'''

import sys
import register
import memory
import alu
import translator
import reportor

# Check Input Argument
if len(sys.argv)!=2:
  print "[-] Usage: python " + sys.argv[0] + " [Assembly File]"

#Get all line from input file
input_file = sys.argv[1]
lines = [e.strip() for e in open(input_file)]

#Init class
mem = memory.memory(ins=lines)
reg = register.register()
tran = translator.translator()
re = reportor.reportor(numMemory=len(lines), startSign='@@@', mem=mem.getAll(), reg=reg.getAll(), pc=0)

#Init variable
exited = False
pc = 0

re.report()

#Start Simulator
while not exited:
  #Fetch ins from mem and translate it
  ins = mem.get(pc)
  pc+=1
  ins = tran.translate(ins)

  #Check opcode and do it
  if ins["op"]==0:
    a = reg.get(ins["rs"])
    b = reg.get(ins["rt"])
    reg.set(ins["rd"], alu.add(a, b))
  elif ins["op"]==1:
    a = reg.get(ins["rs"])
    b = reg.get(ins["rt"])
    reg.set(ins["rd"], alu.nand(a, b))
  elif ins["op"]==2:
    a = reg.get(ins["rs"])
    offset = ins["offset"]
    addr = alu.add(a, offset)
    reg.set(ins["rt"], mem.get(addr))
  elif ins["op"]==3:
    a = reg.get(ins["rs"])
    b = reg.get(ins["rt"])
    offset = ins["offset"]
    print ins["offset"]
    addr = alu.add(a, offset)
    mem.set(addr, b)
  elif ins["op"]==4:
    a = reg.get(ins["rs"])
    b = reg.get(ins["rt"])
    offset = ins["offset"]
    if (alu.equal(a, b)):
      pc = pc+offset
  elif ins["op"]==5:
    reg.set(ins["rd"], pc)
    a = reg.get(ins["rs"])
    pc = a
  elif ins["op"]==6:
    exited = True

  re.update(mem.getAll(), reg.getAll(), pc)
  re.report()

re.summary()
