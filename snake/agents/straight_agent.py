# author: smilu97
# description: Straightly moving, snake agent

# state_code = ['blank', 'tails', 'head', 'food']

class StraightAgent:

    def __init__(self):
        self.idx_to_action = ['left', 'right', 'up', 'down']

    def process(self, state):
        head = None
        for x in range(state.shape[0]):
            for y in range(state.shape[1]):
                if state[x, y] == 2:
                    head = (x, y)
                    break
            if head is not None:
                break
        
        food = None
        for x in range(state.shape[0]):
            for y in range(state.shape[1]):
                if state[x, y] == 3:
                    food = (x, y)
                    break
            if food is not None:
                break
        
        action = 0
        if head[0] < food[0]:
            action = 1
        if head[0] > food[0]:
            action = 0
        if head[1] < food[1]:
            action = 3
        if head[1] > food[1]:
            action = 2
    
        return self.idx_to_action[action]
