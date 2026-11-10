import pygame

pygame.init()
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    #Chek for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...)
            pygame.quit() # Close Window
            quit() # end pygame
