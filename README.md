# Monte Carlo Simulator 

Author: Tatev Gomtsyan <br>
Project Name: Monte Carlo Simulator

## Table of Contents

- [Synopsis](#synopsis)
- [API](#api)
- [Installation](#installation)
- [Usage](#usage)
- [Scenarios](#scenarios)
- [Contributions](#contributing)
- [License info](#license)

## Synopsis

This project implements a dice simulator that allows you to create and roll various types of dice in different games. It includes three main classes: `Die`, `Game`, and `Analyzer`.

- The `Die` class represents a customizable die with user-defined faces and weights.
- The `Game` class simulates rolling multiple dice in a game and keeps track of the results.
- The `Analyzer` class computes descriptive statistics about the game's results.

## API

### Die Class Methods: 

`def __init__(self, faces: np.array):`
    
    """
    Initializes a Die instance with a list of faces, each having an initial weight of 1.

      Args:
          faces: List of distinct symbols or values that are integers or strings representing the faces of the die.

      Returns:
          None
       """
       
`def weight(self, face: str or int, new_weight: float):`      

      """
      Changes the weight of a specific face on the die.

      Args:
       face (str or int): The face value to change the weight of.
       new_weight (float): The new weight to assign to the face.

      Returns:
       None
      """
      
 `def dice_roll(self, times: int = 1) -> List[str or int]:`
       
      """
      Rolls the die one or more times and returns the outcomes.

      Args:
       times (int, optional): The number of times to roll the die. Default is 1.

      Returns:
       List[str or int]: A list of outcomes from rolling the die.
       """
       
`def dice_state(self) -> pd.DataFrame:`
      
      """
      Returns a dictionary containing the current state of the die.

      Returns:
       dict: A dictionary with 'faces' and 'weights' keys representing the current state of the die.
       """


### Game Class Methods:

`def __init__(self, dice_list):`
    
    """
      Initializes a Game instance with a list of Die objects representing the dice in the game.

      Args:
            dice_list (List[Die]): A list of Die objects representing the dice in the game.

      Returns:
            None
        """

`def play(self, num_rolls: 1):`
    
    """
      Rolls all dice a specified number of times and saves the results.

      Args:
         num_rolls (int): The number of times to roll the dice.

      Returns:
         None
         """

`def show_results(self, form = "wide") -> pd.DataFrame:`
    
     """
      Returns the results of the most recent play in wide or narrow format.

      Args:
          form (str, optional): The format for displaying results as either "wide" or "narrow". The default
          is set as "wide".

      Returns:
          pd.DataFrame: The results of the most recent play in the specified format.
      """

### Analyzer Class Methods:

`def __init__(self, game: Game):`
    
    """
      Initializes an Analyzer instance with a Game object for analysis.

      Args:
           game (Game): The Game object's results that will be analyzed.

      Returns:
           None
       """

`def jackpot(self) -> int:`
    
    """
       Computes the number of jackpot results in the game.
       A jackpot is a result where all faces are the same.

       Returns:
           int: The count of jackpot results.
       """

`def face_counts_per_roll(self):`
       
        """
        Computes the count of a specific face rolled in each event (roll).

        Args:
            face (str or int): The face value to count occurrences of.

        Returns:
            pd.DataFrame: A DataFrame with roll numbers as the index, face values as columns, and counts in cells.
        """

`def combo_count(self) -> pd.DataFrame:`
       
        """
        Computes the count of distinct combinations of rolled faces.

        Returns:
            pd.DataFrame: A DataFrame with distinct combinations as the MultiIndex and counts in a column.
        """

`def permutation_count(self) -> pd.DataFrame:`
       
        """
        Computes the count of distinct permutations of rolled faces.

        Returns:
            pd.DataFrame: A DataFrame with distinct permutations as the MultiIndex and counts in a column.
        """

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/tatevmane/tatevmane_ds5100_montecarlo
   cd montecarlo

2. Install required dependencies in terminal: <br>

    pip install numpy <br>
    pip install pandas

3. Import packages: <br>

    `import numpy as np`
   
   ` import pandas as pd`

5. Import necessary classes for script:<br>

    `from montecarlo import Die, Game, Analyzer`

Create instances of Die, Game, and Analyzer classes, and use their methods as described in the documentation.

## Usage

### For Die Class

Define faces for the die: <br>
`faces = [1, 2, 3, 4, 5, 6]`

Create a Die instance: <br>
`my_die = Die(faces)`

Change the weight of a face: <br>
`my_die.weight(1, 2.5)`

Roll the die: <br>
`outcome = my_die.dice_roll()`

Get the current state of the die: <br>
`state = my_die.dice_state()`

### For Game Class

Create Die instances: <br>
`die1 = Die([1, 2, 3, 4, 5, 6])`

`die2 = Die(['A', 'B', 'C', 'D'])`

Create a Game instance: <br>
`my_game = Game([die1, die2])`

Roll the dice and store the results: <br>
`my_game.play(10)`

Display results in wide format: <br>
`wide_results = my_game.show_results("wide")`

Display results in narrow format: <br>
`narrow_results = my_game.show_results("narrow")`

### For Analyzer Class

Create Die instances: <br>
`die1 = Die([1, 2, 3, 4, 5, 6])`

`die2 = Die(['A', 'B', 'C', 'D'])`

Create a Game instance: <br>
`my_game = Game([die1, die2])`

Roll the dice and store the results: <br>
`my_game.play(20)`

Create an Analyzer instance: <br>
`analyzer = Analyzer(my_game)`

Compute the number of jackpot results: <br>
`jackpot_count = analyzer.jackpot()`

Get the counts of specific faces per roll: <br>
`face_counts = analyzer.face_counts_per_roll()`

Get the counts of distinct combinations of rolled faces: <br>
`combo_counts = analyzer.combo_count()`

Get the counts of distinct permutations of rolled faces: <br>
`perm_counts = analyzer.permutation_count()`

## Scenarios
For scenarios demonstrating the usage of the simulator, refer to the provided Tatev_FinalProject.ipynb. Below are snippets from those scenarios as an application example. <br>
![image](https://github.com/tatevmane/tatevmane_ds5100_montecarlo/assets/90347726/a0ab3529-552f-4546-80ba-93ebb4a600e6) 

## Contributing
Contributions to this project are welcome! Feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

