import pygame
import math
import time
import pathlib
from pathlib import Path
from random import randint

directiry = pathlib.Path.cwd()
dir_path = str(directiry)

FPS = 60 

clock = pygame.time.Clock() 

fullscreen_bool = True

def settings_input():
    global fullscreen_bool
    f = open(dir_path+'/data/save/settings.bin','rb')
    while True:
        S = (f.readline()).decode('utf-8')
        if (S == "end"): break
        else:
            V,E,D = S.split()
            if (V == "fullscreen_bool"): fullscreen_bool = bool(int(D))

    f.close()

def settings_output():
    global fullscreen_bool
    f = open(dir_path+'/data/save/settings.bin','wb')
    f.write(("fullscreen_bool = "+str(int(fullscreen_bool))+"\n").encode('utf-8'))
    f.write(("end").encode('utf-8'))
    f.close()
    
settings_input()

Window = pygame.display.set_mode((640, 480), vsync=True)
pygame.display.set_caption("Arcade")

if (fullscreen_bool): pygame .display.toggle_fullscreen()

pygame.mouse.set_visible(False)



effect_1 = [0]*3
coinfalls = [0]*4
intro_screen_1 = pygame.image.load(dir_path+'/data/texture/intro_screen_1.png').convert()
intro_screen_2 = pygame.image.load(dir_path+'/data/texture/intro_screen_2.png').convert()
mainmenu_logo_1 = pygame.image.load(dir_path+'/data/texture/mainmenu_logo_1.png').convert()
mainmenu_logo_2 = pygame.image.load(dir_path+'/data/texture/mainmenu_logo_2.png').convert()
mainmenu_logo_3 = pygame.image.load(dir_path+'/data/texture/mainmenu_logo_3.png').convert()
effect_1[0] = pygame.image.load(dir_path+'/data/texture/effect_1_1.png').convert();effect_1[0].set_alpha(15)
effect_1[1] = pygame.image.load(dir_path+'/data/texture/effect_1_2.png').convert();effect_1[1].set_alpha(15)
effect_1[2] = pygame.image.load(dir_path+'/data/texture/effect_1_3.png').convert();effect_1[2].set_alpha(15)
effect_2_1 = pygame.image.load(dir_path+'/data/texture/effect_2_1.png').convert();effect_2_1.set_alpha(25)
effect_2_2 = pygame.image.load(dir_path+'/data/texture/effect_2_2.png').convert();effect_2_2.set_alpha(25)
effect_3_1 = pygame.image.load(dir_path+'/data/texture/effect_3_1.png').convert();
effect_3_2 = pygame.image.load(dir_path+'/data/texture/effect_3_2.png').convert();
play_button_1 = pygame.image.load(dir_path+'/data/texture/play_button_1.png').convert()
play_button_2 = pygame.image.load(dir_path+'/data/texture/play_button_2.png').convert()
settings_button_1 = pygame.image.load(dir_path+'/data/texture/settings_button_1.png').convert()
settings_button_2 = pygame.image.load(dir_path+'/data/texture/settings_button_2.png').convert()
quit_button_1 = pygame.image.load(dir_path+'/data/texture/quit_button_1.png').convert()
quit_button_2 = pygame.image.load(dir_path+'/data/texture/quit_button_2.png').convert()
version_text = pygame.image.load(dir_path+'/data/texture/version_text.png').convert()
back_button_1 = pygame.image.load(dir_path+'/data/texture/back_button_1.png').convert()
back_button_2 = pygame.image.load(dir_path+'/data/texture/back_button_2.png').convert()
coinfalls[0] = pygame.image.load(dir_path+'/data/texture/coinfalls_1.png').convert()
coinfalls[1] = pygame.image.load(dir_path+'/data/texture/coinfalls_2.png').convert()
coinfalls[2] = pygame.image.load(dir_path+'/data/texture/coinfalls_3.png').convert()
coinfalls[3] = pygame.image.load(dir_path+'/data/texture/coinfalls_4.png').convert()

settmenu_fullscreen_1 = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_1.png').convert()
settmenu_fullscreen_2 = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_2.png').convert()
settmenu_fullscreen_cheak_1 = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_cheak_1.png').convert(); settmenu_fullscreen_cheak_1.set_colorkey((0,0,0))
settmenu_fullscreen_cheak_2 = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_cheak_2.png').convert(); settmenu_fullscreen_cheak_2.set_colorkey((0,0,0))

comingsoon_banner = pygame.image.load(dir_path+'/data/texture/comingsoon_banner.png').convert()
morskaya_ohota_banner = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_banner.png').convert()
gonky_banner = pygame.image.load(dir_path+'/data/texture/gonky_banner.png').convert()
gonky_II_banner = pygame.image.load(dir_path+'/data/texture/gonky_II_banner.png').convert()
safary_banner = pygame.image.load(dir_path+'/data/texture/safary_banner.png').convert()
select_game = pygame.image.load(dir_path+'/data/texture/select_game.png').convert(); select_game.set_colorkey((0,0,0))

