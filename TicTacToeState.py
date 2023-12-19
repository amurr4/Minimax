#class that implements a state and the playing logic of the TicTacToe game.
import Square
from TicTacToeAction import TicTacToeAction


class TicTacToeState:

    def updateUtility(self):

        ## Row check
        i=0
        a=1
        for i in range(3):
            if((self.field[a*i]==self.field[a*i+1]==self.field[a*i+2]) and self.field[a*i]!=Square.EMPTY): 
                if self.field[a*i]==Square.X:
                    self.utility=1
                else:self.utility=-1
                return
            a=3
            
        i=0
        ## Column check
        for i in range(3):
            #print("i:",i," i+3",i+3," i+6",i+6)
            if((self.field[i]==self.field[i+3]==self.field[i+6]) and self.field[i]!=Square.EMPTY): 
                if self.field[i]==Square.X:
                    self.utility=1
                else:self.utility=-1
                return
            
        ## Diagonal check
        if(((self.field[0]==self.field[4]==self.field[8]) or 
           (self.field[2]==self.field[4]==self.field[6])) and self.field[4]!=Square.EMPTY):
                if self.field[4]==Square.X:
                    self.utility=1
                else:
                    self.utility=-1
                return
        
        self.utility=0
        return


    # Default constructor.
    def __init__(self):
        self.field = [] # < The field, consisting of nine squares.First three values correspond to first row, and so on.
        for i in range(9):
            self.field.append(Square.EMPTY)
        self.player = Square.X # < The player, either X or O.
        self.playerToMove = Square.X # < The player that is about to move.
        self.utility = 0 # < The utility value of this state.Can be 0, 1 (won) or -1 (lost).

    def getActions(self):
        actionList=[]

        for i in range(0,9):    

            if self.field[i]==Square.EMPTY:
                someAction=TicTacToeAction(self.playerToMove,i)
                actionList.append(someAction)
     
        return actionList
    
    def getUtility(self):
        return self.utility

    def getResult(self,action):

        #Copy of current field and current player
        newstate = TicTacToeState()
        newstate.field=self.field[:]
        newstate.player=self.player
        newstate.playerToMove=self.playerToMove

        #Switching the player to move
        if newstate.playerToMove==Square.X:
            newstate.playerToMove=Square.O
        else:newstate.playerToMove=Square.X

        newstate.field[action.getPosition()]=action.getPlayer()
        newstate.updateUtility()
        return newstate

    def isTerminal(self):

        if self.utility!=0:
            return True
        
        if all(spot != Square.EMPTY for spot in self.field):
            return True
        
        return False


#COMPLETE
    def printresult(self):
        s = "" + self.field[0] + "|" + self.field[1] + "|" + self.field[2] + "\n"
        s += "-+-+-\n"
        s += self.field[3] + "|" + self.field[4] + "|" + self.field[5] + "\n"
        s += "-+-+-\n"
        s += self.field[6] + "|" + self.field[7] + "|" + self.field[8] + "\n"
        print(s)