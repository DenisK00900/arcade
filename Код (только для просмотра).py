import pygame
import math
import time
import pathlib
from pathlib import Path
from random import randint
import numpy as np
import sys
import cv2

directiry = pathlib.Path.cwd()
dir_path = str(directiry)

FPS = 60 

clock = pygame.time.Clock() 

fullscreen_bool = True

goldencoins = 0

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

def progress_input():
    global goldencoins
    f = open(dir_path+'/data/save/progress.bin','rb')
    while True:
        S = (f.readline()).decode('utf-8')
        if (S == "end"): break
        else:
            V,E,D = S.split()
            if (V == "goldencoins"): goldencoins = int(D)

    f.close()

def progress_output():
    global goldencoins
    f = open(dir_path+'/data/save/progress.bin','wb')
    f.write(("goldencoins = "+str(goldencoins)+"\n").encode('utf-8'))
    f.write(("end").encode('utf-8'))
    f.close()
    
settings_input()
progress_input()

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

prizegame = [0]*4
prizegame[0] = pygame.image.load(dir_path+'/data/texture/prizegame_1.png').convert(); prizegame[0].set_colorkey((0,0,0))
prizegame[1] = pygame.image.load(dir_path+'/data/texture/prizegame_2.png').convert(); prizegame[1].set_colorkey((0,0,0))
prizegame[2] = pygame.image.load(dir_path+'/data/texture/prizegame_3.png').convert(); prizegame[2].set_colorkey((0,0,0))
prizegame[3] = pygame.image.load(dir_path+'/data/texture/prizegame_4.png').convert(); prizegame[3].set_colorkey((0,0,0))

morskaya_ohota_torpedo_way = [0]*60
for i in range(60):
    morskaya_ohota_torpedo_way[i] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_torpedo_way_'+str(i+1)+'.png').convert()
    morskaya_ohota_torpedo_way[i].set_colorkey((255,0,0))

goldcoin_get = pygame.image.load(dir_path+'/data/texture/goldcoin_get.png').convert(); goldcoin_get.set_colorkey((0,0,0))

gonky_roadsegment = pygame.image.load(dir_path+'/data/texture/gonky_roadsegment.png').convert()
gonky_info_finish = pygame.image.load(dir_path+'/data/texture/gonky_info_finish.png').convert()
gonky_info_player_1_go = pygame.image.load(dir_path+'/data/texture/gonky_info_player_1_go.png').convert()
gonky_info_timer_go = pygame.image.load(dir_path+'/data/texture/gonky_info_timer_go.png').convert()
gonky_green_car = [0]*2
gonky_blue_car = [0]*2
gonky_brown_car = [0]*2
gonky_grey_car = [0]*2
gonky_red_car = [0]*2
gonky_vio_car = [0]*2
gonky_green_car[0] = pygame.image.load(dir_path+'/data/texture/gonky_green_car1.png').convert(); gonky_green_car[0].set_colorkey((255,255,255))
gonky_green_car[1] = pygame.image.load(dir_path+'/data/texture/gonky_green_car2.png').convert(); gonky_green_car[1].set_colorkey((255,255,255))
gonky_blue_car[0] = pygame.image.load(dir_path+'/data/texture/gonky_blue_car1.png').convert(); gonky_blue_car[0].set_colorkey((255,255,255))
gonky_blue_car[1] = pygame.image.load(dir_path+'/data/texture/gonky_blue_car2.png').convert(); gonky_blue_car[1].set_colorkey((255,255,255))
gonky_brown_car[0] = pygame.image.load(dir_path+'/data/texture/gonky_brown_car1.png').convert(); gonky_brown_car[0].set_colorkey((255,255,255))
gonky_brown_car[1] = pygame.image.load(dir_path+'/data/texture/gonky_brown_car2.png').convert(); gonky_brown_car[1].set_colorkey((255,255,255))
gonky_grey_car[0] = pygame.image.load(dir_path+'/data/texture/gonky_grey_car1.png').convert(); gonky_grey_car[0].set_colorkey((255,255,255))
gonky_grey_car[1] = pygame.image.load(dir_path+'/data/texture/gonky_grey_car2.png').convert(); gonky_grey_car[1].set_colorkey((255,255,255))
gonky_red_car[0] = pygame.image.load(dir_path+'/data/texture/gonky_red_car1.png').convert(); gonky_red_car[0].set_colorkey((255,255,255))
gonky_red_car[1] = pygame.image.load(dir_path+'/data/texture/gonky_red_car2.png').convert(); gonky_red_car[1].set_colorkey((255,255,255))
gonky_vio_car[0] = pygame.image.load(dir_path+'/data/texture/gonky_vio_car1.png').convert(); gonky_vio_car[0].set_colorkey((255,255,255))
gonky_vio_car[1] = pygame.image.load(dir_path+'/data/texture/gonky_vio_car2.png').convert(); gonky_vio_car[1].set_colorkey((255,255,255))