comingsoon_gamename_1 = pygame.image.load(dir_path+'/data/texture/comingsoon_gamename_1.png').convert()
comingsoon_gamename_2 = pygame.image.load(dir_path+'/data/texture/comingsoon_gamename_2.png').convert()
morskaya_ohota_gamename_1 = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_gamename_1.png').convert()
morskaya_ohota_gamename_2 = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_gamename_2.png').convert()
gonky_gamename_1 = pygame.image.load(dir_path+'/data/texture/gonky_gamename_1.png').convert()
gonky_gamename_2 = pygame.image.load(dir_path+'/data/texture/gonky_gamename_2.png').convert()
gonky_II_gamename_1 = pygame.image.load(dir_path+'/data/texture/gonky_II_gamename_1.png').convert()
gonky_II_gamename_2 = pygame.image.load(dir_path+'/data/texture/gonky_II_gamename_2.png').convert()
safary_gamename_1 = pygame.image.load(dir_path+'/data/texture/safary_gamename_1.png').convert()
safary_gamename_2 = pygame.image.load(dir_path+'/data/texture/safary_gamename_2.png').convert()

morskaya_ohota_map = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_map.png').convert()
morskaya_ohota_bordersmap = [0]*2
morskaya_ohota_bordersmap[0] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_bordersmap1.png').convert(); morskaya_ohota_bordersmap[0].set_colorkey((0,0,0))
morskaya_ohota_bordersmap[1] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_bordersmap2.png').convert(); morskaya_ohota_bordersmap[1].set_colorkey((0,0,0))
morskaya_ohota_periskop = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_periskop.png').convert(); morskaya_ohota_periskop.set_colorkey((255,0,0))
morskaya_ohota_oblako_1 = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_oblako_1.png').convert(); morskaya_ohota_oblako_1.set_colorkey((0,0,0))
morskaya_ohota_torpedo_used = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_torpedo_used.png').convert(); morskaya_ohota_torpedo_used.set_colorkey((0,0,0))
morskaya_ohota_torpedo_unused = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_torpedo_unused.png').convert(); morskaya_ohota_torpedo_unused.set_colorkey((0,0,0))

morskaya_ohota_ship = []
for i in range(4):
    morskaya_ohota_ship.append([0]*2)
morskaya_ohota_ship[0][0] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_1.png').convert(); morskaya_ohota_ship[0][0].set_colorkey((0,0,0))
morskaya_ohota_ship[1][0] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_2.png').convert(); morskaya_ohota_ship[1][0].set_colorkey((0,0,0))
morskaya_ohota_ship[2][0] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_3.png').convert(); morskaya_ohota_ship[2][0].set_colorkey((0,0,0))
morskaya_ohota_ship[3][0] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_4.png').convert(); morskaya_ohota_ship[3][0].set_colorkey((0,0,0))
morskaya_ohota_ship[0][1] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_F1.png').convert(); morskaya_ohota_ship[0][1].set_colorkey((0,0,0))
morskaya_ohota_ship[1][1] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_F2.png').convert(); morskaya_ohota_ship[1][1].set_colorkey((0,0,0))
morskaya_ohota_ship[2][1] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_F3.png').convert(); morskaya_ohota_ship[2][1].set_colorkey((0,0,0))
morskaya_ohota_ship[3][1] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_F4.png').convert(); morskaya_ohota_ship[3][1].set_colorkey((0,0,0))

morskaya_ohota_ship_shadow = []
for i in range(4):
    morskaya_ohota_ship_shadow.append([0]*2)
morskaya_ohota_ship_shadow[0][0] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_shadow_1.png').convert(); morskaya_ohota_ship_shadow[0][0].set_colorkey((255,0,0))
morskaya_ohota_ship_shadow[1][0] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_shadow_2.png').convert(); morskaya_ohota_ship_shadow[1][0].set_colorkey((255,0,0))
morskaya_ohota_ship_shadow[2][0] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_shadow_3.png').convert(); morskaya_ohota_ship_shadow[2][0].set_colorkey((255,0,0))
morskaya_ohota_ship_shadow[3][0] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_shadow_4.png').convert(); morskaya_ohota_ship_shadow[3][0].set_colorkey((255,0,0))
morskaya_ohota_ship_shadow[0][1] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_shadow_F1.png').convert(); morskaya_ohota_ship_shadow[0][1].set_colorkey((255,0,0))
morskaya_ohota_ship_shadow[1][1] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_shadow_F2.png').convert(); morskaya_ohota_ship_shadow[1][1].set_colorkey((255,0,0))
morskaya_ohota_ship_shadow[2][1] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_shadow_F3.png').convert(); morskaya_ohota_ship_shadow[2][1].set_colorkey((255,0,0))
morskaya_ohota_ship_shadow[3][1] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_ship_shadow_F4.png').convert(); morskaya_ohota_ship_shadow[3][1].set_colorkey((255,0,0))

morskaya_ohota_hit = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_hit.png').convert(); morskaya_ohota_hit.set_colorkey((0,0,0))
blackscreen = pygame.image.load(dir_path+'/data/texture/blackscreen.png').convert(); blackscreen.set_alpha(255)

morskaya_ohota_dd = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_dd.png').convert(); morskaya_ohota_dd.set_colorkey((0,0,0))

morskaya_ohota_torpedo_way = [0]*60
for i in range(60):
    morskaya_ohota_torpedo_way[i] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_torpedo_way_'+str(i+1)+'.png').convert()
    morskaya_ohota_torpedo_way[i].set_colorkey((255,0,0))



text=[]
for i in range(46):
    text.append([0]*2)

for i in range(46):
    text[i][0] = pygame.image.load(dir_path+'/data/texture/text/grey/LT'+str(i+1)+'.png').convert(); (text[i][0]).set_colorkey((0,0,0))
    text[i][1] = pygame.image.load(dir_path+'/data/texture/text/white/LT'+str(i+1)+'.png').convert(); (text[i][1]).set_colorkey((0,0,0))
    
