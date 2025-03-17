# pentominoes-puzzle-solver
The programs are designed to run with Clingo to find solutions for a specific puzzle involving the placement of 12 unique pentominoes on a 10x6 grid. The grid is divided into two smaller 5x6 grids by a horizontal line, and the goal is to arrange the pentominoes such that:
- All 12 pieces fit within the 10x6 grid.
- No part of any pentomino overlaps the line separating the two smaller grids.

To solve this puzzle, two variants of the puzzle solver are provided:

- `puzzle_solverv1.lp`: Outputs all possible solutions.
- `puzzle_solverv2.lp`: Outputs only the fundamentally different solutions by removing symmetrical or redundant ones.

  
A visualizer was created with the assistance of ChatGPT to display the final solutions. This visualizer requires Pygame. Ensure you have Pygame installed by running the following command if it’s not already installed:
```bash
pip install pygame
```
## Mini guide 
- If you already have solutions from the Clingo program saved in a JSON file, you can skip the next step.
- Generate solutions by running the following command (example for the first puzzle solver):
    ```bash
    clingo pentomino_encoder.db puzzle_solverv1.lp --outf=2 -n 2 -t 8 > sol.json
    ```
   - This command executes the ASP programs with Clingo, outputting the results in a JSON format (--outf=2).
   - It generates up to 2 solution models (-n 2) and runs in parallel mode using 8 threads (-t 8). The output will be saved to sol.json.
- Visualize the solutions by running the Python script:
    ```bash
    python visualize.py sol.json
    ```
- A Pygame window will open, displaying the solutions. If multiple solutions exist, use the left and right arrow keys on your keyboard to navigate through them.
## Solutions files 
Some solutions files are given in the repository, I'll explain what they are used for :
- `sol.json`: Contains 20 stable models found by the first version of the puzzle solver (puzzle_solverv1.lp).
- `sol2.json`: Contains 20 stable models after fixing the Pentomino T on a specific side of the grid.
- `sol3.json`: Contains 8 models, found after fixing the Pentomino T on a specific side and removing symmetrical solutions for that side.
- `sol4.json`: Contains the 2 final models, representing the fundamentally different solutions.

By using these pre-generated files or generating your own, you can explore and visualize the solutions interactively!