number_x2_white = [0]*10
for i in range(10): number_x2_white[i] = pygame.image.load(dir_path+'/data/texture/number_x2_white_'+str(i)+'.png').convert(); number_x2_white[i].set_colorkey((0,0,0))
goldcoin_have = pygame.image.load(dir_path+'/data/texture/goldcoin_have.png').convert(); goldcoin_have.set_colorkey((0,0,0))

pamat_banner = pygame.image.load(dir_path+'/data/texture/pamat_banner.png').convert(); pamat_banner.set_colorkey((0,0,0))
pamat_gamename_1 = pygame.image.load(dir_path+'/data/texture/pamat_gamename_1.png').convert()
pamat_gamename_2 = pygame.image.load(dir_path+'/data/texture/pamat_gamename_2.png').convert()

gonky_II_roadsegment = pygame.image.load(dir_path+'/data/texture/gonky_II_roadsegment.png').convert()

text=[]
for i in range(77):
    text.append([0]*2)

for i in range(77):
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
blackscreen_timer = 0
prizegame_timer = 0
goldcoin_get_timer = 0
morskaya_ohota_prizegame_bool = False
gonky_game_bool = False
gonky_prizegame_bool = False
gonky_viev_pos = 0
gonky_R_bool = False
gonky_L_bool = False
gonky_F_bool = False
gonky_B_bool = False
gonky_time = 0
gonky_subtime = 0
effect_6_tick = 0
gonky_II_game_bool = False
gonky_II_player1_viev_pos = 0
gonky_II_player2_viev_pos = 0

class CollisionBox():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.size_x = 0
        self.size_y = 0

    def define(self,x,y,s_x,s_y):
        self.pos_x = x
        self.pos_y = y
        self.size_x = s_x
        self.size_y = s_y
        
def cheak_point(point_x,point_y,Box):
    return ((point_x >= Box.pos_x and point_x <= Box.pos_x+Box.size_x) and (point_y >= Box.pos_y and point_y <= Box.pos_y+Box.size_y))

def cheak_BoxC(Box1,Box2):
    return (((cheak_point(Box1.pos_x,Box1.pos_y,Box2)) or (cheak_point(Box2.pos_x,Box2.pos_y,Box1))) or
       ((cheak_point(Box1.pos_x,Box1.pos_y+Box2.size_y,Box2)) or (cheak_point(Box2.pos_x,Box2.pos_y+Box2.size_y,Box1))) or
       ((cheak_point(Box1.pos_x+Box1.size_x,Box1.pos_y,Box2)) or (cheak_point(Box2.pos_x+Box2.size_x,Box2.pos_y,Box1))) or
       ((cheak_point(Box1.pos_x+Box1.size_x,Box1.pos_y+Box2.size_y,Box2)) or (cheak_point(Box2.pos_x+Box2.size_x,Box2.pos_y+Box2.size_y,Box1))))

cartypes = ["brown","grey","red","vio","green","blue"]  
class car():
    def __init__(self):
        self.type = "None"
        self.pos_x = -1
        self.pos_y = -1
        self.speed = 0
        self.hitbox = CollisionBox()
        self.texture = None
        self.control = False
        self.way = True
        self.distract = 0

    def spawn(self,cartype,under,way):
        if (under): self.pos_y = 642 + int(not(way))*600
        else: self.pos_y = -200 - int(not(way))*600
        
        if (cartype == "brown"):
            self.speed = randint(300-100*int(gonky_prizegame_bool),500+50*int(gonky_prizegame_bool))/100
            self.texture = gonky_brown_car
            self.hitbox.define(0,0,36,58)
        if (cartype == "grey"):
            self.speed = randint(350-100*int(gonky_prizegame_bool),700+50*int(gonky_prizegame_bool))/100
            self.texture = gonky_grey_car
            self.hitbox.define(0,0,36,60)
        if (cartype == "red"):
            self.speed = randint(400-100*int(gonky_prizegame_bool),800+50*int(gonky_prizegame_bool))/100
            self.texture = gonky_red_car
            self.hitbox.define(0,0,36,64)
        if (cartype == "vio"):
            self.speed = randint(200-100*int(gonky_prizegame_bool),400+50*int(gonky_prizegame_bool))/100
            self.texture = gonky_vio_car
            self.hitbox.define(0,0,36,130)

        if (way): self.speed = - self.speed
        
    def update(self):
        self.pos_y += self.speed
        if (self.pos_y > 642 + int(not(self.way))*600): self.spawn(cartypes[randint(0,3)],False,self.way)
        if (self.pos_y <-200 - int(not(self.way))*600): self.spawn(cartypes[randint(0,3)],True,self.way)
        
gonky_cars_count = 11
gonky_car = [0]*gonky_cars_count

gonky_car[0] = car()
gonky_car[0].type = "green"
gonky_car[0].control = True
gonky_car[0].pos_x = 340
gonky_car[0].pos_y = -1
gonky_car[0].speed = 5
gonky_car[0].texture = gonky_green_car
gonky_car[0].hitbox.define(0,0,36,64)
gonky_car[0].way = True