loadtick = 0
mainmenu_tick = 0
mainmenu_subtick = 0
effect_2_tick = 0
effect_2_int = 3
mainmenu_select = 1
mainmenu_bool = False
gamemenu_bool = False
gamemenu_select = 0
gamemenu_razdel = 0
settmenu_bool = False
settmenu_select = 0
effect_4_tick = 0
effect_4_pos = 0
game_select = "none"
game_select_button = 0
morskaya_ohota_game_bool = False
coinfalls_tick = 0
morskaya_ohota_var_pos = 0
morskaya_ohota_R_bool = False
morskaya_ohota_L_bool = False
morskaya_ohota_borders_tick = 0
morskaya_ohota_borders_subtick = 0
morskaya_ohota_torpedos_left = 0
morskaya_ohota_hit_bool = False
morskaya_ohota_hit_tick = 0
morskaya_ohota_hit_ship = 0
morskaya_ohota_hit_pos = 0
morskaya_ohota_time = 0
morskaya_ohota_subtime = 0

class MO_TW():
    def __init__(self):
        self.pos_x = -999
        self.tick = -1
        self.subtick = 0
        self.active = False

    def spawn(self,x):
        self.active = True
        self.pos_x = x

    
    def update(self):
        if (self.active):
            self.subtick += 1
            if (self.subtick >= 2):
                self.subtick = 0
                self.tick += 1
            if (self.tick >= 60): self.active = False;
            else: Window.blit(morskaya_ohota_torpedo_way[self.tick],(round(self.pos_x)+int(round(self.pos_x)%2==1)+309-morskaya_ohota_var_pos,240))

class MO_ship():

    def __init__(self):
        self.pos_x = -999
        self.speed = 0
        self.size = 0
        self.dir = False
        self.active = True

    def draw(self):
        Window.blit(morskaya_ohota_ship[self.size][not(self.dir)],(round(self.pos_x)+int(round(self.pos_x)%2==1)-morskaya_ohota_var_pos,216))

    def spawn(self):
        if (self.pos_x == -999):
            self.pos_x = randint(-200+morskaya_ohota_var_pos,1480+morskaya_ohota_var_pos)
            if (randint(0,1)): self.speed = randint(5,10)/10
            else: self.speed = -randint(6,12)/10
        else:
            if (randint(0,1)):
                self.pos_x = -200+morskaya_ohota_var_pos
                self.speed = randint(5,10)/10
            else:
                self.pos_x = 1480+morskaya_ohota_var_pos
                self.speed = -randint(5,10)/10
            
    def update(self):
        self.pos_x += self.speed
        self.dir = self.speed > 0
        if (self.pos_x < -200+morskaya_ohota_var_pos or self.pos_x > 1480+morskaya_ohota_var_pos): self.spawn()

    def hit(self,tx):
        return (tx >= self.pos_x+4+self.size*8 and tx <= self.pos_x+72-4-self.size*8)
        
        
class MO_oblako():

    def __init__(self):
        self.pos_x = -999
        self.pos_y = -999
        self.speed = 0
        
    def draw(self):
        Window.blit(morskaya_ohota_oblako_1,(round(self.pos_x)+int(round(self.pos_x)%2==1)-morskaya_ohota_var_pos,self.pos_y))

    def spawn(self):
        if (self.pos_y == -999):
            self.pos_y = randint(36,48)*2
            self.pos_x = randint(-200+morskaya_ohota_var_pos,1480+morskaya_ohota_var_pos)
            self.speed = randint(2,12)/10
        else:
            self.pos_y = randint(36,48)*2
            if (randint(0,1)):
                self.pos_x = -200+morskaya_ohota_var_pos
                self.speed = randint(2,12)/10
            else:
                self.pos_x = 1480+morskaya_ohota_var_pos
                self.speed = -randint(2,12)/10
            
    def update(self):
        self.pos_x += self.speed + randint(-1,1)/10;
        if (self.pos_x < -200+morskaya_ohota_var_pos or self.pos_x > 1480+morskaya_ohota_var_pos): self.spawn()

MO_oblakos = []
for i in range(16): MO_oblakos.append(MO_oblako())
MO_ships = []
for i in range(10): MO_ships.append(MO_ship())
MO_ships[0].size = 0
MO_ships[1].size = 1
MO_ships[2].size = 1
MO_ships[3].size = 2
MO_ships[4].size = 2
MO_ships[5].size = 2
MO_ships[6].size = 3
MO_ships[7].size = 3
MO_ships[8].size = 3
MO_ships[9].size = 3
MO_TWs = []
for i in range(10): MO_TWs.append(MO_TW())

def take_screen(topleft, bottomright):
    size = bottomright[0] - topleft[0], bottomright[1] - topleft[1]
    img = pygame.Surface(size)
    img.blit(Window, (0, 0), (topleft, size))
    return img

