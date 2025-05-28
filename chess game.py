import pygame

pygame.init()


Width, height = 760, 760
Rows, Cols = 8, 8
Square = Width // Rows


fenetre = pygame.display.set_mode((Width, height))
pygame.display.set_caption("chess game")


imagePionnoir = pygame.image.load("pawn-b.svg")
imagePionblanc = pygame.image.load("pawn-w.svg")
imageTournoir = pygame.image.load("rook-b.svg")
imageTourblanc = pygame.image.load("rook-w.svg")
imageFounoir = pygame.image.load("bishop-b.svg")
imageFoublanc = pygame.image.load("bishop-w.svg")
imageCavaliernoir = pygame.image.load("knight-b.svg")
imageCavalierblanc = pygame.image.load("knight-w.svg")
imageReinenoir = pygame.image.load("queen-b.svg")
imageReineblanc = pygame.image.load("queen-w.svg")
imageRoinoir = pygame.image.load("king-b.svg")
imageRoiblanc = pygame.image.load("king-w.svg")

pieces = {
    (0, 0): imageTournoir,
    (1, 0): imageCavaliernoir,
    (2, 0): imageFounoir,
    (3, 0): imageReinenoir,
    (4, 0): imageRoinoir,
    (5, 0): imageFounoir,
    (6, 0): imageCavaliernoir,
    (7, 0): imageTournoir,
    (0, 1): imagePionnoir,
    (1, 1): imagePionnoir,
    (2, 1): imagePionnoir,
    (3, 1): imagePionnoir,
    (4, 1): imagePionnoir,
    (5, 1): imagePionnoir,
    (6, 1): imagePionnoir,
    (7, 1): imagePionnoir,
    (0, 6): imagePionblanc,
    (1, 6): imagePionblanc,
    (2, 6): imagePionblanc,
    (3, 6): imagePionblanc,
    (4, 6): imagePionblanc,
    (5, 6): imagePionblanc,
    (6, 6): imagePionblanc,
    (7, 6): imagePionblanc,
    (0, 7): imageTourblanc,
    (1, 7): imageCavalierblanc,
    (2, 7): imageFoublanc,
    (3, 7): imageReineblanc,
    (4, 7): imageRoiblanc,
    (5, 7): imageFoublanc,
    (6, 7): imageCavalierblanc,
    (7, 7): imageTourblanc,
}
piece_selectionne=None
joueur_actuel = 'white' 

def dessiner():
    global imagePionnoir, imagePionblanc, imageTournoir, imageTourblanc
    global imageFounoir, imageFoublanc, imageCavaliernoir, imageCavalierblanc
    global imageReinenoir, imageReineblanc, imageRoinoir, imageRoiblanc
    global fenetre
    
    couleurs = [pygame.Color(240, 217, 181), pygame.Color(181, 136, 99)]
    fenetre.fill((255, 255, 255))
    for row in range(Rows):
        for col in range(Cols):
            pygame.draw.rect(fenetre, couleurs[(row + col) % 2], (col * Square, row * Square, Square, Square))
    for (x, y), piece in pieces.items():
        fenetre.blit(pygame.transform.scale(piece, (Square, Square)), (x * Square, y * Square))
    if piece_selectionne:
        pygame.draw.rect(fenetre, (0, 255, 0), (piece_selectionne[0] * Square, piece_selectionne[1] * Square, Square, Square), 5)
    pygame.display.flip()

        
        
   

def gererClavierEtSouris():
    if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or 2 or 3: 
                x, y = pygame.mouse.get_pos()
                col = x // Square
                row = y // Square
              
                
                
def mouvementpion(position_piece, new_position, joueur):
     x, y = position_piece
     new_x, new_y = new_position
     if joueur == 'white':
        if new_x == x and new_y == y - 1 and (new_x, new_y) not in pieces:
            return True
        if y == 6 and new_x == x and new_y == y - 2 and (new_x, new_y) not in pieces:
            return True
     elif joueur == 'black':
        if new_x == x and new_y == y + 1 and (new_x, new_y) not in pieces:
            return True
        if y == 1 and new_x == x and new_y == y + 2 and (new_x, new_y) not in pieces:
            return True
     return False
                 
def mouvement_cavalier(position_piece, new_position):
    x, y = position_piece
    new_x, new_y = new_position
    if abs(new_x - x) == 2 and abs(new_y - y) == 1 or abs(new_x - x) == 1 and abs(new_y - y) == 2:
        return True
    return False    
    







running = True
while running:
    dessiner()
  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or 2 or 3: 
                x, y = pygame.mouse.get_pos()
                col = x // Square
                row = y // Square

                if not piece_selectionne:
                    if (col, row) in pieces: 
                        piece_selectionne = (col, row)
                        print(f"Pièce sélectionnée à la position : {piece_selectionne}")
                    else:
                        print("Aucune pièce à cette position.")
                else:
                    if (col, row) not in pieces:  
                        if piece_selectionne in pieces: 
                            piece_image = pieces[piece_selectionne]
                            if piece_image == imagePionnoir or piece_image == imagePionblanc:
                                if mouvementpion(piece_selectionne, (col, row), joueur_actuel):
                                    pieces[(col, row)] = pieces[piece_selectionne]
                                    del pieces[piece_selectionne]
                                    joueur_actuel = 'black' if joueur_actuel == 'white' else 'white'
                            elif piece_image == imageCavaliernoir or piece_image == imageCavalierblanc:
                                if mouvement_cavalier(piece_selectionne, (col, row)):
                                    pieces[(col, row)] = pieces[piece_selectionne]
                                    del pieces[piece_selectionne]
                                    joueur_actuel = 'black' if joueur_actuel == 'white' else 'white'
                    piece_selectionne = None

pygame.quit()





