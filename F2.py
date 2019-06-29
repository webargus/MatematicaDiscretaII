'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema F2:
    ------------

    Implemente o gerador de números pseudo-aleatórios Middle-Square:
    Dada a semente = X0 , tem-se Xn+1 = dois algarismos centrais de Xn**2.

'''


def middle_square(x0):
    r = []  # lista para acumular números randômicos gerados
    while 1:    # gera randoms até sequência se repetir
        x0 = x0 ** 2  # eleva semente ao quadrado
        s = str(x0)  # converte nova semente em cadeia de caracteres numéricos
        # completa com 1 zero à esquerda caso semente não tenha nº par de algarismos
        if len(s) & 1 == 1:
            s = '0' + s
        # toma substring de comprimento=2 a partir de um caracter à esquerda do meio da string
        init = len(s) // 2 - 1
        s = s[init:init + 2]
        # retorna lista formatada para impressão se semente já ocorreu antes
        if s in r:
            return (", ".join(r))
        r.append(s)  # acumula resultado na lista de resultados
        x0 = int(s)  # transforma string em inteiro e repete o loop










