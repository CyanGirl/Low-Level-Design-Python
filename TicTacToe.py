'''
Tic Tac Toe Requirements:

- Mutiple Players can play
- Players able to win by any winning strategy
- There can be multiple winning strategies
- Entities can have types
- Board can be customised with given size
- Games have specific players and board
'''



from abc import ABC, abstractmethod

###### BOARDS

class Board(ABC):

    @abstractmethod
    def display_board(self):
        pass

    @abstractmethod
    def set_board(self):
        pass

class TicTacToeBoard(Board):

    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.board=[["-"]*cols for _ in range(rows)]
        self.empty=rows*cols

    def set_board(self,row,col,entity):
        self.board[row][col]=entity
        self.empty-=1

    def is_available(self,row,col):
        if self.board[row][col]=="-":
            return True
        return False

    def display_board(self):
        print()
        for row in self.board:
            for col in row:
                if col!="-":
                    print(f"{col.value}  ",end="")
                else:
                    print(f"{col}  ",end="")
            print("\n")



###### ENTITIES

from enum import Enum

class Entity(Enum):
    CIRCLE = "O"
    CROSS = "X"



######## WINNING STRATEGY

class WinningStrategy(ABC):

    @abstractmethod
    def check_win(self,move, board: Board) -> bool:
        pass

class StandardWin(WinningStrategy):

    def check_win(self, move, board: Board) -> bool:
        entity=board.board[move.row][move.col]
        
        row_check = all([sq==entity for sq in board.board[move.row]])
        if row_check: return True

        col_check = True
        for row in range(board.rows):
            if board.board[row][move.col]!=None and board.board[row][move.col]==entity:
                continue
            else:
                col_check=False
                break

        if col_check: return True

        return False



###### PLAYERS

class Player(ABC):
    
    def __init__(self,username) -> None:
        self.username=username
        self.games={}
        self.current_game={}


class TicTacToePlayer(Player):

    def __init__(self, username, entity) -> None:
        super().__init__(username)
        self.entity_selected=entity
        


###### MOVES

class Move(ABC):

    def __init__(self,playerid,row,col) -> None:
        self.player=playerid
        self.row=row
        self.col=col

    @abstractmethod
    def execute(self,board):
        pass

class TicTacToeMove(Move):

    def __init__(self, playerid, row, col) -> None:
        super().__init__(playerid, row, col)

    def execute(self,board):
        self.board[self.row][self.col]=self.playerid.entity_selected
        




####### GAME

class Game(ABC):

    def __init__(self,id, board,players,win_strategy) -> None:
        self.gameId=id
        self.players=players
        self.board=board
        self.win_strategy=win_strategy
        self.winner=None
        self.moves=[]
        self.current_turn=None

    @abstractmethod
    def save_move(self,move):
        pass

    @abstractmethod
    def check_winner(self,entity):
        pass

    @abstractmethod
    def make_move(self, player:Player, nextMove, entity):
        pass

    @abstractmethod
    def get_turn(self):
        pass


class TicTacToeGame(Game):
    def __init__(self, id, board, players, win_strategy) -> None:
        super().__init__(id, board, players, win_strategy)

    def save_move(self, move):
        self.moves.append(move)

    def check_winner(self,move):
        return self.win_strategy.check_win(move,self.board)

    def make_move(self,player,nextMove):
        if self.board.is_available(nextMove.row,nextMove.col):
            self.board.set_board(nextMove.row,nextMove.col,player.entity_selected)
            self.save_move(nextMove)
            return True
        return False


    def get_turn(self):
        idx=self.current_turn
        if idx==None:
            idx=0
        if idx==len(self.players)-1:
            idx=0
        else:
            idx+=1

        self.current_turn = idx

        return self.players[self.current_turn]



####### Driver code

def tic_tac_toe_driver(board:TicTacToeBoard,players):

    print("\n\n_____________ Welcome to Tic Tac Toe ___________\n\nStrategise the Board.....")
    board.display_board()
    
    game=TicTacToeGame(1,board,players,StandardWin())

    while game.winner==None and board.empty>0:
        player=game.get_turn()

        print("Present Turn :",player.username,end=" ")
        moves=input("||  Row Col: ")
        row,col=list(map(int,moves.split(" ")))

        move=TicTacToeMove(player,row,col)
        if not(game.make_move(player,move)):
            print("Could not make the move!")


        board.display_board()

        if game.check_winner(move):
            print(f"\n____________{player.username} Won!!!!__________")
            return


    print(f"Its a draw!!!")


if __name__== "__main__":
    board=TicTacToeBoard(3,3)
    players=[TicTacToePlayer("AAA",Entity.CIRCLE),TicTacToePlayer("BBB",Entity.CROSS)]
    tic_tac_toe_driver(board,players)






    