def text_print(S,l,x,y):
    S = S.lower()
    for C in S:
        if (C == "ц" or C == "щ" or C == "ъ"):
            if (C == "ц"): Window.blit(text[23][l],(x,y))
            if (C == "щ"): Window.blit(text[26][l],(x,y))
            if (C == "ъ"): Window.blit(text[27][l],(x,y))
            x += 14
        elif (C == "." or C == ","):
            if (C == ","): Window.blit(text[44][l],(x,y))
            if (C == "."): Window.blit(text[45][l],(x,y))
            x += 6
        else:
            if   (C == "а"): Window.blit(text[0][l],(x,y))
            elif (C == "б"): Window.blit(text[1][l],(x,y))
            elif (C == "в"): Window.blit(text[2][l],(x,y))            
            elif (C == "г"): Window.blit(text[3][l],(x,y))
            elif (C == "д"): Window.blit(text[4][l],(x,y))
            elif (C == "е"): Window.blit(text[5][l],(x,y))                   
            elif (C == "ё"): Window.blit(text[6][l],(x,y))
            elif (C == "ж"): Window.blit(text[7][l],(x,y))
            elif (C == "з"): Window.blit(text[8][l],(x,y))            
            elif (C == "и"): Window.blit(text[9][l],(x,y))
            elif (C == "й"): Window.blit(text[10][l],(x,y))
            elif (C == "к"): Window.blit(text[11][l],(x,y))             
            elif (C == "л"): Window.blit(text[12][l],(x,y))
            elif (C == "м"): Window.blit(text[13][l],(x,y))
            elif (C == "н"): Window.blit(text[14][l],(x,y))            
            elif (C == "о"): Window.blit(text[15][l],(x,y))
            elif (C == "п"): Window.blit(text[16][l],(x,y))
            elif (C == "р"): Window.blit(text[17][l],(x,y))                   
            elif (C == "с"): Window.blit(text[18][l],(x,y))
            elif (C == "т"): Window.blit(text[19][l],(x,y))
            elif (C == "у"): Window.blit(text[20][l],(x,y))            
            elif (C == "ф"): Window.blit(text[21][l],(x,y))
            elif (C == "х"): Window.blit(text[22][l],(x,y))
            elif (C == "ч"): Window.blit(text[24][l],(x,y))
            elif (C == "ш"): Window.blit(text[25][l],(x,y))           
            elif (C == "ы"): Window.blit(text[28][l],(x,y))
            elif (C == "ь"): Window.blit(text[29][l],(x,y))                   
            elif (C == "э"): Window.blit(text[30][l],(x,y))
            elif (C == "ю"): Window.blit(text[31][l],(x,y))
            elif (C == "я"): Window.blit(text[32][l],(x,y))            
            elif (C == "1"): Window.blit(text[33][l],(x,y))
            elif (C == "2"): Window.blit(text[34][l],(x,y))
            elif (C == "3"): Window.blit(text[35][l],(x,y))             
            elif (C == "4"): Window.blit(text[36][l],(x,y))
            elif (C == "5"): Window.blit(text[37][l],(x,y))
            elif (C == "6"): Window.blit(text[38][l],(x,y))            
            elif (C == "7"): Window.blit(text[39][l],(x,y))
            elif (C == "8"): Window.blit(text[40][l],(x,y))
            elif (C == "9"): Window.blit(text[41][l],(x,y))                   
            elif (C == "0"): Window.blit(text[42][l],(x,y))
            elif (C == "-"): Window.blit(text[43][l],(x,y))
            x += 12
            
            
def effect_4(tick,pos):
    a = abs(10-tick)*2

    a11 = take_screen((0,pos  ),(a*1.25,pos+2  ))    
    a21 = take_screen((0,pos+2),(a*1.50,pos+2+2 ))
    a31 = take_screen((0,pos+4),(a*1.75,pos+4+2 ))
    a41 = take_screen((0,pos+6),(a*2.00,pos+6+2))
    a51 = take_screen((0,pos+8),(a*1.75,pos+8+2))
    a61 = take_screen((0,pos+10),(a*1.50,pos+10+2))
    a71 = take_screen((0,pos+12),(a*1.25,pos+12+2))

    a12 = take_screen((a*1.25,pos),(640,pos+2)) 
    a22 = take_screen((a*1.50,pos+2),(640,pos+2+2)) 
    a32 = take_screen((a*1.75,pos+4),(640,pos+4+2)) 
    a42 = take_screen((a*2.00,pos+6),(640,pos+6+2)) 
    a52 = take_screen((a*1.75,pos+8),(640,pos+8+2)) 
    a62 = take_screen((a*1.50,pos+10),(640,pos+10+2)) 
    a72 = take_screen((a*1.25,pos+12),(640,pos+12+2)) 

    Window.blit(a11,(a,pos))
    Window.blit(a21,(a,pos+2))
    Window.blit(a31,(a,pos+4))
    Window.blit(a41,(a,pos+6))
    Window.blit(a51,(a,pos+8))
    Window.blit(a61,(a,pos+10))
    Window.blit(a71,(a,pos+12))
    
    Window.blit(a12,(0,pos))
    Window.blit(a22,(0,pos+2))
    Window.blit(a32,(0,pos+4))
    Window.blit(a42,(0,pos+6))
    Window.blit(a52,(0,pos+8))
    Window.blit(a62,(0,pos+10))
    Window.blit(a72,(0,pos+12))
    
