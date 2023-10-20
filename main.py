import random

print(" " * 26 + "MATPUZLE")
print(" " * 20 + "CREATIVE COMPUTING")
print(" " * 18 + "MORRISTOWN, NEW JERSEY")
print("\n")

W = int(input("How many words do you want (up to 6): "))
L = int(input("How many letters in each word (must be the same): "))

A = []
B = []
C = []
C_str = []

print("Type one", L, "letter word on each line")
for X in range(W):
    A.append(input())

for X in range(W):
    C_str.append([""] * L)
    B.append([""] * L)
    for Y in range(L):
        C_str[X][Y] = A[X][Y]
        B[X][Y] = A[X][Y]

print()

for P in range(28):
    print("-", end="")
print(" " * 29 + "( TEAR HERE )", end="")
for P1 in range(27):
    print(" " * 43 + "-", end="")
print("\n")

for Z in range(60):
    for _ in range(28):
        F = random.randint(0, W - 1)
        D = random.randint(0, W - 1)
        G = random.randint(0, L - 1)
        E = random.randint(0, L - 1)
        J = B[F][G]
        B[F][G] = B[D][E]
        B[D][E] = J

print(" " * 4, end="")
for Z1 in range(L):
    print(" " * 5 + str(Z1) + " ", end="")
print("\n")

for Z2 in range(W):
    print(Z2 + 1, " ", end="")
    for Z3 in range(L):
        print(B[Z2][Z3] + " ", end="")
    print()

print("\n")

for P in range(L):
    for Q in range(W):
        T = 0
        for R in range(W):
            for S in range(L):
                if T == 1:
                    break
                if B[R][S] != C_str[Q][P]:
                    continue
                C[Q][P] = R + S
                T = 1
                B[R][S] = " "

for X in range(W):
    print(" " * 3, end="")
    for M in range(L):
        if C[X][M] > 9:
            print(C[X][M], " ", end="")
        else:
            print(C[X][M], " ", end="")
    print("\n")

print("\n")
for M1 in range(L):
    print(" " * 2 + "-----" + " ", end="")
print("\n")

Y9 = input("Do you want another run? ")

if Y9 == "YES":
    pass
else:
    exit()
