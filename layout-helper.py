bottom = [["esc", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "del"],
          ['`', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '0', '-', '=', 'backspace'],
          ['tab', 'q', 'w', 'e', 'r', 't', 'y',
              'u', 'i', 'o', 'p', '[', ']', '\\'],
          ['caps', 'a', 's', 'd', 'f', 'g', 'h',
              'j', 'k', 'l', ';', '\'', 'enter'],
          ['shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'shift'],
          ['ctrl', 'fn', 'ew', 'alt', '   space   ', 'alt', 'ctrl']]

bottom_formatted = ''

for i in bottom:
    for j in i:
        bottom_formatted += f"[{j}]"
    bottom_formatted += "\n"

print(bottom_formatted)
