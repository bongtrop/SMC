===
SMC
===

8-register, 32-bit Computer Simulator (Computer Architecture Project)

Written by Pongsakorn Sommalai <bongtrop@gmail.com>.

All code is under a BSD-style license, see LICENSE for details.

Source: https://github.com/bongtrop/SMC


Simulator Detail
================

  Machine Language use decimal number for each  instruction use newline for split instruction

  Example Input File:

    8454151
    9043971
    655361
    16842754
    16842749
    29360128
    25165824
    5
    -1
    2


  ------------------------
  Instruction have 3 class
  ------------------------

    R-type instructions
      Bits 24-22 opcode
  		Bits 21-19 reg A (rs)
  		Bits 18-16 res B (rt)
  		Bits 15-3 dont use
  		Bits 2-0  destReg (rd)

    I-type instructions
  		Bits 24-22 opcode
  		Bits 21-19 reg A (rs)
  		Bits 18-16 reg B (rt)
  		Bits 15-0 offsetField (2's complement)

    J-Type instructions
      Bits 24-22 opcode
  		Bits 21-19 reg A (rs)
  		Bits 18-16 reg B (rd)
  		Bits 15-0 dont use

    O-type instructions
      Bits 24-22 opcode
  		Bits 21-0 dont use


  ------------------------
  Instruction of Simulator
  ------------------------

    Name : Opcode : Type : Action

    add : 000 : R : add rs with rt save in rd
    nand : 001 : R : nand rs with rt save in rd
    lw : 010 : I : load memory address offset+rs save in rt
    sw : 011 : I : store register rt to memory address offset+rs
    beq : 100 : I : if rs=rt move pc to pc+1+offset
    jalr : 101 : J : store pc+1 to rd and move pc to rs
    halt : 110 : O : exit
    noop : 111 : O : do noting


  ---------------
  Have 8 Register
  ---------------

    $0, $1, $2, $3, $4, $5, $6, $7
    For all init by zero


  -----------------------
  Memory have 65536 words
  -----------------------


Requirements
============

python >= 2.7


Usage
=====

  > main.py [INPUT ASSEMBLY FILE]

or you can print output to file

  > main.py [INPUT ASSEMBLY FILE] > [OUTPUT]


Class
=====

----
Main
----

Start Simulator


----
Memory
----

Simulator Memory


----
Register
----

Simulator Register


----
ALU
----

Simulator ALU


----
Translator
----

Translator Dec Instruction to our Data Structure


----
Reportor
----

Report working of Simulator
