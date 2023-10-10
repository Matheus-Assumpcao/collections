# Tuplas - Lista com valores imutaveis - ex: data de nascimento, agencia de banco e etc
# Lista - Lista com valores mutaveis - ex: saldo em conta, data e etc

class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


conta_do_gui = ContaCorrente(15)
print(conta_do_gui)

conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]

print(contas[0])

conta_do_gui.deposita(100)

print(contas[0])

print(conta_do_gui)

print(contas[2])

contas[2].deposita(300)

print(conta_do_gui)

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
#deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0, 76)
print(contas[0], contas[1], contas[2])

#deposita_para_todas(contas)
print(contas[0], contas[1], contas[2])

guilherme = ('Guilherme', 37, 1981)  # tupla
daniela = ('Daniela', 31, 1987)
# paulo = (39, 'Paulo', 1979) # ruim, pois, não segue um padrão

#guilherme.append(6754) # não é possivel realizar um append em uma tupla

conta_do_gui = (15, 1000)
# conta_do_gui.deposita() # variação OO
conta_do_gui[1]

#conta_do_gui[1] += 100

def deposita(conta):  # variação "funcional"(separando o comportamento dos dados) - aqui é possivel alterar o valor de um item da tupla
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

###############################################################################################################
print("Nova parte:")
deposita(conta_do_gui)

conta_do_gui

conta_do_gui = deposita(conta_do_gui)
conta_do_gui

usuarios = [guilherme, daniela]
usuarios.append(('Paulo', 39, 1979)) # adc um novo usuario criado com tupla em uma lista
print(usuarios)

usuarios[0] = 'Guilherme Silveira' # alteração no item 0 da tupla
print(usuarios[0])
print(usuarios)

###############################################################################################################
print("Nova etapa: ")
conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(234876)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)

for conta in contas:
    print(conta)

contas[0].deposita(300) # alteração no saldo da conta que está em uma tupla

for conta in contas:
    print(conta)

###############################################################################################################
print("Nova etapa - enumerated, range e desempacotamento de tuplas: ")

idades = [15, 87, 65, 56, 32, 49, 37]

for idade in idades:
  print(idade)

idades = [15, 87, 32, 65, 56, 32, 49, 37]

print(range(len(idades)))
for i in range(len(idades)):
  print(i)

for i in range(len(idades)):
  print(i, idades[i])

list(range(len(idades))) # forcei a geração dos valores - obs: adc print quando testar
list(enumerate(idades))

for valor in enumerate(idades):
  print(valor)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # ja desempacotando - escolhendo apenas um item
  print(nome)

print("ou")

for nome,_,_ in usuarios: # ja desempacotando, ignorando o resto sem precisar escrever a variavel
  print(nome)

###############################################################################################################
print("Nova etapa - Ordem natural: ")

print(sorted(idades)) # ordem crescente
print(list(reversed(idades))) # ordem decrescente
sorted(idades, reverse=True)
list(reversed(sorted(idades)))

print(idades) # não salva a ordenação

idades.sort() # ordena e salva a lista
print(idades)

###############################################################################################################
print("Nova etapa - Ordem Customizada e Total: ")


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
    print(conta)

sorted(contas)

conta_do_guilherme < conta_da_daniela


def extrai_saldo(conta):
    return conta._saldo


for conta in sorted(contas, key=extrai_saldo):
    print(conta)

from operator import attrgetter

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

conta_do_guilherme < conta_da_daniela


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        return self._saldo < outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

conta_do_guilherme < conta_da_daniela

conta_do_guilherme > conta_da_daniela

for conta in sorted(contas):
    print(conta)

for conta in sorted(contas, reverse=True):
    print(conta)

