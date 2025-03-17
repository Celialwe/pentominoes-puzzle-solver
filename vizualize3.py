import pygame
import json
from pygame.locals import *
import sys

# Configuration
WINDOW_SIZE = (800, 400)
GRID_COLS = 5
GRID_ROWS = 6
CELL_SIZE = 40
MARGIN = 20
GRID_SPACING = 100

# Couleurs
COLORS = {
    't': (255, 0, 0),    # rouge
    'u': (0, 0, 255),    # bleu
    'v': (0, 255, 0),    # vert
    'x': (255, 165, 0),  # orange
    'y': (128, 0, 128),  # violet
    'z': (0, 255, 255),  # cyan
    'f': (255, 192, 203),# rose
    'i': (165, 42, 42),  # marron
    'l': (255, 0, 255),  # magenta
    'n': (0, 128, 128),  # turquoise
    'p': (255, 215, 0),  # or
    'w': (128, 128, 128) # gris
}
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PentominoVisualizer:
    def __init__(self, solutions):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Pentomino Visualizer")
        self.font = pygame.font.Font(None, 24)
        
        self.solutions = solutions  # Liste des solutions (chaînes `case(...)`)
        self.current_solution_index = 0  # Index de la solution actuellement affichée
        self.placements = {'l': {}, 'r': {}}  # Stockage des cases pour une solution

    def parse_solution(self, solution):
        """
        Parse les données de pentominos d'une solution donnée et met à jour les placements.
        """
        self.placements = {'l': {}, 'r': {}}  # Réinitialiser
        for cmd in solution:
            parts = cmd.replace("case(", "").replace(")", "").split(",")
            x = int(parts[0]) - 1  # Ligne (base 0)
            y = int(parts[1]) - 1  # Colonne (base 0)
            pentomino = parts[2]   # Type du pentomino (lettre)
            side = parts[3].strip()  # Grille ('l' ou 'r')
            self.placements[side][(x, y)] = pentomino

    def draw_grid(self, offset_x):
        """
        Dessiner les grilles (lignes et colonnes).
        """
        for col in range(GRID_COLS + 1):
            x = offset_x + col * CELL_SIZE
            pygame.draw.line(self.screen, BLACK, 
                             (x, MARGIN), 
                             (x, MARGIN + GRID_ROWS * CELL_SIZE), 2)
        
        for row in range(GRID_ROWS + 1):
            y = MARGIN + row * CELL_SIZE
            pygame.draw.line(self.screen, BLACK,
                             (offset_x, y),
                             (offset_x + GRID_COLS * CELL_SIZE, y), 2)

    def draw_pentominos(self, side, offset_x):
        """
        Dessine les pentominos sur la grille spécifiée ('l' ou 'r').
        """
        placements = self.placements.get(side, {})
        for (x, y), p in placements.items():
            # Couleur du pentomino
            color = COLORS.get(p, WHITE)
            
            # Dessiner la cellule principale
            rect = pygame.Rect(
                offset_x + y * CELL_SIZE + 2,
                MARGIN + x * CELL_SIZE + 2,
                CELL_SIZE - 4,
                CELL_SIZE - 4
            )
            pygame.draw.rect(self.screen, color, rect)

            # Dessiner l'étiquette (la lettre) au centre de la cellule
            text = self.font.render(p.upper(), True, BLACK)
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

    def run(self):
        """
        Lance l'application pour visualiser les solutions.
        """
        self.parse_solution(self.solutions[self.current_solution_index])  # Première solution
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:  # Passer à la solution suivante
                        self.current_solution_index = (self.current_solution_index + 1) % len(self.solutions)
                        self.parse_solution(self.solutions[self.current_solution_index])
                    elif event.key == K_LEFT:  # Revenir à la solution précédente
                        self.current_solution_index = (self.current_solution_index - 1) % len(self.solutions)
                        self.parse_solution(self.solutions[self.current_solution_index])

            self.screen.fill(WHITE)
            
            # Dessiner la grille gauche
            left_offset = MARGIN
            self.draw_grid(left_offset)
            self.draw_pentominos('l', left_offset)
            
            # Dessiner la grille droite
            right_offset = MARGIN * 2 + GRID_COLS * CELL_SIZE + GRID_SPACING
            self.draw_grid(right_offset)
            self.draw_pentominos('r', right_offset)
            
            # Afficher le numéro de la solution actuelle
            solution_text = self.font.render(f"Solution {self.current_solution_index + 1}/{len(self.solutions)}", True, BLACK)
            self.screen.blit(solution_text, (WINDOW_SIZE[0] // 2 - solution_text.get_width() // 2, 10))
            
            pygame.display.flip()

        pygame.quit()

def load_solutions_from_json(file_path):
    """
    Charge les solutions depuis un fichier JSON produit par Clingo.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    
    # Extraire toutes les solutions (cases)
    solutions = []
    for witness in data["Call"][0]["Witnesses"]:
        solutions.append(witness["Value"])
    
    return solutions

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        json_file = sys.argv[1]
    else :
        print("No json file specified")
        sys.exit()

    all_solutions = load_solutions_from_json(json_file)
    
    # Lancer le visualiseur
    visualizer = PentominoVisualizer(all_solutions)
    visualizer.run()
