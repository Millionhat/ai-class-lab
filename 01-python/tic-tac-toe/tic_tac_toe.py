import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    horizontal=self.horizontal()
    vertical=self.vertical()
    diagonal=self.diagonal()
    if(horizontal !=None or vertical!=None or diagonal!=None):
      if(horizontal==_PLAYER_SYMBOL or vertical==_PLAYER_SYMBOL or diagonal==_PLAYER_SYMBOL):
        self.winner=_PLAYER
        return True
      else:
        self.winner=_MACHINE
        return True
    return self.board.count(None) == 0
  
  def horizontal(self):
    if(self.board[0]==self.board[1] and self.board[1]==self.board[2] and self.board[2]!=None):
      return self.board[0]
    elif(self.board[3]==self.board[4] and self.board[4]==self.board[5] and self.board[5]!=None):
      return self.board[3]
    elif (self.board[6]==self.board[7] and self.board[7]==self.board[8] and self.board[8]!=None):
      return self.board[6]
    
    return None

  def vertical(self):
    if(self.board[0]==self.board[3] and self.board[3]== self.board[6] and self.board[6] != None):
      return self.board[0]
    elif(self.board[1] == self.board[4] and self.board[4]==self.board[7] and self.board[7] !=None):
      return self.board[1]
    elif(self.board[2]==self.board[5] and self.board[5]==self.board[8] and self.board[8]!=None):
      return self.board[2]

    return None

  def diagonal(self):
    if(self.board[0]== self.board[4] and self.board[4]==self.board[8] and self.board[0]!=None):
      return self.board[4]
    elif (self.board[2]==self.board[4] and self.board[4]==self.board[7] and self.board[2]!=None):
      return self.board[4]
    
    return None


  

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    placed=False
    while(placed == False):
      position=random.randint(0,8)
      if self.board[position] is None:
        self.board[position] = _MACHINE_SYMBOL
        placed=True


  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    #  x|o| 
    #   | | 
    #   | | 
    boardCopy = self.board[:]
    for i in range(0,len(boardCopy),1):
      if(boardCopy[i] == None):
        boardCopy[i]=" "
    separation = [boardCopy[i:i+3] for i in range(0,len(boardCopy),3)]
    for x in separation:
      
      print('|'.join(x))
    

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    self.format_board()
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    if(self.winner==None):
      print("The Game ended in a tie")
    else:
      print("The winner is "+ self.winner)
