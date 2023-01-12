"""Syntax Notes Applicable to Python"""

#Classes
class Chess:
    def knight(self, path):
        legal = ["1", "2", "4", "5", "7", "8", "10", "11"]
        if path in legal:
            print("knight to " + user_path)
        else:
            print("not a legal move")

#Variables
white = Chess()
black = Chess()
legal = ["1", "2", "4", "5", "7", "8", "10", "11"]

#Code
while True:
    piece = str(input("Your Piece: "))
    piece = Chess()
    user_path = str(input("Your Move: "))
    white.piece(user_path)
    if user_path in legal:
        break