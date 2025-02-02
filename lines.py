"""

One way to measure the complexity of a program is to count its number of lines of code (LOC), excluding blank lines and comments. For instance, a program like

# Say hello
name = input("What's your name? ")
print(f"hello, {name}")

has just two lines of code, not four, since its first line is a comment, and its second line is blank (i.e., just whitespace). That’s not that many, so odds are the program isn’t that complex.
Of course, just because a program (or even function) has more lines of code than another doesn’t necessarily mean it’s more complex. For instance, a function like

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
isn’t really twice as complex as a function like

def is_even(n):
    return n % 2 == 0
even though the former has (more than) twice as many lines of code. In fact, the former might arguably be simpler if it’s easier to read! So lines of code should be taken with a grain of salt.

Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments and blank lines.
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist,
the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.)
Assume that any line that only contains whitespace isblank.

"""
import sys

def main():
    lines = 0
    try:
        #expects 1 command-line argument
        if len(sys.argv) == 2:
            #debe decir el numero de lineas excluyendo comentarios y lineas en blanco
            prompt = sys.argv[1]
            if prompt.endswith(".py"):
                with open(sys.argv[1], "r") as file:
                    for line in file:
                        #Tengo que asignar a una nueva variable para que sea modificado
                        text = line.strip()
                        if text.startswith("#") or text == "":
                            lines += 0
                        else:
                            lines +=1
                    print(f"{lines}")
            else:
                sys.exit("Not a Python file")

        elif len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