def gamemenu_map(x,d):
    if (d == 1):
        if   (x ==  0): return  0
        
        elif (x ==  1): return  0
        elif (x ==  2): return  0
        elif (x ==  3): return  0
        elif (x ==  4): return  1
        elif (x ==  5): return  2
        elif (x ==  6): return  3
        
        elif (x ==  7): return  4
        elif (x ==  8): return  5
        elif (x ==  9): return  6
        elif (x == 10): return  7
        elif (x == 11): return  8
        elif (x == 12): return  9
        elif (x == 13): return 10
        elif (x == 14): return 11
        elif (x == 15): return 12

        elif (x == 16): return 13
        elif (x == 17): return 14
        elif (x == 18): return 15
        elif (x == 19): return 16
        elif (x == 20): return 17
        elif (x == 21): return 18

    if (d == 2):
        if   (x ==  0): return  1
        
        elif (x ==  1): return  2
        elif (x ==  2): return  3
        elif (x ==  3): return  4
        elif (x ==  4): return  5
        elif (x ==  5): return  6
        elif (x ==  6): return  7
        
        elif (x ==  7): return  8
        elif (x ==  8): return  9
        elif (x ==  9): return 10
        elif (x == 10): return 11
        elif (x == 11): return 12
        elif (x == 12): return 13
        elif (x == 13): return 14
        elif (x == 14): return 15
        elif (x == 15): return 16

        elif (x == 16): return 17
        elif (x == 17): return 18
        elif (x == 18): return 19
        elif (x == 19): return 20
        elif (x == 20): return 21
        elif (x == 21): return 21

    if (d == 3):
        if   (x ==  0): return  1
        
        elif (x ==  1): return  4
        elif (x ==  2): return  5
        elif (x ==  3): return  6
        elif (x ==  4): return  7
        elif (x ==  5): return  8
        elif (x ==  6): return  9
        
        elif (x ==  7): return 10
        elif (x ==  8): return 11
        elif (x ==  9): return 12
        elif (x == 10): return 13
        elif (x == 11): return 14
        elif (x == 12): return 15
        elif (x == 13): return 16
        elif (x == 14): return 17
        elif (x == 15): return 18

        elif (x == 16): return 19
        elif (x == 17): return 20
        elif (x == 18): return 21
        elif (x == 19): return 19
        elif (x == 20): return 20
        elif (x == 21): return 21

    if (d == 4):
        if   (x ==  0): return  0
        
        elif (x ==  1): return  0
        elif (x ==  2): return  1
        elif (x ==  3): return  2
        elif (x ==  4): return  3
        elif (x ==  5): return  4
        elif (x ==  6): return  5
        
        elif (x ==  7): return  6
        elif (x ==  8): return  7
        elif (x ==  9): return  8
        elif (x == 10): return  9
        elif (x == 11): return 10
        elif (x == 12): return 11
        elif (x == 13): return 12
        elif (x == 14): return 13
        elif (x == 15): return 14

        elif (x == 16): return 15
        elif (x == 17): return 16
        elif (x == 18): return 17
        elif (x == 19): return 18
        elif (x == 20): return 19
        elif (x == 21): return 20

def select_game_getpos(x):

    if   (x ==  1): return  (0,1)
    elif (x ==  2): return  (1,1)
    elif (x ==  3): return  (2,1)
    elif (x ==  4): return  (0,2)
    elif (x ==  5): return  (1,2)
    elif (x ==  6): return  (2,2)
        
    elif (x ==  7): return  (0,0)
    elif (x ==  8): return  (1,0)
    elif (x ==  9): return  (2,0)
    elif (x == 10): return  (0,1)
    elif (x == 11): return  (1,1)
    elif (x == 12): return  (2,1)
    elif (x == 13): return  (0,2)
    elif (x == 14): return  (1,2)
    elif (x == 15): return  (2,2)

    elif (x == 16): return  (0,0)
    elif (x == 17): return  (1,0)
    elif (x == 18): return  (2,0)
    elif (x == 19): return  (0,1)
    elif (x == 20): return  (1,1)
    elif (x == 21): return  (2,1)

def chascecount(x):
    return x >= randint(0,100000)/100000


def game_select_update(select):
    
    if (game_select_button):
        Window.blit(play_button_1,(468,80))
        Window.blit(back_button_2,(480,32))        
    else:
        Window.blit(play_button_2,(468,80))
        Window.blit(back_button_1,(480,32))
        
        
    if (game_select == "morskaya_ohota"):
        text_print("Морская охота",1,32,32)
        text_print("- поразите как можно больше",1,32,84)
        text_print("  кораблей торпедами.",1,32,110)
        text_print("- цельтесь с упреждением,",1,32,136)
        text_print("  чтобы поразить цель.",1,32,162)
        text_print("- у вас будет только 10 торпед.",1,32,188)      
        text_print("- время игры - 2 минуты.",1,32,214)
        text_print("- поразите хотя бы 8 кораблей,",1,32,240)
        text_print("  чтобы получить призовую игру.",1,32,266)        
        text_print("- поразите хотя бы 8 кораблей",1,32,292)
        text_print("  в призовой игре, чтобы",1,32,318)
        text_print("  получить золотую монету.",1,32,344)

