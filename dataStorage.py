from tkinter import *
from PIL import Image
from PIL import ImageTk
import piece as p
import check


class dataStorage:

    def __init__(self, data):
        self.data = data
        self.data.dataCenter = 730
        self.data.squareLeft = 40
        self.data.squareTop = 60
        self.data.squareSize = 64
        self.data.promotionStartX = 600
        self.data.promotionStartY = 350

        self.data.backgroundFill = '#C5B5D4'
        self.data.instructionFill = '#F5E5D4'
        self.data.blackFill = '#428542'
        self.data.whiteFill = '#E4E4E4'
        self.data.moveToFill = '#51F9F9'
        self.data.attackFill = '#FF5151'
        self.data.castleFill = 'magenta'

        imgWidth = 40
        imgHeight = 40
        bp = Image.open('pics/black/bp.png').resize((imgWidth, imgHeight))
        br = Image.open('pics/black/br.png').resize((imgWidth, imgHeight))
        bn = Image.open('pics/black/bn.png').resize((imgWidth, imgHeight))
        bb = Image.open('pics/black/bb.png').resize((imgWidth, imgHeight))
        bk = Image.open('pics/black/bk.png').resize((imgWidth, imgHeight))
        bq = Image.open('pics/black/bq.png').resize((imgWidth, imgHeight))
        wp = Image.open("pics/white/wp.png").resize((imgWidth, imgHeight))
        wr = Image.open("pics/white/wr.png").resize((imgWidth, imgHeight))
        wn = Image.open("pics/white/wn.png").resize((imgWidth, imgHeight))
        wb = Image.open("pics/white/wb.png").resize((imgWidth, imgHeight))
        wk = Image.open("pics/white/wk.png").resize((int(imgWidth*1.25), int(imgHeight*1.25)))
        wq = Image.open("pics/white/wq.png").resize((imgWidth, imgHeight))

        self.data.friendPromotionPieces = [wr, wn, wb, wq]
        self.data.opposedPromotionPieces = [br, bn, bb, bq]

        self.data.emptyLocations = []
        for i in range(16, 48):
            self.data.emptyLocations.append(i)
        self.data.friendLocations = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
        self.data.opposedLocations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        self.data.friendPieces = [p.FriendPawn(wp), p.FriendPawn(wp), p.FriendPawn(wp), p.FriendPawn(wp),
                                  p.FriendPawn(wp), p.FriendPawn(wp), p.FriendPawn(wp), p.FriendPawn(wp),
                                  p.Rook(wr, True, False), p.Knight(wn), p.Bishop(wb), p.Queen(wq),
                                  p.King(wk), p.Bishop(wb), p.Knight(wn), p.Rook(wr, False, True)]
        self.data.opposedPieces = [p.Rook(br, False, True), p.Knight(bn), p.Bishop(bb), p.Queen(bq),
                                   p.King(bk), p.Bishop(bb), p.Knight(bn), p.Rook(br, True, False),
                                   p.OpposedPawn(bp), p.OpposedPawn(bp), p.OpposedPawn(bp), p.OpposedPawn(bp),
                                   p.OpposedPawn(bp), p.OpposedPawn(bp), p.OpposedPawn(bp), p.OpposedPawn(bp)]

        self.data.friendName = 'white'
        self.data.opposedName = 'black'

        self.data.canMovePiece = False
        self.data.firstClickLocation = -1
        self.data.moveToLocations = []
        self.data.attackLocations = []
        self.data.castleLocations = []
        self.data.inPromotion = False
        self.data.promotionIndex = -1

        self.data.message1 = 'Play Chess!'
        self.data.message2 = 'White player goes first.'
        self.data.message3 = 'What is it going to be? Hm...'

    def offBoardMessages(self):
        self.data.message1 = "Please click to pick up a piece."
        self.data.message2 = "Do not drag and drop."
        self.data.message3 = "Try again."

