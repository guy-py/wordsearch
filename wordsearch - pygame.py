import pygame
from pygame import mixer
from time import sleep
from random import randint, choice
mixer.init()
pygame.init()
print('''
loading...''')
screen = pygame.display.set_mode((525, 650))
level=[[['antjiojk', 'gembomla', 'awrberbn', 'ctojiojg', 'uomlomla', 'snakehrr', 'jiojiojo', 'lomlomlo'],[[0,1,2],[55, 47, 39, 31, 23, 15, 7, 63],[1, 9, 17, 25],[44, 43, 42, 41, 40]]],
       [['rainwwwr', 'uhbtssun', 'thunderf', 'puhsnowe', 'frdfefre', 'blizzard', 'gshasuhb', 'qwdxfghy'],[[40, 41, 42, 43, 44, 45, 46, 47],[16, 17, 18, 19, 20, 21, 22],[3, 2, 1, 0],[15, 14, 13],[27, 28, 29, 30]]],
       [['bfriesdc', 'uoppizza', 'rnnugget', 'gwafflef', 'erosrmlo', 'rrbeeyoj', 'cocacola', 'qwdxfghy'],[[1, 2, 3, 4, 5],[11, 12, 13, 14, 15],[18, 19, 20, 21, 22, 23],[0, 8, 16, 24, 32, 40],[48, 49, 55, 54, 53, 52, 51, 50],[25, 26, 27, 28, 29, 30]]],
       [['auioacer', 'pdlltggh', 'pdellogh', 'lsyegfbh', 'ejdismkf', 'windowsj', 'dsfdsefd', 'fdsefdsf'],[[0, 8, 16, 24, 32],[4, 5, 6, 7],[40, 41, 42, 43, 44, 45, 46],[17, 18, 19, 20]]],
       [['iscsmceu', 'dsddmidf', 'idmdfeff', 'dsfnefdj', 'headkarm', 'dfehaird', 'feethrtr', 'mouthfdf'],[[32, 33, 34, 35],[37, 38, 39],[43, 44, 45, 46],[48, 49, 50, 51],[60, 58, 57, 56, 59]]],
       [['cactusok', 'aedsfsef', 'rdfewadf', 'rdfesrff', 'odfrdgse', 'tdsfedes', 'gtyhyghu', 'jujmtree'],[[63, 62, 61, 60],[0, 1, 2, 3, 4, 5],[0, 8, 16, 24, 32, 40],[5, 13, 21, 29, 37]]]]
         
theme=['animals & incects', 'weather', 'fast food', 'computer brands', 'body parts', 'plants']
class r:
    i_l=0
    handel=[]
    doned=[]
    yellowed=[]
    mode=0
    spy=[]
    spx=[]
    spl=[]
    ui='start'
white = (255, 255, 255)
green = (255, 255, 0)
blue = (0, 0, 128)
def check_same(l1, l2):
    true=True
    for i in l1:
        if  not i in l2:
            true=False
    if not len(l1)==len(l2):
        true=False
    if l1==[]:
        true=False
    return true
def find(item, li):
    df=0
    for i in li:
        if i==item:
            break
        df+=1
    return df
def make_l(letter, x, y, col1, col2, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(letter, True, col1, col2)
    textR=text.get_rect()
    textR.center=(x,y)
    screen.blit(text, textR)
    return textR
def render_squares():
    if randint(0,12)==1:
        r.spy.append(710)
        r.spx.append(randint(0, 525))
        r.spl.append(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']))
    i_d=0
    for y in r.spy:
        if y< -60:
            del r.spy[i_d]
            del r.spx[i_d]
            del r.spl[i_d]
        else:
            r.spy[find(y,r.spy)]-=15
            x=r.spx[i_d]
            make_l(r.spl[i_d], x, y, (0, 255, 0), white, 32)
        i_d+=1
def render_ui():
    if r.ui=='start':
        make_l('press s to start', 262.5,325,(0, 255, 0),blue,64)
        make_l('WORDSEARCH', 262.5,40, (0, 255, 0), (255,255,255),70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            r.ui='game'
    elif r.ui=='game':
        render()
def render():
    step=64
    x= -(step/2)
    y= -(step/2)
    i= -1
    font = pygame.font.Font('freesansbold.ttf', step)
    try:
        for word in level[r.i_l][0]:
            x= -(step/2)
            y+=step
            for letter in word:
                i+=1
                x+=step
                if i in r.handel:
                    col=blue
                elif i in r.yellowed:
                    col=green
                else:
                    col=white
                textR=make_l(letter, x, y, (0, 255, 0), col, step)
                mpos = pygame.mouse.get_pos()
                if textR.collidepoint(mpos) and pygame.mouse.get_pressed()[0]:
                    if not i in r.handel:
                        r.handel.append(i)
                        print(r.handel)
        io=0
        for i in level[r.i_l][1]:
            if check_same(r.handel, i) and not io in r.doned:
                r.doned.append(io)
                for i in r.handel:
                    r.yellowed.append(i)
                r.handel=[]
            io+=1
        text = font.render(str(len(level[r.i_l][1])-len(r.doned))+' remaining', True, (0, 255, 0), white)
        textR=text.get_rect()
        textR.center=(262.5,615)
        screen.blit(text, textR)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(theme[r.i_l], True, (0, 255, 0), white)
        textR=text.get_rect()
        textR.center=(262.5,550)
        screen.blit(text, textR)
    except IndexError:
        text = font.render('0 remaining', True, (0, 255, 0), white)
        textR=text.get_rect()
        textR.center=(262.5,615)
        screen.blit(text, textR)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('game over', True, (0, 255, 0), white)
        textR=text.get_rect()
        textR.center=(262.5,550)
        screen.blit(text, textR)
def ccheck():
    fo=pygame.key.get_pressed()
    if fo[pygame.K_SPACE]:
        r.handel=[]
    try:
        if len(r.doned)==len(level[r.i_l][1]):
            r.i_l+=1
            r.handel=[]
            r.doned=[]
            r.yellowed=[]
    except IndexError:
        pass
while True:
    screen.fill(white)
    render_squares()
    render_ui()
    ccheck()
    pygame.event.get()
    pygame.display.update()
