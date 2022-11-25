def TPilha(vetor):
    pilha = []

    if len(vetor) == 15:
        for i in range(len(vetor)):
            if vetor[i] % 2 == 0:
                pilha.append(vetor[i])
            else:
                if len(pilha) > 0:
                    continue

        for i in range(len(pilha)):
            print(pilha.pop(0))


x = TPilha([11, 54, 38, 22, 12, 42, 73, 45, 72, 182, 133, 243, 453, 563, 573])
