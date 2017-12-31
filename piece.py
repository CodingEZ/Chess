def horizontal_movements(spot, opposedLocations, emptyLocations):
    emptySpaces = []
    attackSpaces = []
    row = spot // 8
    column = spot % 8

    while row != 0 and ((row - 1) * 8 + column in emptyLocations):
        emptySpaces.append((row - 1) * 8 + column)
        row -= 1
    if row != 0 and ((row - 1) * 8 + column in opposedLocations):
        attackSpaces.append((row - 1) * 8 + column)
    row = spot // 8

    while row != 7 and ((row + 1) * 8 + column in emptyLocations):
        emptySpaces.append((row + 1) * 8 + column)
        row += 1
    if row != 7 and ((row + 1) * 8 + column in opposedLocations):
        attackSpaces.append((row + 1) * 8 + column)
    row = spot // 8

    while column != 0 and (row * 8 + (column - 1) in emptyLocations):
        emptySpaces.append(row * 8 + (column - 1))
        column -= 1
    if column != 0 and (row * 8 + (column - 1) in opposedLocations):
        attackSpaces.append(row * 8 + (column - 1))
    column = spot % 8

    while column != 7 and (row * 8 + (column + 1) in emptyLocations):
        emptySpaces.append(row * 8 + (column + 1))
        column += 1
    if column != 7 and (row * 8 + (column + 1) in opposedLocations):
        attackSpaces.append(row * 8 + (column + 1))

    return emptySpaces, attackSpaces
    
def diagonal_movements(spot, opposedLocations, emptyLocations):
    emptySpaces = []
    attackSpaces = []
    row = spot // 8
    column = spot % 8

    while row != 0 and column != 0 and ((row - 1) * 8 + (column - 1) in emptyLocations):
        emptySpaces.append((row - 1) * 8 + (column - 1))
        row -= 1
        column -= 1
    if row != 0 and column != 0 and ((row - 1) * 8 + (column - 1) in opposedLocations):
        attackSpaces.append((row - 1) * 8 + (column - 1))
    row = spot // 8
    column = spot % 8

    while row != 7 and column != 0 and ((row + 1) * 8 + (column - 1) in emptyLocations):
        emptySpaces.append((row + 1) * 8 + (column - 1))
        row += 1
        column -= 1
    if row != 7 and column != 0 and ((row + 1) * 8 + (column - 1) in opposedLocations):
        attackSpaces.append((row + 1) * 8 + (column - 1))
    row = spot // 8
    column = spot % 8

    while row != 0 and column != 7 and ((row - 1) * 8 + (column + 1) in emptyLocations):
        emptySpaces.append((row - 1) * 8 + (column + 1))
        row -= 1
        column += 1
    if row != 0 and column != 7 and ((row - 1) * 8 + (column + 1) in opposedLocations):
        attackSpaces.append((row - 1) * 8 + (column + 1))
    row = spot // 8
    column = spot % 8

    while row != 7 and column != 7 and ((row + 1) * 8 + (column + 1) in emptyLocations):
        emptySpaces.append((row + 1) * 8 + (column + 1))
        row += 1
        column += 1
    if row != 7 and column != 7 and ((row + 1) * 8 + (column + 1) in opposedLocations):
        attackSpaces.append((row + 1) * 8 + (column + 1))

    return emptySpaces, attackSpaces

