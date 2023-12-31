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

conta1 = ContaSalario(99)
conta2 = ContaSalario(99)

print(conta1 == conta2)
print(isinstance(ContaSalario(16), ContaSalario)) # verifica a igualdade com bool