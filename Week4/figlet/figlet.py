import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
argv1 = ["-f", "--font"]


def main():
    #Random font
    if len(sys.argv) < 2:
        font = random.choice(figlet.getFonts())
        fig("Input: ", font)
    #Choosen font
    elif len(sys.argv) > 2 and sys.argv[1] in argv1 and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        fig("Input: ", font)
    #Neither
    else:
        sys.exit("Invalid usage")

#Turn text into figlet
def fig(prompt, f):
    txt = input(prompt)
    figlet.setFont(font=f)
    print("Output:")
    print(figlet.renderText(txt))


main()
