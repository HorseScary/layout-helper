def read_layout(file):
    file = open("file", "r")

    row = 0
    layout = [[]]
    for i in file:
        if i != "\n":
            layout[row].append(i.rstrip("\n"))
        else:
            row += 1
            layout.append([])
    return (layout)


def format_layout(layout):
    formatted_layout = ''
    for i in layout:
        for j in i:
            formatted_layout += (f"[{j}]")
        formatted_layout += "\n"
    return (formatted_layout.rstrip("\n"))


if __name__ == "__main__":
    print(format_layout(read_layout("bottom.txt")))