for i in range(5):
    gonky_car[i+1] = car()
    gonky_car[i+1].control = False
    gonky_car[i+1].pos_y = -999
    gonky_car[i+1].pos_x = 332+52*i

for i in range(5):
    gonky_car[i+6] = car()
    gonky_car[i+6].control = False
    gonky_car[i+6].way = False
    gonky_car[i+6].pos_y = -999
    gonky_car[i+6].pos_x = 64+52*i

gonky_II_cars_count = 10
gonky_II_car = [0]*gonky_II_cars_count

gonky_II_car[0] = car()
gonky_II_car[0].type = "green"
gonky_II_car[0].control = True
gonky_II_car[0].pos_x = 168
gonky_II_car[0].pos_y = -1
gonky_II_car[0].speed = 5
gonky_II_car[0].texture = gonky_green_car
gonky_II_car[0].hitbox.define(0,0,36,64)
gonky_II_car[0].way = True

gonky_II_car[1] = car()
gonky_II_car[1].type = "blue"
gonky_II_car[1].control = True
gonky_II_car[1].pos_x = 488
gonky_II_car[1].pos_y = -1
gonky_II_car[1].speed = 5
gonky_II_car[1].texture = gonky_blue_car
gonky_II_car[1].hitbox.define(0,0,36,64)
gonky_II_car[1].way = True
    
class MO_TW():
    def __init__(self):
        self.pos_x = -999
        self.tick = -1
        self.subtick = 0
        self.active = False

    def clear(self):
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

    def clear(self):
        self.pos_x = -999
        self.speed = 0
        self.dir = False
        self.active = True
            
    def draw(self):
        Window.blit(morskaya_ohota_ship[self.size][not(self.dir)],(round(self.pos_x)+int(round(self.pos_x)%2==1)-morskaya_ohota_var_pos,216))

    def spawn(self):
        if (self.pos_x == -999):
            self.pos_x = randint(-200+morskaya_ohota_var_pos,1480+morskaya_ohota_var_pos)
            if (randint(0,1)): self.speed = randint(5,10)/10
            else: self.speed = -randint(5,10)/10
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
        return (tx >= self.pos_x+4+self.size*8-8 and tx <= (self.pos_x+68)-(self.size*8)-8)
        
        
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

class MO_PG_ship():

    def __init__(self):
        self.pos_x = -999
        self.speed = 0
        self.size = 0
        self.dir = False
        self.active = True

    def clear(self):
        self.pos_x = -999
        self.speed = 0
        self.dir = False
        self.active = True
            
    def draw(self):
        Window.blit(morskaya_ohota_ship[self.size][not(self.dir)],(round(self.pos_x)+int(round(self.pos_x)%2==1)-morskaya_ohota_var_pos,216))

    def spawn(self):
        if (self.pos_x == -999):
            self.pos_x = randint(-200+morskaya_ohota_var_pos,1480+morskaya_ohota_var_pos)
            if (randint(0,1)): self.speed = randint(6,14)/10
            else: self.speed = -randint(6,14)/10
        else:
            if (randint(0,1)):
                self.pos_x = -200+morskaya_ohota_var_pos
                self.speed = randint(6,14)/10
            else:
                self.pos_x = 1480+morskaya_ohota_var_pos
                self.speed = -randint(6,14)/10
            
    def update(self):
        self.pos_x += self.speed
        self.dir = self.speed > 0
        if (self.pos_x < -200+morskaya_ohota_var_pos or self.pos_x > 1480+morskaya_ohota_var_pos): self.spawn()

    def hit(self,tx):
        return (tx >= self.pos_x+4+self.size*8-8 and tx <= (self.pos_x+68)-self.size*8-8)
    
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
MO_PG_ships = []
for i in range(10): MO_PG_ships.append(MO_PG_ship())
MO_PG_ships[0].size = 0
MO_PG_ships[1].size = 1
MO_PG_ships[2].size = 1
MO_PG_ships[3].size = 2
MO_PG_ships[4].size = 2
MO_PG_ships[5].size = 2
MO_PG_ships[6].size = 3
MO_PG_ships[7].size = 3
MO_PG_ships[8].size = 3
MO_PG_ships[9].size = 3
MO_TWs = []
for i in range(10): MO_TWs.append(MO_TW())

def take_screen(topleft, bottomright):
    size = bottomright[0] - topleft[0], bottomright[1] - topleft[1]
    img = pygame.Surface(size)
    img.blit(Window, (0, 0), (topleft, size))
    return img

def rot_center(image, rect, angle): #Функция поворота
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

