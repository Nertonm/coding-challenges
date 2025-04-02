import sys
import math

# O GCD de dois números é o maior número que divide ambos
def get_gcd(a, b):
    return math.gcd(a, b)

# O LCM de dois números é o menor número que é múltiplo de ambos
# O LCM pode ser calculado usando a fórmula: LCM(a, b) = (a * b) // GCD(a, b)
def get_lcm(a, b):
    return a * b // get_gcd(a, b)

# A função get_divisors retorna todos os divisores de um número T
# A complexidade é O(sqrt(T)), pois percorre até a raiz quadrada de T
# Para cada divisor i encontrado, adiciona também T // i
# Isso garante que todos os divisores são encontrados
def get_divisors(T):
    divisors = set()
    for i in range(1, int(math.isqrt(T)) + 1):
        if T % i == 0:
            divisors.add(i)
            divisors.add(T // i)
    return divisors

def solve():
    for line in sys.stdin:
        # Lê cada linha da entrada padrão
        parts = line.strip().split()
        if len(parts) < 3:
            continue
        # Converte os primeiros três elementos para inteiros
        T, A, B = map(int, parts[:3])
        # Se T, A e B forem zero, encerra o loop
        if T == 0 and A == 0 and B == 0:
            break

        divisors = sorted(get_divisors(T))
        valid_times = []
        
        # Calcula o LCM de A e B
        lcm_ab = get_lcm(A, B)
        for d in divisors:
            # Verifica se o LCM de LCM(A, B) e d é igual a T
            lcm_abc = get_lcm(lcm_ab, d)
            # Se o LCM for igual a T, adiciona d à lista de tempos válidos
            # Isso significa que d é um divisor de T e também é um múltiplo do LCM(A, B)
            # Isso garante que o tempo d é um múltiplo comum de A e B e também é um divisor de T
            if lcm_abc == T:
                valid_times.append(d)
        # Ordena os tempos válidos
        valid_times = sorted(valid_times)
        # Imprime os tempos válidos
        print(' '.join(map(str, valid_times)))
solve()