def kingIndex(pieces):
    index = 0  # find your king
    while pieces[index].notKing:
        index += 1
    return index

def leftRookIndex(pieces):
    index = 0  # find left rook
    while not pieces[index].isRook or not pieces[index].isLeftRook:
        index += 1
    return index

def rightRookIndex(pieces):
    index = 0  # find right rook
    while not pieces[index].isRook or not pieces[index].isRightRook:
        index += 1
    return index

def noPiecesLeft(friendPieces, friendLocations, emptyLocations):
    # for castling only
    index = kingIndex(friendPieces)     # find your king
    column = friendLocations[index] % 8
    if column == 0:
        return False
    for space in range(1, column):
        if friendLocations[index] - space not in emptyLocations:
            return False
    return True

def noPiecesRight(friendPieces, friendLocations, emptyLocations):
    # for castling only
    index = kingIndex(friendPieces)  # find your king
    column = friendLocations[index] % 8
    if column == 7:
        return False
    for space in range(1, 7 - column):
        if friendLocations[index] + space not in emptyLocations:
            return False
    return True

def ifTurnInCheck(friendPieces, friendLocations, opposedPieces, opposedLocations, emptyLocations):
    allAttackSpaces = []    # obtain all attacked squares
    print('Set')
    for (piece, location) in zip(opposedPieces, opposedLocations):
        allAttackSpaces += piece.movements(location, friendLocations, emptyLocations)[1]
    print(allAttackSpaces)
        
    index = kingIndex(friendPieces)   # find your king
    if friendLocations[index] in allAttackSpaces:
        print(friendLocations[index])
        return True
    return False

def ifNotTurnInCheck(friendPieces, friendLocations, opposedPieces, opposedLocations, emptyLocations):
    allAttackSpaces = []    # obtain all attacked squares
    for (piece, location) in zip(friendPieces, friendLocations):
        allAttackSpaces += piece.movements(location, opposedLocations, emptyLocations)[1]
        
    index = kingIndex(opposedPieces)   # find your king
    if opposedLocations[index] in allAttackSpaces:
        return True
    return False

def canMoveHere(movement, firstClickLocation, friendPieces, friendLocations, opposedPieces, opposedLocations, emptyLocations):
    # if a rook is moved, remove castling on that side
    # if a king is moved, remove castling on both sides
    index = friendLocations.index(firstClickLocation)
    friendLocations[index] = movement
    index2 = emptyLocations.index(movement)
    emptyLocations[index2] = firstClickLocation

    # checks if the move puts you in check
    if ifTurnInCheck(friendPieces, friendLocations, opposedPieces, opposedLocations, emptyLocations):
        friendLocations[index] = firstClickLocation
        emptyLocations[index2] = movement
        return False
    else:
        friendLocations[index] = firstClickLocation
        emptyLocations[index2] = movement
        return True

def canMoveAndRemoveHere(movement, firstClickLocation, friendPieces, friendLocations, opposedPieces, opposedLocations, emptyLocations):
    # if a rook is moved or a rook is taken, remove castling on that side
    # if a king is moved, remove castling on both sides
    index = friendLocations.index(firstClickLocation)
    friendLocations[index] = movement
    if friendPieces[index].isPawn and friendPieces[index].canEnpassantLeft:
        index2 = opposedLocations.index(movement + 8)
    elif friendPieces[index].isPawn and friendPieces[index].canEnpassantRight:
        index2 = opposedLocations.index(movement + 8)
    else:
        index2 = opposedLocations.index(movement)
    opposedLocations.pop(index2)
    emptyLocations.append(firstClickLocation)

    # checks if the move puts you in check
    if ifTurnInCheck(friendPieces, friendLocations, opposedPieces, opposedLocations, emptyLocations):
        if friendPieces[index].isPawn and (friendPieces[index].canEnpassantLeft or friendPieces[index].canEnpassantRight):
            opposedLocations.insert(index2, movement + 8)
        else:
            opposedLocations.insert(index2, movement)
        friendLocations[index] = firstClickLocation
        emptyLocations.remove(firstClickLocation)
        return False
    else:
        if friendPieces[index].isPawn and (friendPieces[index].canEnpassantLeft or friendPieces[index].canEnpassantRight):
            opposedLocations.insert(index2, movement + 8)
        else:
            opposedLocations.insert(index2, movement)
        friendLocations[index] = firstClickLocation
        emptyLocations.remove(firstClickLocation)
        return True