def changColor(image, color): #Функция, меняющая цвет
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage


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
            elif (C == "a"): Window.blit(text[46][l],(x,y))
            elif (C == "b"): Window.blit(text[47][l],(x,y))
            elif (C == "c"): Window.blit(text[48][l],(x,y))            
            elif (C == "d"): Window.blit(text[49][l],(x,y))
            elif (C == "e"): Window.blit(text[50][l],(x,y))
            elif (C == "f"): Window.blit(text[51][l],(x,y))                   
            elif (C == "g"): Window.blit(text[52][l],(x,y))
            elif (C == "h"): Window.blit(text[53][l],(x,y))
            elif (C == "i"): Window.blit(text[54][l],(x,y))            
            elif (C == "j"): Window.blit(text[55][l],(x,y))
            elif (C == "k"): Window.blit(text[56][l],(x,y))
            elif (C == "l"): Window.blit(text[57][l],(x,y))             
            elif (C == "m"): Window.blit(text[58][l],(x,y))
            elif (C == "n"): Window.blit(text[59][l],(x,y))
            elif (C == "o"): Window.blit(text[60][l],(x,y))            
            elif (C == "p"): Window.blit(text[61][l],(x,y))
            elif (C == "q"): Window.blit(text[62][l],(x,y))
            elif (C == "r"): Window.blit(text[63][l],(x,y))                   
            elif (C == "s"): Window.blit(text[64][l],(x,y))
            elif (C == "t"): Window.blit(text[65][l],(x,y))                   
            elif (C == "u"): Window.blit(text[66][l],(x,y))
            elif (C == "v"): Window.blit(text[67][l],(x,y))
            elif (C == "w"): Window.blit(text[68][l],(x,y))            
            elif (C == "x"): Window.blit(text[69][l],(x,y))
            elif (C == "y"): Window.blit(text[70][l],(x,y))
            elif (C == "z"): Window.blit(text[71][l],(x,y))
            elif (C == "+"): Window.blit(text[72][l],(x,y))
            elif (C == "-"): Window.blit(text[73][l],(x,y))            
            elif (C == "*"): Window.blit(text[74][l],(x,y))
            elif (C == "%"): Window.blit(text[75][l],(x,y))
            elif (C == "="): Window.blit(text[76][l],(x,y))            
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

def effect_5():

    if (1):

        src = pygame.surfarray.array3d(Window)
    
        h, w = src.shape[0:2]
     
        intrinsics = np.zeros((3, 3), np.float64)
     
        intrinsics[0, 0] = 5000
        intrinsics[1, 1] = 5000
        intrinsics[2, 2] = 1.0
        intrinsics[0, 2] = w/2.
        intrinsics[1, 2] = h/2.
     
        newCamMtx = np.zeros((3, 3), np.float64)
        newCamMtx[0, 0] = 5000
        newCamMtx[1, 1] = 5000
        newCamMtx[2, 2] = 1.0
        newCamMtx[0, 2] = w/2.
        newCamMtx[1, 2] = h/2.
     
        dist_coeffs = np.zeros((1, 4), np.float64)
        dist_coeffs[0, 0] = 30.0
        dist_coeffs[0, 1] = 0
        dist_coeffs[0, 2] = 0
        dist_coeffs[0, 3] = 0
     
        map1, map2 = cv2.initUndistortRectifyMap(intrinsics, dist_coeffs, None, newCamMtx, [src.shape[1],src.shape[0]], cv2.CV_16SC2)
        
        if (effect_6_tick > 0):
            res = cv2.cvtColor(src, cv2.COLOR_BGR2HSV )
            res = cv2.remap(res, map1, map2, cv2.INTER_LINEAR)
        else:
            res = cv2.remap(src, map1, map2, cv2.INTER_LINEAR)
        
        
        pygame.pixelcopy.array_to_surface(Window,res)

    
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

    if (game_select == "gonky"):
        text_print("Гонки",1,32,32)
        text_print("- Доберитесь до финиша как",1,32,84)
        text_print("  можно быстрее.",1,32,110)
        text_print("- Столкновения с другими",1,32,136)
        text_print("  машинами замедляют вас.",1,32,162)
        text_print("- время игры - 2 минуты.",1,32,188)      
        text_print("- Доберитесь до финиша,",1,32,214)
        text_print("  чтобы получить призовую игру.",1,32,240)
        text_print("- Доберитесь до финиша в",1,32,266)        
        text_print("  призовой игре, чтобы",1,32,292)
        text_print("  получить золотую монету.",1,32,318)

    if (game_select == "gonky_II"):
        text_print("Гонки II",1,32,32)
        text_print("- Игра для двоих игроков,",1,32,84)
        text_print("  используйте WASD + Q и",1,32,110)
        text_print("  стрелочки + правый CTRL.",1,32,136)
        text_print("- Доберитесь до финиша как",1,32,162)
        text_print("  можно быстрее.",1,32,188)
        text_print("- Столкновения с другими",1,32,214)
        text_print("  машинами замедляют вас.",1,32,240)
        text_print("- время игры - 2 минуты.",1,32,266)      
        text_print("- По истечении времени",1,32,292)
        text_print("  игрок с большей дистанцией",1,32,318)
        text_print("  побеждает.",1,32,344)        
        text_print("- В этой игре нельзя",1,32,370)
        text_print("  получить золотую монету.",1,32,396)

