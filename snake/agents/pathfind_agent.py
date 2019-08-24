# author: smilu97
# description: Pathfinding, snake agent

# state_code = ['blank', 'tails', 'head', 'food']

import numpy as np
import random

nn = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs_pathfind(m, init, target):
    '''
    pathfind
    code:
        0: blank
        1: wall
    '''
    q = [init]
    visit = np.zeros_like(m)
    back = np.zeros_like(m)
    found = False

    while len(q) > 0:
        u = q[0]
        q = q[1:]
        nis = list(range(4))
        random.shuffle(nis)
        for ni in nis:
            v = (u[0]+nn[ni][0], u[1]+nn[ni][1])
            if v[0] < 0 or v[0] >= m.shape[0]: continue
            if v[1] < 0 or v[1] >= m.shape[1]: continue
            if m[v] == 1: continue
            if visit[v] == 1: continue
            visit[v] = 1
            back[v] = ni
            q.append(v)
            if v == target:
                q = []
                found = True
                break

    return back, found


class PathfindAgent:

    def __init__(self):
        self.idx_to_action = ['left', 'right', 'up', 'down']
        self.moves = []
    
    def update_moves(self, state):
        m = np.zeros_like(state)
            
        init = None
        for x in range(state.shape[0]):
            for y in range(state.shape[1]):
                if state[x, y] == 2:
                    init = (x, y)
                    break
            if init is not None: break
        target = None
        for x in range(state.shape[0]):
            for y in range(state.shape[1]):
                if state[x, y] == 3:
                    target = (x, y)
                    break
            if target is not None: break
        for x in range(state.shape[0]):
            for y in range(state.shape[1]):
                if state[x, y] == 1:
                    m[x, y] = 1
                else:
                    m[x, y] = 0
        
        back, found = bfs_pathfind(m, init, target)
        if not found: return 'left'
        
        backs = []
        cur = target
        while cur != init:
            backs.append(back[cur])
            nd =  nn[back[cur]]
            cur = (cur[0] - nd[0], cur[1] - nd[1])
        backs.reverse()

        self.moves = backs

    def process(self, state):
        if len(self.moves) == 0:
            self.update_moves(state)
        
        if len(self.moves) == 0:
            return 'left'
        action = self.moves[0]
        self.moves = self.moves[1:]
        return self.idx_to_action[action]
