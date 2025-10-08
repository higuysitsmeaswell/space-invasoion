import pygame, sys
pygame.init()
WIDTH,HEIGHT = 900,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("blue")
pygame.display.set_caption("Space Invasion")
bg = pygame.image.load("Space.png")
sw,sh = 55,40
YELLOWHIT = pygame.USEREVENT+1 #pygame has 32 number events in that 23 are user events and 9 events are free
REDHIT = pygame.USEREVENT+2
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
MAXBULLET = 3
BULLETVEL = 7
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
def drawplayers(yellowrect,redrect,redhealth,yellowhealth,yellowbullets,redbullets):
    screen.blit(bg,(0,0))
    screen.blit(yellowrocket,(yellowrect.x,yellowrect.y))
    screen.blit(redrocket,(redrect.x,redrect.y))
    pygame.draw.rect(screen,"black",BORDER)
    redtext = HEALTH_FONT.render("Health:" + str(redhealth),True,"red")
    screen.blit(redtext,(WIDTH-redtext.get_width(),10))
    yellowtext = HEALTH_FONT.render("Health:" + str(yellowhealth),True,"yellow")
    screen.blit(yellowtext,(0,10))
    for bullet in yellowbullets:
        pygame.draw.rect(screen,"yellow",bullet)
    for bullet in redbullets:
        pygame.draw.rect(screen,"red",bullet)
    pygame.display.update()

def movebullets(yellowbullets,redbullets,redrect,yellowrect):
    for bullet in yellowbullets:
        bullet.x+=BULLETVEL
        if redrect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(REDHIT))
            yellowbullets.remove(bullet)
        elif bullet.x>WIDTH:
            yellowbullets.remove(bullet)
    for bullet in redbullets:
        bullet.x-=BULLETVEL
        if yellowrect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOWHIT))
            redbullets.remove(bullet)
        elif bullet.x<0:
            redbullets.remove(bullet)
    
def drawwinner(txt):
    text = WINNER_FONT.render(txt,True,"Green")
    screen.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    yellowrect = pygame.Rect(100,250,sw,sh)
    redrect = pygame.Rect(800,250,sw,sh)
    clock = pygame.time.Clock()
    redhealth = 10
    yellowhealth = 10
    redbullets = []
    yellowbullets = []

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellowbullets)<MAXBULLET:
                    bullet = pygame.Rect(yellowrect.x+yellowrect.width,yellowrect.y+yellowrect.height/2,10,5)
                    yellowbullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(redbullets)<MAXBULLET:
                    bullet = pygame.Rect(redrect.x,redrect.y+redrect.height/2,10,5)
                    redbullets.append(bullet)
            if event.type == YELLOWHIT:
                yellowhealth-=1
            if event.type == REDHIT:
                redhealth-=1
        winnertext = ""
        if redhealth <= 0:
            winnertext = "Yellow wins"
        if yellowhealth <= 0:
            winnertext = "Red wins"
        if winnertext != "":
            drawwinner(winnertext)

            break
        keys_pressed = pygame.key.get_pressed()
        yellowmove(keys_pressed,yellowrect)
        redmove(keys_pressed,redrect)
        movebullets(yellowbullets,redbullets,redrect,yellowrect)
        drawplayers(yellowrect,redrect,redhealth,yellowhealth,yellowbullets,redbullets)
    main()
if __name__ == "__main__":
    main()