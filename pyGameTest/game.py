import pygame

#initializes the font portion of the modual... necesary for some reason
pygame.font.init()

#constants
width, height = 500,500
mogus_width, mogus_height = 300, 300
fps = 60

#loads amongus then transforms the image
mogus = pygame.image.load('755.webp')
mogus = pygame.transform.scale(mogus,(mogus_height,mogus_width))
mogus = pygame.transform.rotate(mogus,15)

#creates the main window
window = pygame.display.set_mode((width,height))
#sets title at the top of the window
pygame.display.set_caption("minions: rise of gru")

def draw_window(hitbox, rando_rect, text_surface):
    #fills the window with a pinkish color
    window.fill((255,125,125))

    window.blit(text_surface, (20,20))    
    
    pygame.draw.rect(window, (0,0,255), rando_rect)

    #used to draw a surface onto a screen
    window.blit(mogus,(hitbox.x,hitbox.y))
    #updates the window... makes changes visible to player
    pygame.display.update() 

def main():
    #creates a clock object that can be used to control the speed of our game loop
    clock = pygame.time.Clock()

    #initialize the font for writing text
    font = pygame.font.SysFont('helvetica', 24)
    #creates a surface from a string
    text_surface = font.render('hello',True,(0,0,0))


    hitbox = pygame.Rect(100,100,mogus_width,mogus_height)

    run = True
    #the main game loop... runs until "run" becomes false
    while run:
        #a dynamic delay that ensures 
        #the function does not run over 60 times per second
        clock.tick(fps)
        
        #detects if the window is closed and stops the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #moves mogus 1 pixel to the right every frame
        hitbox.x +=1

        #returns a dictionary with every key, and whether or not it is pressed    
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_m]:
            hitbox.x -= 2

        #just want to demonstrate drawing rectangles
        rando_rect = pygame.Rect(50,50,30,30)

        draw_window(hitbox, rando_rect, text_surface)

    pygame.quit()


if __name__ == "__main__":
   main() 
