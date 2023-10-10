idades = [39, 30, 27, 18]

print(type(idades))
print(len(idades)) # tamanho - qtde de itens na lista
print(idades[0]) # ordem na fila - sempre começa em 0

idades.append(12) # adc ao final da lista
print(idades)

for idade in idades:
    print(idade)

idades.remove(12) # remove a primeira aparição - se tiver dois itens iguais, exclui apenas um
print(idades)

print(20 in idades) # pergunta ao programa se há esse item na lista - retorna bool
print(39 in idades)

if 39 in idades:
    idades.remove(39)
    print(idades)

idades.insert(0, 39) # insere um item após o index selecionado
idades.insert(2, 99)
print(idades)

idades.extend([10, 87]) # adc mais de um item a lista de uma vez
print(idades)

for idade in idades:
    print(idade + 1) # aumenta todos os itens da lista

idades_no_ano_que_vem = [] # cria lista vazia
for idade in idades:
  idades_no_ano_que_vem.append(idade+1)
print(idades_no_ano_que_vem)

idades_no_ano_que_vem = [idade+1 for idade in idades]
print(idades_no_ano_que_vem)

print([idade for idade in idades if idade > 21]) # condição apenas para maiores de 21

def faz_processamento_de_visualizacao(lista = list()):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

def faz_processamento_de_visualizacao(lista = []):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

