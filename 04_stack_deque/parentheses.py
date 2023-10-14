text = input()
parentheses = []
for synbol in range(len(text)):
    if text[synbol] == "(":
        parentheses.append(synbol)
    elif text[synbol] == ")":
        start_index = parentheses.pop()
        print(text[start_index:synbol + 1])
