import random as rand
import math
from functions import functions as func
import pandas

pandas.set_option('display.max_columns', None)
import hashlib

# размер ключей 128 бит
# 64-битовые простые числа

# Вариант 1. Реализовать схему Шаума с монетами одинакового достоинства и сдачей.
# В протоколе 3 стороны - продавец, покупатель и банк. Размер ключей 128 бит (64-битовые простые числа).
# В схеме должны быть протоколы для трех транзакций: снятие со счета, депозит, платеж.
bits = 16


def calc_h(S):
    #    print("S =", bin(S))
    k = len(bin(S)) - 2
    result = 1
    #    num=[]
    for i in range(k):
        if (bin(S)[i + 2] == "1"):
            r = p_primes[i]  # func.rmutpr(phi_n)
            result *= r
    #            print("r =", r)
    return (result)


def calc_h_inv(h):
    return func.inv(h, phi_n)


def f(x):
    res = hashlib.sha256()
    res.update(x.to_bytes((x.bit_length() + 7) // 8, 'big'))
    return int.from_bytes(res.digest(), 'big')


def deposit(Nn, d):
    for i in range(len(usedCoins)):
        if (usedCoins[i] == Nn):
            print("Монета уже была использована")
            return
    J = pow(f(Nn) % n, calc_h_inv(d), n)
    print("A->T:  N* =", Nn, ", J =", J)
    usedCoins.append(Nn)


# print(calculate_h(12))
def withdrawal(h, S):  # S=номинал
    print("ВЫДАЧА БАНКНОТЫ")
    print()
    #    h=calc_h(S)
    N = func.rpr(bits) + rand.randint(1, 99999)
    r = func.rmutpr(n)
    print("A:  N =", N, ",  r =", r)
    b = ((f(N) % n) * pow(r, h, n)) % n
    print("A->T:  b =", b)
    c = pow(b, calc_h_inv(h), n)
    print("T->A:  c =", c)
    x = ((c % n) * func.inv(r, n)) % n
    print("A:  Банкнота:")
    print("    N =", N, ",  x =", x, ", S =", S)

    print(pow(x, h, n))
    print(f(N) % n)
    print()
    print()
    return x, N


def purchase(S, s, x, N, h):  # S=номинал, s=сумма покупки
    print("ПОКУПКА")
    print()

    for i in range(len(usedCoins)):
        if (usedCoins[i] == N):
            print("Монета уже была использована")
            return

    if (s > S):
        print("Недостаточно средств")
        return
    #    h=calc_h(S)
    print("h =", h)
    g = calc_h(s)
    print("g =", g)
    #    d=calc_h(S-s)
    d = h // g
    print("d =", d)

    #    Nn=func.rpr(bits)+rand.randint(1,99999)
    r = func.rmutpr(n)
    print("A:  N* =", Nn, ",  r =", r)
    l = pow(x, d, n)
    z = ((f(Nn) % n) * pow(r, d, n)) % n
    print("A->B:  l =", l, ", z =", z)
    print("       S =", S, ", s =", s, ", N =", N)
    print("B->T:  l =", l, ", z =", z)
    print("       S =", S, ", s =", s, ", N =", N)
    print(pow(l, g, n))
    print(f(N) % n)
    print()
    usedCoins.append(N)
    if (S == s):
        return

    y = pow(z, calc_h_inv(d), n)
    print("T->B:  y =", y)
    print("B->A:  y =", y)
    xn = ((y % n) * func.inv(r, n)) % n
    print("A:  x* =", xn, ", N* =", Nn)
    print()
    print(pow(xn, d, n))
    print(f(Nn) % n)
    print()

    return Nn, d


p = func.rpr(bits)
print("p =", p)
q = func.rpr(bits)
print("q =", q)
n = p * q  # модуль RSA
print("n =", n)
print()
phi_n = (p - 1) * (q - 1)
p_primes = []
for i in range(4):
    p_primes.append(func.rmutpr(phi_n))
print(p_primes)
print()

# p_=func.rpr(bits)
# print("p_ =", p_)
# q_=func.rpr(bits)
# print("q_ =", q_)
# n_=p_*q_ # модуль RSA
# print("n_ =", n_)
usedCoins = []
summa = 15
H = calc_h(summa)
Nn = func.rpr(bits) + rand.randint(1, 99999)

xg, Ng = withdrawal(H, summa)

purchase(summa, 9, xg, Ng, H)
# purchase(summa, 9, xg, Ng, H)

deposit(Nng, dg)
deposit(Nng, dg)

# print(653492782367003299189548981783645305/71872331892972137)
# print(653492782367003299189548981783645305//71872331892972137)
# print(9092411017638117265*71872331892972137)
# print((26122883169854919//273229743385307547)*273229743385307547)