# 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# 1111111 all first click situations 11111111111111111111111111111111111111111111111111111111111111

    def firstClick(self, spot):
        self.pickupPiece(spot)
        index = self.data.friendLocations.index(spot)
        movements = self.data.friendPieces[index].movements(spot,
                                                            self.data.opposedLocations,
                                                            self.data.emptyLocations)

        self.data.moveToLocations = self.returnMoveToLocations(movements)
        self.data.attackLocations = self.returnAttackLocations(movements)
        self.data.castleLocations = self.returnCastleLocations(index)

    def pickupPiece(self, spot):
        self.data.message1 = "Clicked on piece."
        self.data.message2 = "1. Click on a spot it can go to, or"
        self.data.message3 = "2. Click the same spot to drop piece"
        self.data.canMovePiece = True
        self.data.firstClickLocation = spot

    def returnMoveToLocations(self, movements):
        moveToLocations = []  # checking if the locations the piece can move to are legal
        for movement in movements[0]:
            if check.canMoveHere(movement, self.data.firstClickLocation, self.data.friendPieces,
                                 self.data.friendLocations, self.data.opposedPieces,
                                 self.data.opposedLocations, self.data.emptyLocations):
                moveToLocations.append(movement)  # performs actual check
        return moveToLocations

    def returnAttackLocations(self, movements):
        attackLocations = []  # checking if the locations the piece can move to are legal
        for movement in movements[1]:
            if check.canMoveAndRemoveHere(movement, self.data.firstClickLocation, self.data.friendPieces,
                                          self.data.friendLocations, self.data.opposedPieces,
                                          self.data.opposedLocations, self.data.emptyLocations):
                attackLocations.append(movement)  # performs actual check
        return attackLocations

    def returnCastleLocations(self, index):
        # first check if king is in check, then use canCastleLeft and canCastleRight and noPiecesLeft and noPiecesRight
        # to add castling as a possible movement
        castleLocations = []
        if not check.ifTurnInCheck(self.data.friendPieces, self.data.friendLocations,
                                   self.data.opposedPieces, self.data.opposedLocations, self.data.emptyLocations):
            if not self.data.friendPieces[index].notKing:
                if self.data.friendPieces[index].canCastleLeft \
                        and check.noPiecesLeft(self.data.friendPieces, self.data.friendLocations, self.data.emptyLocations):
                    castleLocations.append(self.data.friendLocations[index] - 2)
                if self.data.friendPieces[index].canCastleRight \
                        and check.noPiecesRight(self.data.friendPieces, self.data.friendLocations, self.data.emptyLocations):
                    castleLocations.append(self.data.friendLocations[index] + 2)
        return castleLocations

