'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema R1:
    ------------

    Uma senha s foi compartilhada entre duas pessoas. A primeira delas recebeu
    o par de inteiros (a,m) e a segunda recebeu o par (b,n), onde mdc(m,n) = 1
    e a,b,m,n foram calculados de modo que
        s ≡ a (mod m)
        s ≡ b (mod n)
    Implemente um programa que recebe os pares de inteiros (a,m) e (b,n) e
    (a) verifica se o sistema tem solução e informa isso ao usuário;
    (b) caso tenha solução s, a encontra através do método geométrico e imprime essa senha.
'''


def mdc(p, q):      # função auxiliar recursiva que retorna o MDC entre dois inteiros
    r = p % q
    if r == 0:
        return q
    return mdc(q, r)


#   Loop para entrada e validação dos dados
while 1:
    try:
        a, m = [int(x) for x in input("Entre o par (a, m) separado por espaço: ").split()]
        if (a >= m) or (a < 0) or (m < 2):
            raise ValueError
        print("(a, m) = (%d, %d)" % (a, m))
        b, n = [int(x) for x in input("Entre o par (b, n) separado por espaço: ").split()]
        if (b >= n) or (b < 0) or (n < 2):
            raise ValueError
        print("(b, n) = (%d, %d)" % (b, n))
        break
    except ValueError:
        print("Entrada inválida! Por favor, entre novamente os dados.")

# (a) para o sistema ter solução, é necessário que o MDC entre m e n seja = 1
MDC = mdc(m, n)
print("MDC(%d, %d) = %d" % (m, n, MDC))

if MDC != 1:
    print("O sistema não tem solução, pois m e n não são primos entre si.")
    exit()
print("...calculando...dependendo das entradas, isso pode levar alguns minutos...")

#  (b) simulação de preenchimento de matriz m X n para mimetizar o método geométrico
x = y = s = 0
while 1:
    #  print("(x, y) = (%d, %d)" % (x, y))  # debug
    if x == a and y == b:   # bingo! chegamos à linha (x) e coluna (y) dadas por (a, b)
        break
    # incrementa a linha (x), a coluna (y) e o resultado correspondente à posição (x, y)
    s += 1
    x += 1
    y += 1
    # sai do loop qdo percorrer toda a matriz
    if x == m and y == n:
        break
    # retorna para a posição 0 quando a posição na linha cai fora da matriz
    if x == m:
        x = 0
    # retorna para a posição 0 quando a posição na coluna cai fora da matriz
    if y == n:
        y = 0

print("Solução: s = %d" % s)






