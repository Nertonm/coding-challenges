def calcular_media(notas):
    if len(notas) == 1:
        return notas[0] / 2
    if len(notas) == 2:
        return (notas[0] + notas[1]) / 2
    if len(notas) == 3:
        return (notas[0] + notas[1] + notas[2]) / 3
    if len(notas) == 4:
        notas.sort()
        notas.pop(0)
        return (notas[0] + notas[1] + notas[2]) / 3
    return 0
    
N = int(input())
resultado_alunos = []
for i in range(N):
    nome = input()
    nota_str = input().split()
    notas = []
    for nota in nota_str:
        nota_float = float(nota)
        notas.append(nota_float)
    media = calcular_media(notas)
    resultado_alunos.append(f"{nome}: {media:.1f}")

for resultado in resultado_alunos:
    print(resultado)