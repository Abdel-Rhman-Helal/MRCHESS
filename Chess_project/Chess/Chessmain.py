"""
this is our main driver file which will resposible for handling user inputs and displaying the current GameState
"""
import pygame as p
import pygame.image

from Chess import ChessEngine
WIDTH = HEIGHT = 512  # dah el size
DIMENSION = 8  # dimension of the chess board (8x8)
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # 15 frame per second we will need in the the animation of movement
IMAGES = {}
p.display.set_caption("MR. Chess")
'''
Initialze a global dictionary of images , this will be called exactly one in the main lo load the images form file pack
'''



def loadImages():
    # fokk mn el try2a deh
    # IMAGES['wP']=  p.image.load("images/wP.png")
    # IMAGES['wN'] = p.image.load("images/wN.png")
    # IMAGES['wK'] = p.image.load("images/wK.png")
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("C:\\Chess_project\\Chess\\images\\" + piece + ".png"), (SQ_SIZE,SQ_SIZE))  # 2el lazmt el transform.scale 34an make sure el size of images ykon 2d el square belzabt fb3t leha el image k link w length=square size w width = square size
    # so now we can access and call images my IMAGES['wP']


'''
the main driver for our code .this will handle user input and updating graphics
'''


def main():
    DARK = (184, 139, 74)
    LIGHT = (227, 193, 111)
    undoafterrest = False
    counter_of_cancel_undo = 0;
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color(LIGHT))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMovie()
    moveMade = False ##boolean expersion for move
    loadImages()  # we will do this once before while loop
    running = True
    sqSelected = ()  # no square is selected,keep track of the last click of the user as a tuple(row,col)
    playerClicks = []  # keep track player clicks with one list contain two tuples    [(r1,c1),(r2,c2)]  exampe (two tuples [(6,4) ,(4,4)] )
    gameOver = False
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #the controll of mouse to move picess
            elif e.type == p.MOUSEBUTTONDOWN:  # here we put mouse event handles so when we click on piece then click where it will go
                if not gameOver:
                    location = p.mouse.get_pos()  # to get (x,y) location of mouse as tuple
                    col = location[0] // SQ_SIZE  # x divided by square size
                    row = location[1] // SQ_SIZE  # y divided by square size
                    if sqSelected == (row, col):  # which mean if user click on the same square twice
                        sqSelected = ()  # deactivate the selected
                        playerClicks = []  # deselect (clear) player click
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)  # append for both 1st and clicks
                    if len(playerClicks) == 2:  # after 2nd click
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(validMoves[i])
                                moveMade = True
                                sqSelected = ()  # for reset the user clicks
                                playerClicks = []
                            # if move in validMoves:
                            #     gs.makeMove(move)
                            #     moveMade = True
                            #     sqSelected = ()  # for reset the user clicks
                            #     playerClicks = []
                            # else:
                            #     playerClicks = [sqSelected]
                        if not moveMade:
                            playerClicks = [sqSelected]
            # key handling actions
            elif e.type == p.KEYDOWN:
                e.type == p.key.get_pressed()
                if e.key == p.K_z :   # if the pressed key is Z to undo the movment
                    gs.undoMove()
                    moveMade = True
                    undoafterrest == False
                    counter_of_cancel_undo = counter_of_cancel_undo + 1
                elif e.key == p.K_x and undoafterrest == False and counter_of_cancel_undo <=1 :
                    gs.cancelUndo(move)
                    moveMade = True
                    counter_of_cancel_undo = counter_of_cancel_undo - 1
                if  e.key == p.K_r: #reset the board if 'r' is preesd
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMovie()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = False
                    undoafterrest = True
                if e.key == p.K_1:
                    DARK != (184, 139, 74)
                    LIGHT != (227, 193, 111)
                    DARK = (128,128,128)
                    LIGHT = (225, 225, 225)
                if e.key == p.K_2:
                    DARK != (184, 139, 74)
                    LIGHT != (227, 193, 111)
                    DARK = (112,102,119)
                    LIGHT = (204, 183, 174)
                if e.key == p.K_3:
                    DARK != (184, 139, 74)
                    LIGHT != (227, 193, 111)
                    DARK = (111,115,210)
                    LIGHT = (157, 172, 255)
                if e.key == p.K_4:
                    DARK != (184, 139, 74)
                    LIGHT != (227, 193, 111)
                    DARK = (187,190,100)
                    LIGHT = (234, 240, 206)
                if e.key == p.K_5:
                    DARK != (184, 139, 74)
                    LIGHT != (227, 193, 111)
                    DARK = (111,143,114)
                    LIGHT = (173, 189, 143)
                if e.key == p.K_6:
                    DARK = (184, 139, 74)
                    LIGHT = (227, 193, 111)

        if moveMade:
            validMoves = gs.getValidMovie()
            moveMade = False
        clock.tick(MAX_FPS)
        p.display.flip()
        drawGameState(screen, gs,validMoves , sqSelected, DARK ,LIGHT )

        if gs.checkMate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen,'BLACK WIN BY checkMate')
            else:
                drawText(screen, 'WHITE WIN BY checkMate')
        elif gs.staleMate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen, 'StaleMate')





'''
highlite squer move 
'''
def highlightsquers(screen , gs , validMoves , sqSelected):
    if sqSelected !=():
        r,c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            # avilabel moives for chossen pice
            s = p.Surface((SQ_SIZE,SQ_SIZE))
            s.set_alpha(100)
            s.fill(p.Color('blue'))
            #highlite for chossen pice
            screen.blit(s,(c*SQ_SIZE,r*SQ_SIZE))
            s.fill(p.Color('green'))
            for move in validMoves :
                if move.startRow == r and move.startCol ==c:
                    screen.blit(s,(move.endCol*SQ_SIZE,move.endRow*SQ_SIZE))


'''
Responsible for all graphics within game
'''


def drawGameState(screen, gs ,validMoves , sqSelected, DARK ,LIGHT ):
    drawBoard(screen, DARK, LIGHT)  # draw square on the boards
    # we will add in piece highlighting and suggest movement latter
    highlightsquers(screen,gs,validMoves , sqSelected)
    drawPieces(screen, gs.board)  # draw pieces on the top of those squares


'''
the top left square is always light
so if we add row(i)+col(j) %2 ==0 even si it will color this as white square as the top left is white ,else (odd) grey square
sor example row(0),col(0) always light
row(0) col(1) -----0+1=1%2 !=0 odd so we will color it grey
row(1) col(1)------1+1=2%2==0 even so we will color it light...etc
'''


def drawBoard(screen , DARK ,LIGHT ):
    colors = [p.Color(LIGHT), p.Color(DARK)]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE,SQ_SIZE))  # hna its just drawing the rectangle pygame, draw rectangle on screen with the given color so we will draw it at rectangle object ,
            # we draw col by row because the col is the x value left and right while row is the y value up and down , the last two parameter square size for length and square size for width


'''
draw the pieces in the board using current Game state.board
'''


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":  # not empty space
                screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawText (screen , text):
    font = p.font.SysFont("Helvitca",32,True,False)
    textObject = font.render(text,0,p.Color('Black'))
    textLocation = p.Rect(100,256,WIDTH,HEIGHT)
    screen.blit(textObject,textLocation)


if __name__ == '__main__':
    main()