def gonky_II_game_update():


    
    Window.blit(gonky_II_roadsegment,(0,int(gonky_II_player1_viev_pos%480) + int(gonky_II_player1_viev_pos%2 == 1)))
    Window.blit(gonky_II_roadsegment,(320,int(gonky_II_player2_viev_pos%480) + int(gonky_II_player2_viev_pos%2 == 1)))

    Window.blit(gonky_II_car[0].texture[0],(gonky_II_car[0].pos_x,374))
    Window.blit(gonky_II_car[1].texture[0],(gonky_II_car[1].pos_x,374))

def gonky_game_update():
    global gonky_viev_pos, gonky_R_bool, gonky_L_bool, gonky_F_bool, gonky_B_bool, gonky_time, gonky_subtime, gonky_prizegame_bool, gonky_game_bool, prizegame_timer, blackscreen_timer,gamemenu_bool
    
    Window.blit(gonky_roadsegment,(0,int(gonky_viev_pos%480) + int(gonky_viev_pos%2 == 1)))
    Window.blit(gonky_roadsegment,(0,int(gonky_viev_pos%480)-480 + int(gonky_viev_pos%2 == 1)))

    Window.blit(gonky_info_player_1_go,(614,442))
    Window.blit(gonky_info_timer_go,(628,442))
    Window.blit(gonky_info_finish,(612,30))

    if (round(gonky_viev_pos/1000) > 50):
        gonky_car[0].distract = 0
        gonky_game_bool = False
        gonky_prizegame_bool = True
        prizegame_timer = 240
        gonky_viev_pos = 0
        gonky_time = 120
        gonky_car[0].type = "green"
        gonky_car[0].control = True
        gonky_car[0].pos_x = 340
        gonky_car[0].pos_y = -1
        gonky_car[0].speed = 6
        gonky_car[0].texture = gonky_green_car
        gonky_car[0].hitbox.define(0,0,36,64)
        gonky_car[0].way = True

    elif (round((120-gonky_time)/240*100) > 50):
        gonky_game_bool = False
        gamemenu_bool = True
        blackscreen_timer = 120

    for i in range(round(gonky_viev_pos/1000)):
        Window.blit(gonky_info_player_1_go,(614,442-((i+1)*8)))

    for i in range(round((120-gonky_time)/240*100)):
        Window.blit(gonky_info_timer_go,(628,442-((i+1)*8)))       



    gonky_viev_pos += gonky_car[0].speed

    if (gonky_car[0].distract == 0 and gonky_F_bool): gonky_car[0].speed += 0.0625
    if (gonky_B_bool): gonky_car[0].speed -= 0.0625

    if (gonky_car[0].speed < 0): gonky_car[0].speed = 0
    if (gonky_car[0].speed > 12): gonky_car[0].speed = 12

    if (gonky_R_bool and gonky_car[0].speed != 0): gonky_car[0].pos_x += 2
    if (gonky_L_bool and gonky_car[0].speed != 0): gonky_car[0].pos_x -= 2

    if (gonky_car[0].pos_x < 38): gonky_car[0].pos_x = 38
    if (gonky_car[0].pos_x > 566): gonky_car[0].pos_x = 566

    if (gonky_car[0].distract > 0): gonky_car[0].distract -= 1
            
    if ((gonky_car[0].distract/2)%2 == 0):Window.blit(gonky_car[0].texture[int(gonky_B_bool or gonky_car[0].speed == 0)],(gonky_car[0].pos_x,374))

    Boxs = CollisionBox()
    Boxt = CollisionBox()
        
    Boxs.define(gonky_car[0].pos_x,374,gonky_car[0].hitbox.size_x,gonky_car[0].hitbox.size_y)
            
    for i in range(1,gonky_cars_count,1):
        if (gonky_car[i].hitbox.size_y > 64): S = gonky_car[i].hitbox.size_y-64
        else: S = 0
        Boxt.define(gonky_car[i].pos_x,gonky_car[i].pos_y+S,gonky_car[i].hitbox.size_x,gonky_car[i].hitbox.size_y)
        if (gonky_car[0].distract == 0 and cheak_BoxC(Boxs,Boxt)):
            gonky_car[0].distract = 60
            gonky_car[0].speed = round((gonky_car[0].speed*0.25)*16)/16
            
        gonky_car[i].update()
        gonky_car[i].pos_y += gonky_car[0].speed
            
        Window.blit(gonky_car[i].texture[not(gonky_car[i].way)],(gonky_car[i].pos_x,round(gonky_car[i].pos_y)+int(round(gonky_car[i].pos_y)%2 == 1)))       

    gonky_subtime += 1
    if (gonky_subtime >= 59):
        gonky_subtime = 0
        gonky_time -= 1

