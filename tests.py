import unittest
import heuristics as h
from utils import *

class HeuristicTest(unittest.TestCase):

    def test_weightVoidLine(self):
        initpos = (1,1)
        direction = (1,0)
        board = {}
        state = Struct(to_move= 'X',
                          utility=0,
                          board=board, moves=[], realPlayer='X')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4),0)

    def test_weightNoFourLine(self):
        initpos = (1,1)
        direction = (1,0)
        board = {(1,1):'X',(1,2):'O',(1,3):'X',(1,4):'O',(1,5):'O',(1,6):'O', (1,7):'X'}
        state = Struct(to_move= 'X',
                      utility=0,
                      board=board, moves=[], realPlayer='X')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4),0)

    def test_weightRandom(self):
        initpos = (1,1)
        direction = (1,0)
        board = {(1,3):'X',(1,4):'X',(1,5):'O', (1,7):'O'}
        state = Struct(to_move= 'X',
                      utility=0,
                      board=board, moves=[], realPlayer='X')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4), 8)

    def test_weightRandom2(self):
        initpos = (1,1)
        direction = (1,0)
        board = {(1,1):'O',(1,2):'O',(1,3):'X',(1,4):'O',(1,5):'X',(1,6):'O', (1,7):'O'}
        state = Struct(to_move= 'X',
                      utility=0,
                      board=board, moves=[], realPlayer='X')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4), 0)

    def test_weightRandom3(self):
        initpos = (1,1)
        direction = (1,0)
        board = {(1,1):'X',(1,2):'X',(1,3):'O',(1,4):'O', (1,7):'X'}
        state = Struct(to_move= 'O',
                      utility=0,
                      board=board, moves=[], realPlayer='O')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4), 8)

    def test_weight1Enemy(self):
        initpos = (1,1)
        direction = (1,0)
        board = {(1,3):'X',(1,4):'O'}
        state = Struct(to_move= 'X',
                      utility=0,
                      board=board, moves=[], realPlayer='X')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4), -4)

    def test_weight2Enemy(self):
        initpos = (1,1)
        direction = (1,0)
        board = {(1,3):'X',(1,4):'O',(1,6):'O'}
        state = Struct(to_move= 'X',
                      utility=0,
                      board=board, moves=[], realPlayer='X')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4), -8)

    def test_weight1Me2Enemy(self):
        initpos = (1,1)
        direction = (1,0)
        board = {(1,2):'O',(1,5):'X'}
        state = Struct(to_move= 'X',
                      utility=0,
                      board=board, moves=[], realPlayer='O')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4), -4)

    def test_vertical(self):
        initpos = (1,1)
        direction = (0,1)
        board = {(2,1):'O',(4,1):'X'}
        state = Struct(to_move= 'X',
                      utility=0,
                      board=board, moves=[], realPlayer='O')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4), -4)

    def test_diagonal(self):
        initpos = (1,5)
        direction = (1,-1)
        board = {(5,1):'O',(4,2):'X'}
        state = Struct(to_move= 'X',
                      utility=0,
                      board=board, moves=[], realPlayer='O')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4), -4)

    def test_diagonal2(self):
        initpos = (1,1)
        direction = (1,1)
        board = {(2,2):'O',(3,3):'X'}
        state = Struct(to_move= 'X',
                      utility=0,
                      board=board, moves=[], realPlayer='O')

        self.assertEqual(h.lineWeight(state, initpos, direction, placedcellsmultiplier=4), -4)

if __name__ == '__main__':
    unittest.main()