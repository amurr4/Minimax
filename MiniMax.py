#class that implements the MiniMax algorithm.
import random
import sys
import Square
from TicTacToeAction import TicTacToeAction
from TicTacToeState import TicTacToeState


class MiniMax:
    def __init__(self):
        self.numberOfStates=0
        self.usePruning=False

    def MinimaxDecision(self,state,usePruning):
        self.usePruning=usePruning
        if usePruning:
            alpha = float("-inf")
            beta = float("inf")
        else:
            alpha = None
            beta = None
    
        moveList=[]
    
        for action in state.getActions():
            utility=self.MinValue(state.getResult(action),alpha,beta)
            print("UTILITY:",utility," at pos:",action.position)
            moveList.append([utility,action])
        
        max_utility = max(moveList, key=lambda x: x[0])[0]
        best_moves = [element[1] for element in moveList if element[0] == max_utility]
        chosenAction = random.choice(best_moves)
        print("State space size: " , self.numberOfStates)
        return chosenAction


    def MinValue(self, state, alpha, beta):
        self.numberOfStates += 1
        
        if state.isTerminal():
            return state.utility
        
        val=float('inf')
        for action in state.getActions():
            val=min(val,self.MaxValue(state.getResult(action),alpha,beta))

            if self.usePruning:

                if val<=alpha:
                    return val
                beta=min(beta,val)

        return val
        
    def MaxValue(self,state,alpha,beta):
        self.numberOfStates+=1
        if state.isTerminal():
            return state.utility
        
        val=float('-inf')
        for action in state.getActions():
            val=max(val,self.MinValue(state.getResult(action),alpha,beta))

            if self.usePruning:

                if val>=beta:
                    return val
                alpha=max(alpha,val)
                
        return val
     