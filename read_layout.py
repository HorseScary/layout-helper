def read_layout(file):
    file = open(f"./{file}", "r")

    row = 0
    formatted = [[]]
    for i in file:
        if i != "\n":
            formatted[row].append(i.rstrip("\n"))
        else:
            row += 1
            formatted.append([])
    return (formatted)


if __name__ == "__main__":
    layout = read_layout("bottom.txt")
    for i in layout:
        for j in i:
            print(f"[{j}]", end="")
        print('')
