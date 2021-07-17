def minion_game(string):
    vow = "AEIOU"
    slen = len(string)
    tsub = int(slen * (slen + 1) / 2)
    k = sum(slen - i for i in range(slen) if string[i] in vow)   
    s = tsub - k

    if s > k: print(f"Stuart {s}")
    elif s < k: print(f"Kevin {k}")
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)