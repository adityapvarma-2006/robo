import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants for window size and grid settings
WINDOW_WIDTH = 800  # Increased window width
WINDOW_HEIGHT = 600  # Increased window height
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BORDER_WIDTH = 10

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Robot Movement Simulation with FPS and Speed Control")

# Set up clock for controlling frame rate
clock = pygame.time.Clock()

# Load the robot image
robot_image = pygame.image.load('robot.png')  # We initialize an image to the variable
robot_image = pygame.transform.scale(robot_image, (GRID_SIZE, GRID_SIZE))  # Scale image to grid size

# Start the robot at the center of the screen
robot_x = WINDOW_WIDTH // 2 - GRID_SIZE // 2
robot_y = WINDOW_HEIGHT // 2 - GRID_SIZE // 2

# Movement speed
robot_speed = 5
min_speed = 1  # Minimum speed
max_speed = 20  # Maximum speed
direction = None  # Initial direction is None

# FPS control
fps = 5           # Default FPS
min_fps = 5       # Minimum FPS
max_fps = 15      # Maximum FPS

# Popup message function
def show_popup(message, color):
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render(message, True, color)
    rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    screen.blit(text_surface, rect)
    pygame.display.flip()
    pygame.time.wait(1500)  # Display the message for 1.5 seconds

# Function to draw grid lines on the screen
def draw_grid():
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WINDOW_WIDTH, y))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Check for key presses for movement and speed control
    keys = pygame.key.get_pressed()

    # Direction control
    if keys[K_n]:
        direction = "N"
    elif keys[K_s]:
        direction = "S"
    elif keys[K_e]:
        direction = "E"
    elif keys[K_w]:
        direction = "W"

    # Speed control
    if keys[K_EQUALS] or keys[K_PLUS]:  # Press '+' or '=' to increase FPS
        if fps < max_fps:
            fps += 1
        elif fps == max_fps:
            show_popup("This is the maximum speed limit!", RED)  # Warning in red
    elif keys[K_MINUS]:  # Press '-' to decrease FPS
        if fps > min_fps:
            fps -= 1

    # Movement logic
    if direction == "N":
        if robot_y > BORDER_WIDTH:
            robot_y -= robot_speed
        else:
            show_popup("You can't go any further north!", RED)
            direction = None
    elif direction == "S":
        if robot_y < WINDOW_HEIGHT - GRID_SIZE - BORDER_WIDTH:
            robot_y += robot_speed
        else:
            show_popup("You can't go any further south!", RED)
            direction = None
    elif direction == "E":
        if robot_x < WINDOW_WIDTH - GRID_SIZE - BORDER_WIDTH:
            robot_x += robot_speed
        else:
            show_popup("You can't go any further east!", RED)
            direction = None
    elif direction == "W":
        if robot_x > BORDER_WIDTH:
            robot_x -= robot_speed
        else:
            show_popup("You can't go any further west!", RED)
            direction = None

    # Clear the screen and fill it with green
    screen.fill(GREEN)

    # Draw grid lines
    draw_grid()

    # Draw border lines indicating maximum movement area
    pygame.draw.rect(screen, BLACK, (BORDER_WIDTH, BORDER_WIDTH, WINDOW_WIDTH - 2 * BORDER_WIDTH, WINDOW_HEIGHT - 2 * BORDER_WIDTH), BORDER_WIDTH)

    # Draw the robot image at the current position
    screen.blit(robot_image, (robot_x, robot_y))

    # Display the current speed and FPS on the screen
    font = pygame.font.SysFont(None, 36)
    speed_text = font.render(f"Speed: {robot_speed}", True, WHITE)
    fps_text = font.render(f"FPS: {fps}", True, BLUE)  # Display FPS in blue
    screen.blit(speed_text, (10, 10))
    screen.blit(fps_text, (10, 50))

    # Update the display
    pygame.display.flip()

    # Set the frame rate to the current FPS
    clock.tick(fps)
