def parse_tents_from_sol(sol_file):
    tent_coordinates = sol_file.readline().split(" ")

    ret_value = []

    for x in tent_coordinates:
        coord = x.replace("tentAt(", "").replace(")", "").split(",")
        ret_value.append((int(coord[0]), int(coord[1])))
    return ret_value


if __name__ == '__main__':
    input = open("examples/input/input-16-16-easy")
    solution = open("examples/solutions/solution-16-16-easy.txt")

    tents = parse_tents_from_sol(solution)

    height, width = input.readline().replace("\n", "").split(" ")

    lines = []

    for i in range(int(height)):
        lines.append(list(input.readline().replace("\n", "").split(" ")[0]))

    for i in range(int(height)):
        for j in range(int(width)):
            if (i + 1, j + 1) in tents:
                lines[i][j] = "#"

    for i in range(int(height)):
        print("".join(lines[i]))
