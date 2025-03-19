from SearchProblem import SearchProblem, Edge
import os

class Chezz(SearchProblem):

    startingColour = 'w'

    def __init__( self, colour, board=None, i1 = None, i2 = None, i3 = None):
        
        self.path = ''
        self.colour = colour
        if not(i1 == None):
            self.i1 = i1
        if not(i2 == None):
            self.i2 = i2
        if not(i3 == None):
            self.i3 = i3
            
        if board == None:
            raise TypeError("Needs state")
        else:
            self.board = board

    def setStartingColour(c):
        Chezz.startingColour = c

    #Input is a board, makes file out of that board
    #Doesnt call edges
    def outputBoard(self, board):
        counter = 000
        output = '' 
       
        # Three integers sho8ld be here
        
        dest = board
        counter += 1
        if self.colour == 'w':
            col = 'b'
        elif self.colour == 'b':
            col = 'w'
        output = ''
        output = output + col + ' ' + str(self.i1)+' ' +str(self.i2)+ ' ' +str(self.i3)+ '\n' + '{' + '\n'
        for pair in dest.items():
            
            key, value = pair
            if value != ' ':
                output = output + '  ' + Chezz.convertKeyToCoords(key) + ': \'' + str(value) + '\',\n'
    
        output = output + '}\n' #integers should be here

        print(output)
        # f = open('board.' + Chezz.fileNumber(counter), "w")
        # f.write(output)
        # f.close()


    def makeBoards(self):

        newMoves = self.edges()
        counter = 000
        output = '' 
       
        # Three integers sho8ld be here
        for e in newMoves:
            dest = e.destination.board
            counter += 1
            if self.colour == 'w':
                col = 'b'
            elif self.colour == 'b':
                col = 'w'
            output = ''
            output = output + col + ' ' + str(self.i1)+' ' +str(self.i2)+ ' ' +str(self.i3)+ '\n' + '{' + '\n'
            for pair in dest.items():
                
                key, value = pair
                if value != ' ':
                    output = output + '  ' + Chezz.convertKeyToCoords(key) + ': \'' + str(value) + '\',\n'
        
            output = output + '}\n' #integers should be here

            f = open('board.' + Chezz.fileNumber(counter), "w")
            f.write(output)
            f.close()
    
    def fileNumber(value):
        if value < 10:
            return "00" + str(value)
        elif value < 100:
            return "0" + str(value)
        else:
            return str(value)

    def colourFilter(self, pair):
        key, value = pair

        if value[0] == self.colour:
            return True
        else:
            return False
    
    def enemyFilter(self, pair):
        key, value = pair
        
        if self.colour == 'w':
            if value[0] == 'b': return True
            else: return False
        elif self.colour == 'b':
            if value[0] == 'w': return True
            else: return False

    def getColouredPieces(self):
        
        teamPieces = dict(filter(self.colourFilter, self.board.items()))
        return teamPieces

    def getEnemyPieces(self):
        
        teamPieces = dict(filter(self.enemyFilter, self.board.items()))
        return teamPieces

    

    def movePeon(self, key):
        moves = []

        if self.colour == 'w':


            if self.empty(self.checkSpace((key[0], key[1] + 1))):
                moves.append(self.move(key, (key[0], key[1] + 1), 'P'))
            if self.enemy(self.checkSpace((key[0] + 1, key[1] + 1))[0]):
                moves.append(self.move(key, (key[0] + 1, key[1] + 1), 'P'))
            if self.enemy(self.checkSpace((key[0] - 1, key[1] + 1))[0]):
                moves.append(self.move(key, (key[0] - 1, key[1] + 1), 'P'))
        
        elif self.colour == 'b':


            if self.empty(self.checkSpace((key[0], key[1] - 1))):
                moves.append(self.move(key, (key[0], key[1] - 1), 'P'))
            if self.enemy(self.checkSpace((key[0] - 1, key[1] - 1))[0]):
                moves.append(self.move(key, (key[0] - 1, key[1] - 1), 'P'))
            if self.enemy(self.checkSpace((key[0] + 1, key[1] - 1))[0]):
                moves.append(self.move(key, (key[0] + 1, key[1] - 1), 'P'))
       

        return moves   
    def moveZombie(self, key):

        moves = []

        moves.extend(self.moveOneStepRook(key, 'Z'))

        return moves

    def moveKing(self, key):
        moves = []
        moves.extend(self.moveOneStepRook(key, 'K'))
        moves.extend(self.moveOneStepBishop(key, 'K'))
        return moves

    def moveRook(self, key):
        return self.moveRookLong(key, 'R')
    
    def moveBishop(self, key):
        return self.moveBishopLong(key,'B')
    
    def moveQueen(self, key):
        moves = []
        moves.extend(self.moveRookLong(key, 'Q'))
        moves.extend(self.moveBishopLong(key, 'Q'))
        return moves
    

    def moveKnight(self, key):
        moves = []
        piece = 'N'
        if self.notTeam(self.checkSpace((key[0] + 2, key[1] - 1))[0] ):
            moves.append(self.move(key, (key[0] + 2, key[1] - 1), piece))
        if self.notTeam(self.checkSpace((key[0]  + 2, key[1] + 1))[0]):
            moves.append(self.move(key, (key[0] + 2, key[1] + 1), piece))
        
        if self.notTeam(self.checkSpace((key[0] - 2, key[1] + 1))[0]):
            moves.append(self.move(key, (key[0] -2 , key[1] + 1), piece))
        if self.notTeam(self.checkSpace((key[0] - 2, key[1] - 1))[0]):
            moves.append(self.move(key, (key[0] -2 , key[1] - 1), piece))
        
        if self.notTeam(self.checkSpace((key[0] + 1, key[1] + 2))[0] ):
            moves.append(self.move(key, (key[0] + 1, key[1] + 2), piece))
        if self.notTeam(self.checkSpace((key[0] - 1, key[1] + 2))[0]):
            moves.append(self.move(key, (key[0] - 1, key[1] + 2), piece))
        
        if self.notTeam(self.checkSpace((key[0] - 1, key[1] - 2))[0]):
            moves.append(self.move(key, (key[0] - 1, key[1] - 2), piece))
        if self.notTeam(self.checkSpace((key[0] + 1 , key[1] - 2))[0]):
            moves.append(self.move(key, (key[0] + 1, key[1] - 2), piece))

        return moves
    
    def moveCannon(self, key):
        moves = []
        piece = 'C'
        moves.extend(self.moveOneStepRookNoCapture(key, piece))

        if self.checkDiagonal(key, 1, 1):
            moves.append(self.shoot(key, 1, 1))
        if self.checkDiagonal(key, 1, -1):
            moves.append(self.shoot(key, 1, -1))
        if self.checkDiagonal(key, -1, 1):
            moves.append(self.shoot(key, -1, 1))
        if self.checkDiagonal(key, -1, -1):
            moves.append(self.shoot(key, -1, -1))
        


        return moves

    def moveFlinger(self, key):
        moves = []
        piece = 'F'
        moves.extend(self.moveOneStepRookNoCapture(key, piece))
        moves.extend(self.moveOneStepBishopNoCapture(key, piece))

        #Diagonal moves
        if self.team(self.checkSpace((key[0] + 1 , key[1] + 1))[0]): 
            moves.extend(self.possibleFlings((key[0] + 1 , key[1] + 1), key))
        
        if self.team(self.checkSpace((key[0] + 1 , key[1] - 1))[0]): 
            moves.extend(self.possibleFlings((key[0] + 1 , key[1] - 1), key))
        
        if self.team(self.checkSpace((key[0] - 1 , key[1] + 1))[0]): 
            moves.extend(self.possibleFlings((key[0] - 1 , key[1] + 1), key))
        
        if self.team(self.checkSpace((key[0] - 1 , key[1] - 1))[0]): 
            moves.extend(self.possibleFlings((key[0] - 1 , key[1] - 1), key))

        #Orthonginal moves
        if self.team(self.checkSpace((key[0], key[1] + 1))[0]): 
            moves.extend(self.possibleFlings((key[0] , key[1] + 1), key))
        
        if self.team(self.checkSpace((key[0], key[1] - 1))[0]): 
            moves.extend(self.possibleFlings((key[0] , key[1] - 1), key))
        
        if self.team(self.checkSpace((key[0] - 1 , key[1]))[0]): 
            moves.extend(self.possibleFlings((key[0] - 1 , key[1]), key))
        
        if self.team(self.checkSpace((key[0] + 1 , key[1]))[0]): 
            moves.extend(self.possibleFlings((key[0] + 1 , key[1] ), key))

        
        
        
        
        return moves


    def moveRookLong(self, key, piece):
        moves = []
        
        for i in range(1,8):
            if self.notTeam(self.checkSpace((key[0], key[1] - i))[0] ):
                moves.append(self.move(key, (key[0], key[1] - i), piece))
            if not(self.empty(self.checkSpace((key[0], key[1] - i))[0] )) or self.offBoard(self.checkSpace((key[0], key[1] - i))[0] ):
                break
        
        for i in range(1,8):
            if self.notTeam(self.checkSpace((key[0] - i, key[1]))[0] ):
                moves.append(self.move(key, (key[0] - i, key[1]), piece))
            if not(self.empty(self.checkSpace((key[0] - i, key[1]))[0] )) or self.offBoard(self.checkSpace((key[0] - i, key[1]))[0] ):
                break
        
        for i in range(1,8):
            if self.notTeam(self.checkSpace((key[0], key[1] + i))[0] ):
                moves.append(self.move(key, (key[0], key[1] + i), piece))
            if not(self.empty(self.checkSpace((key[0], key[1] + i))[0] )) or self.offBoard(self.checkSpace((key[0], key[1] + i))[0] ):
                break

        for i in range(1,8):
            if self.notTeam(self.checkSpace((key[0] + i, key[1]))[0] ):
                moves.append(self.move(key, (key[0] + i, key[1]), piece))
            if not(self.empty(self.checkSpace((key[0] + i, key[1]))[0] )) or self.offBoard(self.checkSpace((key[0] + i, key[1]))[0] ):
                break
        
        return moves
    

    def moveBishopLong(self, key, piece):
        moves = []
        
        for i in range(1,8):
            if self.notTeam(self.checkSpace((key[0]- i, key[1] - i))[0] ):
                moves.append(self.move(key, (key[0] - i, key[1] - i), piece))
            if not(self.empty(self.checkSpace((key[0] - i, key[1] - i))[0] )) or self.offBoard(self.checkSpace((key[0] - i, key[1] - i))[0] ):
                break
        
        for i in range(1,8):
            if self.notTeam(self.checkSpace((key[0] - i, key[1] + i))[0] ):
                moves.append(self.move(key, (key[0] - i, key[1] + i), piece))
            if not(self.empty(self.checkSpace((key[0] - i, key[1] + i))[0] )) or self.offBoard(self.checkSpace((key[0]- i, key[1] + i))[0] ):
                break
        
        for i in range(1,8):
            if self.notTeam(self.checkSpace((key[0] + i, key[1] + i))[0] ):
                moves.append(self.move(key, (key[0] + i, key[1] + i), piece))
            if not(self.empty(self.checkSpace((key[0] + i, key[1] + i))[0] )) or self.offBoard(self.checkSpace((key[0] + i, key[1] + i))[0] ):
                break

        for i in range(1,8):
            if self.notTeam(self.checkSpace((key[0] + i, key[1] - i))[0] ):
                moves.append(self.move(key, (key[0] + i, key[1] - i), piece))
            if not(self.empty(self.checkSpace((key[0] + i, key[1]- i))[0] )) or self.offBoard(self.checkSpace((key[0] + i, key[1] - i))[0] ):
                break
        
        return moves


    def moveOneStepRookNoCapture(self, key, piece):
        moves = []

        if self.empty(self.checkSpace((key[0], key[1] - 1))[0] ):
            moves.append(self.move(key, (key[0], key[1] - 1), piece))
        if self.empty(self.checkSpace((key[0] - 1, key[1]))[0]):
            moves.append(self.move(key, (key[0] - 1, key[1]), piece))
        if self.empty(self.checkSpace((key[0], key[1] + 1))[0]):
            moves.append(self.move(key, (key[0], key[1] + 1), piece))
        if self.empty(self.checkSpace((key[0] + 1, key[1]))[0]):
            moves.append(self.move(key, (key[0] + 1, key[1]), piece))

        return moves
    
    def moveOneStepBishopNoCapture(self, key, piece):
        moves = []
        if self.empty(self.checkSpace((key[0] - 1, key[1] - 1))[0]):
            moves.append(self.move(key, (key[0] - 1, key[1] - 1), piece))
        if self.empty(self.checkSpace((key[0] - 1, key[1] + 1))[0]):
            moves.append(self.move(key, (key[0] - 1, key[1] + 1), piece))
        if self.empty(self.checkSpace((key[0] + 1, key[1] + 1))[0]):
            moves.append(self.move(key, (key[0] + 1, key[1] + 1), piece))
        if self.empty(self.checkSpace((key[0] + 1, key[1] - 1))[0]):
            moves.append(self.move(key, (key[0] + 1, key[1] - 1), piece))

        return moves
    
    def moveOneStepRook(self, key, piece):
        moves = []
        if self.notTeam(self.checkSpace((key[0], key[1] - 1))[0] ):
            moves.append(self.move(key, (key[0], key[1] - 1), piece))
        if self.notTeam(self.checkSpace((key[0] - 1, key[1]))[0]):
            moves.append(self.move(key, (key[0] - 1, key[1]), piece))
        if self.notTeam(self.checkSpace((key[0], key[1] + 1))[0]):
            moves.append(self.move(key, (key[0], key[1] + 1), piece))
        if self.notTeam(self.checkSpace((key[0] + 1, key[1]))[0]):
            moves.append(self.move(key, (key[0] + 1, key[1]), piece))

        return moves
    
    def moveOneStepBishop(self, key, piece):
        moves = []
        if self.notTeam(self.checkSpace((key[0] - 1, key[1] - 1))[0]):
            moves.append(self.move(key, (key[0] - 1, key[1] - 1), piece))
        if self.notTeam(self.checkSpace((key[0] - 1, key[1] + 1))[0]):
            moves.append(self.move(key, (key[0] - 1, key[1] + 1), piece))
        if self.notTeam(self.checkSpace((key[0] + 1, key[1] + 1))[0]):
            moves.append(self.move(key, (key[0] + 1, key[1] + 1), piece))
        if self.notTeam(self.checkSpace((key[0] + 1, key[1] - 1))[0]):
            moves.append(self.move(key, (key[0] + 1, key[1] - 1), piece))

        return moves
    
    
    
    



    def move(self, old, new, tempPiece):
    

        newBoard = self.board.copy()

        newBoard[old] = ' '
       
        newBoard[new] = self.colour + tempPiece
        tempCh = Chezz(self.colour, newBoard)

        tempCh.contagion()
        
        
        if self.colour == 'w':

            
            
            piece = self.promotion(tempPiece, new)
            tempCh.board[new] = "w" + piece
            chezz = Chezz('b', tempCh.board)

            

        
        if self.colour == 'b':

            piece = self.promotion(tempPiece, new)
            tempCh.board[new] = "b" + piece
            chezz = Chezz('w', tempCh.board)
            
        return Edge(self, str(old) + '-' + str(new), chezz)
    
    #dirX and dirY should be +or - 1 and therefore determine which diagonal to shoot on
    #StartKey is where the cannon is
    #Returns the Edge where the dest board is what would happen after that shot
    def shoot(self, startKey, dirX, dirY):
    

        newBoard = self.board.copy()
       

        for i in range(1,8):
            key = (startKey[0] + i * dirX, startKey[1] + i * dirY)
            value = self.checkSpace(key)[0] 
            if not(self.offBoard(value)):
                newBoard[key] = " "
            else:
                break

        
        
        
        if self.colour == 'w':
            tempCh = Chezz('w', newBoard)
            tempCh.contagion()
            chezz = Chezz('b', tempCh.board)

            

        if self.colour == 'b':
            tempCh = Chezz('b', newBoard)
            tempCh.contagion()
            chezz = Chezz('w', tempCh.board)
            
        return Edge(self, str(key) + '=' + str((dirX,dirY)), chezz)

    
    def fling(self, startKey, endKey, piece):
    

        newBoard = self.board.copy()
       
        
        newBoard[startKey] = " "
        endValue = self.checkSpace(endKey)[0] 
        if self.empty(endValue):
            newBoard[endKey] = self.colour + piece
        elif self.enemy(endValue):
            newBoard[endKey] = ' '
        else:
            print('Invalid fling called')
                    
    
        if self.colour == 'w':
            tempCh = Chezz('w', newBoard)
            tempCh.contagion()
            chezz = Chezz('b', tempCh.board)

            

        if self.colour == 'b':
            tempCh = Chezz('b', newBoard)
            tempCh.contagion()
            chezz = Chezz('w', tempCh.board)
            
        return Edge(self, str(startKey) + '-' + str(endKey), chezz)


    def checkDiagonal(self ,startKey, dirX, dirY):
        diagClear = True

        for i in range(1,8):
            key = (startKey[0] + i * dirX, startKey[1] + i * dirY)
            value = self.checkSpace(key)[0] 
            if self.offBoard(value):
                break
            elif not(self.empty(value)):
                diagClear = False
        
        return not(diagClear)
            
    def possibleFlings(self, startKey, flingerKey):
        moves = []
        toThrow = self.checkSpace(startKey)

        dirX = flingerKey[0] - startKey[0]
        dirY = flingerKey[1] - startKey[1]
        for i in range(1,8):
            endKey = (flingerKey[0] + i * dirX, flingerKey[1] + i * dirY)
            value = self.checkSpace(endKey)
            if self.offBoard(value[0]):
                break
            if self.notTeam(value[0]):
                if self.empty(value[0]):
                    moves.append(self.fling(startKey, endKey, toThrow[1]))
                else:
                    if value[1] != 'K':
                        moves.append(self.fling(startKey, endKey, toThrow[1]))


        return moves
                   

    def contagion(self):
        for key, value in self.getColouredPieces().items():
            
            if value[1] == 'Z':
                
                if self.enemy(self.checkSpace((key[0], key[1] - 1))[0]):
                    self.infect((key[0], key[1] - 1))
                if self.enemy(self.checkSpace((key[0] - 1, key[1]))[0]) :
                    self.infect((key[0] - 1, key[1]))
                if self.enemy(self.checkSpace((key[0], key[1] + 1))[0]):
                    self.infect((key[0], key[1] + 1))
                if self.enemy(self.checkSpace((key[0] - 1, key[1]))[0]) :
                    self.infect((key[0] - 1, key[1]))
                    
    def infect(self, key):
        value = self.board[key]
        if value[1] != 'Z' and value[1] != 'K':
            self.board[key] = self.colour + 'Z'
           
        
                

    def promotion(self, piece, new):
        if piece == 'P':
            if self.colour == 'w'and new[1] == 7:
                return 'Z'
            elif self.colour == 'b' and new[1] == 0:
                return 'Z'
            else:
                return 'P'
        else:
            return piece
        
       



    def checkSpace(self, key):


        if key[0] < 0 or key[0] > 7 or key[1] > 7 or key[1] < 0:
           return 'eY'
         

        value = self.board[key]

        if value == ' ':
            return ' '
        else:
            return value
    

    def edges( self ):
        allEdges = []
        for key, value in self.getColouredPieces().items():
            
            if value[1] == 'P':
                allEdges.extend(self.movePeon(key))
            elif value[1] == 'Z':
                allEdges.extend(self.moveZombie(key))
            elif value[1] == 'K':
                allEdges.extend(self.moveKing(key))
            elif value[1] == 'R':
                allEdges.extend(self.moveRook(key))
            elif value[1] == 'B':
                allEdges.extend(self.moveBishop(key))
            elif value[1] == 'Q':
                 allEdges.extend(self.moveQueen(key))
            elif value[1] == 'N':
                  allEdges.extend(self.moveKnight(key))
            elif value[1] == 'C':
                  allEdges.extend(self.moveCannon(key))
            elif value[1] == 'F':
                  allEdges.extend(self.moveFlinger(key))

       
        return allEdges



    def convertKeyToCoords(key):
        coords = ''
        if key[0] == 0:
            coords += 'a'
        elif key[0] == 1:
            coords += 'b'
        elif key[0] == 2:
            coords += 'c'
        elif key[0] == 3:
            coords += 'd'
        elif key[0] == 4:
            coords += 'e'
        elif key[0] == 5:
            coords += 'f'
        elif key[0] == 6:
            coords += 'g'
        elif key[0] == 7:
            coords += 'h'
            
        
        coords += str(key[1] + 1)
        return coords
         
    def enemy(self, char):
        if self.colour == 'w':
            if char == 'b': return True
            else: return False
        elif self.colour == 'b':
            if char == 'w': return True
            else: return False
    
    def notTeam(self,char):
        if char != self.colour and char != 'e':
            return True
        else:
            return False

    def team(self,char):
        if char == self.colour and char != 'e':
            return True
        else:
            return False
    
    def empty(self,char):
        if char == ' ':
            return True
        else:
            return False
        
    def offBoard(self,char):
        if char == 'e':
            return True
        else:
            return False





    def removeBoards():
        for i in range(1000):
            try:
                os.remove('board.' + Chezz.fileNumber(i))
            except FileNotFoundError:
                pass

    def trueSelfFilter(self, pair):
        key, value = pair

        if value[0] == Chezz.startingColour:
            return True
        else:
            return False
    
    def trueEnemyFilter(self, pair):
        key, value = pair
        
        if Chezz.startingColour == 'w':
            if value[0] == 'b': return True
            else: return False
        elif Chezz.startingColour == 'b':
            if value[0] == 'w': return True
            else: return False

    def getTrueSelfPieces(self):
        
        teamPieces = dict(filter(self.trueSelfFilter, self.board.items()))
        return teamPieces

    def getTrueEnemyPieces(self):
        
        teamPieces = dict(filter(self.trueEnemyFilter, self.board.items()))
        return teamPieces

    #Score for the players who's turn it is in that board
    def evaluate(self):
        piece_values = {
            'P': 100,   # Pawn
            'Z': 300,   # Zombie
            'N': 300,   # Knight
            'B': 330,   # Bishop slightly more than Knight
            'R': 500,   # Rook
            'C': 600,   # Cannon
            'F': 600,   # Flinger
            'Q': 900,   # Queen
            'K': 10000  # King
        }
        
        score = 0
        
        # Material evaluation
        for key, value in self.getTrueSelfPieces().items():
            score += piece_values.get(value[1], 0)
        
        for key, value in self.getTrueEnemyPieces().items():
            score -= piece_values.get(value[1], 0)
        

        # Position evaluation - piece square tables
        self_pieces = self.getTrueSelfPieces()
    
        # Add positional bonuses
        for pos, piece in self_pieces.items():
            piece_type = piece[1]
            row, col = pos
            
            # Center control bonus for pawns and knights
            if piece_type in ['P', 'N', 'Z']:
                center_distance = abs(3.5 - row) + abs(3.5 - col)
                score += max(0, 15 - 3 * center_distance)
            
            # Bonus for developed pieces
            if piece_type in ['N', 'B'] and row in [6, 7]:  # Assuming 0-7 board index
                score += 10
                
            # Penalty for undeveloped pieces
            if piece_type in ['N', 'B', 'F'] and row == 7:  # Starting row
                score -= 15

        return score

    def sortByScore( e):
        return e[1]

    def pickABestMove(self):
        newMoves = self.edges()
       
        moveScores = []
        # Three integers sho8ld be here
        for e in newMoves:
            dest = e.destination

            score = dest.evaluate()
            
            moveScores.append([dest, score])

        moveScores.sort(reverse=True ,key=Chezz.sortByScore)
        return moveScores
    

                
    def pickBestScore(self,depth):
        
        allMoveScores = []
        allMoveScores.extend(self.pickABestMove())
        for move in allMoveScores:
            move[1] = move[0].getScoreRecursive(depth-1)
            
        
        allMoveScores.sort(reverse=True ,key=Chezz.sortByScore)

        # for i in allMoveScores:
        #     print(i[1])
        print(allMoveScores[0][1])
        self.outputBoard(allMoveScores[0][0].board)

    def getScoreRecursive(self, depth):
        nextMoveScores = []

        nextMoveScores.extend(self.pickABestMove())

        if self.colour == Chezz.startingColour:
            nextMoveScores = nextMoveScores[:len(nextMoveScores)//2]
        else:
            nextMoveScores = nextMoveScores[len(nextMoveScores)//2:]

        bestScore = -100000
        for move in nextMoveScores:
            

            if depth > 1:
                
                score = move[0].getScoreRecursive(depth-1)
                # if score == None:
                #     print(move[0])
                    
                #print(str(bestScore) + " " + str(score) + " ")
                if bestScore < score:
                    bestScore = score
            else:
                
                if self.colour == Chezz.startingColour:
                    return nextMoveScores[0][1]
                else:
                    return nextMoveScores[len(nextMoveScores) - 1][1]
    
        return bestScore
    def find_best_move(self, depth):
        score, move = self.max_score(depth)
        # Return the actual move that led to this state
        self.outputBoard(move[0].board) 
    
    def max_score(self, depth, alpha=-10000000, beta=10000000):
        if depth == 0:
            nextMovesScores = self.pickABestMove()
            return nextMovesScores[0][1], nextMovesScores[0][0]
            
                
            
        bestScore = -10000000
        bestMove = None
        successors = self.pickABestMove()  # This returns list of [dest, score]
        successors = successors[len(successors)//2:]
        for moveScore in successors:
            nextState = moveScore[0]  # The destination board
            
            # Recursive call (note we're passing nextState correctly)
            score, _ = nextState.min_score(depth-1, alpha, beta)
            
            if score > bestScore:
                bestScore = score
                bestMove = moveScore  # Save the entire moveScore object
                
            # Beta cutoff
            if score >= beta:
                return bestScore, bestMove
                
            alpha = max(alpha, score)
            
        return bestScore, bestMove

    def min_score(self, depth, alpha, beta):
        if depth == 0:
            nextMovesScores = self.pickABestMove()
            return nextMovesScores[len(nextMovesScores) - 1][1],  nextMovesScores[len(nextMovesScores) - 1][0]
            
        worstScore = 10000000  # Initialize to a high value
        worstMove = None
        successors = self.pickABestMove()  # This returns list of [dest, score]
        successors = successors[:len(successors)//2]
        for moveScore in successors:  
            nextState = moveScore[0]  # The destination board
            
            # Recursive call
            score, _ = nextState.max_score(depth-1, alpha, beta)
            
            if score < worstScore:
                worstScore = score
                worstMove = moveScore  # Save the entire moveScore object
                
            # Alpha cutoff
            if score <= alpha:
                return worstScore, worstMove
                
            beta = min(beta, score)
            
        return worstScore, worstMove
            


                
                    

        




