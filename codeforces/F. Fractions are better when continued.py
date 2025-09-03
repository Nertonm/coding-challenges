"""
F. Fractions are better when continued
---------------------------------------
time limit per test: 1 second
memory limit per test: 256 megabytes

Little Charles was one of the best competitive programmers in the world.
However, he never really liked programming. Now that he is retired, he
can dedicate his studies to what he really loves: continued fractions.

To prepare for the upcoming Imensa Competição de Phrações Contínuas (ICPC),
he needs to solve the following problem:

Define p_0 = 1 as the level 0 fraction. Then define:

p_1 = 1 + 1/1

as the level 1 fraction, p_1. And also,

p_2 = 1 + 1/(1 + 1/1)

as the level 2 fraction, p_2, and so on.

Given an integer value N, help Charles determine the value of the numerator
of the fraction p_N.

Input
-----
The first and only line contains an integer N (1 <= N <= 40).

Output
------
The value p_N can be written as a fraction of the form a/b, where a and b
are coprime. Print a line containing the value of a.
"""

"""
n = int(input())
numeros_fibonacci = [
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 
    1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 
    121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 
    3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986
]

print(f"{numeros_fibonacci[n -1 ]}")
"""

n = int(input())
fib = [1, 1]
# Começa no número 2 porque os elementos nas posições 0 e 1 da lista já estão definidos.
for i in range(2, n + 2):
    # fib[-1]: Pega o último número da lista.
    # fib[-2]: Pega o penúltimo número da lista.
    fib.append(fib[-1] + fib[-2])
print(fib[n])