#!/usr/bin/env python3
import sys


def solve(W: int, H: int, N: int, p: "List[int]", q: "List[int]", A: int, a: "List[int]", B: int, b: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    p = [int()] * (N)  # type: "List[int]"
    q = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        p[i] = int(next(tokens))
        q[i] = int(next(tokens))
    A = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    B = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    solve(W, H, N, p, q, A, a, B, b)

if __name__ == '__main__':
    main()