# 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# 1111111 promotion situation 11111111111111111111111111111111111111111111111111111111111111

    def badPromotionClick(self):
        self.data.message1 = 'Clicked in wrong location.'
        self.data.message2 = 'Please click on a promotion piece.'
        self.data.message3 = 'Pieces located in instruction box.'

    def promote(self, clickX, clickY):
        rightRow = self.data.promotionStartY - clickY < 0.5 * self.data.squareSize \
                   and clickY - self.data.promotionStartY < 0.5 * self.data.squareSize
        rightColumns = clickX - self.data.promotionStartX > 0 \
                       and clickX - self.data.promotionStartX < 4 * self.data.squareSize
        if rightRow and rightColumns:
            rookColumn = clickX - self.data.promotionStartX > 0 \
                         and clickX - self.data.promotionStartX < self.data.squareSize
            knightColumn = clickX - self.data.promotionStartX > self.data.squareSize \
                           and clickX - self.data.promotionStartX < 2 * self.data.squareSize
            bishopColumn = clickX - self.data.promotionStartX > 2 * self.data.squareSize \
                           and clickX - self.data.promotionStartX < 3 * self.data.squareSize
            queenColumn = clickX - self.data.promotionStartX > 3 * self.data.squareSize \
                          and clickX - self.data.promotionStartX < 4 * self.data.squareSize
            if rookColumn:
                self.data.friendPieces[self.data.promotionIndex] = p.Rook(self.data.friendPromotionPieces[0], False,
                                                                          False)
                self.data.message1 = 'Piece promoted to rook!'
            elif knightColumn:
                self.data.friendPieces[self.data.promotionIndex] = p.Knight(self.data.friendPromotionPieces[1])
                self.data.message1 = 'Piece promoted to knight!'
            elif bishopColumn:
                self.data.friendPieces[self.data.promotionIndex] = p.Bishop(self.data.friendPromotionPieces[2])
                self.data.message1 = 'Piece promoted to bishop!'
            elif queenColumn:
                self.data.friendPieces[self.data.promotionIndex] = p.Queen(self.data.friendPromotionPieces[3])
                self.data.message1 = 'Piece promoted to queen!'

            # check for checks
            if check.ifNotTurnInCheck(self.data.friendPieces, self.data.friendLocations,
                                      self.data.opposedPieces, self.data.opposedLocations,
                                      self.data.emptyLocations):
                self.data.message1 += ' ' + self.data.opposedName + ' is in check.'
            self.data.message2 = 'It is now ' + self.data.opposedName + " player's turn."
            self.data.message3 = 'Click on any ' + self.data.opposedName + ' piece.'

            self.data.inPromotion = False
            self.data.promotionIndex = -1
            self.changeTurn()

        else:
            self.badPromotionClick()

