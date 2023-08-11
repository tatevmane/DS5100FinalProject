#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:55:21 2023

@author: tatevgomtsyan
"""
#import packages
import numpy as np
import pandas as pd
from typing import List

class Die:
    
    """
    A class representing a single multi-sided die with customizable faces and weights.

    Attributes:
        faces: List of distinct symbols or values that are integers or strings representing each face of the die.
        weights: Dictionary that maps each face to its associated weight.

    Methods:
        __init__(faces: List[str or int]):
            Initializes a Die instance with the provided list of faces, each with default weight 1.

        weight(face: str or int, new_weight: float):
            Changes the weight of a face on the die.

        dice_roll(times: int = 1) -> List[str or int]:
            Rolls the die one or more times and returns a list of outcomes.

        dice_state() -> dict:
            Returns a dictionary containing the current states of the faces and their weights.
    """
    
    def __init__(self, faces: np.array):
        """
      Initializes a Die instance with a list of faces, each having an initial weight of 1.

      Args:
          faces: List of distinct symbols or values that are integers or strings representing the faces of the die.

      Returns:
          None
       """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array.")
        
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces must contain distinct values.")
        
        self.faces = faces
        self.weights = np.ones(len(faces))  # Initialize weights with 1 for each face
        
        self.die = pd.DataFrame({'weights': self.weights}, index = self.faces)
    
    def weight(self, face: str or int, new_weight: float):
        """
      Changes the weight of a specific face on the die.

      Args:
       face (str or int): The face value to change the weight of.
       new_weight (float): The new weight to assign to the face.

      Returns:
       None
       """
       
        if face not in self.faces:
            raise IndexError("Invalid face value.")
        
        if not isinstance(new_weight, (int, float)) or new_weight < 0:
            raise TypeError("Weight must be a non-negative number.")
        
        face_index = np.where(self.faces == face)[0][0]
        self.weights[face_index] = new_weight
        self.die = pd.DataFrame({'weights': self.weights}, index = self.faces)
    
    def dice_roll(self, times: int = 1) -> List[str or int]:
        """
      Rolls the die one or more times and returns the outcomes.

      Args:
       times (int, optional): The number of times to roll the die. Default is 1.

      Returns:
       List[str or int]: A list of outcomes from rolling the die.
       """
       # outcomes = np.random.choice(self.faces, times, p=self.weights / np.sum(self.weights))
        #return outcomes.tolist()
        
        play = np.random.choice(self.faces, times, 
                                 p = self.die['weights'] / np.sum(self.die['weights']))
        final_outcome = play.tolist()
        return final_outcome
    
    def dice_state(self) -> pd.DataFrame:
        """
      Returns a dictionary containing the current state of the die.

      Returns:
       dict: A dictionary with 'faces' and 'weights' keys representing the current state of the die.
       """

        data = {'Faces': self.faces, 'Weights': self.weights}
        state_df = pd.DataFrame(data)
        state_df.set_index('Faces', inplace=True)
        return state_df


# Game class
#objects initialized with die object

class Game:
    """
    Represents a game involving rolling multiple dice.

    Attributes:
        dice_list (List[Die]): List of Die objects representing the dice in the game.

    Methods:
        __init__(dice_list: List[Die]):
            Initializes a Game instance with a list of Die objects.

        play(num_rolls: int):
            Rolls all dice a specified number of times and saves the results.

        show_results(format: str = "wide") -> pd.DataFrame:
            Returns the results of the most recent play in wide or narrow format.
    """
    
    def __init__(self, dice_list):
        """
      Initializes a Game instance with a list of Die objects representing the dice in the game.

      Args:
            dice_list (List[Die]): A list of Die objects representing the dice in the game.

      Returns:
            None
        """
        self.dice_list = dice_list
        self.play_results = pd.DataFrame()

    def play(self, num_rolls: 1):
        """
      Rolls all dice a specified number of times and saves the results.

      Args:
         num_rolls (int): The number of times to roll the dice.

      Returns:
         None
         """
        results = {}
        for index, die in enumerate(self.dice_list):
            results[f"Die_{index}"] = die.dice_roll(num_rolls)
        
        self.play_results = pd.DataFrame(results)
    

    def show_results(self, form = "wide") -> pd.DataFrame:
        """
      Returns the results of the most recent play in wide or narrow format.

      Args:
          form (str, optional): The format for displaying results as either "wide" or "narrow". The default
          is set as "wide".

      Returns:
          pd.DataFrame: The results of the most recent play in the specified format.
      """
      
        if form == 'wide':
            wide_df = self.play_results.copy()
            return wide_df
        
        elif form == "narrow":
            return self.play_results.melt(ignore_index=False, var_name="Die", value_name="Outcome")
        
# Analyzer class
# initialized with game object

class Analyzer:

    """
    Computes descriptive statistical properties about a game's results.

    Attributes:
        game (Game): The game object's results that are being analyzed.

    Methods:
        __init__(game: Game):
            Initializes an Analyzer instance with a Game object for analysis.

        jackpot() -> int:
            Computes the number of jackpot results (all faces are the same) in the game.
            Returns the count of jackpots as an integer.

        face_counts_per_roll(face: str or int) -> pd.DataFrame:
            Computes the count of a specific face rolled in each event (roll).
            Returns a DataFrame with roll numbers as the index, face values as columns, and counts in cells.

        combo_count() -> pd.DataFrame:
            Computes the count of distinct combinations of rolled faces.
            Returns a DataFrame with distinct combinations as the MultiIndex and counts in a column.

        permutation_count() -> pd.DataFrame:
            Computes the count of distinct permutations of rolled faces.
            Returns a DataFrame with distinct permutations as the MultiIndex and counts in a column.
    """
    def __init__(self, game: Game):
        """
      Initializes an Analyzer instance with a Game object for analysis.

      Args:
           game (Game): The Game object's results that will be analyzed.

      Returns:
           None
       """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object.")
        
        self.game = game

    def jackpot(self) -> int:
        """
       Computes the number of jackpot results in the game.
       A jackpot is a result where all faces are the same.

       Returns:
           int: The count of jackpot results.
       """
       
        jackpot_count = 0
        for _, row in self.game.play_results.iterrows():
            if row.nunique() == 1:
                jackpot_count += 1
    
        return jackpot_count

    def face_counts_per_roll(self):
        """
        Computes the count of a specific face rolled in each event (roll).

        Args:
            face (str or int): The face value to count occurrences of.

        Returns:
            pd.DataFrame: A DataFrame with roll numbers as the index, face values as columns, and counts in cells.
        """
        
        #return self.game.show_results().apply(pd.Series.value_counts, axis = 1).fillna(0).astype(int)
        face_counts = self.game.play_results.apply(lambda x: x.value_counts()).fillna(0)
        face_counts = face_counts.astype(int)
        return face_counts

    def combo_count(self) -> pd.DataFrame:
        """
        Computes the count of distinct combinations of rolled faces.

        Returns:
            pd.DataFrame: A DataFrame with distinct combinations as the MultiIndex and counts in a column.
        """

        combos = self.game.play_results.apply(lambda x: tuple(sorted(x))).value_counts()
        combos = combos.reset_index()
        return combos

    def permutation_count(self) -> pd.DataFrame:
        """
        Computes the count of distinct permutations of rolled faces.

        Returns:
            pd.DataFrame: A DataFrame with distinct permutations as the MultiIndex and counts in a column.
        """
        #perm_counts = {}
        perms = self.game.play_results.apply(lambda x: tuple(x.tolist())).value_counts()
        perms = perms.reset_index()
        return perms







