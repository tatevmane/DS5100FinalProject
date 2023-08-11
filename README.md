# Monte Carlo Simulator 

Author: Tatev Gomtsyan
Project Name: Monte Carlo Simulator

Synopsis: Show brief demo code of how the classes are used, i.e. code snippets showing how to install, import, and use the code to (1) create dice, (2) play a game, and (3) analyze a game. You can use preformatted blocks for the code.

API description: A list of all classes with their public methods and attributes. Each item should show their docstrings. All parameters (with data types and defaults) should be described. All return values should be described. Do not describe private methods and attributes.


TEMPLATE OUTLINING STEPS FOR PROJECT TO USER:
# Dice Simulator Project

This project implements a dice simulator that allows you to create and roll various types of dice in different games. It includes three main classes: `Die`, `Game`, and `Analyzer`.

- The `Die` class represents a customizable die with user-defined faces and weights.
- The `Game` class simulates rolling multiple dice in a game and keeps track of the results.
- The `Analyzer` class computes descriptive statistics about the game's results.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example Scenarios](#scenarios)
- [Contributions](#contributing)
- [License info](#license)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/tatevmane/tatevmane_ds5100_montecarlo
   cd montecarlo

Install required dependencies:
pip install numpy 
pip install pandas

import packages:
import numpy as np
import pandas as pd

import necessary classes for script:
from montecarlo import Die, Game, Analyzer

Create instances of Die, Game, and Analyzer classes, and use their methods as described in the documentation.

## Usage

### For Die Class

Define faces for the die: <br>
faces = [1, 2, 3, 4, 5, 6]

Create a Die instance: <br>
my_die = Die(faces)

Change the weight of a face: <br>
my_die.weight(1, 2.5)

Roll the die: <br>
outcome = my_die.dice_roll()

Get the current state of the die: <br>
state = my_die.dice_state()

### For Game Class

Create Die instances: <br>
die1 = Die([1, 2, 3, 4, 5, 6]) <br>
die2 = Die(['A', 'B', 'C', 'D'])

Create a Game instance: <br>
my_game = Game([die1, die2]) 

Roll the dice and store the results: <br>
my_game.play(10)

Display results in wide format: <br>
wide_results = my_game.show_results("wide")

Display results in narrow format: <br>
narrow_results = my_game.show_results("narrow")

### For Analyzer Class

Create Die instances: <br>
die1 = Die([1, 2, 3, 4, 5, 6]) <br>
die2 = Die(['A', 'B', 'C', 'D'])

Create a Game instance: <br>
my_game = Game([die1, die2])

Roll the dice and store the results: <br>
my_game.play(20)

Create an Analyzer instance: <br>
analyzer = Analyzer(my_game)

Compute the number of jackpot results: <br>
jackpot_count = analyzer.jackpot()

Get the counts of specific faces per roll: <br>
face_counts = analyzer.face_counts_per_roll()

Get the counts of distinct combinations of rolled faces: <br>
combo_counts = analyzer.combo_count()

Get the counts of distinct permutations of rolled faces: <br>
perm_counts = analyzer.permutation_count()

## Example Scenarios
For scenarios demonstrating the usage of the simulator, refer to the provided Tatev_FinalProject.ipynb. Below are snippets from those scenarios as an application example. <br>
![image](https://github.com/tatevmane/tatevmane_ds5100_montecarlo/assets/90347726/a0ab3529-552f-4546-80ba-93ebb4a600e6) 

## Contributing
Contributions to this project are welcome! Feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

