##Three sample bayes nets are defined here. ##
from bnetbase import *

A = Variable('A', ['a', '-a'])
B = Variable('B', ['b', '-b'])
C = Variable('C', ['c', '-c'])
D = Variable('D', ['d', '-d'])
E = Variable('E', ['e', '-e'])
F = Variable('F', ['f', '-f'])
G = Variable('G', ['g', '-g'])
H = Variable('H', ['h', '-h'])
I = Variable('I', ['i', '-i'])

FA = Factor('P(A)', [A])
FA.add_values([['a', 0.9], ['-a', 0.1]])

FB = Factor('P(B|A,H)', [B, A, H])
FB.add_values([['b', 'a', 'h', 1], ['b', 'a', '-h', 0], ['b', '-a', 'h', 0.5], ['b', '-a', '-h', 0.6],
               ['-b', 'a', 'h', 0], ['-b', 'a', '-h', 1], ['-b', '-a', 'h', 0.5], ['-b', '-a', '-h', 0.4]])

FC = Factor('P(C|B,G)', [C, B, G])
FC.add_values([['c', 'b', 'g', 0.9], ['c', 'b', '-g', 0.9], ['c', '-b', 'g', 0.1], ['c', '-b', '-g', 1],
               ['-c', 'b', 'g', 0.1], ['-c', 'b', '-g', 0.1], ['-c', '-b', 'g', 0.9], ['-c', '-b', '-g', 0]])

FD = Factor('P(D|C,F)', [D, C, F])
FD.add_values([['d', 'c', 'f', 0], ['d', 'c', '-f', 1], ['d', '-c', 'f', 0.7], ['d', '-c', '-f', 0.2],
               ['-d', 'c', 'f', 1], ['-d', 'c', '-f', 0], ['-d', '-c', 'f', 0.3], ['-d', '-c', '-f', 0.8]])

FE = Factor('P(E|C)', [E, C])
FE.add_values([['e', 'c', 0.2], ['e', '-c', 0.4],
               ['-e', 'c', 0.8], ['-e', '-c', 0.6]])

FF = Factor('P(F)', [F])
FF.add_values([['f', 0.1], ['-f', 0.9]])

FG = Factor('P(G)', [G])
FG.add_values([['g', 1], ['-g', 0]])

FH = Factor('P(H)', [H])
FH.add_values([['h', 0.5], ['-h', 0.5]])

FI = Factor('P(I|B)', [I, B])
FI.add_values([['i', 'b', 0.3], ['i', '-b', 0.9],
               ['-i', 'b', 0.7], ['-i', '-b', 0.1]])
Q4 = BN('Sample', [A,B,C,D,E,F,G,H,I], [FA,FB,FC,FD,FE,FF,FG,FH,FI])

if __name__ == '__main__':
    #(a)
    print("Test 1 ....", end = '')
    A.set_evidence('a')
    probs = VE(Q4, B, [A])
    print('P(b|a) = {} P(-b|a) = {}'.format(probs[0], probs[1]))

    #(b)
    print("Test 2 ....", end = '')
    A.set_evidence('a')
    probs = VE(Q4, C, [A])
    print('P(c|a) = {} P(-c|a) = {}'.format(probs[0], probs[1]))

    #(c)
    print("Test 3 ....", end = '')
    A.set_evidence('a')
    E.set_evidence('-e')
    probs = VE(Q4, C, [A, E])

    print('P(c|a,-e) = {} P(-c|a,-e) = {}'.format(probs[0],probs[1]))

    #(d)
    print("Test 4 ....", end = '')
    A.set_evidence('a')
    F.set_evidence('-f')
    probs = VE(Q4, C, [A, F])

    print('P(c|a,-f) = {} P(-c|a,-f) = {}'.format(probs[0],probs[1]))

