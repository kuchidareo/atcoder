#!/usr/bin/env python3
import sys


def main():
    N = int(input())
    S = []
    A = []
    min_age = float('inf')
    min_index = 0

    for i in range(N):
        s, a = input().split()
        a = int(a)

        S.append(s)
        A.append(a)

        if a < min_age:
            min_age = a
            min_index = i

    for j in range(min_index, N):
        print(S[j])
    for j in range(min_index):
        print(S[j])



   
if __name__ == '__main__':
    main()