def gonky_prizegame_update():
    global gonky_viev_pos, gonky_R_bool, gonky_L_bool, gonky_F_bool, gonky_B_bool, gonky_time, gonky_subtime, gonky_prizegame_bool, gonky_game_bool, prizegame_timer, blackscreen_timer, goldcoin_get_timer,gamemenu_bool, goldencoins
    
    Window.blit(gonky_roadsegment,(0,int(gonky_viev_pos%480) + int(gonky_viev_pos%2 == 1)))
    Window.blit(gonky_roadsegment,(0,int(gonky_viev_pos%480)-480 + int(gonky_viev_pos%2 == 1)))

    Window.blit(gonky_info_player_1_go,(614,442))
    Window.blit(gonky_info_timer_go,(628,442))
    Window.blit(gonky_info_finish,(612,30))

    if (round(gonky_viev_pos/1000) > 50):
        gamemenu_bool = True
        gonky_prizegame_bool = False
        goldencoins += 1
        progress_output()
        goldcoin_get_timer = 240
        
    elif (round((120-gonky_time)/240*100) > 50):
        gamemenu_bool = True
        gonky_prizegame_bool = False
        blackscreen_timer = 120

    for i in range(round(gonky_viev_pos/1000)):
        Window.blit(gonky_info_player_1_go,(614,442-((i+1)*8)))

    for i in range(round((120-gonky_time)/240*100)):
        Window.blit(gonky_info_timer_go,(628,442-((i+1)*8)))       



    gonky_viev_pos += gonky_car[0].speed

    if (gonky_car[0].distract == 0 and gonky_F_bool): gonky_car[0].speed += 0.0625
    if (gonky_B_bool): gonky_car[0].speed -= 0.0625

    if (gonky_car[0].speed < 0): gonky_car[0].speed = 0
    if (gonky_car[0].speed > 12): gonky_car[0].speed = 12

    if (gonky_R_bool and gonky_car[0].speed != 0): gonky_car[0].pos_x += 2
    if (gonky_L_bool and gonky_car[0].speed != 0): gonky_car[0].pos_x -= 2

    if (gonky_car[0].pos_x < 38): gonky_car[0].pos_x = 38
    if (gonky_car[0].pos_x > 566): gonky_car[0].pos_x = 566

    if (gonky_car[0].distract > 0): gonky_car[0].distract -= 1
            
    if ((gonky_car[0].distract/2)%2 == 0):Window.blit(gonky_car[0].texture[int(gonky_B_bool or gonky_car[0].speed == 0)],(gonky_car[0].pos_x,374))

    Boxs = CollisionBox()
    Boxt = CollisionBox()
        
    Boxs.define(gonky_car[0].pos_x,374,gonky_car[0].hitbox.size_x,gonky_car[0].hitbox.size_y)
            
    for i in range(1,gonky_cars_count,1):
        if (gonky_car[i].hitbox.size_y > 64): S = gonky_car[i].hitbox.size_y-64
        else: S = 0
        Boxt.define(gonky_car[i].pos_x,gonky_car[i].pos_y+S,gonky_car[i].hitbox.size_x,gonky_car[i].hitbox.size_y)
        if (gonky_car[0].distract == 0 and cheak_BoxC(Boxs,Boxt)):
            gonky_car[0].distract = 90
            gonky_car[0].speed = round((gonky_car[0].speed*0.20)*16)/16
            
        gonky_car[i].update()
        gonky_car[i].pos_y += gonky_car[0].speed
            
        Window.blit(gonky_car[i].texture[not(gonky_car[i].way)],(gonky_car[i].pos_x,round(gonky_car[i].pos_y)+int(round(gonky_car[i].pos_y)%2 == 1)))       

    gonky_subtime += 1
    if (gonky_subtime >= 59):
        gonky_subtime = 0
        gonky_time -= 1

def morskaya_ohota_game_update():
    global morskaya_ohota_var_pos, morskaya_ohota_borders_subtick, morskaya_ohota_borders_tick,morskaya_ohota_hit_bool, morskaya_ohota_hit_tick, morskaya_ohota_hit_ship, morskaya_ohota_hit_pos
    global morskaya_ohota_subtime, morskaya_ohota_time, morskaya_ohota_game_bool, gamemenu_bool, blackscreen_timer, prizegame_timer, morskaya_ohota_prizegame_bool, morskaya_ohota_torpedos_left

    F = False
    for i in range(10):
        F = F or MO_TWs[i].active
    F = not(F) and morskaya_ohota_torpedos_left == 0
    if (morskaya_ohota_time <= 0 or F):
        S = 0
        for i in range(10):
            S += int(not(MO_ships[i].active))

        if (S < 8):
            morskaya_ohota_game_bool = False
            gamemenu_bool = True
            blackscreen_timer = 120
        else:
            morskaya_ohota_game_bool = False
            morskaya_ohota_prizegame_bool = True
            prizegame_timer = 240
            morskaya_ohota_var_pos = 640
            morskaya_ohota_torpedos_left = 10
            morskaya_ohota_time = 120
            for i in range(10):
                MO_PG_ships[i].clear()
                MO_ships[i].clear()
                MO_TWs[i].clear()

    else:
        
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

