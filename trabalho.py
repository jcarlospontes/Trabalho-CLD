def xor_function(x,y):
	if (x == y):
		return 0
	else:
		return 1
		
def or_function(x,y):
	if ((x == 1) or (y == 1)):
		return 1
	else:
		return 0

def nand_function(x,y):
	if ((x == 1) or (y == 1)):
		return 1
	else:
		return 0

def and_function(x,y):
	if ((x == 0) or (y == 0)):
		return 0
	else:
		return 1

def not_function(x):
	if (x == 0):
		return 1
	else:
		return 0

entradas = []
saidas = []
gates = []
tabela = []
binarios = []

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
#tabela.append(entradas + saidas)

numero_linhas = 2**len(entradas)
numero_colunas = len(entradas + saidas)

def tabela_constructor():
	tabela.append(entradas + saidas)
	lim = 1
	cont = 0
	while lim <= numero_linhas:
		tabela.append([])
		while cont < numero_colunas:
			tabela[lim].append("coluna {}".format(cont+1))
			cont += 1
		lim += 1
		cont = 0

tabela_constructor()

def print_tabela():
	lim = 0
	while lim <= numero_linhas:
		print(tabela[lim])
		lim +=1

print_tabela()

def converte_binario():
	x = 0
	y = 0
	while x < numero_linhas:
		y = bin(x).replace("b","0")
		if x > 1:
			y = y[1:]
		binarios.append(y)
		x+=1
converte_binario()
def print_binarios():
	x = 0
	while x < numero_linhas:
		print(binarios[x])
		x +=1
print_binarios()
#print_tabela()
