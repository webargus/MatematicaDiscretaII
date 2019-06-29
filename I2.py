
'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema I2:
    ------------

    Teste de primalidade - Método ingênuo
    Escreva um programa que recebe um inteiro n > 1 e que verifica, através de divisões
    sucessivas se este inteiro é um número primo.

    OBS: por falta de uma definição precisa do que seja o método ingênuo, implementamos duas
    funções, is_prime e is_prime_naif; ambas verificam a primalidade através de divisões
    sucessivas, sendo que a primeira (is_prime) descarta a verificação dos pares, testa a
    divisibilidade apenas por inteiros ímpares e executa a verificação somente até a raiz quadrada
    do inteiro cuja primalidade queremos verificar.
'''

from threading import  Thread

# função auxiliar para verificar se um inteiro é primo
# algoritmo seletivo(ingênuo?): descarta o teste de divisibilidade quando o inteiro é par e
# verifica divisibilidade por inteiros ímpares somente até a raiz quadrada do número
def is_prime(nn):
    if nn == 2:     # retorna True pois 2 é primo
        return True
    if nn % 2 == 0:     # descarta os pares
        return False
    for div in range(3, int(nn**.5) + 1, 2):        # testa divisibilidade até raiz de n
        if nn % div == 0:
            return False
    return True


# função para verificar se um inteiro é primo
# algoritmo ingênuo (?): testa divisibilidade por todos os inteiros de 3 até n-1
def is_prime_naif(nn):
    if nn == 2:     # retorna True pois 2 é primo
        return True
    for div in range(3, nn):     # verifica divisibilidade desde 3 até n-1, inclusive pelos pares
        if nn % div == 0:
            return False
    return True


# funções auxiliares para realizar a primalidade em threads e evitar o travamento
# do processo, dependendo do inteiro pesquisado

def _is_prime_thread(n, callback):
    callback(is_prime(n), n)


def is_prime_naif_thread(n, callback):
    callback(is_prime_naif(n), n)


def check_prime_thread(n, option, callback):
    if option == 0:
        thread = Thread(target=_is_prime_thread, args=(n, callback))
    else:
        thread = Thread(target=is_prime_naif_thread, args=(n, callback))
    thread.start()




