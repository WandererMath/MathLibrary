import pygame
import pygame.draw as draw
from copy import deepcopy
from time import sleep

WIDTH = 1200
HEIGHT = 600
A=5
X_MAX=WIDTH//A
Y_MAX=HEIGHT//A
white=(255,255,255)
BACKGROUND = (0, 0, 0)
K=[]

def get_K_from_file(file):
    global K
    with open(file, "r") as f:
        text=f.read()
        table=[k.split('\t') for k in text.split('\n')]
    for i in range(X_MAX):
        for j in range(Y_MAX):
            try:
                if table[j][i]=='1':
                    K.append((i,j))
            except:
                pass
    #print(K)

def get_num_adj(x,y):
    global K
    count=0
    for i in [-1,1,0]:
        for j in [-1,1,0]:
            if (x+i,y+j) in K:
                if not (i==0 and j==0):
                    count+=1
    return count
    

def update(screen):
    global K
    new_K=[]

    render(screen, K)

    for i in range(X_MAX):
        for j in range(Y_MAX):
            if not (i, j) in K:
                if get_num_adj(i, j)==3:
                    new_K.append((i,j))
            else:
                if get_num_adj(i, j)==2 or get_num_adj(i, j)==3:
                    new_K.append((i,j))
    #K=deepcopy(new_K)
    K=new_K
    #print(K)
    



def render(screen,K):
    for (x, y) in K:
        r=pygame.Rect(x*A,y*A,A,A)
        draw.rect(screen, white, r)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(BACKGROUND)

    while True:
        
        pygame.display.flip()

        #clock.tick(2)
        #sleep(0.1)
        screen.fill(BACKGROUND)
        update(screen)
        for e in pygame.event.get():
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_q:
                    return 

if __name__ == "__main__":
    get_K_from_file("a2.csv")
    main()
    