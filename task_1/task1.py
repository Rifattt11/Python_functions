def check(s, opened=""):
    pairs = {"]": "[",")": "(", "}": "{"}

    if not s:
        return "Неправильно" if opened else "Правильно"

    if s[0] in "[({":
        opened += s[0]
    elif s[0] in pairs:
        if not opened or opened[-1] != pairs[s[0]]:
            return "Неправильно"
        opened = opened[:-1]

    return check(s[1:], opened)


print(check(input()))(иукро)