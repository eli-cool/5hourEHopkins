import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Basic Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the clock for frame rate control
clock = pygame.time.Clock()

# Define the Mario class
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = screen_height - 100
        self.speed = 5
        self.gravity = 1
        self.velocity_y = 0
        self.on_ground = False

    def update(self, platforms):
        self.on_ground = False
        keys = pygame.key.get_pressed()

        # Move left and right
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Jumping
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -15  # Jump speed

        # Apply gravity
        self.rect.y += self.velocity_y
        self.velocity_y += self.gravity

        # Check for collisions with platforms
        self.check_platform_collisions(platforms)

    def check_platform_collisions(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y >= 0:
                if self.rect.bottom <= platform.rect.top + 10:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                    return  # Stop checking for further collisions after landing

# Set up the platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Create the player (Mario)
mario = Mario()
all_sprites.add(mario)

# Create some platforms
ground = Platform(0, screen_height - 50, screen_width, 50)
platform1 = Platform(100, screen_height - 150, 200, 20)
platform2 = Platform(400, screen_height - 250, 200, 20)
platform3 = Platform(200, screen_height - 350, 200, 20)

platforms.add(ground, platform1, platform2, platform3)
all_sprites.add(platforms)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update(platforms)

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
