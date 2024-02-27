import getopt
import sys


def parse_tents_from_sol(sol_file):
    tent_coordinates = sol_file.readline().split(" ")

    ret_value = []

    for x in tent_coordinates:
        coord = x.replace("tentAt(", "").replace(")", "").split(",")
        ret_value.append((int(coord[0]), int(coord[1])))
    return ret_value


long_options = ["help", "puzzle", "solution"]

if __name__ == '__main__':

    argumentList = sys.argv[1:]
    options = "p:s:"
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)
        puzzle = ""
        solution = ""
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--Help"):
                print("Usage:")
                print("    --puzzle, -p:        Relative path the puzzle input.")
                print("    --solution, -s:      Relative path to solution file.")
            elif currentArgument in ("-p", "--puzzle"):
                puzzle = currentValue
            elif currentArgument in ("-s", "--solution"):
                solution = currentValue

        if puzzle == "" or solution == "":
            print("Path to puzzle and path to solution must be provided. Check -h for help.")
            exit(1)

        puzzle_input = open(puzzle)
        output = open(solution)

        tents = parse_tents_from_sol(output)

        height, width = puzzle_input.readline().replace("\n", "").split(" ")

        lines = []

        for i in range(int(height)):
            lines.append(list(puzzle_input.readline().replace("\n", "").split(" ")[0]))

        for i in range(int(height)):
            for j in range(int(width)):
                if (i + 1, j + 1) in tents:
                    lines[i][j] = "#"

        for i in range(int(height)):
            print("".join(lines[i]))
    except getopt.error as err:
        print(str(err))
