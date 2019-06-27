def xor_function(x,y):
	if x == y:
		return 0
	else:
		return 1
		
def or_function(x,y):
	if (x == 1) or (y == 1):
		return 1
	else:
		return 0

def and_function(x,y):
	if x == 0 or y == 0:
		return 0
	else:
		return 1

def not_function(x):
	if x == 0:
		return 1
	else:
		return 0

entradas = []
saidas = []
gates = []

def ler_entrada():
	f = open("entrada.txt", "r")
	lines = f.readlines()
	x = lines[0].split(",")
	num = x[1]
	num = int(num)
	lim = 2
	while lim <= num + 1:
		entradas.append(x[lim].rstrip('\n'))
		lim += 1
	f.close()

def ler_saida():
	f = open("entrada.txt","r")
	lines = f.readlines()
	x = lines[1].split(",")
	num = x[1]
	num = int(num)
	lim = 2
	while lim <= num + 1:
		saidas.append(x[lim].rstrip('\n'))
		lim += 1
	f.close()
	
def ler_gates():
	f = open("entrada.txt","r")
	lines = f.readlines()
	x = lines[2].split(",")
	num = x[1]
	num = int(num)
	lim = 2
	while lim <= num + 1:
		gates.append(x[lim].rstrip('\n'))
		lim += 1
	f.close()
	
ler_entrada()
ler_saida()
ler_gates()
