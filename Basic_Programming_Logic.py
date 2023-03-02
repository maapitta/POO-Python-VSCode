
'''
Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada
uma lista e três itens e retorna 1, se os três itens estiverem armazenados
na lista, e 0 caso contrário.
'''


def pertence(lista, item1, item2, item3):
    try:
        lista.index(item1)
        lista.index(item2)
        lista.index(item3)
        return 1
    except:
        return 0

'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada
uma tupla e dois itens (velho e novo) e retorna uma tupla onde todas as
ocorrências do item velho são substituídas pelo item novo.
'''


def substituir(tupla, velho, novo):
    lista = list(tupla)
    try:
        repeat = lista.count(velho)
        for x in range(repeat):
            pos = lista.index(velho)
            lista.remove(velho)
            lista.insert(pos,novo)
        tuplaNova = tuple(lista)
        return tuplaNova
    except ValueError:
        print('O valor não se encontra na tupla')

'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''


def posicoes(tupla, item):
    pass