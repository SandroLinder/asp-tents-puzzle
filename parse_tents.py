import getopt
import sys


def parse_input_and_create_tmp_clingo_input(file_path):
    file = open(file_path, "r")
    x, y = file.readline().replace("\n", "").split(" ")

    lines = []

    for i in range(0, int(x)):
        (line, colsum) = file.readline().replace("\n", "").split(" ")
        lines.append((line, colsum))

    colsums = file.readline().replace("\n", "").split(" ")
    file.close()

    clingo_input = open("input.lp", "w+")

    clingo_input.write("lines(" + x + ").\n")
    clingo_input.write("columns(" + y + ").\n")

    clingo_input.write("\n")

    for i in range(int(x)):
        clingo_input.write("line(" + str(i + 1) + ").\n")

    clingo_input.write("\n")

    for i in range(int(y)):
        clingo_input.write("column(" + str(i + 1) + ").\n")

    clingo_input.write("\n")

    clingo_input.write("\n")

    for i in range(len(colsums)):
        clingo_input.write("colsum(" + str(i + 1) + ", " + colsums[i] + ").\n")

    clingo_input.write("\n")

    for x in range(len(lines)):
        clingo_input.write("rowsum(" + str(x + 1) + ", " + lines[x][1] + ").\n")

    clingo_input.write("\n")

    for x in range(len(lines)):
        for y in range(len(lines[x][0])):
            if lines[x][0][y] == "T":
                clingo_input.write("tree(" + str(x + 1) + ", " + str(y + 1) + ").\n")
    clingo_input.write("\n")

    for x in range(len(lines)):
        for y in range(len(lines[x][0])):
            if lines[x][0][y] == ".":
                clingo_input.write("free(" + str(x + 1) + ", " + str(y + 1) + ").\n")

    clingo_input.close()


long_options = ["help", "puzzle"]

if __name__ == '__main__':
    argumentList = sys.argv[1:]
    options = "hp:"
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)

        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--help"):
                print("Usage:")
                print("    --puzzle, -p: Relative path to puzzle input.")
            elif currentArgument in ("-", "--puzzle"):
                parse_input_and_create_tmp_clingo_input(currentValue)
    except getopt.error as err:
        print(str(err))
