import numpy as np
def pilha_maior_elemento(pilha):
    maior = pilha[0]
    for i in range(len(pilha)):
        if pilha[i] > maior:
            maior = pilha[i]
    return maior


elementos = pilha_maior_elemento([1000, 435, 576, 12, 9])
print(elementos)
