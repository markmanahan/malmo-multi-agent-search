# Created by Minbiao Han and Roman Sharykin
# AI fall 2018

# PA2- Ben Hughes (bch3jh) and Mark Manahan (mmm5ja)

'''
Reference materials:
-- https://github.com/filR/edX-CS188.1x-Artificial-Intelligence/blob/master/Project%202%20-%20Multi-Agent%20Pacman/multiAgents.py
-- https://github.com/takeitallsource/berkeley-cs-188/blob/master/project-2/multiagent/multiAgents.py
-- https://github.com/kevjames3/CS188.1x-Project2/blob/master/multiAgents.py
'''

from __future__ import print_function
from __future__ import division

from builtins import range
from past.utils import old_div
import MalmoPython
import json
import logging
import math
import os
import random
import sys
import time
import re
import uuid
from collections import namedtuple
from operator import add
from random import choice, randint
import numpy as np


### You should define your evaluation function here
# Inputs: pos - tuple (position of player), enemy_pos - tuple, food - array
# Output: your evaluation score
def evalfuncReflex(pos, enemy_pos, dest_blocks):

    closest_food = min(manhattan_distance(pos, some_food) for some_food in dest_blocks)

    # compute score for enemy distance
    enemy_dist = manhattan_distance(pos, enemy_pos)

    #Instead of a function, we 'hardcode' certain weights. If enemy is more than 3 blocks away, ignore him.
    if enemy_dist == 2:
        enemy_score = -1
    elif enemy_dist == 1 or enemy_dist == 0:
        enemy_score = -10
    elif enemy_dist == 3:
        enemy_score = -0.5
    else:
        enemy_score = 0

    # compute score for closest food
    closest_food_score = 1 / (closest_food + 1)
    #idea: The less food here is, the more valuable the food around you is and vis-versa, but NOT
    #      enough to put the agent in danger
    remaining_food_score = 1 / len(dest_blocks)


    return closest_food_score + enemy_score + remaining_food_score


### Implement a way for the agent to decide which way to move
# Inputs: pos - tuple (position of player), world_state, enemy_pos - tuple, food - array
# Output: direction in which to move (can be a string, int, or whatever way you want to implement it)
def chooseAction(pos, wstate, dest_blocks, enemy_pos):

    # get a list of legal moves
    legal_moves = legalMoves(wstate)



    # here we must account for our location begin (x.5, y.5), so we subtract by -.5 and
    # add +-1 to the appropriate coordinate.
    scores = []
    for legal_move in legal_moves:
        if legal_move == "left":
            scores.append(evalfuncReflex((pos[0]+0.5, pos[1]-0.5), enemy_pos, dest_blocks))
        elif legal_move == "right":
            scores.append(evalfuncReflex((pos[0]-1.5, pos[1]-0.5),enemy_pos, dest_blocks))
        elif legal_move == "forward":
            scores.append(evalfuncReflex((pos[0]-0.5, pos[1]+0.5),enemy_pos, dest_blocks))
        else: #backward
            scores.append(evalfuncReflex((pos[0]-0.5, pos[1]-1.5), enemy_pos, dest_blocks))


    # optimal score is the highest score in the list
    best_score = max(scores)

    # optimal moves are those moves with scores that match the highest score in the list of scores
    best_moves = [index for index in range(len(scores)) if scores[index] == best_score]
    # choose some best move
    some_best_move = random.choice(best_moves)

    # returns the chosen best move
    return legal_moves[some_best_move]


### Move the agent here
# Output: void (should just call the correct movement function)
def reflexAgentMove(agent, pos, wstate, dest_blocks, enemy_pos):
    ### YOUR CODE HERE ###
    # determine what action should be taken based on the current world state
    action = chooseAction(pos, wstate, dest_blocks, enemy_pos)

    if action == "right":
        moveRight(agent)

    elif action == "left":
        moveLeft(agent)

    elif action == "forward":
        moveStraight(agent)

    elif action == "back":
        moveBack(agent)

    return


### Helper methods for you to use ###

# Simple movement functions
# Hint: if you want your execution to run faster you can decrease time.sleep
def moveRight(ah):
    ah.sendCommand("strafe 1")
    time.sleep(0.1)


def moveLeft(ah):
    ah.sendCommand("strafe -1")
    time.sleep(0.1)


def moveStraight(ah):
    ah.sendCommand("move 1")
    time.sleep(0.1)


def moveBack(ah):
    ah.sendCommand("move -1")
    time.sleep(0.1)


# Used to find which movements will result in the player walking into a wall
### Input: current world state
### Output: An array directional strings
def illegalMoves(world_state):
    blocks = []
    if world_state.number_of_observations_since_last_state > 0:
        msg = world_state.observations[-1].text
        observations = json.loads(msg)
        grid = observations.get(u'floor3x3W', 0)
        if grid[3] == u'diamond_block':
            blocks.append("right")
        if grid[1] == u'diamond_block':
            blocks.append("back")
        if grid[5] == u'diamond_block':
            blocks.append("left")
        if grid[7] == u'diamond_block':
            blocks.append("forward")

        return blocks


def legalMoves(world_state):
    blocks = []
    if world_state.number_of_observations_since_last_state > 0:
        msg = world_state.observations[-1].text
        observations = json.loads(msg)
        grid = observations.get(u'floor3x3W', 0)
        if grid[3] != u'diamond_block':
            blocks.append("right")
        if grid[1] != u'diamond_block':
            blocks.append("back")
        if grid[5] != u'diamond_block':
            blocks.append("left")
        if grid[7] != u'diamond_block':
            blocks.append("forward")

        return blocks


# Used to find the Manhattan distance between two tuples
def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)


# Do not modify!
###
###
# This functions moves the enemy agent randomly #
def enemyAgentMoveRand(agent, ws):
    time.sleep(0.1)
    illegalgrid = illegalMoves(ws)
    legalLST = ["right", "left", "forward", "back"]
    for x in illegalgrid:
        if x in legalLST:
            legalLST.remove(x)
    y = randint(0,len(legalLST)-1)
    togo = legalLST[y]
    if togo == "right":
        moveRight(agent)

    elif togo == "left":
        moveLeft(agent)

    elif togo == "forward":
        moveStraight(agent)

    elif togo == "back":
        moveBack(agent)