#!/usr/bin/env python3
import sys


def solve(s: str):
    ans = ""
    for i in s:
        if i == "0":
            ans += "1" 
        else:
            ans += "0"
    print(ans)
    return 


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()
