import translator

#nand gate
def nand(a, b):

  a = translator.com2s2bin(a)
  b = translator.com2s2bin(b)

  result = ""

  for i in range(0,32):
    if (not (a[i] and b[i])):
      result+='1'
    else:
      result+='0'

  return int(result, 2)

#adder
def add(a, b):
  return a+b

#get zero bit
def equal(a, b):
  return a==b
