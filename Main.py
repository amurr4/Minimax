import Square
from MiniMax import MiniMax
from TicTacToeAction import TicTacToeAction
from TicTacToeState import TicTacToeState

if __name__ == '__main__':
    print("The squares are numbered as follows:")
    print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n")
    mark=False
    print("Do you want to use pruning? 1=no 2=yes ")
    use=(int)(input())
    if use == 2:
        mark=True
    print("Who should start? 1=you 2=computer ")
    temp =(int)(input())
    s = TicTacToeState()
    s.player = Square.X
    if (temp == 1):
        s.playerToMove = Square.O
    else :
        s.playerToMove = Square.X
    while (True):
        if (s.playerToMove == Square.X):
            minimax=MiniMax()
            a=minimax.MinimaxDecision(s, mark)
            s = s.getResult(a)
        else :
            print("Which square do you want to set? (1--9) ")
            while (True):
                temp = (int)(input())
                if  temp >= 1 & temp <= 9 :
                     break
            a = TicTacToeAction(Square.O, temp - 1)
            s = s.getResult(a)
        s.printresult()
        if s.isTerminal():
            break
    if (s.getUtility() > 0):
        print("You lost")
    elif (s.getUtility() < 0):
        print("You win")
    else:
        print("Draw")
