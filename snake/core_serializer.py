# author: smilu97
# description: serialize states in core

import numpy as np

state_code = ['blank', 'tails', 'head', 'food']

def serialize(core):
    w = core.max_x + 1
    h = core.max_y + 1
    state = np.zeros((w, h), np.int32)

    def getidx(x, y):
        return x + y * w

    for pos in core.trails:
        state[pos] = 1
    state[core.x, core.y] = 2
    state[core.fx, core.fy] = 3
    
    return state
    