def knight_movements(spot, opposedLocations, emptyLocations):
    emptySpaces = []
    attackSpaces = []
    row = spot // 8
    column = spot % 8

    if (row >= 2) and (column != 0):
        if (row - 2) * 8 + (column - 1) in opposedLocations:
            attackSpaces.append((row - 2) * 8+(column - 1))
        elif (row - 2) * 8 + (column - 1) in emptyLocations:
            emptySpaces.append((row - 2) * 8 + (column - 1))

    if (row != 0) and (column >= 2):
        if (row - 1) * 8 + (column - 2) in opposedLocations:
            attackSpaces.append((row - 1) * 8 + (column - 2))
        elif (row - 1) * 8 + (column - 2) in emptyLocations:
            emptySpaces.append((row - 1) * 8 + (column - 2))

    if (row >= 2) and (column != 7):
        if (row - 2) * 8 + (column + 1) in opposedLocations:
            attackSpaces.append((row - 2) * 8 + (column + 1))
        elif (row - 2) * 8 + (column + 1) in emptyLocations:
            emptySpaces.append((row - 2) * 8 + (column + 1))

    if (row != 0) and (column <= 5):
        if (row - 1) * 8 + (column + 2) in opposedLocations:
            attackSpaces.append((row - 1) * 8 + (column + 2))
        elif (row - 1) * 8 + (column + 2) in emptyLocations:
            emptySpaces.append((row - 1) * 8 + (column + 2))

    if (row <= 5) and (column != 0):
        if (row + 2) * 8 + (column - 1) in opposedLocations:
            attackSpaces.append((row + 2) * 8 + (column - 1))
        elif (row + 2) * 8 + (column - 1) in emptyLocations:
            emptySpaces.append((row + 2) * 8 + (column - 1))

    if (row != 7) and (column >= 2):
        if (row + 1) * 8 + (column - 2) in opposedLocations:
            attackSpaces.append((row + 1) * 8 + (column - 2))
        elif (row+1)*8+(column-2) in emptyLocations:
            emptySpaces.append((row + 1) * 8 + (column - 2))

    if (row <= 5) and (column != 7):
        if (row + 2) * 8 + (column + 1) in opposedLocations:
            attackSpaces.append((row + 2) * 8 + (column + 1))
        elif (row + 2) * 8 + (column + 1) in emptyLocations:
            emptySpaces.append((row + 2) * 8 + (column + 1))

    if (row != 7) and (column <= 5):
        if (row + 1) * 8 + (column + 2) in opposedLocations:
            attackSpaces.append((row + 1) * 8 + (column + 2))
        elif (row + 1) * 8 + (column + 2) in emptyLocations:
            emptySpaces.append((row + 1) * 8 + (column + 2))

    return emptySpaces, attackSpaces

def king_movements(spot, opposedLocations, emptyLocations):
    emptySpaces = []
    attackSpaces = []
    row = spot // 8
    column = spot % 8

    if row != 0:
        if column != 0:
            if (row - 1) * 8 + (column - 1) in emptyLocations:
                emptySpaces.append((row - 1) * 8 + (column - 1))
            elif (row - 1) * 8 + (column - 1) in opposedLocations:
                attackSpaces.append((row - 1) * 8 + (column - 1))
        if column != 7:
            if (row - 1) * 8 + (column + 1) in emptyLocations:
                emptySpaces.append((row - 1) * 8 + (column + 1))
            elif (row - 1) * 8 + (column + 1) in opposedLocations:
                attackSpaces.append((row - 1) * 8 + (column + 1))
        if (row - 1) * 8 + column in emptyLocations:
            emptySpaces.append((row - 1) * 8 + column)
        elif (row - 1) * 8 + column in opposedLocations:
            attackSpaces.append((row - 1) * 8 + column)
    if row != 7:
        if column != 0:
            if (row + 1) * 8 + (column - 1) in emptyLocations:
                emptySpaces.append((row + 1) * 8 + (column - 1))
            elif (row + 1) * 8 + (column - 1) in opposedLocations:
                attackSpaces.append((row + 1) * 8 + (column - 1))
        if column != 7:
            if (row + 1) * 8 + (column + 1) in emptyLocations:
                emptySpaces.append((row + 1) * 8 + (column + 1))
            elif (row + 1) * 8 + (column + 1) in opposedLocations:
                attackSpaces.append((row + 1) * 8 + (column + 1))
        if (row + 1) * 8 + column in emptyLocations:
            emptySpaces.append((row + 1) * 8 + column)
        elif (row + 1) * 8 + column in opposedLocations:
            attackSpaces.append((row + 1) * 8 + column)
    if column != 0:
        if row * 8 + (column - 1) in emptyLocations:
            emptySpaces.append(row * 8 + (column - 1))
        elif row * 8 + (column - 1) in opposedLocations:
            attackSpaces.append(row * 8 + (column - 1))
    if column != 7:
        if row * 8 + (column + 1) in emptyLocations:
            emptySpaces.append(row * 8 + (column + 1))
        elif row * 8 + (column + 1) in opposedLocations:
            attackSpaces.append(row * 8 + (column + 1))

    return emptySpaces, attackSpaces

