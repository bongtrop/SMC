'''
Translator Class
Detail: Translator Dec Instruction to our Data Structure
Date: 24/11/2014
Autor: Pongsakorn Sommalai
'''

class translator:
  #Constructor ins_type tell type of each instruction
  def __init__(self, ins_type = ['R', 'R', 'I', 'I', 'I', 'J', 'O', 'O']):
    self.ins_type = ins_type

  #Method change int to bin by 2's complement
  def com2s2bin(self, x):
    if x < 0:
      result = bin((eval("0b"+str(int(bin(x)[3:].zfill(4).replace("0","2").replace("1","0").replace("2","1"))))+eval("0b1")))[2:].zfill(4)
      result = (32-len(result))*'1' + result
    else:
      result = bin(x)[2:].zfill(4)
      result = (32-len(result))*'0' + result

    return result

  #Method change bin to by int 2's complement
  def bin2com2s(self, bin):
    x = int(bin, 2)
    if bin[0] == '1': # "sign bit", big-endian
       x -= 2**len(bin)
    return x

  #Method translate
  def translate(self, x):
    tran = self.com2s2bin(x)
    op = tran[7:10]

    result = {}
    result["op"] = int(op, 2)
    result["type"] = self.ins_type[result["op"]]
    if (result["type"]=='R'):
      result["rs"] = int(tran[10:13], 2)
      result["rt"] = int(tran[13:16], 2)
      result["rd"] = self.bin2com2s(tran[-3:])
    elif(result["type"]=='I'):
      result["rs"] = int(tran[10:13], 2)
      result["rt"] = int(tran[13:16], 2)
      result["offset"] = self.bin2com2s(tran[16:])
    elif(result["type"]=='J'):
      result["rs"] = int(tran[10:13], 2)
      result["rd"] = int(tran[13:16], 2)

    return result
