import pygame, sys
pygame.init()
WIDTH,HEIGHT = 900,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("blue")
pygame.display.set_caption("Space Invasion")
bg = pygame.image.load("Space.png")
sw,sh = 55,40
yellow = pygame.image.load("PlayerRocket2.png")
yellowr = pygame.transform.scale(yellow,(sw,sh))
yellowrocket = pygame.transform.rotate(yellowr,90)
red = pygame.image.load("PlayerRocket1.png")
redr = pygame.transform.scale(red,(sw,sh))
redrocket = pygame.transform.rotate(redr,270)
BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
VEL = 5
FPS = 60
HEALTH_FONT = pygame.font.SysFont("comicsans",40)
WINNER_FONT = pygame.font.SysFont("comicsans",100)
pygame.display.update()

def yellowmove(keys_pressed,yellowrect):
    if keys_pressed[pygame.K_a] and yellowrect.x>0:
        yellowrect.x-=VEL
    if keys_pressed[pygame.K_w] and yellowrect.y>0:
        yellowrect.y-=VEL
    if keys_pressed[pygame.K_d] and yellowrect.x+yellowrect.width<BORDER.x:
        yellowrect.x+=VEL
    if keys_pressed[pygame.K_s] and yellowrect.y+yellowrect.height<HEIGHT:
        yellowrect.y+=VEL
def redmove(keys_pressed,redrect):
    if keys_pressed[pygame.K_LEFT] and redrect.x>BORDER.x+BORDER.width:
        redrect.x-=VEL
    if keys_pressed[pygame.K_UP] and redrect.y>0:
        redrect.y-=VEL
    if keys_pressed[pygame.K_RIGHT] and redrect.x+redrect.width<WIDTH:
        redrect.x+=VEL
    if keys_pressed[pygame.K_DOWN] and redrect.y+redrect.height<HEIGHT:
        redrect.y+=VEL
def drawplayers(yellowrect,redrect,redhealth,yellowhealth):
    screen.blit(bg,(0,0))
    screen.blit(yellowrocket,(yellowrect.x,yellowrect.y))
    screen.blit(redrocket,(redrect.x,redrect.y))
    pygame.draw.rect(screen,"black",BORDER)
    redtext = HEALTH_FONT.render("Health:" + str(redhealth),True,"red")
    screen.blit(redtext,(WIDTH-redtext.get_width(),10))
    yellowtext = HEALTH_FONT.render("Health:" + str(yellowhealth),True,"yellow")
    screen.blit(yellowtext,(0,10))
    pygame.display.update()

def main():
    yellowrect = pygame.Rect(100,250,sw,sh)
    redrect = pygame.Rect(800,250,sw,sh)
    clock = pygame.time.Clock()
    redhealth = 10
    yellowhealth = 10
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        drawplayers(yellowrect,redrect,redhealth,yellowhealth)
        keys_pressed = pygame.key.get_pressed()
        yellowmove(keys_pressed,yellowrect)
        redmove(keys_pressed,redrect)
if __name__ == "__main__":
    main()