def morskaya_ohota_prizegame_update():
    global morskaya_ohota_var_pos, morskaya_ohota_borders_subtick, morskaya_ohota_borders_tick,morskaya_ohota_hit_bool, morskaya_ohota_hit_tick, morskaya_ohota_hit_ship, morskaya_ohota_hit_pos
    global morskaya_ohota_subtime, morskaya_ohota_time, morskaya_ohota_game_bool, gamemenu_bool, blackscreen_timer, goldcoin_get_timer, morskaya_ohota_prizegame_bool, morskaya_ohota_torpedos_left
    global goldencoins

    F = False
    for i in range(10):
        F = F or MO_TWs[i].active
    F = not(F) and morskaya_ohota_torpedos_left == 0
    if (morskaya_ohota_time <= 0 or F):
        S = 0
        for i in range(10):
            S += int(not(MO_PG_ships[i].active))

        if (S < 8):
            morskaya_ohota_prizegame_bool = False
            gamemenu_bool = True
            blackscreen_timer = 120
        else:
            morskaya_ohota_prizegame_bool = False
            gamemenu_bool = True
            goldencoins += 1
            progress_output()
            goldcoin_get_timer = 240
        
    else:
        
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
                if (MO_PG_ships[i].active): MO_PG_ships[i].draw()

                    
            Window.blit(morskaya_ohota_bordersmap[morskaya_ohota_borders_tick],(-morskaya_ohota_var_pos,0))

            for i in range(16):
                MO_oblakos[i].draw()


            Window.blit(blackscreen,(0,0))
                    
            Window.blit(morskaya_ohota_hit,(morskaya_ohota_hit_pos-morskaya_ohota_var_pos,194))

            Window.blit(morskaya_ohota_ship_shadow[MO_PG_ships[morskaya_ohota_hit_ship].size][not(MO_PG_ships[morskaya_ohota_hit_ship].dir)],(MO_PG_ships[morskaya_ohota_hit_ship].pos_x-morskaya_ohota_var_pos,216))

            morskaya_ohota_hit_tick+=1

            if (morskaya_ohota_hit_tick >= 59):
                morskaya_ohota_hit_bool = False

        else:

            for i in range(10):
                MO_TWs[i].update()
                for j in range(10):
                    if (MO_TWs[i].subtick == 0 and MO_TWs[i].tick == 59 and MO_PG_ships[9-j].active and MO_PG_ships[9-j].hit(MO_TWs[i].pos_x+309)):
                        morskaya_ohota_hit_tick = 0
                        morskaya_ohota_hit_bool = True
                        morskaya_ohota_hit_ship = 9-j
                        morskaya_ohota_hit_pos = MO_TWs[i].pos_x+309
                        MO_PG_ships[9-j].active = False
                        break
                        
                        
            morskaya_ohota_borders_subtick += 1
            if (morskaya_ohota_borders_subtick >= 30):
                morskaya_ohota_borders_subtick = 0
                morskaya_ohota_borders_tick += 1
                if (morskaya_ohota_borders_tick >= 2):
                    morskaya_ohota_borders_tick = 0

            for i in range(10):
                if ((MO_PG_ships[i]).active):
                    MO_PG_ships[i].update()
                    MO_PG_ships[i].draw()

                    
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
    global effect_2_tick, effect_4_tick, coinfalls_tick,blackscreen_timer, prizegame_timer, goldcoin_get_timer, effect_6_tick
    
    Window.fill((0,0,0))

    if (blackscreen_timer > 0):
        blackscreen.set_alpha(255)
        blackscreen_timer -= 1
        Window.blit(blackscreen,(0,0))

    elif (prizegame_timer > 0):
        prizegame_timer -= 1
        if (prizegame_timer >= 60 and prizegame_timer <= 180):
            Window.blit(prizegame[3-prizegame_timer//10%4],(164,168))

    elif (goldcoin_get_timer > 0):
        goldcoin_get_timer -= 1
        if (goldcoin_get_timer >= 60 and goldcoin_get_timer <= 180):
            Window.blit(goldcoin_get,(270,190))
        
    else:
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

                        Window.blit(goldcoin_have,(558,24))
                        GH = str(goldencoins)
                        if (len(GH) == 1):  GH = "0"+GH
                        Window.blit(number_x2_white[int(GH[0])],(502,32))
                        Window.blit(number_x2_white[int(GH[1])],(526,32))

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
                        Window.blit(pamat_banner,(240,368))
                        if (gamemenu_select == 5): Window.blit(pamat_gamename_1,(236,338))
                        else: Window.blit(pamat_gamename_2,(236,338))
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
                    if (coinfalls_tick >= 20 and coinfalls_tick < 100): Window.blit(coinfalls[3-(coinfalls_tick-20)//20],(268,168))
                else:
                    if (morskaya_ohota_game_bool): morskaya_ohota_game_update()
                    elif (morskaya_ohota_prizegame_bool): morskaya_ohota_prizegame_update()
                    
                    if (gonky_game_bool): gonky_game_update()
                    elif (gonky_prizegame_bool): gonky_prizegame_update()

                    if (gonky_II_game_bool): gonky_II_game_update()
                        

                    
            
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

    if (effect_6_tick > 0):
        effect_6_tick -= 1
        if (effect_6_tick == 0):
            Window.blit(blackscreen,(0,0))

    effect_5()
    
Run = True
while Run:

    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: Run = False 
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE): Run = False
            if (loadtick < 420 and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL)):
                loadtick = 419
                mainmenu_bool = True

            if (loadtick >= 420):

                if (blackscreen_timer <= 0 and prizegame_timer <= 0 and goldcoin_get_timer <= 0):
            
                    if (mainmenu_bool):
                        if (event.key == pygame.K_UP or event.key == pygame.K_w):
                            if (mainmenu_select > 1): mainmenu_select -= 1
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                            if (mainmenu_select < 3): mainmenu_select += 1
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
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
                            
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
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
                            
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                                if (gamemenu_select == 0):
                                    gamemenu_bool = False
                                    mainmenu_bool = True
                                    mainmenu_select = 1
                                if (gamemenu_select == 1):
                                    gamemenu_bool = False
                                    game_select = "morskaya_ohota"
                                    mainmenu_select = 0
                                if (gamemenu_select == 2):
                                    gamemenu_bool = False
                                    game_select = "gonky"
                                    mainmenu_select = 0
                                if (gamemenu_select == 3):
                                    gamemenu_bool = False
                                    game_select = "gonky_II"
                                    mainmenu_select = 0                                


                    elif (game_select != "none"):
                        if (event.key == pygame.K_UP or event.key == pygame.K_w):
                            if (game_select_button > 0): game_select_button -= 1
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                            if (game_select_button < 1): game_select_button += 1
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            if (game_select_button == 0):
                                game_select = "none"
                                gamemenu_bool = True
                            if (game_select_button == 1):
                                
                                if (game_select == "morskaya_ohota"):
                                    morskaya_ohota_game_bool = True
                                    morskaya_ohota_var_pos = 640
                                    morskaya_ohota_torpedos_left = 10
                                    morskaya_ohota_time = 120
                                    for i in range(10):
                                        MO_PG_ships[i].clear()
                                        MO_ships[i].clear()
                                        MO_TWs[i].clear()
                                    morskaya_ohota_R_bool = False
                                    morskaya_ohota_L_bool = False

                                if (game_select == "gonky"):
                                    gonky_game_bool = True
                                    gonky_R_bool = False
                                    gonky_L_bool = False
                                    gonky_F_bool = False
                                    gonky_B_bool = False
                                    gonky_time = 120

                                    gonky_viev_pos = 0
                                    gonky_car[0].distract = 0
                                    gonky_car[0].type = "green"
                                    gonky_car[0].control = True
                                    gonky_car[0].pos_x = 340
                                    gonky_car[0].pos_y = -1
                                    gonky_car[0].speed = 5
                                    gonky_car[0].texture = gonky_green_car
                                    gonky_car[0].hitbox.define(0,0,36,64)
                                    gonky_car[0].way = True

                                    for i in range(5):
                                        gonky_car[i+1].control = False
                                        gonky_car[i+1].pos_y = -999
                                        gonky_car[i+1].pos_x = 332+52*i

                                    for i in range(5):
                                        gonky_car[i+6].control = False
                                        gonky_car[i+6].way = False
                                        gonky_car[i+6].pos_y = -999
                                        gonky_car[i+6].pos_x = 64+52*i

                                if (game_select == "gonky_II"):
                                    gonky_II_game_bool = True
                                    
                                game_select = "none"
                                gamemenu_bool = False
                                coinfalls_tick = 120
                                game_select_button = 0
                                

                    elif (morskaya_ohota_game_bool or morskaya_ohota_prizegame_bool):
                        if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): morskaya_ohota_R_bool = True
                        if (event.key == pygame.K_LEFT or event.key == pygame.K_a): morskaya_ohota_L_bool = True
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            if (morskaya_ohota_torpedos_left > 0):
                                morskaya_ohota_torpedos_left -= 1
                                MO_TWs[morskaya_ohota_torpedos_left].spawn(morskaya_ohota_var_pos)
                                
                    elif (gonky_game_bool or gonky_prizegame_bool):
                        if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): gonky_R_bool = True
                        if (event.key == pygame.K_LEFT or event.key == pygame.K_a): gonky_L_bool = True
                        if (event.key == pygame.K_UP or event.key == pygame.K_w): gonky_F_bool = True
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s): gonky_B_bool = True
                    
                    

        if (event.type == pygame.KEYUP):
                if (morskaya_ohota_game_bool or morskaya_ohota_prizegame_bool):
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): morskaya_ohota_R_bool = False
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a): morskaya_ohota_L_bool = False
                elif (gonky_game_bool or gonky_prizegame_bool):
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): gonky_R_bool = False
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a): gonky_L_bool = False
                    if (event.key == pygame.K_UP or event.key == pygame.K_w): gonky_F_bool = False
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s): gonky_B_bool = False
                    
    if (chascecount(0.0025) and effect_4_tick == 0):
        effect_4_tick = 20
        effect_4_pos = randint(0,234)*2

    if (chascecount(0.0003) and effect_6_tick == 0):
        effect_6_tick = randint(12,48)

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
