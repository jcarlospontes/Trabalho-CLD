#Função que lê uma lista "xor" e retorna um valor.
def xor_function(lista, *args):
	zero = False
	for x in lista:
		if x == 0:
			zero = True
	if zero == True and sum(lista) > 0:
		return 1
	else:
		return 0

#Função que lê uma lista "nor" e retorna um valor.
def nor_function(lista, *args):
	if sum(lista) == 0:
		return 1
	else:
		return 0

#Função que lê uma lista "or" e retorna um valor.
def or_function(lista, *args):
	if sum(lista) == 0:
		return 0
	else:
		return 1

#Função que lê uma lista "nand" e retorna um valor.
def nand_function(lista, *args):
	alerta = False
	for x in lista:
		if x == 0:
			alerta = True
	if alerta == True:
		return 1
	else:
		return 0

#Função que lê uma lista "and" e retorna um valor.
def and_function(lista, *args):
	zero = False
	for x in lista:
		if x == 0:
			zero = True
	if zero == True:
		return 0
	else:
		return 1

#Fução que transforma 0 em 1 e 1 em 0.
def not_function(valor):
	if (valor == 0):
		return 1
	else:
		return 0


entradas = []
saidas = []
entradas_e_saidas = []
lista_copia = []
gates = []
tabela = []
binarios = []
comportamento = []
linha = []

#Função que lê os nomes de entrada das portas lógicas do arquivo de descrição.
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

#Função que lê os nomes de saidas das portas lógicas do arquivo de descrição.
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

#Função que lê os nomes das portas lógicas do arquivo de descrição.
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

def ler_gates_comportamento():
	f = open("entrada.txt","r")
	lines = f.readlines()
	lim = 3
	while lim <= len(gates)+2:
		comportamento.append(lines[lim].rstrip('\n').split(','))
		lim +=1
	f.close()

ler_entrada()
ler_saida()
ler_gates()
ler_gates_comportamento()
entradas_e_saidas = entradas + gates + saidas
numero_linhas = 2**len(entradas)
numero_colunas = len(entradas + saidas + gates)

#Função que constroi o "corpo" da matriz onde será alocada a tabela verdade.
def tabela_constructor():
	lim = 0
	cont = 0
	while lim <= numero_linhas:
		tabela.append([])
		while cont < numero_colunas:
			tabela[lim].append("null")
			cont += 1
		lim += 1
		cont = 0


def print_tabela():
	lim = 0
	print(entradas_e_saidas)
	while lim < numero_linhas:
		print(tabela[lim])
		lim +=1

tabela_constructor()

def converte_binario():
	i = 0
	j = 0
	cont = 0
	repete = numero_linhas/2
	colunas = len(entradas)-1
	while j <= colunas:
		while i < numero_linhas:
			while cont < repete:
				tabela[i][j] = 0
				cont +=1
				i +=1
			cont = 0
			while cont < repete:
				tabela[i][j] = 1
				cont += 1
				i += 1
			cont = 0
		repete = repete/2
		i = 0
		j += 1

converte_binario()
print_tabela()

print(comportamento[0].index("A"))

def copia_lista():
	i = len(entradas)
	j = 0
	lista_copia.extend(entradas_e_saidas)
	while i < len(lista_copia) - 2:
		if comportamento[j][2] in lista_copia:
			i +=1
			j += 1
			continue
		lista_copia[i] = comportamento[j][2]
		i +=1
		j += 1

copia_lista()
