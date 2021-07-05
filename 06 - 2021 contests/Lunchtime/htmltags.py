#UnRated Problem

def html(s):
    if (s == ""):
        return False

    for i in s:
        ascii_val = ord(i)

        if (47 < ascii_val < 58 or 96 < ascii_val <123):
            continue
        else:
            return False
    return True

t = int(input())
for q in range(0, t):
    s = input()

    if (s[:2] == "</" and s[-1] == ">" and html(s[2:-1])):
        print("Success")
    else:
        print("Error")
