#!/usr/bin/env python
# author: smilu97
# description: Run simple snake game(./snake)

from snake import *
import sys

select = int(sys.argv[1])
if select > 0:
    renderable = int(sys.argv[2])
    if not renderable:
        playcount = int(sys.argv[3])

agents = [RandomAgent, StraightAgent, PathfindAgent]

if select == 0:  # manual play
    player = SnakePlayer()
    player.run()
else:  # random agent play
    if renderable:
        agent = agents[select - 1]()
        player = SnakeAgentPlayer(agent, True)
        player.run()
    else:
        for i in range(playcount): 
            agent = agents[select - 1]()
            player = SnakeAgentPlayer(agent, False)
            player.run()
