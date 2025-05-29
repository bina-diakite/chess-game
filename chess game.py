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
piece_selectionne = None
joueur_actuel = 'white'

def pionblanc(piece):
    return piece in [imagePionblanc, imageTourblanc, imageFoublanc, imageCavalierblanc, imageReineblanc, imageRoiblanc]

def pionnoire(piece):
    return piece in [imagePionnoir, imageTournoir, imageFounoir, imageCavaliernoir, imageReinenoir, imageRoinoir]

def dessiner():
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
                
def mouvementtour(position_piece, new_position):
    x, y = position_piece
    new_x, new_y = new_position
    return x == new_x or y == new_y

def mouvementfou(position_piece, new_position):
    x, y = position_piece
    new_x, new_y = new_position
    return abs(new_x - x) == abs(new_y - y)

def mouvementcavalier(position_piece, new_position):
    x, y = position_piece
    new_x, new_y = new_position
    return (abs(new_x - x) == 2 and abs(new_y - y) == 1) or (abs(new_x - x) == 1 and abs(new_y - y) == 2)

def mouvementreine(position_piece, new_position):
    return mouvementtour(position_piece, new_position) or mouvementfou(position_piece, new_position)

def mouvementroi(position_piece, new_position):
    x, y = position_piece
    new_x, new_y = new_position
    return abs(new_x - x) <= 1 and abs(new_y - y) <= 1

def mouvementpion(position_piece, new_position, player):
    x, y = position_piece
    new_x, new_y = new_position
    direction = -1 if player == 'white' else 1
    ligne_depart = 6 if player == 'white' else 1

    if new_x == x and new_y == y + direction and (new_x, new_y) not in pieces:
        return True
    if y == ligne_depart and new_x == x and new_y == y + 2 * direction and (new_x, y + direction) not in pieces and (new_x, new_y) not in pieces:
        return True
    if abs(new_x - x) == 1 and new_y == y + direction and (new_x, new_y) in pieces:
        if player == 'white' and pionnoire(pieces[(new_x, new_y)]):
            return True
        if player == 'black' and pionblanc(pieces[(new_x, new_y)]):
            return True
    return False

def promotionpion(position, player):
    x, y = position
    if player == 'white' and y == 0:
        pieces[(x, y)] = imageReineblanc
    elif player == 'black' and y == 7:
        pieces[(x, y)] = imageReinenoir

running = True
while running:
    dessiner()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in [1, 2, 3]:
                x, y = pygame.mouse.get_pos()
                col = x // Square
                row = y // Square
                if not piece_selectionne:
                    if (col, row) in pieces:
                        piece = pieces[(col, row)]
                        if (joueur_actuel == 'white' and pionblanc(piece)) or (joueur_actuel == 'black' and pionnoire(piece)):
                            piece_selectionne = (col, row)
                            print(f"Pièce sélectionnée à la position : {piece_selectionne}")
                        else:
                            print("Ce n'est pas votre tour ou pièce adverse.")
                    else:
                        print("Aucune pièce à cette position.")
                else:
                    if piece_selectionne in pieces:
                        piece_image = pieces[piece_selectionne]
                        deplacement_valide = False

                        if piece_image in [imagePionnoir, imagePionblanc]:
                            deplacement_valide = mouvementpion(piece_selectionne, (col, row), joueur_actuel)
                        elif piece_image in [imageCavaliernoir, imageCavalierblanc]:
                            deplacement_valide = mouvementcavalier(piece_selectionne, (col, row))
                        elif piece_image in [imageTournoir, imageTourblanc]:
                            deplacement_valide = mouvementtour(piece_selectionne, (col, row))
                        elif piece_image in [imageFounoir, imageFoublanc]:
                            deplacement_valide = mouvementfou(piece_selectionne, (col, row))
                        elif piece_image in [imageReinenoir, imageReineblanc]:
                            deplacement_valide = mouvementreine(piece_selectionne, (col, row))
                        elif piece_image in [imageRoinoir, imageRoiblanc]:
                            deplacement_valide = mouvementroi(piece_selectionne, (col, row))

                        if deplacement_valide:
                            if (col, row) not in pieces or \
                               (joueur_actuel == 'white' and pionnoire(pieces.get((col, row)))) or \
                               (joueur_actuel == 'black' and pionblanc(pieces.get((col, row)))):
                                pieces[(col, row)] = pieces[piece_selectionne]
                                del pieces[piece_selectionne]
                                if piece_image in [imagePionnoir, imagePionblanc]:
                                    promotionpion((col, row), joueur_actuel)
                                joueur_actuel = 'black' if joueur_actuel == 'white' else 'white'
                            else:
                                print("Impossible de capturer votre propre pièce.")
                    piece_selectionne = None

pygame.quit()