# 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# 1111111 all second click situations 1111111111111111111111111111111111111111111111111111111111111

    def secondClick(self, spot):
        if spot == self.data.firstClickLocation:
            self.dropPiece()
        elif spot in self.data.moveToLocations:
            self.move(spot)
        elif spot in self.data.attackLocations:
            self.moveAndRemove(spot)
        elif spot in self.data.castleLocations:
            self.castle(spot)
        else:
            self.badSecondClick()
        self.clickReset()

    def dropPiece(self):
        self.data.message1 = "Dropped piece."
        self.data.message2 = "Click on a piece to move."
        self.data.message3 = "Waiting..."

    def move(self, spot):
        index = self.data.friendLocations.index(self.data.firstClickLocation)
        self.data.friendLocations[index] = spot
        index2 = self.data.emptyLocations.index(spot)
        self.data.emptyLocations[index2] = self.data.firstClickLocation
        self.data.emptyLocations = sorted(self.data.emptyLocations)

        # check castling
        self.castleCheck(index)

        # check canEnpassant
        if self.data.friendPieces[index].isPawn and self.data.firstClickLocation % 8 == 2 \
                and self.data.firstClickLocation // 8 - spot  // 8 == 2:
            if spot - 1 in self.data.opposedLocations:
                index = self.data.opposedLocations.index(spot - 1)
                if self.data.opposedPieces[index].isPawn:
                    self.data.opposedPieces[index].canEnpassantLeft = True
            if spot + 1 in self.data.opposedLocations:
                index2 = self.data.opposedLocations.index(spot + 1)
                if self.data.opposedPieces[index2].isPawn:
                    self.data.opposedPieces[index2].canEnpassantRight = True

        # check for checks
        if check.ifNotTurnInCheck(self.data.friendPieces, self.data.friendLocations,
                                  self.data.opposedPieces, self.data.opposedLocations, self.data.emptyLocations):
            self.data.message1 = 'Moved piece! ' + self.data.opposedName + ' is in check.'
            self.data.message2 = 'It is now ' + self.data.opposedName + " player's turn."
            self.data.message3 = 'Click on any ' + self.data.opposedName + ' piece.'
            self.changeTurn()
        else:
            self.data.message1 = 'Moved piece!'
            if self.data.friendPieces[index].isPawn and self.data.friendLocations[index] // 8 == 0:
                self.data.inPromotion = True
                self.data.promotionIndex = index
                self.data.message2 = 'The ' + self.data.friendName + ' player has moved a pawn to promotion.'
                self.data.message3 = 'Choose a piece to the right to promote into.'
            else:
                self.data.message2 = 'It is now ' + self.data.opposedName + " player's turn."
                self.data.message3 = 'Click on any ' + self.data.opposedName + ' piece.'
                self.changeTurn()

    def moveAndRemove(self, spot):
        index = self.data.friendLocations.index(self.data.firstClickLocation)
        self.data.friendLocations[index] = spot
        if self.data.friendPieces[index].isPawn and self.data.friendPieces[index].canEnpassantLeft:
            index2 = self.data.opposedLocations.index(spot + 8)
            self.data.emptyLocations.append(self.data.firstClickLocation - 1)
            self.data.emptyLocations.remove(spot)
        elif self.data.friendPieces[index].isPawn and self.data.friendPieces[index].canEnpassantRight:
            index2 = self.data.opposedLocations.index(spot + 8)
            self.data.emptyLocations.append(self.data.firstClickLocation + 1)
            self.data.emptyLocations.remove(spot)
        else:
            index2 = self.data.opposedLocations.index(spot)
        self.data.opposedLocations.pop(index2)
        self.data.opposedPieces.pop(index2)
        self.data.emptyLocations.append(self.data.firstClickLocation)
        self.data.emptyLocations = sorted(self.data.emptyLocations)

        # check castling
        self.castleCheck(index)
        
        # check for checks
        if check.ifNotTurnInCheck(self.data.friendPieces, self.data.friendLocations,
                                  self.data.opposedPieces, self.data.opposedLocations, self.data.emptyLocations):
            self.data.message1 = 'Moved and removed piece! ' + self.data.opposedName + ' is in check.'
            self.data.message2 = 'It is now ' + self.data.opposedName + " player's turn."
            self.data.message3 = 'Click on any ' + self.data.opposedName + ' piece.'
            self.changeTurn()
        else:
            self.data.message1 = 'Moved and removed piece!'
            if self.data.friendPieces[index].isPawn and self.data.friendLocations[index] // 8 == 0:
                self.data.inPromotion = True
                self.data.promotionIndex = index
                self.data.message2 = 'The ' + self.data.friendName + ' player has moved a pawn to promotion.'
                self.data.message3 = 'Choose a piece to the right to promote into.'
            else:
                self.data.message2 = 'It is now ' + self.data.opposedName + " player's turn."
                self.data.message3 = 'Click on any ' + self.data.opposedName + ' piece.'
                self.changeTurn()

    def castleCheck(self, index):
        if not self.data.friendPieces[index].notKing:
            self.data.friendPieces[index].canCastleLeft = False
            self.data.friendPieces[index].canCastleRight = False
        elif self.data.friendPieces[index].isRook:
            index3 = check.kingIndex(self.data.friendPieces)
            # left or right rook?
            if self.data.friendPieces[index].isLeftRook:
                self.data.friendPieces[index3].canCastleLeft = False
            else:
                self.data.friendPieces[index3].canCastleRight = False

    def castle(self, spot):
        index = self.data.friendLocations.index(self.data.firstClickLocation)
        self.data.friendLocations[index] = spot
        if spot > self.data.firstClickLocation:
            index2 = check.rightRookIndex(self.data.friendPieces)
            self.data.friendLocations[index2] = spot - 1
            self.data.emptyLocations.remove(spot - 1)
            if self.data.firstClickLocation % 8 == 3:
                self.data.emptyLocations.append(spot + 2)
            self.data.emptyLocations.append(spot + 1)
            self.data.emptyLocations.append(self.data.firstClickLocation)
        else:
            index2 = check.leftRookIndex(self.data.friendPieces)
            self.data.friendLocations[index2] = spot + 1
            self.data.emptyLocations.remove(spot + 1)
            if self.data.firstClickLocation % 8 == 4:
                self.data.emptyLocations.append(spot - 2)
            self.data.emptyLocations.append(spot - 1)
            self.data.emptyLocations.append(self.data.firstClickLocation)
        self.data.emptyLocations.remove(spot)
        self.data.emptyLocations = sorted(self.data.emptyLocations)

        self.data.friendPieces[index].canCastleLeft = False
        self.data.friendPieces[index].canCastleRight = False

        # check for checks
        if check.ifNotTurnInCheck(self.data.friendPieces, self.data.friendLocations,
                                  self.data.opposedPieces, self.data.opposedLocations, self.data.emptyLocations):
            self.data.message1 = 'Castled king! ' + self.data.opposedName + ' is in check.'
        else:
            self.data.message1 = 'Castled king!'
        self.data.message2 = 'It is now ' + self.data.opposedName + " player's turn."
        self.data.message3 = 'Click on any ' + self.data.opposedName + ' piece.'
        self.changeTurn()

    def badSecondClick(self):
        self.data.message1 = "Error, second click must be a square you can reach."
        self.data.message2 = "Click has reset."
        self.data.message3 = "Try again."

    def clickReset(self):
        self.data.firstClickLocation = -1       # if can switch, reset first click no matter what
        self.data.canMovePiece = False    # if can switch, reset boolean no matter what
        self.data.moveToLocations = []
        self.data.attackLocations = []
        self.data.castleLocations = []

    def changeTurn(self):
        # first convert the pawns
        for index1 in range(len(self.data.friendPieces)):
            piece = self.data.friendPieces[index1]
            if piece.isPawn:
                self.data.friendPieces[index1] = p.OpposedPawn(piece.image,
                                                               False,
                                                               False)       # resets enpassant
        for index2 in range(len(self.data.opposedPieces)):
            piece = self.data.opposedPieces[index2]
            if piece.isPawn:
                self.data.opposedPieces[index2] = p.FriendPawn(piece.image,
                                                               piece.canEnpassantLeft,
                                                               piece.canEnpassantRight)

        placehold1 = self.data.friendPieces
        self.data.friendPieces = self.data.opposedPieces
        self.data.opposedPieces = placehold1

        for index3 in range(len(self.data.friendLocations)):
            location = self.data.friendLocations[index3]
            self.data.friendLocations[index3] = 63 - location
        for index4 in range(len(self.data.opposedLocations)):
            location = self.data.opposedLocations[index4]
            self.data.opposedLocations[index4] = 63 - location
            
        placehold2 = self.data.friendLocations
        self.data.friendLocations = self.data.opposedLocations
        self.data.opposedLocations = placehold2
        placehold3 = self.data.friendPromotionPieces
        self.data.friendPromotionPieces = self.data.opposedPromotionPieces
        self.data.opposedPromotionPieces = placehold3
        placehold4 = self.data.friendName
        self.data.friendName = self.data.opposedName
        self.data.opposedName = placehold4
        for index5 in range(len(self.data.emptyLocations)):
            self.data.emptyLocations[index5] = 63 - self.data.emptyLocations[index5]

