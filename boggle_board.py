import random 

class BoggleBoard:
  
  def __init__(self):
    self.rows = "_ _ _ _\n"*4


  

  def shake(self):
    holding_string=""
  
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = random.randint(0,25)
    count = 0
    for letter in range(16):
      holding_string = holding_string + alphabet[number] + " "
      number = random.randint(0,25)
      count+=1 
      if count % 4 == 0:
        holding_string = holding_string + "\n"

    self.rows = holding_string    
    
    return self.rows

  def smart_boggle(self):
    dice = '''AAEEGN
ELRTTY
AOOTTW
ABBJOO
EHRTVW
CIMOTU
DISTTY
EIOSST
DELRVY
ACHOPS
HIMNQU
EEINSU
EEGHNW
AFFKPS
HLNNRZ
DEILRX'''

    dice_list = dice.split('\n')
    dice_number = random.randint(0,5)
    holding_string = ''
    count = 0

    for dice in dice_list:
      if dice[dice_number]=="Q":
        holding_string = holding_string + "Qu "
      else:
        holding_string = holding_string + dice[dice_number]+ "  "
      count+=1 
      if count % 4 == 0:
         holding_string = holding_string + "\n"
    return holding_string     
      



  
  

    


board_one = BoggleBoard()
print(board_one.smart_boggle())
#print(board_one.shake())