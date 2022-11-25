def TPilha2(N, P, vetor):
    for i in range(len(vetor)):
        if vetor[i] == 0:
            if len(N) > 0:
                print(f"Valor retirado: {N[len(N)-1]}")
                N.pop()
            if len(P) > 0:
                print(f"Valor retirado: {P[len(P) - 1]}")
                P.pop()
        elif vetor[i] > 0:
            P.append(vetor[i])
        else:
            N.append(vetor[i])

    print(f"Os valores negativos: {N}. Os valores positivos: {P}")


parametros = TPilha2([], [], [5, -2, 2, 5, -4, -7, 9, 1, -7, 0, -1])
