#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, u: "List[int]", v: "List[int]", K: int, x: "List[int]", y: "List[int]", Q: int, p: "List[int]", q: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    K = int(next(tokens))  # type: int
    x = [int()] * (K)  # type: "List[int]"
    y = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    p = [int()] * (Q)  # type: "List[int]"
    q = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i] = int(next(tokens))
        q[i] = int(next(tokens))
    solve(N, M, u, v, K, x, y, Q, p, q)

if __name__ == '__main__':
    main()