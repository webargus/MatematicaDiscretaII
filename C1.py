
'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema C1:
    ------------

    Primeira sequência de Recamán: Subtraia se for possível; caso contrário, some.
    A primeira sequência de Recamán é definida da seguinte forma:
    • R(0) = 0
    • R(n+1) = R(n) − n, se esse número não for um dos anteriores.
      Caso contrário, R(n+1) = R(n) + n.
    Escreva um programa que recebe um inteiro n ≥ 0 e retorne uma lista com os
    n + 1 primeiros números da primeira sequência de Recamán.
'''


def recaman(n):
    s = [0]
    for i in range(1, n+1):
        ri = s[i-1] - i
        if (ri < 0) or (ri in s):
            ri = s[i-1] + i
        s.append(ri)

    return "R(%d)=" % (n+1) + ",".join([str(x) for x in s])







