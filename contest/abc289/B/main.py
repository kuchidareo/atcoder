#!/usr/bin/env python3
import sys


def solve(N: int, M: int, a: "List[int]"):
    ori = [i for i in range(1, N+1)]
    ans = ori.copy()
    
    if M != 0:
        devided_a = [[a[0]]]

        for i in range(M-1):
            if a[i+1] == a[i] + 1:
                devided_a[-1].append(a[i+1])
            else:
                devided_a.append([a[i+1]])

        for section in devided_a:
            s_ind = (section[0]-1)
            e_ind = (section[-1]-1) + 2
            ans[s_ind: e_ind] = ori[s_ind: e_ind][::-1]
    
    print(' '.join(str(x) for x in ans))
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
    a = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, a)

if __name__ == '__main__':
    main()