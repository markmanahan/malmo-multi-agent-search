# Created by Minbiao Han and Roman Sharykin
# AI fall 2018

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
from random import *
import numpy as np


### You should define your evaluation function here
# Inputs: pos - tuple (position of player), enemy_pos - tuple, food - array
# Output: your evaluation score
def evalfuncReflex(pos, enemy_pos, dest_blocks):
    # make a copy of destination blocks
    # temp_food_list = list(dest_blocks)

    # a list of distances to pieces of food
    food_distances = []

    # for some_dest in dest_blocks:  # for every destination block
    #    if some_dest in temp_food_list:  # if the destination block is "marked" as having food
    #        food_distances.append(manhattan_distance(pos, some_dest))  # append the distance to that food to the list
    #        del temp_food_list[some_dest]  # "un-mark" the block to account for the food being eaten

    # TO-DO: evaluate scores; depth 1, best possible action for the given state; play around with constants

    #  find the closest piece of food
    # closest_food = min(manhattan_distance(pos, dest_blocks[i]) for i in range(len(dest_blocks)))
    for i in range(len(dest_blocks)):
        food_distances.append(manhattan_distance(pos, dest_blocks[i]))

    closest_food = min(food_distances)

    # compute score for enemy distance
    enemy_score = -2 / (manhattan_distance(pos, enemy_pos) + 1)

    # compute score for closest food
    closest_food_score = 0.5 / (closest_food + 1)

    # returns a combined score comprised of closest food score, enemy score, and amount of food left
    return closest_food_score + enemy_score + len(dest_blocks)


### Implement a way for the agent to decide which way to move
# Inputs: pos - tuple (position of player), world_state, enemy_pos - tuple, food - array
# Output: direction in which to move (can be a string, int, or whatever way you want to implement it)
def chooseAction(pos, wstate, dest_blocks, enemy_pos):
    # get a list legal moves
    legal_moves = legalMoves(wstate)

    # retrieve current coordinates and form coordinates for directions, given that there is not a wall in the direction
    pos_x, pos_y = pos
    if "forward" in legal_moves:
        up = (pos_x, pos_y + 1)
    if "back" in legal_moves:
        down = (pos_x, pos_y - 1)
    if "left" in legal_moves:
        left = (pos_x - 1, pos_y)
    if "right" in legal_moves:
        right = (pos_x + 1, pos_y)

    # a list for the computed scores for directional moves
    scores = [0, 0, 0, 0]  # up score, down score, left score, right score

    # boolean variables to remember directional moves that were checked
    bool_up = False
    bool_down = False
    bool_left = False
    bool_right = False

    for legal_move in legal_moves:  # for every legal move (until we have looked at all directions)
        if legal_move == "forward" and not bool_up:  # check the world state above
            scores[0] = (evalfuncReflex(up, dest_blocks, enemy_pos))
            bool_up = True
        elif legal_move == "back" and not bool_down:  # below
            scores[1] = (evalfuncReflex(down, dest_blocks, enemy_pos))
            bool_down = True
        elif legal_move == "left" and not bool_left:  # to the left
            scores[2] = (evalfuncReflex(left, dest_blocks, enemy_pos))
            bool_left = True
        elif legal_move == "right" and not bool_right:  # to the right
            scores[3] = (evalfuncReflex(right, dest_blocks, enemy_pos))
            bool_right = True
        if bool_up and bool_down and bool_left and bool_right:  # if we have checked every direction already
            break  # stop checking other legal moves

    # find the optimal score, the highest score in the list
    best_score = max(scores)

    # optimal moves are those moves with scores that match the highest score
    best_moves = [index for index in range(len(scores)) if scores[index] == best_score]

    # choose some best move
    some_best_move = random.choice(best_moves)

    # returns the chosen best move and deletes the corresponding food; don't need to account for deleeting dest-blocks/food at all
    if some_best_move == 0:  # up
        return "forward"
    elif some_best_move == 1:  # down
        return "back"
    elif some_best_move == 2:  # left
        return "left"
    elif some_best_move == 3:  # right
        return "right"


### Move the agent here
# Output: void (should just call the correct movement function)
def reflexAgentMove(agent, pos, wstate, dest_blocks, enemy_pos):
    # determine what action should be taken based on the current world state
    action = chooseAction(pos, wstate, dest_blocks, enemy_pos)

    if action == "forward":
        moveStraight(agent)
    elif action == "back":
        moveBack(agent)
    elif action == "left":
        moveLeft(agent)
    elif action == "right":
        moveRight(agent)

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
