#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:37:07 2023

@author: tatevgomtsyan
"""

import numpy as np 
import pandas as pd
import unittest
from montecarlo import Die, Game, Analyzer 

class TestMethods(unittest.TestCase):
    
    def test_init_die(self):
        # Test Die initialization
        my_die = Die(np.array([1, 2, 3, 4, 5, 6]))
        faces = [1, 2, 3, 4, 5, 6]
        expected_df = pd.DataFrame({"Weights": [1.0,1.0,1.0,1.0,1.0,1.0]}, index=faces)
        expected_df.index.name = 'Faces'
        actual_df = my_die.dice_state()
        self.assertTrue(actual_df.equals(expected_df))

    def test_weight(self):
        # Test changing weight of a face
        my_die = Die(np.array([1, 2, 3, 4, 5, 6]))
        my_die.weight(1, 2.5)
        self.assertEqual(my_die.weights[0], 2.5)
        
    def test_dice_roll(self):
        # Test rolling the die
        my_die = Die(np.array([1, 2, 3, 4, 5, 6]))
        outcomes = my_die.dice_roll(5)
        self.assertEqual(len(outcomes), 5)
        
    def test_dice_state(self):
        # Test showing the state of the die
        my_die = Die(np.array([1, 2, 3, 4, 5, 6]))
        state = my_die.dice_state()
        #self.assertTrue(isinstance(state, pd.DataFrame))
        self.assertEqual(type(state), pd.DataFrame)
        
    def test_init_game(self):
        my_die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        my_die2 = Die(np.array([1, 2, 3, 4]))
        game = Game([my_die1, my_die2])
        self.assertEqual(type(game), Game)
        
    def test_play(self):
        my_die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        my_die2 = Die(np.array([1, 2, 3, 4]))
        game = Game([my_die1, my_die2])
        game.play(10)
        self.assertEqual(game.play_results.shape, (10, 2))

    def test_show_results(self):
        my_die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        my_die2 = Die(np.array([1, 2, 3, 4]))
        game = Game([my_die1, my_die2])
        game.play(5)
        results = game.show_results(form='wide')
        self.assertEqual(results.shape, (5, 2))
    
    def test_init_analyzer(self):
        my_die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        my_die2 = Die(np.array([1, 2, 3, 4]))
        game = Game([my_die1, my_die2])
        analyzer = Analyzer(game)
        self.assertEqual(type(analyzer), Analyzer)
    
    def test_jackpot(self):
        my_die1 = Die(np.array([1]))
        game = Game([my_die1])
        game.play(10)
        analyzer = Analyzer(game)
        self.assertEqual(analyzer.jackpot(), 10)

    def test_face_counts_per_roll(self):
        my_die1 = Die(np.array([1]))
        game = Game([my_die1])
        game.play(10)
        analyzer = Analyzer(game)
        self.assertIsInstance(analyzer.face_counts_per_roll(), pd.DataFrame)
        
    def test_combo_count(self):
        my_die1 = Die(np.array([1,2]))
        my_die2 = Die(np.array([1,2]))
        game = Game([my_die1, my_die2])
        game.play(10)
        analyzer = Analyzer(game)
        self.assertIsInstance(analyzer.combo_count(), pd.DataFrame)
    
    def test_permutation_count(self):
        my_die1 = Die(np.array([1,2]))
        game = Game([my_die1])
        game.play(10)
        analyzer = Analyzer(game)
        self.assertEqual(len(analyzer.permutation_count()), 2)   
    

if __name__ == '__main__':
    unittest.main(verbosity=3)
   