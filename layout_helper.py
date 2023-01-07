from functions import *
import argparse

parser = argparse.ArgumentParser(
    prog="layout_helper",
    description="shows the keyboard layout",
    epilog="made by HorseScary"
)

parser.add_argument(
    "layer", choices=["bottom", "shift", "alt"], help='Possible layers are "bottom", "shift", and "alt"')

args = parser.parse_args()

print(format_layout(read_layout(f"./{args.layer}.txt")))
