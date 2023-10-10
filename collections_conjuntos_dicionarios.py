# Operação de conjuto

class OperacaoSet:
    usuarios_data_science = [15, 23, 43, 56]
    usuarios_machine_learning = [13, 23, 56, 42]

    assistiram = usuarios_data_science.copy()
    assistiram.extend(usuarios_machine_learning)
    assistiram

    len(assistiram)

    set(assistiram) # set - retira o item duplicado, coloca em ordem aleatoria e nao possui index
    set([1,2,3,1])

    usuarios_data_science = {15, 23, 43, 56}
    usuarios_machine_learning = {13, 23, 56, 42}

    usuarios_machine_learning

    for usuario in set(assistiram):
        print(usuario)

    print(usuarios_data_science | usuarios_machine_learning) # | - ou

    print("A partir daqui começa outras operações de conjutos: ")

    print(usuarios_data_science & usuarios_machine_learning) # & - e
    print(usuarios_data_science - usuarios_machine_learning)

    fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
    print(15 in fez_ds_mas_nao_fez_ml)

    print(usuarios_data_science ^ usuarios_machine_learning)

    print("###################################")
    print("^--Aqui acaba a Primeira Classe--^")
    print("###################################")
    print("v--Aqui começa a Segunda Classe--v")

class FrozenSet:

    usuarios = {1, 5, 76, 34, 52, 13, 17}
    len(usuarios)

    usuarios.add(13)
    len(usuarios)

    usuarios.add(765)
    len(usuarios)
    print(usuarios)

    usuarios = frozenset(usuarios)
    print(usuarios)
    type(usuarios)

    meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
    set(meu_texto.split())