class Piece:
    def __init__(self, image, notKing=True, isRook=False, isPawn=False):
        self.image = image
        self.notKing = notKing
        self.isRook = isRook
        self.isPawn = isPawn

class FriendPawn(Piece):
    def __init__(self, image, canEnpassantLeft=False, canEnpassantRight=False):
        Piece.__init__(self, image)
        self.isPawn = True
        self.canEnpassantLeft = canEnpassantLeft
        self.canEnpassantRight = canEnpassantRight
        
    def movements(self, spot, opposedLocations, emptyLocations):
        emptySpaces = []
        attackSpaces = []
        row = spot // 8
        
        if spot - 8 in emptyLocations:
            emptySpaces.append(spot - 8)
        if row == 6 and (spot - 16 in emptyLocations):
            emptySpaces.append(spot - 16)

        if ((spot - 7) in opposedLocations) and (spot % 8 != 7):
            attackSpaces.append(spot - 7)
        elif self.canEnpassantRight:
            attackSpaces.append(spot - 7)

        if ((spot - 9) in opposedLocations) and (spot % 8 != 0):
            attackSpaces.append(spot - 9)
        elif self.canEnpassantLeft:
            attackSpaces.append(spot - 9)

        return emptySpaces, attackSpaces

class OpposedPawn(Piece):
    def __init__(self, image, canEnpassantLeft=False, canEnpassantRight=False):
        Piece.__init__(self, image)
        self.isPawn = True
        self.canEnpassantLeft = canEnpassantLeft
        self.canEnpassantRight = canEnpassantRight
        
    def movements(self, spot, opposedLocations, emptyLocations):
        emptySpaces = []
        attackSpaces = []
        row = spot // 8
        
        if spot + 8 in emptyLocations:
            emptySpaces.append(spot + 8)
        if row == 1 and (spot + 16 in emptyLocations):
            emptySpaces.append(spot + 16)

        if ((spot + 7) in opposedLocations) and (spot % 8 != 0):
            attackSpaces.append(spot + 7)
        elif self.canEnpassantRight:
            attackSpaces.append(spot + 7)
            
        if ((spot + 9) in opposedLocations) and (spot % 8 != 7):
            attackSpaces.append(spot + 9)
        elif self.canEnpassantLeft:
            attackSpaces.append(spot + 9)

        return emptySpaces, attackSpaces

class Rook(Piece):
    def __init__(self, image, isLeftRook, isRightRook):
        Piece.__init__(self, image)
        self.isRook = True
        self.isLeftRook = isLeftRook
        self.isRightRook = isRightRook
    
    def movements(self, spot, opposedLocations, emptyLocations):
        return horizontal_movements(spot, opposedLocations, emptyLocations)

class Knight(Piece):
    def movements(self, spot, opposedLocations, emptyLocations):
        return knight_movements(spot, opposedLocations, emptyLocations)

class Bishop(Piece):
    def movements(self, spot, opposedLocations, emptyLocations):
        return diagonal_movements(spot, opposedLocations, emptyLocations)

class Queen(Piece):
    def movements(self, spot, opposedLocations, emptyLocations):
        diagonals = diagonal_movements(spot, opposedLocations, emptyLocations)
        horizontals = horizontal_movements(spot, opposedLocations, emptyLocations)
        return diagonals[0]+horizontals[0], diagonals[1]+horizontals[1]

class King(Piece):
    def __init__(self, image):
        Piece.__init__(self, image)
        self.notKing = False
        self.canCastleLeft = True
        self.canCastleRight = True
    
    def movements(self, spot, opposedLocations, emptyLocations):
        return king_movements(spot, opposedLocations, emptyLocations)
