import pygame
import asyncio
import random
import string
import platform

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Initial setup
words = ['awesome', 'bicycle', 'cartoon', 'dancing', 'freedom']
word = random.choice(words)
display_word = ['_' for _ in word]
guessed_letters = []
parts_assembled = 0  # 0 to 6 parts
max_parts = 6
lives = 6
game_state = "playing"

async def main():
    global running, game_state
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and game_state == "playing":
                if event.unicode.lower() in string.ascii_lowercase and event.unicode.lower() not in guessed_letters:
                    letter = event.unicode.lower()
                    guessed_letters.append(letter)
                    if letter in word:
                        # Correct guess: add a part
                        parts_assembled = min(parts_assembled + 1, max_parts)
                        for i, char in enumerate(word):
                            if char == letter:
                                display_word[i] = letter
                        if '_' not in display_word:
                            game_state = "win"
                    else:
                        # Incorrect guess: lose a life
                        lives -= 1
                        if lives <= 0:
                            game_state = "lose"

        # Rendering
        screen.fill((255, 255, 255))  # White background
        if game_state == "playing":
            # Display word
            word_text = " ".join(display_word)
            text_surface = pygame.font.SysFont('arial', 36).render(word_text, True, (0, 0, 0))
            screen.blit(text_surface, (300, 200))
            # Display guessed letters
            guessed_text = "Guessed: " + ", ".join(guessed_letters)
            text_surface = pygame.font.SysFont('arial', 24).render(guessed_text, True, (0, 0, 0))
            screen.blit(text_surface, (50, 300))
            # Display lives
            lives_text = f"Lives: {lives}"
            text_surface = pygame.font.SysFont('arial', 24).render(lives_text, True, (0, 0, 0))
            screen.blit(text_surface, (50, 350))
            # Placeholder for parts (replace with image logic)
            parts_text = f"Parts: {parts_assembled}/{max_parts}"
            text_surface = pygame.font.SysFont('arial', 24).render(parts_text, True, (0, 0, 0))
            screen.blit(text_surface, (50, 400))
        elif game_state == "win":
            text_surface = pygame.font.SysFont('arial', 36).render("You won! Character complete!", True, (0, 255, 0))
            screen.blit(text_surface, (50, 50))
        elif game_state == "lose":
            text_surface = pygame.font.SysFont('arial', 36).render(f"You lost! Word was: {word}", True, (255, 0, 0))
            screen.blit(text_surface, (50, 50))

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(1.0 / 60)  # For Pyodide compatibility

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())

pygame.quit()
               
 
