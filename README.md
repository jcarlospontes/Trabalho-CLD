# Trabalho-CLD

Programa feito para a cadeira de Circuitos Lógicos Digitais 2019.1

Exercício Computacional 1

Objetivo: Escrever um programa de computador em Python que recebe como entrada um arquivo texto (.txt)
e gera como saída outro arquivo de texto. O arquivo texto de entrada deve conter descrição
nominal de um circuito digital combinatório, no formato descrito e exemplificado no exemplo
dado anexo. O arquivo texto gerado como saída deve apresentar a Tabela Verdade do circuito combinatório.


Exemplo de descrição de circuito:


% Linhas iniciando com % são linhas de comentários.

% Circuito 1 - Somador completo

% Parte 1: dados quantitativo de ids do circuito.

n_entr,3,Cin,A,B

n_said,2,S,Cout

n_gate,5,gi,g2,g3,g4,g5

% Parte 2 da descrição: interconexões (ID do gate,tipo, saída, lista de entradas; y1 é a saída do gate g1).

g1,xor,y1,A,B

g2,xor,S,y1,Cin

g3,and,y3,y1,Cin

g4,and,y4,B,A

g5,or,Cout,y3,y4