def morskaya_ohota_game_update():
    global morskaya_ohota_var_pos, morskaya_ohota_borders_subtick, morskaya_ohota_borders_tick,morskaya_ohota_hit_bool, morskaya_ohota_hit_tick, morskaya_ohota_hit_ship, morskaya_ohota_hit_pos
    global morskaya_ohota_subtime, morskaya_ohota_time

    if (morskaya_ohota_R_bool): morskaya_ohota_var_pos += 2
    if (morskaya_ohota_L_bool): morskaya_ohota_var_pos -= 2

    if (morskaya_ohota_var_pos < -100): morskaya_ohota_var_pos = -100
    if (morskaya_ohota_var_pos > 1380): morskaya_ohota_var_pos = 1380
    
    Window.blit(morskaya_ohota_map,(-morskaya_ohota_var_pos,0))

    if(morskaya_ohota_hit_bool):

        if (morskaya_ohota_hit_tick <= 10): blackscreen.set_alpha(round(255*(morskaya_ohota_hit_tick/10)))
        if (morskaya_ohota_hit_tick >10 and morskaya_ohota_hit_tick < 50): blackscreen.set_alpha(255)
        if (morskaya_ohota_hit_tick >= 50): blackscreen.set_alpha(round(255*((morskaya_ohota_hit_tick-50)/10)))

        for i in range(10):
            if (MO_ships[i].active): MO_ships[i].draw()

                
        Window.blit(morskaya_ohota_bordersmap[morskaya_ohota_borders_tick],(-morskaya_ohota_var_pos,0))

        for i in range(16):
            MO_oblakos[i].draw()


        Window.blit(blackscreen,(0,0))
                
        Window.blit(morskaya_ohota_hit,(morskaya_ohota_hit_pos-morskaya_ohota_var_pos,194))

        Window.blit(morskaya_ohota_ship_shadow[MO_ships[morskaya_ohota_hit_ship].size][not(MO_ships[morskaya_ohota_hit_ship].dir)],(MO_ships[morskaya_ohota_hit_ship].pos_x-morskaya_ohota_var_pos,216))

        morskaya_ohota_hit_tick+=1

        if (morskaya_ohota_hit_tick >= 59):
            morskaya_ohota_hit_bool = False

    else:

        for i in range(10):
            MO_TWs[i].update()
            for j in range(10):
                if (MO_TWs[i].subtick == 0 and MO_TWs[i].tick == 59 and MO_ships[9-j].active and MO_ships[9-j].hit(MO_TWs[i].pos_x+309)):
                    morskaya_ohota_hit_tick = 0
                    morskaya_ohota_hit_bool = True
                    morskaya_ohota_hit_ship = 9-j
                    morskaya_ohota_hit_pos = MO_TWs[i].pos_x+309
                    MO_ships[9-j].active = False
                    break
                    
                    
        morskaya_ohota_borders_subtick += 1
        if (morskaya_ohota_borders_subtick >= 30):
            morskaya_ohota_borders_subtick = 0
            morskaya_ohota_borders_tick += 1
            if (morskaya_ohota_borders_tick >= 2):
                morskaya_ohota_borders_tick = 0

        for i in range(10):
            if ((MO_ships[i]).active):
                MO_ships[i].update()
                MO_ships[i].draw()

                
        Window.blit(morskaya_ohota_bordersmap[morskaya_ohota_borders_tick],(-morskaya_ohota_var_pos,0))

        for i in range(16):
            MO_oblakos[i].update()
            MO_oblakos[i].draw()

        morskaya_ohota_subtime += 1
        if (morskaya_ohota_subtime >= 59):
            morskaya_ohota_subtime = 0
            morskaya_ohota_time -= 1
    
    Window.blit(morskaya_ohota_periskop,(0,0))

    text_print(str(morskaya_ohota_time//60),1,390,390)
    ss = str(morskaya_ohota_time%60)
    if (len(ss)==1): ss = "0" + ss
    text_print(ss,1,406,390)
    Window.blit(morskaya_ohota_dd,(404,396))

    for i in range(morskaya_ohota_torpedos_left): Window.blit(morskaya_ohota_torpedo_unused,(212+16*i,394))
    for i in range(10-morskaya_ohota_torpedos_left): Window.blit(morskaya_ohota_torpedo_used,(212+16*(9-i),394))
        
def update():
    global effect_2_tick, effect_4_tick, coinfalls_tick
    
    Window.fill((0,0,0))

    if (loadtick < 420):
        if (loadtick >= 60 and loadtick < 180): Window.blit(intro_screen_1,(0,0))
        if (loadtick >= 180 and loadtick < 300): Window.blit(intro_screen_2,(0,0))
        if (loadtick >= 360 and loadtick < 420): Window.blit(mainmenu_logo_1,(0,0))
    else:


        if (mainmenu_bool):
            if (mainmenu_tick): Window.blit(mainmenu_logo_2,(0,0))
            else: Window.blit(mainmenu_logo_3,(0,0))

            if (mainmenu_select == 1):
                 Window.blit(play_button_1,(250,222))
                 Window.blit(settings_button_2,(214,270-12))
                 Window.blit(quit_button_2,(262,318))
            if (mainmenu_select == 2):
                 Window.blit(play_button_2,(250,222))
                 Window.blit(settings_button_1,(214,270-12))
                 Window.blit(quit_button_2,(262,318))
            if (mainmenu_select == 3):
                 Window.blit(play_button_2,(250,222))
                 Window.blit(settings_button_2,(214,270-12))
                 Window.blit(quit_button_1,(262,318))

            Window.blit(version_text,(258,458))

        if (settmenu_bool):
            if (settmenu_select == 0): Window.blit(back_button_1,(32,32))
            else: Window.blit(back_button_2,(32,32))

            if (settmenu_select == 1):
                Window.blit(settmenu_fullscreen_1,(62,100))
                if (fullscreen_bool): Window.blit(settmenu_fullscreen_cheak_1,(62,100))
            else:
                Window.blit(settmenu_fullscreen_2,(62,100))
                if (fullscreen_bool): Window.blit(settmenu_fullscreen_cheak_2,(62,100))

        if (gamemenu_bool):
                if (gamemenu_razdel == 0):
                    if (gamemenu_select == 0): Window.blit(back_button_1,(32,32))
                    else: Window.blit(back_button_2,(32,32))

                    Window.blit(morskaya_ohota_banner,( 32,208))
                    if (gamemenu_select == 1): Window.blit(morskaya_ohota_gamename_1,(28,178))
                    else: Window.blit(morskaya_ohota_gamename_2,(28,178))
                    Window.blit(gonky_banner,(240,208))
                    if (gamemenu_select == 2): Window.blit(gonky_gamename_1,(236,178))
                    else: Window.blit(gonky_gamename_2,(236,178))
                    Window.blit(gonky_II_banner,(448,208))
                    if (gamemenu_select == 3): Window.blit(gonky_II_gamename_1,(444,178))
                    else: Window.blit(gonky_II_gamename_2,(444,178))

                    Window.blit(safary_banner,( 32,368))
                    if (gamemenu_select == 4): Window.blit(safary_gamename_1,(28,338))
                    else: Window.blit(safary_gamename_2,(28,338))
                    Window.blit(comingsoon_banner,(240,368))
                    if (gamemenu_select == 5): Window.blit(comingsoon_gamename_1,(236,338))
                    else: Window.blit(comingsoon_gamename_2,(236,338))
                    Window.blit(comingsoon_banner,(448,368))
                    if (gamemenu_select == 6): Window.blit(comingsoon_gamename_1,(444,338))
                    else: Window.blit(comingsoon_gamename_2,(444,338))                

                if (gamemenu_razdel == 1):

                    Window.blit(comingsoon_banner,( 32, 48))
                    if (gamemenu_select == 7): Window.blit(comingsoon_gamename_1,(28,18))
                    else: Window.blit(comingsoon_gamename_2,(28,18))
                    Window.blit(comingsoon_banner,(240, 48))
                    if (gamemenu_select == 8): Window.blit(comingsoon_gamename_1,(236,18))
                    else: Window.blit(comingsoon_gamename_2,(236,18))
                    Window.blit(comingsoon_banner,(448, 48))
                    if (gamemenu_select == 9): Window.blit(comingsoon_gamename_1,(444,18))
                    else: Window.blit(comingsoon_gamename_2,(444,18))
                    
                    Window.blit(comingsoon_banner,( 32,208))
                    if (gamemenu_select ==10): Window.blit(comingsoon_gamename_1,(28,178))
                    else: Window.blit(comingsoon_gamename_2,(28,178))
                    Window.blit(comingsoon_banner,(240,208))
                    if (gamemenu_select ==11): Window.blit(comingsoon_gamename_1,(236,178))
                    else: Window.blit(comingsoon_gamename_2,(236,178))
                    Window.blit(comingsoon_banner,(448,208))
                    if (gamemenu_select ==12): Window.blit(comingsoon_gamename_1,(444,178))
                    else: Window.blit(comingsoon_gamename_2,(444,178))

                    Window.blit(comingsoon_banner,( 32,368))
                    if (gamemenu_select ==13): Window.blit(comingsoon_gamename_1,(28,338))
                    else: Window.blit(comingsoon_gamename_2,(28,338))
                    Window.blit(comingsoon_banner,(240,368))
                    if (gamemenu_select ==14): Window.blit(comingsoon_gamename_1,(236,338))
                    else: Window.blit(comingsoon_gamename_2,(236,338))
                    Window.blit(comingsoon_banner,(448,368))
                    if (gamemenu_select ==15): Window.blit(comingsoon_gamename_1,(444,338))
                    else: Window.blit(comingsoon_gamename_2,(444,338))    

                if (gamemenu_razdel == 2):

                    Window.blit(comingsoon_banner,( 32, 48))
                    if (gamemenu_select ==16): Window.blit(comingsoon_gamename_1,(28,18))
                    else: Window.blit(comingsoon_gamename_2,(28,18))
                    Window.blit(comingsoon_banner,(240, 48))
                    if (gamemenu_select ==17): Window.blit(comingsoon_gamename_1,(236,18))
                    else: Window.blit(comingsoon_gamename_2,(236,18))
                    Window.blit(comingsoon_banner,(448, 48))
                    if (gamemenu_select ==18): Window.blit(comingsoon_gamename_1,(444,18))
                    else: Window.blit(comingsoon_gamename_2,(444,18))
                    
                    Window.blit(comingsoon_banner,( 32,208))
                    if (gamemenu_select ==19): Window.blit(comingsoon_gamename_1,(28,178))
                    else: Window.blit(comingsoon_gamename_2,(28,178))
                    Window.blit(comingsoon_banner,(240,208))
                    if (gamemenu_select ==20): Window.blit(comingsoon_gamename_1,(236,178))
                    else: Window.blit(comingsoon_gamename_2,(236,178))
                    Window.blit(comingsoon_banner,(448,208))
                    if (gamemenu_select ==21): Window.blit(comingsoon_gamename_1,(444,178))
                    else: Window.blit(comingsoon_gamename_2,(444,178))
                    
                if (gamemenu_select != 0):
                    n,m = select_game_getpos(gamemenu_select)
                    Window.blit(select_game,(32+208*n-4,48+160*m-4))
        else:
            
            if (game_select != "none"): game_select_update(game_select)

            if (coinfalls_tick > 0):
                coinfalls_tick -= 1
                if (coinfalls_tick >= 10 and coinfalls_tick < 70): Window.blit(coinfalls[3-(coinfalls_tick-10)//15],(268,168))
            else:
                if (morskaya_ohota_game_bool): morskaya_ohota_game_update()
                    

                
        
    if (effect_2_tick > 0):

        for i in range(effect_2_int+randint(-1,1)):
            R = randint(1,60)
            Window.blit(pygame.transform.scale(effect_3_1,(R,480)),(randint(0,639-R),0))
        for i in range(effect_2_int+randint(-1,1)):
            R = randint(1,60)
            Window.blit(pygame.transform.scale(effect_3_2,(640,R)),(0,randint(0,479-R)))

    for i in range(randint(1,5) + int(bool(effect_2_tick)) * effect_2_int * 100):
        lpx = randint(0,319); lpy = randint(0,239)
        pygame.draw.rect(Window, (0,0,0),(lpx*2,lpy*2, 2, 2))

    Window.blit(effect_1[mainmenu_subtick%3],(0,0))

    if (effect_2_tick > 0):
        effect_2_tick -= 1
            
        for i in range(effect_2_int+randint(-1,1)):
            R = randint(1,60)
            Window.blit(pygame.transform.scale(effect_2_1,(R,480)),(randint(0,639-R),0))
        for i in range(effect_2_int+randint(-1,1)):
            R = randint(1,60)
            Window.blit(pygame.transform.scale(effect_2_2,(640,R)),(0,randint(0,479-R)))

    if (effect_4_tick > 0) :
        effect_4(effect_4_tick,effect_4_pos)
        effect_4_tick -= 1
    
Run = True
while Run:

    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: Run = False 
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE): Run = False

            if (loadtick >= 420):
            
                if (mainmenu_bool):
                    if (event.key == pygame.K_UP or event.key == pygame.K_w):
                        if (mainmenu_select > 1): mainmenu_select -= 1
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                        if (mainmenu_select < 3): mainmenu_select += 1
                    if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                        if (mainmenu_select == 1):
                            mainmenu_bool = False
                            gamemenu_bool = True
                            gamemenu_select = 0
                        if (mainmenu_select == 2):
                            mainmenu_bool = False
                            settmenu_bool = True
                            settmenu_select = 0
                        if (mainmenu_select == 3):
                            Run = False

                elif (settmenu_bool):
                    if (event.key == pygame.K_UP or event.key == pygame.K_w):
                        if (settmenu_select > 0): settmenu_select -= 1
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                        if (settmenu_select < 1): settmenu_select += 1
                        
                    if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                            if (settmenu_select == 0):
                                settmenu_bool = False
                                mainmenu_bool = True
                                mainmenu_select = 2
                            if (settmenu_select == 1):
                                fullscreen_bool = not(fullscreen_bool)
                                pygame .display.toggle_fullscreen()
                                settings_output()
                                
                elif (gamemenu_bool):
                    if (event.key == pygame.K_UP or event.key == pygame.K_w): gamemenu_select = gamemenu_map(gamemenu_select,1)
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s): gamemenu_select = gamemenu_map(gamemenu_select,3)
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): gamemenu_select = gamemenu_map(gamemenu_select,2)
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a): gamemenu_select = gamemenu_map(gamemenu_select,4)

                    if   (gamemenu_select >= 0 and gamemenu_select <= 6): gamemenu_razdel = 0
                    elif (gamemenu_select >= 7 and gamemenu_select <= 15): gamemenu_razdel = 1
                    elif (gamemenu_select >= 16 and gamemenu_select <= 21): gamemenu_razdel = 2
                        
                    if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                            if (gamemenu_select == 0):
                                gamemenu_bool = False
                                mainmenu_bool = True
                                mainmenu_select = 1
                            if (gamemenu_select == 1):
                                gamemenu_bool = False
                                game_select = "morskaya_ohota"
                                mainmenu_select = 0

                elif (game_select != "none"):
                    if (event.key == pygame.K_UP or event.key == pygame.K_w):
                        if (game_select_button > 0): game_select_button -= 1
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                        if (game_select_button < 1): game_select_button += 1
                    if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                        if (game_select_button == 0):
                            game_select = "none"
                            gamemenu_bool = True
                        if (game_select_button == 1):
                            if (game_select == "morskaya_ohota"): morskaya_ohota_game_bool = True                 
                            game_select = "none"
                            gamemenu_bool = False
                            coinfalls_tick = 80
                            morskaya_ohota_var_pos = 640
                            morskaya_ohota_torpedos_left = 10
                            morskaya_ohota_time = 120

                elif (morskaya_ohota_game_bool):
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): morskaya_ohota_R_bool = True
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a): morskaya_ohota_L_bool = True
                    if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                        if (morskaya_ohota_torpedos_left > 0):
                            morskaya_ohota_torpedos_left -= 1
                            MO_TWs[morskaya_ohota_torpedos_left].spawn(morskaya_ohota_var_pos)
                        


        if (event.type == pygame.KEYUP):
            if (morskaya_ohota_game_bool):
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): morskaya_ohota_R_bool = False
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a): morskaya_ohota_L_bool = False
                    
    if (chascecount(0.0025) and effect_4_tick == 0):
        effect_4_tick = 20
        effect_4_pos = randint(0,234)*2

    if (loadtick < 420):
        loadtick += 1
        if (loadtick == 50 or loadtick == 170 or loadtick == 290): effect_2_tick = 20
        if (loadtick == 420): mainmenu_bool = True
        
    mainmenu_subtick += 1
    if (mainmenu_subtick >= 60):
        mainmenu_subtick = 0
        mainmenu_tick += 1
        if (mainmenu_tick >= 2):
            mainmenu_tick = 0
    
    update()
    pygame.display.flip()
    
pygame.quit()
