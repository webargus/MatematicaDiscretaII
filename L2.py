'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema L2:
    ------------

    Escreva um programa que recebe duas cadeias de bits x e y e retorna
    as cadeias x OR y, x XOR y e x AND y, onde essas operações são realizadas bit a bit.

'''


def bloco1_logica_l2(x, y):
    return [x | y,   # executa operação OR bit a bit do Python
            x ^ y,   # executa operação XOR bit a bit do Python
            x & y    # executa operação AND bit a bit do Python
            ]




