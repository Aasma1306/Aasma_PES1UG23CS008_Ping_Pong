import pygame
from game.game_engine import GameEngine

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ping Pong Game")
    clock = pygame.time.Clock()

    game = GameEngine(screen)
    game.start_menu()

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        game.move_ai()
        game.ball.move()
        game.draw()
        game.update_score()

        if game.check_game_over():
            game.replay_option()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