# 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# 111111111111111 End of Move Making 11111111111111111111111111111111111111111111111111111111111111

    def mousePressed(self, event):
        # EDIT: still need enpassant
        column = ((event.x - self.data.squareLeft) // self.data.squareSize)
        if column > 7 or column < 0:
            column = 64        # if outside of board, column is only used for the board
        row = ((event.y - self.data.squareTop) // self.data.squareSize)
        spot = row*8 + column          # spot in grid

        # case of promotion
        if self.data.inPromotion:
            self.promote(event.x, event.y)
        elif self.data.canMovePiece:
            self.secondClick(spot)
        elif spot in self.data.friendLocations:
            self.firstClick(spot)

    def keyPressed(self, event):
        pass

    def drawBoardSquare(self, canvas, row, column, fillColor):
        data = self.data
        canvas.create_rectangle(data.squareLeft + column*data.squareSize,
                                data.squareTop + row*data.squareSize,
                                data.squareLeft + column*data.squareSize + data.squareSize,
                                data.squareTop + row*data.squareSize + data.squareSize,
                                fill=fillColor)

    def redrawAll(self, canvas):
        data = self.data
        
        spotList = []           # used to make a list of spots for the board
        for i in range(64):
            spotList.append(i)

        # instruction background
        canvas.create_rectangle(0, 0, self.data.width, self.data.height, fill=data.backgroundFill)
        canvas.create_rectangle(data.dataCenter-150, 15, data.dataCenter+150, 440, fill=data.instructionFill)
            
        for spot in spotList:
            row = spot // 8
            column = spot % 8
            
            if row % 2 == column % 2:
                self.drawBoardSquare(canvas, row, column, data.whiteFill)
            else:
                self.drawBoardSquare(canvas, row, column, data.blackFill)

            if spot in data.moveToLocations:
                self.drawBoardSquare(canvas, row, column, data.moveToFill)
            elif spot in data.attackLocations:
                self.drawBoardSquare(canvas, row, column, data.attackFill)
            elif spot in data.castleLocations:
                self.drawBoardSquare(canvas, row, column, data.castleFill)
            
            if spot in data.friendLocations:
                # import picture of white piece
                index = data.friendLocations.index(spot)
                piece = data.friendPieces[index]
                pic = ImageTk.PhotoImage(piece.image)
                label = Label(image=pic)
                label.image = pic       # keep a reference!
                canvas.create_image(data.squareLeft+(column+.5)*data.squareSize,
                                    data.squareTop+(row+.5)*data.squareSize,
                                    image=pic)

            elif spot in data.opposedLocations:
                # import picture of black piece
                index = data.opposedLocations.index(spot)
                piece = data.opposedPieces[index]
                pic = ImageTk.PhotoImage(piece.image)  
                label = Label(image=pic)
                label.image = pic       # keep a reference!
                canvas.create_image(data.squareLeft+(column+.5)*data.squareSize,
                                    data.squareTop+(row+.5)*data.squareSize,
                                    image=pic)

            if data.inPromotion:
                for (friendPiece, iterator) in zip(data.friendPromotionPieces, [0, 1, 2, 3]):
                    pic = ImageTk.PhotoImage(friendPiece)
                    label = Label(image=pic)
                    label.image = pic       # keep a reference!
                    canvas.create_rectangle(data.promotionStartX + iterator*data.squareSize,
                                            data.promotionStartY - 0.5*data.squareSize,
                                            data.promotionStartX + (iterator+1)*data.squareSize,
                                            data.promotionStartY + 0.5*data.squareSize)
                    canvas.create_image(data.promotionStartX + (iterator+0.5)*data.squareSize,
                                        data.promotionStartY,
                                        image=pic)

        # draw the buttons
        canvas.create_rectangle(data.dataCenter - 25, 400, data.dataCenter + 25, 430, fill='brown')
        canvas.create_text(data.dataCenter, 415, text='Undo', font='Arial 10')

        # draw the text
        canvas.create_text(285, 30, text='Chess Board', font='Arial 20')
        canvas.create_text(data.dataCenter, 40, text='Instructions', font='Arial 15')
        canvas.create_text(data.dataCenter, 80, text='Click a piece of your color to pick it up.')
        canvas.create_text(data.dataCenter, 100, text='Click the undo button to undo the opponent\'s move.')
        canvas.create_text(data.dataCenter, 120, text='Pawns on the second rank can move 1 or 2 spaces.')
        canvas.create_text(data.dataCenter, 160, text='Messages', font='Arial 15')
        canvas.create_text(data.dataCenter, 200, text=data.message1, font='Arial 10')
        canvas.create_text(data.dataCenter, 220, text=data.message2, font='Arial 10')
        canvas.create_text(data.dataCenter, 240, text=data.message3, font='Arial 10')
