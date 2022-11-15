#### Snake & Ladder

from enum import Enum
import random
from copy import deepcopy

class EntityType(Enum):
    SNAKE=1
    LADDER=2


class Board:
    def __init__(self):
        self.board=[]
        self.entities={}
        self.size=0
        self.players={}

    # adding snakes and ladders to quickly access the sqaures blockers
    def add_entity(self,entities):
        for entity in entities:
            self.entities[entity.start]=entity

    def init_board(self,size,entities):
        self.size=size
        self.board=[[j+i for i in range(1,size+1)]  for j in range(0,size*size,size)]
        self.add_entity(entities)

    def display_board(self):
        flag=True if self.size%2==0 else False
        for i in range(self.size-1,-1,-1):
            row=[]
            for j in range(self.size-1,-1,-1):
                pos=self.board[i][j]
                entity=self.entities.get(pos)
                if entity and entity.etype==EntityType.SNAKE:
                    row.append("SN")
                elif entity and entity.etype==EntityType.LADDER:
                    row.append("LD")
                elif self.players.get(pos):
                    row.append(str(self.players.get(pos).username[:2]))
                else:
                    row.append(str(pos))

            print("  ".join(row) if flag else "  ".join(row[::-1]))
            flag=not(flag)


class Entity:
    def __init__(self,start,end,etype):
        # start and ends will be ints ranging from 1-100
        self.start=start
        self.end=end
        self.etype=etype


class Snake(Entity):
    def __init__(self,start,end):
        Entity.__init__(self,start,end,EntityType.SNAKE)


class Ladder(Entity):
    def __init__(self,start,end):
        Entity.__init__(self,start,end,EntityType.LADDER)


class Dice:
    def __init__(self):
        self.rolls=[]

    def roll_dice(self):
        return random.randint(1,6)


class Game:
    def __init__(self,id,players,board):
        self.id=id
        self.lastTurn=None
        self.players=players
        self.winner=None
        self.board=board

    
    def get_turn(self):

        if self.lastTurn==None:
            self.lastTurn=random.randint(0,len(self.players)-1)
        if self.lastTurn==len(self.players)-1:
            self.lastTurn=0
        else:
            self.lastTurn+=1


        return self.players[self.lastTurn]


    def make_move(self,player,steps):

        player.position+=steps

        if player.position>self.board.size**2:
            player.position-=steps
            return False

        if self.board.entities.get(player.position):
            entity=self.board.entities[player.position]
            player.position=entity.end
        
        self.board.players[player.position]=deepcopy(player)

        return True


    def has_winner(self,player=None):
        if player:
            return self.board.board[-1][-1]==player.position
        return self.board.players.get(self.board.size**2)!=None


    def start_game(self):

        dice=Dice()
        gameOver=False
        
        while gameOver==False:
            player=self.get_turn()

            user=input(f"\n>>>Player Turn: {player.username}\n      Enter 'y' to make move: ")
            if user!="y":
                break

            rolls=dice.roll_dice()
            print(f"Rolling Dice............And it's a {rolls}!\n")

            checkmove= self.make_move(player,rolls)

            if checkmove==False:
                print("Whoops! No move allowed!")
                continue
            
            self.board.display_board()
            gameOver=self.has_winner(player)

        if gameOver:
            print(f"\n\n >>>>>>> Hurray!!!! {player.username} has Won!    <<<<<<<")

            
class Player:
    def __init__(self,username):
        self.username=username
        self.games=None
        self.position=0


if __name__=="__main__":

    print("\n\n-----------------------------------------------------------")
    print(">>>>>>>>  WELCOME TO INTERACTIVE SNAKE & LADDER   <<<<<<<<")
    print("-----------------------------------------------------------\n\n")

    print(">>>>>>>   Board Setup   <<<<<<<\n")
    board_size=int(input("Board Size: ").strip())
    entities=[]

    total_snakes = int(input("Total Snakes: ").strip())
    for i in range(total_snakes):
        temp=input(f"Snake {i+1}  (Start  end): ").strip().split(" ")
        snake=Snake(int(temp[0]),int(temp[-1]))
        entities.append(snake)

    total_ladder = int(input("Total Ladders: ").strip())
    for i in range(total_ladder):
        temp=input(f"Ladder {i+1}  (Start  end): ").strip().split(" ")
        ladder=Ladder(int(temp[0]),int(temp[-1]))
        entities.append(ladder)

    board=Board()
    board.init_board(board_size,entities)

    print("\n\n>>>>>>>   Display Board   <<<<<<<\n")
    board.display_board()

    print("\n\n>>>>>>>>   Players Time   <<<<<<<<")
    total_players = int(input("Total Players: ").strip())
    players=[]

    print("Usernames: ")
    for i in range(total_players):
        username=input(f"    Player {i+1} : ")
        player=Player(username)
        players.append(player)

    game=Game(1,players,board)

    print("\n\n-----------------------------------------------------------")
    print(">>>>>>>>>>>>>>>  HOLD TIGHT! STARTING THE GAME  <<<<<<<<<<")
    print("-----------------------------------------------------------\n\n")

    game.start_game()



