import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants for window size and grid settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BORDER_WIDTH = 10

# Set up clock for controlling frame rate
clock = pygame.time.Clock()

# FPS control
min_fps = 5
max_fps = 15


class Robot:
    def __init__(self):
       # """Initialize the robot's position, speed, and direction."""
        self.image = pygame.image.load('robot.png')
        self.image = pygame.transform.scale(self.image, (GRID_SIZE, GRID_SIZE))
        self.x = WINDOW_WIDTH // 2 - GRID_SIZE // 2
        self.y = WINDOW_HEIGHT // 2 - GRID_SIZE // 2
        self.speed = 5
        self.direction = None

    def move(self, keys):
       # """Update robot's position based on input direction."""
        if keys[K_n]:
            self.direction = "N"
        elif keys[K_s]:
            self.direction = "S"
        elif keys[K_e]:
            self.direction = "E"
        elif keys[K_w]:
            self.direction = "W"

        if self.direction == "N" and self.y > BORDER_WIDTH:
            self.y -= self.speed
        elif self.direction == "S" and self.y < WINDOW_HEIGHT - GRID_SIZE - BORDER_WIDTH:
            self.y += self.speed
        elif self.direction == "E" and self.x < WINDOW_WIDTH - GRID_SIZE - BORDER_WIDTH:
            self.x += self.speed
        elif self.direction == "W" and self.x > BORDER_WIDTH:
            self.x -= self.speed
        else:
            self.direction = None

    def draw(self, surface):
       # """Draw the robot image at its current position."""
        surface.blit(self.image, (self.x, self.y))


class Game:
    def __init__(self):
       # """Set up the window."""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Robot Movement Simulation with OOP")
        self.robot = Robot()
        self.fps = 5

    def show_popup(self, message, color):
       # """Display a temporary message on the screen."""
        font = pygame.font.SysFont(None, 48)
        text_surface = font.render(message, True, color)
        rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(text_surface, rect)
        pygame.display.flip()
        pygame.time.wait(1500)

    def draw_grid(self):
       # """Draw grid lines on the screen."""
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, BLACK, (0, y), (WINDOW_WIDTH, y))

    def run(self):
        #Main running loop where everything gets executed.
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            # Get key inputs for controlling the robot and FPS
            keys = pygame.key.get_pressed()

            # Control FPS
            if keys[K_EQUALS] or keys[K_PLUS]:
                if self.fps < max_fps:
                    self.fps += 1
                else:
                    self.show_popup("This is the maximum speed limit!", RED)
            elif keys[K_MINUS]:
                if self.fps > min_fps:
                    self.fps -= 1

            # Move the robot
            self.robot.move(keys)

            # Clear the screen and fill it with green
            self.screen.fill(GREEN)

            # Draw grid and border
            self.draw_grid()
            pygame.draw.rect(self.screen, BLACK, (
            BORDER_WIDTH, BORDER_WIDTH, WINDOW_WIDTH - 2 * BORDER_WIDTH, WINDOW_HEIGHT - 2 * BORDER_WIDTH),
                             BORDER_WIDTH)

            # Draw the robot
            self.robot.draw(self.screen)

            # Display FPS and speed
            font = pygame.font.SysFont(None, 36)
            fps_text = font.render(f"FPS: {self.fps}", True, BLUE)
            speed_text = font.render(f"Speed: {self.robot.speed}", True, WHITE)
            self.screen.blit(fps_text, (10, 50))
            self.screen.blit(speed_text, (10, 10))

            # Update the display
            pygame.display.flip()

            # Control the frame rate
            clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()
