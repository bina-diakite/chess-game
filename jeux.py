import pygame

pygame.init()

# Définition des dimensions
Width, height = 760, 760
Rows, Cols = 8, 8
Square = Width // Rows

# Création de la fenêtre
fenetre = pygame.display.set_mode((Width, height))
pygame.display.set_caption("chess game")

# Chargement des images
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

# Définition des positions des pièces (par défaut)
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

# Variable pour gérer le déplacement
selected_piece = None  # La pièce sélectionnée   selected_piece
current_player= 'white'  # Le joueur actuel ('white' ou 'black') current_player

# Fonction pour dessiner le damier et les pièces
def dessiner():
    # Couleurs du damier
    couleurs = [pygame.Color(240, 217, 181), pygame.Color(181, 136, 99)]  # clair et foncé

    # Nettoyage de la fenêtre
    fenetre.fill((255, 255, 255))

    # Dessiner le damier
    for row in range(Rows):
        for col in range(Cols):
            pygame.draw.rect(fenetre, couleurs[(row + col) % 2], (col * Square, row * Square, Square, Square))

    # Dessiner les pièces
    for (x, y), piece in pieces.items():
        fenetre.blit(pygame.transform.scale(piece, (Square, Square)), (x * Square, y * Square))

    # Si une pièce est sélectionnée, l'afficher avec un contour
    if selected_piece:
        pygame.draw.rect(fenetre, (0, 255, 0), (selected_piece[0] * Square, selected_piece[1] * Square, Square, Square), 5)

    # Rafraîchissement de la fenêtre
    pygame.display.flip()

# Fonction pour vérifier les mouvements valides d'un pion 
def mouvement_pion(piece_position, new_position, player):
    x, y = piece_position
    new_x, new_y = new_position
    
    # Déplacement pour un pion (avance d'une case ou deux)
    if player == 'white':
        if new_x == x and new_y == y - 1 and (new_x, new_y) not in pieces:
            return True
        if y == 6 and new_x == x and new_y == y - 2 and (new_x, new_y) not in pieces:
            return True
    elif player == 'black':
        if new_x == x and new_y == y + 1 and (new_x, new_y) not in pieces:
            return True
        if y == 1 and new_x == x and new_y == y + 2 and (new_x, new_y) not in pieces:
            return True
    return False

# Fonction pour vérifier le mouvement d'un cavalier
def mouvement_cavalier(piece_position, new_position):
    x, y = piece_position
    new_x, new_y = new_position
    # Mouvement en L
    if abs(new_x - x) == 2 and abs(new_y - y) == 1 or abs(new_x - x) == 1 and abs(new_y - y) == 2:
        return True
    return False

# Fonction pour vérifier si une prise est possible
def prise(piece_position, new_position, player):
    # Capture diagonale
   if new_position in pieces:
        if player == 'white' and pieces[new_position] in imagePionnoir:  # Adversaire noir
            return True
        if player == 'black' and pieces[new_position] in imagePionblanc:  # Adversaire blanc
            return True
        return False

# Boucle principale
running = True
while running:
    dessiner()

    # Détection des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Détecter le clic gauche
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or 2 or 3:  # 1 = clic gauche
                x, y = pygame.mouse.get_pos()
                col = x // Square
                row = y // Square

                # Si aucune pièce n'est sélectionnée, sélectionner la pièce à cette position
                if not selected_piece:
                    if (col, row) in pieces:  # Si une pièce est présente
                        selected_piece = (col, row)
                        print(f"Pièce sélectionnée à la position : {selected_piece}")
                    else:
                        print("Aucune pièce à cette position.")
                else:
                    # Si une pièce est sélectionnée, déplacer la pièce à la nouvelle position
                    if (col, row) not in pieces:  # On déplace la pièce sur une case vide
                        # Vérification si le mouvement est valide
                        if selected_piece in pieces:  # Si la pièce est valide
                            piece_image = pieces[selected_piece]
                            if piece_image == imagePionnoir or piece_image == imagePionblanc:
                                if mouvement_pion(selected_piece, (col, row), current_player):
                                    pieces[(col, row)] = pieces[selected_piece]
                                    del pieces[selected_piece]
                                    current_player = 'black' if current_player == 'white' else 'white'
                            elif piece_image == imageCavaliernoir or piece_image == imageCavalierblanc:
                                if mouvement_cavalier(selected_piece, (col, row)):
                                    pieces[(col, row)] = pieces[selected_piece]
                                    del pieces[selected_piece]
                                    current_player = 'black' if current_player == 'white' else 'white'
                    # Réinitialiser la sélection
                    selected_piece = None

pygame.quit()
