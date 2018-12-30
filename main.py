import pygame

pygame.init()

WHITE=(255,255,255)

DISPLAY_WIDTH=800
DISPLAY_HEIGHT=700

BOARD_SIZE=500
PIECE_SIZE=59

boardX= ( DISPLAY_WIDTH - BOARD_SIZE ) / 2
boardY= ( DISPLAY_HEIGHT - BOARD_SIZE ) / 2
SQUARE_SIZE=BOARD_SIZE/8


screen=pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('Chess Board')
clock = pygame.time.Clock()


board = pygame.image.load("images/board.png")


def get_pos(x,y):
    y_pos = (8 - x) * SQUARE_SIZE + boardY + (SQUARE_SIZE - PIECE_SIZE) * 0.5
    x_pos = (y - 1) * SQUARE_SIZE + boardX + (SQUARE_SIZE - PIECE_SIZE) * 0.5
    return x_pos,y_pos

def coordinate_pointing():
    x,y=pygame.mouse.get_pos()
    if boardX+BOARD_SIZE>x>boardX and boardY+BOARD_SIZE>y>boardY :
        squarex=(x-boardX)//SQUARE_SIZE
        squarey=(y-boardY)//SQUARE_SIZE
        return (8-squarey,squarex+1)
    else:
        return 0

class piece(object):
    def __init__(self,color,coordinate,sprite):
        self.coordinate=coordinate
        self.color=color
        self.sprite=pygame.image.load(f"images/{sprite}")
        self.x,self.y=get_pos(self.coordinate[0],self.coordinate[1])
    def draw(self,window):
        window.blit(self.sprite,(self.x,self.y))
class knight(piece):
    pass
class bishop(piece):
    pass
class king(piece):
    pass
class queen(piece):
    pass
class pawn(piece):
    pass
class rook(piece):
    pass

#defining objects
wn1 = knight(1,(1,2),"wn.png")
wn2 = knight(1,(1,7),"wn.png")
wb1 = bishop(1,(1,3),"wb.png")
wb2 = bishop(1,(1,6),"wb.png")
wr1 = rook(1,(1,1),"wr.png")
wr2 = rook(1,(1,8),"wr.png")
wq = queen(1,(1,4),"wq.png")
wk = king(1,(1,5),"wk.png")
wp=[pawn(1,(2,i),"wp.png") for i in range(1,9)]

bn1 = knight(0,(8,2),"bn.png")
bn2 = knight(0,(8,7),"bn.png")
bb1 = bishop(0,(8,3),"bb.png")
bb2 = bishop(0,(8,6),"bb.png")
br1 = rook(0,(8,1),"br.png")
br2 = rook(0,(8,8),"br.png")
bq = queen(0,(8,4),"bq.png")
bk = king(0,(8,5),"bk.png")
bp=[pawn(0,(7,i),"bp.png") for i in range(1,9)]

pieces=[wr1,wn1,wb1,wq,wk,wb2,wn2,wr2]+wp+bp+[br1,bn1,bb1,bq,bk,bb2,bn2,br2]

board_dict={x.coordinate:x for x in pieces}

dragging=False
gameExit = False

recent_pointer=(0,0)
def gameloop():
    for piece in pieces:
        piece.draw(screen)


while not gameExit:
    clock.tick(100)

    screen.fill(WHITE)
    screen.blit(board,(boardX,boardY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            recent_pointer = coordinate_pointing()
            dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            latest_pointer=coordinate_pointing()
            if recent_pointer in board_dict:
                piece_ = board_dict[recent_pointer]
                if latest_pointer and (latest_pointer not in board_dict):
                    del board_dict[recent_pointer]
                    board_dict[latest_pointer]=piece_
                    piece_.x, piece_.y=get_pos(latest_pointer[0],latest_pointer[1])
                    piece_.coordinate=latest_pointer
                else:
                    piece_.x,piece_.y=get_pos(piece_.coordinate[0],piece_.coordinate[1])
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                try:
                    mousex, mousey = pygame.mouse.get_pos()
                    board_dict[recent_pointer].x=mousex-PIECE_SIZE//2
                    board_dict[recent_pointer].y=mousey-PIECE_SIZE//2
                except:
                    pass

    gameloop()
    pygame.display.update()


pygame.quit()
quit()