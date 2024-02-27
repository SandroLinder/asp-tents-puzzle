# Tents Puzzle ASP Solver

## Puzzle
Tents (sometimes known as "Tents and Trees") is a popular logic puzzle. According to https://wpcunofficial.miraheze.org/wiki/Tents it was first published by Léon Balmaekers with the Dutch name "Alle Ballen Verzamelen" in 1989.

Rules:

* Place tents on the grid, so that each tree has a unique horizontally or vertically adjacent tent. This also means that no tent can "serve" more than one tree.
* Tents should not be adjacent to each other (neither horizontally, nor vertically, and also not diagonally).
* The given numbers for rows and columns have be equal to the number of placed tents in the respective row or column.

## Solver
## Examples

This folder contains example inputs taken from https://www.puzzle-tents.com/ and https://www.brainbashers.com/tents.asp. These example inputs were converted into this format:

```
5 10
.......... 0
......T... 2
..T...T... 0
.......... 1
.......... 0
0 0 1 0 0 0 1 1 0 0
```

The converted puzzles can be found in the text folder. The input folder contains these puzzles converted into the ASP clingo syntax that was generated by the parse_tents.py file. The solution folder contains the solutions that the solver produced for the different puzzles.
