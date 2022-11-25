
def compara_pilhas(pilha1, pilha2):
    if pilha1 == pilha2:
        return True
    else:
        return False


pilha1 = compara_pilhas([88, 89, 90, 91], [88, 89, 90])
pilha2 = compara_pilhas([-1, -2, -4], [-1, -2, -4])
print(pilha1)
print(pilha2)
