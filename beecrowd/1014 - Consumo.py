distancia = float(input())
combustivel = float(input())
consumo = distancia / combustivel

# .3f para 3 casas decimais 
print(f"{consumo:.3f} km/l")