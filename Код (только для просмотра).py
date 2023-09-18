import pygame
import math
import time
import pathlib
from pathlib import Path
from random import randint
import numpy as np
import sys
import cv2
pygame.init()

directiry = pathlib.Path.cwd()
dir_path = str(directiry)

FPS = 60 

clock = pygame.time.Clock()

fullscreen_bool = True
merzanie_bool = True
effect_2_int = 2
linza_effect = 3
defects_bool = True
retropixel_bool = True
languare = "RUS"
volume_GN = 100
volume_WN = 100
volume_EF = 100
volume_MS = 100

goldencoins = 0

def settings_input():
    global fullscreen_bool, merzanie_bool, effect_2_int, linza_effect, defects_bool, retropixel_bool, languare, volume_GN, volume_WN, volume_EF, volume_MS
    f = open(dir_path+'/data/save/settings.bin','rb')
    while True:
        S = (f.readline()).decode('utf-8')
        if (S == "end"): break
        else:
            V,E,D = S.split()
            if (V == "fullscreen_bool"): fullscreen_bool = bool(int(D))
            if (V == "merzanie_bool"): merzanie_bool = bool(int(D))
            if (V == "effect_2_int"): effect_2_int = (int(D))
            if (V == "linza_effect"): linza_effect = (int(D))
            if (V == "defects_bool"): defects_bool = bool(int(D))
            if (V == "retropixel_bool"): retropixel_bool = bool(int(D))
            if (V == "languare"): languare = (str(D))
            if (V == "volume_GN"): volume_GN = (float(D))
            if (V == "volume_WN"): volume_WN = (float(D))
            if (V == "volume_EF"): volume_EF = (float(D))
            if (V == "volume_MS"): volume_MS = (float(D))

    f.close()

def settings_output():
    global fullscreen_bool, merzanie_bool, effect_2_int, linza_effect, defects_bool, retropixel_bool, languare, volume_GN, volume_WN, volume_EF, volume_MS        
    f = open(dir_path+'/data/save/settings.bin','wb')
    f.write(("fullscreen_bool = "+str(int(fullscreen_bool))+"\n").encode('utf-8'))
    f.write(("merzanie_bool = "+str(int(merzanie_bool))+"\n").encode('utf-8'))
    f.write(("effect_2_int = "+str(int(effect_2_int))+"\n").encode('utf-8'))
    f.write(("linza_effect = "+str(int(linza_effect))+"\n").encode('utf-8'))
    f.write(("defects_bool = "+str(int(defects_bool))+"\n").encode('utf-8'))
    f.write(("retropixel_bool = "+str(int(retropixel_bool))+"\n").encode('utf-8'))
    f.write(("languare = "+str(languare)+"\n").encode('utf-8'))
    f.write(("volume_GN = "+str(volume_GN)+"\n").encode('utf-8'))
    f.write(("volume_WN = "+str(volume_WN)+"\n").encode('utf-8'))
    f.write(("volume_EF = "+str(volume_EF)+"\n").encode('utf-8'))
    f.write(("volume_MS = "+str(volume_MS)+"\n").encode('utf-8'))
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

icon = pygame.image.load(dir_path+"/data/texture/icon.ico").convert()
icon.set_colorkey((0,0,0))
pygame.display.set_icon(icon)

if (fullscreen_bool): pygame .display.toggle_fullscreen()

pygame.mouse.set_visible(False)

def chascecount(x):
    return x >= randint(0,100000)/100000

effect_1 = [0]*3
coinfalls = [0]*4
intro_screen_1_RUS = pygame.image.load(dir_path+'/data/texture/intro_screen_1.png').convert()
intro_screen_1_ENG = pygame.image.load(dir_path+'/data/texture/intro_screen_1_ENG.png').convert()
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
play_button_1_RUS = pygame.image.load(dir_path+'/data/texture/play_button_1.png').convert()
play_button_2_RUS = pygame.image.load(dir_path+'/data/texture/play_button_2.png').convert()
play_button_1_ENG = pygame.image.load(dir_path+'/data/texture/play_button_1_ENG.png').convert()
play_button_2_ENG = pygame.image.load(dir_path+'/data/texture/play_button_2_ENG.png').convert()
settings_button_1_RUS = pygame.image.load(dir_path+'/data/texture/settings_button_1.png').convert()
settings_button_2_RUS = pygame.image.load(dir_path+'/data/texture/settings_button_2.png').convert()
settings_button_1_ENG = pygame.image.load(dir_path+'/data/texture/settings_button_1_ENG.png').convert()
settings_button_2_ENG = pygame.image.load(dir_path+'/data/texture/settings_button_2_ENG.png').convert()
quit_button_1_RUS = pygame.image.load(dir_path+'/data/texture/quit_button_1.png').convert()
quit_button_2_RUS = pygame.image.load(dir_path+'/data/texture/quit_button_2.png').convert()
quit_button_1_ENG = pygame.image.load(dir_path+'/data/texture/quit_button_1_ENG.png').convert()
quit_button_2_ENG = pygame.image.load(dir_path+'/data/texture/quit_button_2_ENG.png').convert()
version_text_RUS = pygame.image.load(dir_path+'/data/texture/version_text.png').convert()
version_text_ENG = pygame.image.load(dir_path+'/data/texture/version_text_ENG.png').convert()
back_button_1_RUS = pygame.image.load(dir_path+'/data/texture/back_button_1.png').convert()
back_button_2_RUS = pygame.image.load(dir_path+'/data/texture/back_button_2.png').convert()
back_button_1_ENG = pygame.image.load(dir_path+'/data/texture/back_button_1_ENG.png').convert()
back_button_2_ENG = pygame.image.load(dir_path+'/data/texture/back_button_2_ENG.png').convert()
coinfalls[0] = pygame.image.load(dir_path+'/data/texture/coinfalls_1.png').convert()
coinfalls[1] = pygame.image.load(dir_path+'/data/texture/coinfalls_2.png').convert()
coinfalls[2] = pygame.image.load(dir_path+'/data/texture/coinfalls_3.png').convert()
coinfalls[3] = pygame.image.load(dir_path+'/data/texture/coinfalls_4.png').convert()

settmenu_fullscreen_1_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_1.png').convert()
settmenu_fullscreen_2_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_2.png').convert()
settmenu_fullscreen_cheak_1_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_cheak_1.png').convert(); settmenu_fullscreen_cheak_1_RUS.set_colorkey((0,0,0))
settmenu_fullscreen_cheak_2_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_cheak_2.png').convert(); settmenu_fullscreen_cheak_2_RUS.set_colorkey((0,0,0))
settmenu_fullscreen_1_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_1_ENG.png').convert()
settmenu_fullscreen_2_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_2_ENG.png').convert()
settmenu_fullscreen_cheak_1_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_cheak_1_ENG.png').convert(); settmenu_fullscreen_cheak_1_ENG.set_colorkey((0,0,0))
settmenu_fullscreen_cheak_2_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_fullscreen_cheak_2_ENG.png').convert(); settmenu_fullscreen_cheak_2_ENG.set_colorkey((0,0,0))

settmenu_grahigs_1_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_grahigs_1.png').convert()
settmenu_grahigs_2_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_grahigs_2.png').convert()
settmenu_grahigs_1_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_grahigs_1_ENG.png').convert()
settmenu_grahigs_2_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_grahigs_2_ENG.png').convert()
settmenu_audio_1_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_audio_1.png').convert()
settmenu_audio_2_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_audio_2.png').convert()
settmenu_audio_1_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_audio_1_ENG.png').convert()
settmenu_audio_2_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_audio_2_ENG.png').convert()
settmenu_languare_1_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_languare_1.png').convert()
settmenu_languare_2_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_languare_2.png').convert()
settmenu_languare_1_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_languare_1_ENG.png').convert()
settmenu_languare_2_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_languare_2_ENG.png').convert()
settmenu_resetprogress_1_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_resetprogress_1.png').convert()
settmenu_resetprogress_2_RUS = pygame.image.load(dir_path+'/data/texture/settmenu_resetprogress_2.png').convert()
settmenu_resetprogress_1_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_resetprogress_1_ENG.png').convert()
settmenu_resetprogress_2_ENG = pygame.image.load(dir_path+'/data/texture/settmenu_resetprogress_2_ENG.png').convert()

settmenu_languare_rus_1 = pygame.image.load(dir_path+'/data/texture/settmenu_languare_rus_1.png').convert()
settmenu_languare_rus_2 = pygame.image.load(dir_path+'/data/texture/settmenu_languare_rus_2.png').convert()
settmenu_languare_eng_1 = pygame.image.load(dir_path+'/data/texture/settmenu_languare_eng_1.png').convert()
settmenu_languare_eng_2 = pygame.image.load(dir_path+'/data/texture/settmenu_languare_eng_2.png').convert()

resetprogress_1_RUS = pygame.image.load(dir_path+'/data/texture/resetprogress_1.png').convert()
resetprogress_2_RUS = pygame.image.load(dir_path+'/data/texture/resetprogress_2.png').convert()
resetprogress_1_ENG = pygame.image.load(dir_path+'/data/texture/resetprogress_1_ENG.png').convert()
resetprogress_2_ENG = pygame.image.load(dir_path+'/data/texture/resetprogress_2_ENG.png').convert()

grafmenu_merzanie_str_RUS = [0]*2
grafmenu_merzanie_str_RUS[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_1.png').convert()
grafmenu_merzanie_str_RUS[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_2.png').convert()
grafmenu_merzanie_RUS = [[0,0],[0,0]]
grafmenu_merzanie_RUS[0][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_off_2.png').convert(); grafmenu_merzanie_RUS[0][0].set_colorkey((0,0,0))
grafmenu_merzanie_RUS[0][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_off_1.png').convert(); grafmenu_merzanie_RUS[0][1].set_colorkey((0,0,0))
grafmenu_merzanie_RUS[1][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_on_2.png').convert(); grafmenu_merzanie_RUS[1][0].set_colorkey((0,0,0))
grafmenu_merzanie_RUS[1][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_on_1.png').convert(); grafmenu_merzanie_RUS[1][1].set_colorkey((0,0,0))

grafmenu_merzanie_str_ENG = [0]*2
grafmenu_merzanie_str_ENG[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_1_ENG.png').convert()
grafmenu_merzanie_str_ENG[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_2_ENG.png').convert()
grafmenu_merzanie_ENG = [[0,0],[0,0]]
grafmenu_merzanie_ENG[0][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_off_2_ENG.png').convert(); grafmenu_merzanie_ENG[0][0].set_colorkey((0,0,0))
grafmenu_merzanie_ENG[0][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_off_1_ENG.png').convert(); grafmenu_merzanie_ENG[0][1].set_colorkey((0,0,0))
grafmenu_merzanie_ENG[1][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_on_2_ENG.png').convert(); grafmenu_merzanie_ENG[1][0].set_colorkey((0,0,0))
grafmenu_merzanie_ENG[1][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_merzanie_on_1_ENG.png').convert(); grafmenu_merzanie_ENG[1][1].set_colorkey((0,0,0))

grafmenu_lostpixel_str_RUS = [0]*2
grafmenu_lostpixel_str_RUS[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel1.png').convert()
grafmenu_lostpixel_str_RUS[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel2.png').convert()
grafmenu_lostpixel_RUS = [[0,0],[0,0],[0,0],[0,0],[0,0]]
grafmenu_lostpixel_RUS[0][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_1_1.png').convert(); grafmenu_lostpixel_RUS[0][1].set_colorkey((0,0,0))
grafmenu_lostpixel_RUS[0][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_1_2.png').convert(); grafmenu_lostpixel_RUS[0][0].set_colorkey((0,0,0))
grafmenu_lostpixel_RUS[1][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_2_1.png').convert(); grafmenu_lostpixel_RUS[1][1].set_colorkey((0,0,0))
grafmenu_lostpixel_RUS[1][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_2_2.png').convert(); grafmenu_lostpixel_RUS[1][0].set_colorkey((0,0,0))
grafmenu_lostpixel_RUS[2][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_3_1.png').convert(); grafmenu_lostpixel_RUS[2][1].set_colorkey((0,0,0))
grafmenu_lostpixel_RUS[2][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_3_2.png').convert(); grafmenu_lostpixel_RUS[2][0].set_colorkey((0,0,0))
grafmenu_lostpixel_RUS[3][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_4_1.png').convert(); grafmenu_lostpixel_RUS[3][1].set_colorkey((0,0,0))
grafmenu_lostpixel_RUS[3][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_4_2.png').convert(); grafmenu_lostpixel_RUS[3][0].set_colorkey((0,0,0))
grafmenu_lostpixel_RUS[4][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_5_1.png').convert(); grafmenu_lostpixel_RUS[4][1].set_colorkey((0,0,0))
grafmenu_lostpixel_RUS[4][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_5_2.png').convert(); grafmenu_lostpixel_RUS[4][0].set_colorkey((0,0,0))

grafmenu_lostpixel_str_ENG = [0]*2
grafmenu_lostpixel_str_ENG[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel1_ENG.png').convert()
grafmenu_lostpixel_str_ENG[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel2_ENG.png').convert()
grafmenu_lostpixel_ENG = [[0,0],[0,0],[0,0],[0,0],[0,0]]
grafmenu_lostpixel_ENG[0][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_1_1_ENG.png').convert(); grafmenu_lostpixel_ENG[0][1].set_colorkey((0,0,0))
grafmenu_lostpixel_ENG[0][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_1_2_ENG.png').convert(); grafmenu_lostpixel_ENG[0][0].set_colorkey((0,0,0))
grafmenu_lostpixel_ENG[1][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_2_1_ENG.png').convert(); grafmenu_lostpixel_ENG[1][1].set_colorkey((0,0,0))
grafmenu_lostpixel_ENG[1][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_2_2_ENG.png').convert(); grafmenu_lostpixel_ENG[1][0].set_colorkey((0,0,0))
grafmenu_lostpixel_ENG[2][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_3_1_ENG.png').convert(); grafmenu_lostpixel_ENG[2][1].set_colorkey((0,0,0))
grafmenu_lostpixel_ENG[2][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_3_2_ENG.png').convert(); grafmenu_lostpixel_ENG[2][0].set_colorkey((0,0,0))
grafmenu_lostpixel_ENG[3][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_4_1_ENG.png').convert(); grafmenu_lostpixel_ENG[3][1].set_colorkey((0,0,0))
grafmenu_lostpixel_ENG[3][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_4_2_ENG.png').convert(); grafmenu_lostpixel_ENG[3][0].set_colorkey((0,0,0))
grafmenu_lostpixel_ENG[4][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_5_1_ENG.png').convert(); grafmenu_lostpixel_ENG[4][1].set_colorkey((0,0,0))
grafmenu_lostpixel_ENG[4][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_lostpixel_var_5_2_ENG.png').convert(); grafmenu_lostpixel_ENG[4][0].set_colorkey((0,0,0))

grafmenu_linza_str_RUS = [0]*2
grafmenu_linza_str_RUS[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza1.png').convert()
grafmenu_linza_str_RUS[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza2.png').convert()
grafmenu_linza_str_ENG = [0]*2
grafmenu_linza_str_ENG[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza1_ENG.png').convert()
grafmenu_linza_str_ENG[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza2_ENG.png').convert()
grafmenu_linza = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
grafmenu_linza[0][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_1_1.png').convert(); grafmenu_linza[0][1].set_colorkey((0,0,0))
grafmenu_linza[0][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_1_2.png').convert(); grafmenu_linza[0][0].set_colorkey((0,0,0))
grafmenu_linza[1][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_2_1.png').convert(); grafmenu_linza[1][1].set_colorkey((0,0,0))
grafmenu_linza[1][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_2_2.png').convert(); grafmenu_linza[1][0].set_colorkey((0,0,0))
grafmenu_linza[2][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_3_1.png').convert(); grafmenu_linza[2][1].set_colorkey((0,0,0))
grafmenu_linza[2][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_3_2.png').convert(); grafmenu_linza[2][0].set_colorkey((0,0,0))
grafmenu_linza[3][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_4_1.png').convert(); grafmenu_linza[3][1].set_colorkey((0,0,0))
grafmenu_linza[3][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_4_2.png').convert(); grafmenu_linza[3][0].set_colorkey((0,0,0))
grafmenu_linza[4][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_5_1.png').convert(); grafmenu_linza[4][1].set_colorkey((0,0,0))
grafmenu_linza[4][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_5_2.png').convert(); grafmenu_linza[4][0].set_colorkey((0,0,0))
grafmenu_linza[5][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_6_1.png').convert(); grafmenu_linza[5][1].set_colorkey((0,0,0))
grafmenu_linza[5][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_6_2.png').convert(); grafmenu_linza[5][0].set_colorkey((0,0,0))
grafmenu_linza[6][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_7_1.png').convert(); grafmenu_linza[6][1].set_colorkey((0,0,0))
grafmenu_linza[6][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_7_2.png').convert(); grafmenu_linza[6][0].set_colorkey((0,0,0))
grafmenu_linza[7][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_8_1.png').convert(); grafmenu_linza[7][1].set_colorkey((0,0,0))
grafmenu_linza[7][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_8_2.png').convert(); grafmenu_linza[7][0].set_colorkey((0,0,0))
grafmenu_linza[8][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_9_1.png').convert(); grafmenu_linza[8][1].set_colorkey((0,0,0))
grafmenu_linza[8][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_9_2.png').convert(); grafmenu_linza[8][0].set_colorkey((0,0,0))
grafmenu_linza[9][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_10_1.png').convert(); grafmenu_linza[9][1].set_colorkey((0,0,0))
grafmenu_linza[9][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_10_2.png').convert(); grafmenu_linza[9][0].set_colorkey((0,0,0))
grafmenu_linza[10][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_11_1.png').convert(); grafmenu_linza[10][1].set_colorkey((0,0,0))
grafmenu_linza[10][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_11_2.png').convert(); grafmenu_linza[10][0].set_colorkey((0,0,0))
grafmenu_linza[11][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_12_1.png').convert(); grafmenu_linza[11][1].set_colorkey((0,0,0))
grafmenu_linza[11][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_12_2.png').convert(); grafmenu_linza[11][0].set_colorkey((0,0,0))
grafmenu_linza[12][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_13_1.png').convert(); grafmenu_linza[12][1].set_colorkey((0,0,0))
grafmenu_linza[12][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_linza_var_13_2.png').convert(); grafmenu_linza[12][0].set_colorkey((0,0,0))

grafmenu_defects_str_RUS = [0]*2
grafmenu_defects_str_RUS[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_1.png').convert()
grafmenu_defects_str_RUS[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_2.png').convert()
grafmenu_defects_RUS = [[0,0],[0,0]]
grafmenu_defects_RUS[0][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_off_1.png').convert(); grafmenu_defects_RUS[0][1].set_colorkey((0,0,0))
grafmenu_defects_RUS[0][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_off_2.png').convert(); grafmenu_defects_RUS[0][0].set_colorkey((0,0,0))
grafmenu_defects_RUS[1][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_on_1.png').convert(); grafmenu_defects_RUS[1][1].set_colorkey((0,0,0))
grafmenu_defects_RUS[1][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_on_2.png').convert(); grafmenu_defects_RUS[1][0].set_colorkey((0,0,0))

grafmenu_defects_str_ENG = [0]*2
grafmenu_defects_str_ENG[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_1_ENG.png').convert()
grafmenu_defects_str_ENG[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_2_ENG.png').convert()
grafmenu_defects_ENG = [[0,0],[0,0]]
grafmenu_defects_ENG[0][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_off_1_ENG.png').convert(); grafmenu_defects_ENG[0][1].set_colorkey((0,0,0))
grafmenu_defects_ENG[0][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_off_2_ENG.png').convert(); grafmenu_defects_ENG[0][0].set_colorkey((0,0,0))
grafmenu_defects_ENG[1][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_on_1_ENG.png').convert(); grafmenu_defects_ENG[1][1].set_colorkey((0,0,0))
grafmenu_defects_ENG[1][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_defects_on_2_ENG.png').convert(); grafmenu_defects_ENG[1][0].set_colorkey((0,0,0))

grafmenu_retropixel_str_RUS = [0]*2
grafmenu_retropixel_str_RUS[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_1.png').convert()
grafmenu_retropixel_str_RUS[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_2.png').convert()
grafmenu_retropixel_RUS = [[0,0],[0,0]]
grafmenu_retropixel_RUS[0][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_off_1.png').convert(); grafmenu_retropixel_RUS[0][1].set_colorkey((0,0,0))
grafmenu_retropixel_RUS[0][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_off_2.png').convert(); grafmenu_retropixel_RUS[0][0].set_colorkey((0,0,0))
grafmenu_retropixel_RUS[1][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_on_1.png').convert(); grafmenu_retropixel_RUS[1][1].set_colorkey((0,0,0))
grafmenu_retropixel_RUS[1][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_on_2.png').convert(); grafmenu_retropixel_RUS[1][0].set_colorkey((0,0,0))

grafmenu_retropixel_str_ENG = [0]*2
grafmenu_retropixel_str_ENG[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_1_ENG.png').convert()
grafmenu_retropixel_str_ENG[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_2_ENG.png').convert()
grafmenu_retropixel_ENG = [[0,0],[0,0]]
grafmenu_retropixel_ENG[0][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_off_1_ENG.png').convert(); grafmenu_retropixel_ENG[0][1].set_colorkey((0,0,0))
grafmenu_retropixel_ENG[0][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_off_2_ENG.png').convert(); grafmenu_retropixel_ENG[0][0].set_colorkey((0,0,0))
grafmenu_retropixel_ENG[1][1] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_on_1_ENG.png').convert(); grafmenu_retropixel_ENG[1][1].set_colorkey((0,0,0))
grafmenu_retropixel_ENG[1][0] = pygame.image.load(dir_path+'/data/texture/grafmenu_retropixel_on_2_ENG.png').convert(); grafmenu_retropixel_ENG[1][0].set_colorkey((0,0,0))

grafmenu_setdefents_RUS = [0]*2
grafmenu_setdefents_RUS[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_setdefents_1.png').convert()
grafmenu_setdefents_RUS[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_setdefents_2.png').convert()
grafmenu_setdefents_ENG = [0]*2
grafmenu_setdefents_ENG[1] = pygame.image.load(dir_path+'/data/texture/grafmenu_setdefents_1_ENG.png').convert()
grafmenu_setdefents_ENG[0] = pygame.image.load(dir_path+'/data/texture/grafmenu_setdefents_2_ENG.png').convert()

volumenu_effects_1_RUS = pygame.image.load(dir_path+'/data/texture/volumenu_effects_1.png').convert()
volumenu_effects_2_RUS = pygame.image.load(dir_path+'/data/texture/volumenu_effects_2.png').convert()
volumenu_general_1_RUS = pygame.image.load(dir_path+'/data/texture/volumenu_general_1.png').convert()
volumenu_general_2_RUS = pygame.image.load(dir_path+'/data/texture/volumenu_general_2.png').convert()
volumenu_music_1_RUS = pygame.image.load(dir_path+'/data/texture/volumenu_music_1.png').convert()
volumenu_music_2_RUS = pygame.image.load(dir_path+'/data/texture/volumenu_music_2.png').convert()
volumenu_white_noise_1_RUS = pygame.image.load(dir_path+'/data/texture/volumenu_white_noise_1.png').convert()
volumenu_white_noise_2_RUS = pygame.image.load(dir_path+'/data/texture/volumenu_white_noise_2.png').convert()

volumenu_effects_1_ENG = pygame.image.load(dir_path+'/data/texture/volumenu_effects_1_ENG.png').convert()
volumenu_effects_2_ENG = pygame.image.load(dir_path+'/data/texture/volumenu_effects_2_ENG.png').convert()
volumenu_general_1_ENG = pygame.image.load(dir_path+'/data/texture/volumenu_general_1_ENG.png').convert()
volumenu_general_2_ENG = pygame.image.load(dir_path+'/data/texture/volumenu_general_2_ENG.png').convert()
volumenu_music_1_ENG = pygame.image.load(dir_path+'/data/texture/volumenu_music_1_ENG.png').convert()
volumenu_music_2_ENG = pygame.image.load(dir_path+'/data/texture/volumenu_music_2_ENG.png').convert()
volumenu_white_noise_1_ENG = pygame.image.load(dir_path+'/data/texture/volumenu_white_noise_1_ENG.png').convert()
volumenu_white_noise_2_ENG = pygame.image.load(dir_path+'/data/texture/volumenu_white_noise_2_ENG.png').convert()

volume_pr_S = [0]*21
volume_pr_U = [0]*21
for i in range (21):
    volume_pr_S[i] = pygame.image.load(dir_path+'/data/texture/volume_pr_S_'+str(i+1)+'.png').convert()
    volume_pr_U[i] = pygame.image.load(dir_path+'/data/texture/volume_pr_U_'+str(i+1)+'.png').convert()

safari_piramid = pygame.image.load(dir_path+'/data/texture/safari_piramid.png').convert(); safari_piramid.set_colorkey((255,255,255))

comingsoon_banner_RUS = pygame.image.load(dir_path+'/data/texture/comingsoon_banner.png').convert()
comingsoon_banner_ENG = pygame.image.load(dir_path+'/data/texture/comingsoon_banner_ENG.png').convert()
morskaya_ohota_banner = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_banner.png').convert()
gonky_banner = pygame.image.load(dir_path+'/data/texture/gonky_banner.png').convert()
gonky_II_banner = pygame.image.load(dir_path+'/data/texture/gonky_II_banner.png').convert()
safary_banner = pygame.image.load(dir_path+'/data/texture/safary_banner.png').convert()
ralli_banner = pygame.image.load(dir_path+'/data/texture/ralli_banner.png').convert()
select_game = pygame.image.load(dir_path+'/data/texture/select_game.png').convert(); select_game.set_colorkey((0,0,0))

comingsoon_gamename_1_RUS = pygame.image.load(dir_path+'/data/texture/comingsoon_gamename_1.png').convert()
comingsoon_gamename_2_RUS = pygame.image.load(dir_path+'/data/texture/comingsoon_gamename_2.png').convert()
comingsoon_gamename_1_ENG = pygame.image.load(dir_path+'/data/texture/comingsoon_gamename_1_ENG.png').convert()
comingsoon_gamename_2_ENG = pygame.image.load(dir_path+'/data/texture/comingsoon_gamename_2_ENG.png').convert()
morskaya_ohota_gamename_1_RUS = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_gamename_1.png').convert()
morskaya_ohota_gamename_2_RUS = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_gamename_2.png').convert()
morskaya_ohota_gamename_1_ENG = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_gamename_1_ENG.png').convert()
morskaya_ohota_gamename_2_ENG = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_gamename_2_ENG.png').convert()
gonky_gamename_1_RUS = pygame.image.load(dir_path+'/data/texture/gonky_gamename_1.png').convert()
gonky_gamename_2_RUS = pygame.image.load(dir_path+'/data/texture/gonky_gamename_2.png').convert()
gonky_gamename_1_ENG = pygame.image.load(dir_path+'/data/texture/gonky_gamename_1_ENG.png').convert()
gonky_gamename_2_ENG = pygame.image.load(dir_path+'/data/texture/gonky_gamename_2_ENG.png').convert()
gonky_II_gamename_1 = pygame.image.load(dir_path+'/data/texture/gonky_II_gamename_1.png').convert()
gonky_II_gamename_2 = pygame.image.load(dir_path+'/data/texture/gonky_II_gamename_2.png').convert()
safary_gamename_1_RUS = pygame.image.load(dir_path+'/data/texture/safary_gamename_1.png').convert()
safary_gamename_2_RUS = pygame.image.load(dir_path+'/data/texture/safary_gamename_2.png').convert()
safary_gamename_1_ENG = pygame.image.load(dir_path+'/data/texture/safary_gamename_1_ENG.png').convert()
safary_gamename_2_ENG = pygame.image.load(dir_path+'/data/texture/safary_gamename_2_ENG.png').convert()
ralli_gamename_1_RUS = pygame.image.load(dir_path+'/data/texture/ralli_gamename_1.png').convert()
ralli_gamename_2_RUS = pygame.image.load(dir_path+'/data/texture/ralli_gamename_2.png').convert()
ralli_gamename_1_ENG = pygame.image.load(dir_path+'/data/texture/ralli_gamename_1_ENG.png').convert()
ralli_gamename_2_ENG = pygame.image.load(dir_path+'/data/texture/ralli_gamename_2_ENG.png').convert()

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

prizegame_RUS = [0]*4
prizegame_RUS[0] = pygame.image.load(dir_path+'/data/texture/prizegame_1.png').convert(); prizegame_RUS[0].set_colorkey((0,0,0))
prizegame_RUS[1] = pygame.image.load(dir_path+'/data/texture/prizegame_2.png').convert(); prizegame_RUS[1].set_colorkey((0,0,0))
prizegame_RUS[2] = pygame.image.load(dir_path+'/data/texture/prizegame_3.png').convert(); prizegame_RUS[2].set_colorkey((0,0,0))
prizegame_RUS[3] = pygame.image.load(dir_path+'/data/texture/prizegame_4.png').convert(); prizegame_RUS[3].set_colorkey((0,0,0))
prizegame_ENG = [0]*4
prizegame_ENG[0] = pygame.image.load(dir_path+'/data/texture/prizegame_1_ENG.png').convert(); prizegame_ENG[0].set_colorkey((0,0,0))
prizegame_ENG[1] = pygame.image.load(dir_path+'/data/texture/prizegame_2_ENG.png').convert(); prizegame_ENG[1].set_colorkey((0,0,0))
prizegame_ENG[2] = pygame.image.load(dir_path+'/data/texture/prizegame_3_ENG.png').convert(); prizegame_ENG[2].set_colorkey((0,0,0))
prizegame_ENG[3] = pygame.image.load(dir_path+'/data/texture/prizegame_4_ENG.png').convert(); prizegame_ENG[3].set_colorkey((0,0,0))

morskaya_ohota_torpedo_way = [0]*60
for i in range(60):
    morskaya_ohota_torpedo_way[i] = pygame.image.load(dir_path+'/data/texture/morskaya_ohota_torpedo_way_'+str(i+1)+'.png').convert()
    morskaya_ohota_torpedo_way[i].set_colorkey((255,0,0))

goldcoin_get = pygame.image.load(dir_path+'/data/texture/goldcoin_get.png').convert(); goldcoin_get.set_colorkey((0,0,0))

wins_player1 = pygame.image.load(dir_path+'/data/texture/wins_player1.png').convert(); wins_player1.set_colorkey((0,0,0))
wins_player2 = pygame.image.load(dir_path+'/data/texture/wins_player2.png').convert(); wins_player2.set_colorkey((0,0,0))

p2p_button_1_RUS = pygame.image.load(dir_path+'/data/texture/2p_button_1.png').convert();
p2p_button_2_RUS = pygame.image.load(dir_path+'/data/texture/2p_button_2.png').convert();
p2p_button_1_ENG = pygame.image.load(dir_path+'/data/texture/2p_button_1_ENG.png').convert();
p2p_button_2_ENG = pygame.image.load(dir_path+'/data/texture/2p_button_2_ENG.png').convert();

gonky_roadsegment = pygame.image.load(dir_path+'/data/texture/gonky_roadsegment.png').convert()
gonky_info_finish = pygame.image.load(dir_path+'/data/texture/gonky_info_finish.png').convert()
gonky_info_player_1_go = pygame.image.load(dir_path+'/data/texture/gonky_info_player_1_go.png').convert()
gonky_info_player_2_go = pygame.image.load(dir_path+'/data/texture/gonky_info_player_2_go.png').convert()
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
pamat_gamename_1_RUS = pygame.image.load(dir_path+'/data/texture/pamat_gamename_1.png').convert()
pamat_gamename_2_RUS = pygame.image.load(dir_path+'/data/texture/pamat_gamename_2.png').convert()
pamat_gamename_1_ENG = pygame.image.load(dir_path+'/data/texture/pamat_gamename_1_ENG.png').convert()
pamat_gamename_2_ENG = pygame.image.load(dir_path+'/data/texture/pamat_gamename_2_ENG.png').convert()
pamat_base = pygame.image.load(dir_path+'/data/texture/pamat_base.png').convert()
pamat_ans_b_d = [0]*4
pamat_ans_f_d = [0]*4
pamat_ans_b_l = [0]*4
pamat_ask_1 = [0]*4
pamat_ask_2 = [0]*4
pamat_ask_3 = [0]*4
pamat_vrema = [0]*4
for i in range(4):
    pamat_ans_b_d[i] = pygame.image.load(dir_path+'/data/texture/pamat_ans_b_d_'+str(i+1)+'.png').convert(); pamat_ans_b_d[i].set_colorkey((0,0,0))
    pamat_ans_f_d[i] = pygame.image.load(dir_path+'/data/texture/pamat_ans_f_d_'+str(i+1)+'.png').convert(); pamat_ans_f_d[i].set_colorkey((0,0,0))
    pamat_ans_b_l[i] = pygame.image.load(dir_path+'/data/texture/pamat_ans_b_l_'+str(i+1)+'.png').convert(); pamat_ans_b_l[i].set_colorkey((0,0,0))

    pamat_ask_1[i] = pygame.image.load(dir_path+'/data/texture/pamat_ask_1_'+str(i+1)+'.png').convert(); pamat_ask_1[i].set_colorkey((0,0,0))
    pamat_ask_2[i] = pygame.image.load(dir_path+'/data/texture/pamat_ask_2_'+str(i+1)+'.png').convert(); pamat_ask_2[i].set_colorkey((0,0,0))
    pamat_ask_3[i] = pygame.image.load(dir_path+'/data/texture/pamat_ask_3_'+str(i+1)+'.png').convert(); pamat_ask_3[i].set_colorkey((0,0,0))
    pamat_vrema[i] = pygame.image.load(dir_path+'/data/texture/pamat_vrema_'+str(i+1)+'.png').convert();

pamat_wrong = pygame.image.load(dir_path+'/data/texture/pamat_wrong.png').convert()
pamat_right = pygame.image.load(dir_path+'/data/texture/pamat_right.png').convert()
pamat_ans_l = pygame.image.load(dir_path+'/data/texture/pamat_ans_l.png').convert(); pamat_ans_l.set_colorkey((0,0,0))
pamat_choise = pygame.image.load(dir_path+'/data/texture/pamat_choise.png').convert(); pamat_choise.set_colorkey((0,0,0))

gonky_II_roadsegment = pygame.image.load(dir_path+'/data/texture/gonky_II_roadsegment.png').convert()
gonky_II_info_finish = pygame.image.load(dir_path+'/data/texture/gonky_II_info_finish.png').convert()

safari_map = pygame.image.load(dir_path+'/data/texture/safari_map.png').convert()
safari_shots_base = pygame.image.load(dir_path+'/data/texture/safari_shots_base.png').convert(); safari_shots_base.set_colorkey((0,0,0))
safari_shots_unysed = pygame.image.load(dir_path+'/data/texture/safari_shots_unysed.png').convert(); safari_shots_unysed.set_colorkey((0,0,0))
safari_palma = [0]*4
for i in range(4): safari_palma[i] = pygame.image.load(dir_path+'/data/texture/safari_palma_'+str(i+1)+'.png').convert(); safari_palma[i].set_colorkey((255,255,255))
safari_bullet = pygame.image.load(dir_path+'/data/texture/safari_bullet.png').convert(); safari_bullet.set_colorkey((255,255,255))
safari_player = [0]*4
for i in range(4): safari_player[i] = pygame.image.load(dir_path+'/data/texture/safari_player_'+str(i+1)+'.png').convert(); safari_player[i].set_colorkey((255,255,255))
safari_palma = [0]*4
for i in range(4): safari_palma[i] = pygame.image.load(dir_path+'/data/texture/safari_palma_'+str(i+1)+'.png').convert(); safari_palma[i].set_colorkey((255,255,255))
safari_nosorog = [0]*4
for i in range(4): safari_nosorog[i] = pygame.image.load(dir_path+'/data/texture/safari_nosorog_'+str(i+1)+'.png').convert(); safari_nosorog[i].set_colorkey((255,0,0))
safari_zebra = [0]*4
for i in range(4): safari_zebra[i] = pygame.image.load(dir_path+'/data/texture/safari_zebra_'+str(i+1)+'.png').convert(); safari_zebra[i].set_colorkey((255,0,0))
safari_kaban = [0]*4
for i in range(4): safari_kaban[i] = pygame.image.load(dir_path+'/data/texture/safari_kaban_'+str(i+1)+'.png').convert(); safari_kaban[i].set_colorkey((255,0,0))
safari_animals_cathc = pygame.image.load(dir_path+'/data/texture/safari_animals_cathc.png').convert(); safari_animals_cathc.set_colorkey((0,0,0))
safari_oblako = [0]*3
for i in range(3): safari_oblako[i] = pygame.image.load(dir_path+'/data/texture/safari_oblako_'+str(i+1)+'.png').convert(); safari_oblako[i].set_colorkey((0,0,0))

ralli_map = pygame.image.load(dir_path+'/data/texture/ralli_map.png').convert();
ralli_car = pygame.image.load(dir_path+'/data/texture/ralli_car.png').convert();
ralli_car_2 = pygame.image.load(dir_path+'/data/texture/ralli_car_2.png').convert();
ralli_segm_road = [0]*7
for i in range(7): ralli_segm_road[i] = pygame.image.load(dir_path+'/data/texture/ralli_segm_road_'+str(i+1)+'.png').convert();
ralli_segm_stantion_1 = pygame.image.load(dir_path+'/data/texture/ralli_segm_stantion_1.png').convert();
ralli_segm_stantion_2 = pygame.image.load(dir_path+'/data/texture/ralli_segm_stantion_2.png').convert();

ralli_segm_house = []
for i in range(4):
    ralli_segm_house.append([0]*4)

for i in range(4):
    for j in range(4):
        ralli_segm_house[i][j] = pygame.image.load(dir_path+'/data/texture/ralli_segm_house_'+str(i+1)+'_'+str(j+1)+'.png').convert(); ralli_segm_house[i][j].set_colorkey((0,0,0))


ralli_segm_flag_R = []
for i in range(3):
    ralli_segm_flag_R.append([0]*4)

ralli_segm_flag_G = []
for i in range(3):
    ralli_segm_flag_G.append([0]*4)

for i in range(3):
    for j in range(4):
        ralli_segm_flag_R[i][j] = pygame.image.load(dir_path+'/data/texture/ralli_flag_R_'+str(i+1)+'_'+str(j+1)+'.png').convert(); ralli_segm_flag_R[i][j].set_colorkey((0,0,0))
        ralli_segm_flag_G[i][j] = pygame.image.load(dir_path+'/data/texture/ralli_flag_G_'+str(i+1)+'_'+str(j+1)+'.png').convert(); ralli_segm_flag_G[i][j].set_colorkey((0,0,0))

ralli_segm_flag_base = pygame.image.load(dir_path+'/data/texture/ralli_segm_flag_base.png').convert(); ralli_segm_flag_base.set_colorkey((0,0,0))
ralli_board_time = pygame.image.load(dir_path+'/data/texture/ralli_board_time.png').convert();
ralli_board_points = pygame.image.load(dir_path+'/data/texture/ralli_board_points.png').convert();
ralli_green_num = [0]*10
for i in range(10): ralli_green_num[i] = pygame.image.load(dir_path+'/data/texture/ralli_green_num_'+str(i+1)+'.png').convert(); ralli_green_num[i].set_colorkey((0,0,0))
ralli_blue_num = [0]*10
for i in range(10): ralli_blue_num[i] = pygame.image.load(dir_path+'/data/texture/ralli_blue_num_'+str(i+1)+'.png').convert(); ralli_blue_num[i].set_colorkey((0,0,0))

text=[]
for i in range(77):
    text.append([0]*2)

for i in range(77):
    text[i][0] = pygame.image.load(dir_path+'/data/texture/text/grey/LT'+str(i+1)+'.png').convert(); (text[i][0]).set_colorkey((0,0,0))
    text[i][1] = pygame.image.load(dir_path+'/data/texture/text/white/LT'+str(i+1)+'.png').convert(); (text[i][1]).set_colorkey((0,0,0))



menu_button_click = pygame.mixer.Sound(dir_path+'/data/audio/menu_button_click.mp3')
intro_sound = pygame.mixer.Sound(dir_path+'/data/audio/intro_sound.mp3')
game_start = pygame.mixer.Sound(dir_path+'/data/audio/game_start.mp3')
white_noise = pygame.mixer.Sound(dir_path+'/data/audio/white_noise.mp3')
expl = pygame.mixer.Sound(dir_path+'/data/audio/expl.mp3')
missed = pygame.mixer.Sound(dir_path+'/data/audio/missed.mp3')
prizegame_sound = pygame.mixer.Sound(dir_path+'/data/audio/prizegame.mp3')
hit = pygame.mixer.Sound(dir_path+'/data/audio/hit.mp3')
win = pygame.mixer.Sound(dir_path+'/data/audio/win.mp3')
crash = pygame.mixer.Sound(dir_path+'/data/audio/crash.mp3')
jump = pygame.mixer.Sound(dir_path+'/data/audio/jump.mp3')
wrong = pygame.mixer.Sound(dir_path+'/data/audio/wrong.mp3')

def languare_choise(lang):
    global intro_screen_1, play_button_1, play_button_2, settings_button_1, settings_button_2, quit_button_1, quit_button_2, back_button_1, back_button_2, p2p_button_1, p2p_button_2
    global version_text, comingsoon_banner, morskaya_ohota_gamename_1, morskaya_ohota_gamename_2, pamat_gamename_1, pamat_gamename_2, comingsoon_gamename_1, comingsoon_gamename_2
    global gonky_gamename_1, gonky_gamename_2, safary_gamename_1, safary_gamename_2, ralli_gamename_1, ralli_gamename_2, settmenu_fullscreen_1, settmenu_fullscreen_2, prizegame
    global settmenu_fullscreen_cheak_1, settmenu_fullscreen_cheak_2, settmenu_grahigs_1, settmenu_grahigs_2, settmenu_audio_1, settmenu_audio_2, grafmenu_lostpixel_str, grafmenu_lostpixel
    global settmenu_languare_1, settmenu_languare_2, settmenu_resetprogress_1, settmenu_resetprogress_2, grafmenu_defects_str, grafmenu_defects, grafmenu_linza_str, volumenu_effects_1
    global grafmenu_retropixel_str, grafmenu_retropixel, grafmenu_merzanie_str, grafmenu_merzanie, grafmenu_setdefents, volumenu_effects_2, volumenu_general_1, volumenu_general_2
    global volumenu_music_1, volumenu_music_2, volumenu_white_noise_1, volumenu_white_noise_2, resetprogress_1, resetprogress_2
    
    if (lang == "RUS"):
        intro_screen_1 = intro_screen_1_RUS
        play_button_1 = play_button_1_RUS
        play_button_2 = play_button_2_RUS
        settings_button_1 = settings_button_1_RUS
        settings_button_2 = settings_button_2_RUS
        quit_button_1 = quit_button_1_RUS
        quit_button_2 = quit_button_2_RUS
        back_button_1 = back_button_1_RUS
        back_button_2 = back_button_2_RUS
        p2p_button_1 = p2p_button_1_RUS
        p2p_button_2 = p2p_button_2_RUS
        version_text = version_text_RUS
        comingsoon_banner = comingsoon_banner_RUS
        morskaya_ohota_gamename_1 = morskaya_ohota_gamename_1_RUS
        morskaya_ohota_gamename_2 = morskaya_ohota_gamename_2_RUS
        pamat_gamename_1 = pamat_gamename_1_RUS
        pamat_gamename_2 = pamat_gamename_2_RUS
        comingsoon_gamename_1 = comingsoon_gamename_1_RUS
        comingsoon_gamename_2 = comingsoon_gamename_2_RUS
        gonky_gamename_1 = gonky_gamename_1_RUS
        gonky_gamename_2 = gonky_gamename_2_RUS
        safary_gamename_1 = safary_gamename_1_RUS
        safary_gamename_2 = safary_gamename_2_RUS
        ralli_gamename_1 = ralli_gamename_1_RUS
        ralli_gamename_2 = ralli_gamename_2_RUS
        settmenu_fullscreen_1 = settmenu_fullscreen_1_RUS
        settmenu_fullscreen_2 = settmenu_fullscreen_2_RUS
        settmenu_fullscreen_cheak_1 = settmenu_fullscreen_cheak_1_RUS
        settmenu_fullscreen_cheak_2 = settmenu_fullscreen_cheak_2_RUS
        settmenu_grahigs_1 = settmenu_grahigs_1_RUS
        settmenu_grahigs_2 = settmenu_grahigs_2_RUS
        settmenu_audio_1 = settmenu_audio_1_RUS
        settmenu_audio_2 = settmenu_audio_2_RUS
        settmenu_languare_1 = settmenu_languare_1_RUS
        settmenu_languare_2 = settmenu_languare_2_RUS
        settmenu_resetprogress_1 = settmenu_resetprogress_1_RUS
        settmenu_resetprogress_2 = settmenu_resetprogress_2_RUS
        prizegame = prizegame_RUS
        grafmenu_lostpixel_str = grafmenu_lostpixel_str_RUS
        grafmenu_lostpixel = grafmenu_lostpixel_RUS
        grafmenu_defects_str = grafmenu_defects_str_RUS
        grafmenu_defects = grafmenu_defects_RUS
        grafmenu_linza_str = grafmenu_linza_str_RUS
        grafmenu_retropixel_str = grafmenu_retropixel_str_RUS
        grafmenu_retropixel = grafmenu_retropixel_RUS
        grafmenu_merzanie_str = grafmenu_merzanie_str_RUS
        grafmenu_merzanie = grafmenu_merzanie_RUS
        grafmenu_setdefents = grafmenu_setdefents_RUS
        volumenu_effects_1 = volumenu_effects_1_RUS
        volumenu_effects_2 = volumenu_effects_2_RUS
        volumenu_general_1 = volumenu_general_1_RUS
        volumenu_general_2 = volumenu_general_2_RUS
        volumenu_music_1 = volumenu_music_1_RUS
        volumenu_music_2 = volumenu_music_2_RUS
        volumenu_white_noise_1 = volumenu_white_noise_1_RUS
        volumenu_white_noise_2 = volumenu_white_noise_2_RUS
        resetprogress_1 = resetprogress_1_RUS
        resetprogress_2 = resetprogress_2_RUS
        
    if (lang == "ENG"):
        intro_screen_1 = intro_screen_1_ENG
        play_button_1 = play_button_1_ENG
        play_button_2 = play_button_2_ENG
        settings_button_1 = settings_button_1_ENG
        settings_button_2 = settings_button_2_ENG
        quit_button_1 = quit_button_1_ENG
        quit_button_2 = quit_button_2_ENG
        back_button_1 = back_button_1_ENG
        back_button_2 = back_button_2_ENG  
        p2p_button_1 = p2p_button_1_ENG
        p2p_button_2 = p2p_button_2_ENG
        version_text = version_text_ENG
        comingsoon_banner = comingsoon_banner_ENG
        morskaya_ohota_gamename_1 = morskaya_ohota_gamename_1_ENG
        morskaya_ohota_gamename_2 = morskaya_ohota_gamename_2_ENG
        pamat_gamename_1 = pamat_gamename_1_ENG
        pamat_gamename_2 = pamat_gamename_2_ENG
        comingsoon_gamename_1 = comingsoon_gamename_1_ENG
        comingsoon_gamename_2 = comingsoon_gamename_2_ENG
        gonky_gamename_1 = gonky_gamename_1_ENG
        gonky_gamename_2 = gonky_gamename_2_ENG
        safary_gamename_1 = safary_gamename_1_ENG
        safary_gamename_2 = safary_gamename_2_ENG
        ralli_gamename_1 = ralli_gamename_1_ENG
        ralli_gamename_2 = ralli_gamename_2_ENG
        settmenu_fullscreen_1 = settmenu_fullscreen_1_ENG
        settmenu_fullscreen_2 = settmenu_fullscreen_2_ENG
        settmenu_fullscreen_cheak_1 = settmenu_fullscreen_cheak_1_ENG
        settmenu_fullscreen_cheak_2 = settmenu_fullscreen_cheak_2_ENG
        settmenu_grahigs_1 = settmenu_grahigs_1_ENG
        settmenu_grahigs_2 = settmenu_grahigs_2_ENG
        settmenu_audio_1 = settmenu_audio_1_ENG
        settmenu_audio_2 = settmenu_audio_2_ENG
        settmenu_languare_1 = settmenu_languare_1_ENG
        settmenu_languare_2 = settmenu_languare_2_ENG
        settmenu_resetprogress_1 = settmenu_resetprogress_1_ENG
        settmenu_resetprogress_2 = settmenu_resetprogress_2_ENG
        prizegame = prizegame_ENG
        grafmenu_lostpixel_str = grafmenu_lostpixel_str_ENG
        grafmenu_lostpixel = grafmenu_lostpixel_ENG
        grafmenu_defects_str = grafmenu_defects_str_ENG
        grafmenu_defects = grafmenu_defects_ENG
        grafmenu_linza_str = grafmenu_linza_str_ENG
        grafmenu_retropixel_str = grafmenu_retropixel_str_ENG
        grafmenu_retropixel = grafmenu_retropixel_ENG
        grafmenu_merzanie_str = grafmenu_merzanie_str_ENG
        grafmenu_merzanie = grafmenu_merzanie_ENG
        grafmenu_setdefents = grafmenu_setdefents_ENG
        volumenu_effects_1 = volumenu_effects_1_ENG
        volumenu_effects_2 = volumenu_effects_2_ENG
        volumenu_general_1 = volumenu_general_1_ENG
        volumenu_general_2 = volumenu_general_2_ENG
        volumenu_music_1 = volumenu_music_1_ENG
        volumenu_music_2 = volumenu_music_2_ENG
        volumenu_white_noise_1 = volumenu_white_noise_1_ENG
        volumenu_white_noise_2 = volumenu_white_noise_2_ENG
        resetprogress_1 = resetprogress_1_ENG
        resetprogress_2 = resetprogress_2_ENG
        
def volume_choise(GN,WN,EF,MS):
    global white_noise, intro_sound, game_start, menu_button_click, expl, missed, prizegame_sound, hit, win, crash, jump, wrong

    GN = GN/100.0
    WN = WN/100.0 * GN
    EF = EF/100.0 * GN
    MS = MS/100.0 * GN
    
    white_noise.set_volume(WN)
    
    intro_sound.set_volume(EF)
    game_start.set_volume(EF)
    menu_button_click.set_volume(EF)
    expl.set_volume(EF)
    missed.set_volume(EF)
    prizegame_sound.set_volume(EF)
    hit.set_volume(EF)
    win.set_volume(EF)
    crash.set_volume(EF)
    jump.set_volume(EF)
    wrong.set_volume(EF)
        
languare_choise(languare)
volume_choise(volume_GN,volume_WN,volume_EF,volume_MS)

loadtick = 0
mainmenu_tick = 0
mainmenu_subtick = 0
effect_2_tick = 0
mainmenu_select = 1
mainmenu_bool = False
gamemenu_bool = False
gamemenu_select = 0
gamemenu_razdel = 0
settmenu_bool = False
settmenu_select = 0
grafmenu_bool = False
grafmenu_select = 0
audimenu_bool = False
audimenu_select = 0
langmenu_bool = False
langmenu_select = 0
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
gonky_II_R1_bool = False
gonky_II_L1_bool = False
gonky_II_F1_bool = False
gonky_II_B1_bool = False
gonky_II_R2_bool = False
gonky_II_L2_bool = False
gonky_II_F2_bool = False
gonky_II_B2_bool = False
gonky_II_timer = 0
gonky_II_subtime = 0
wins_player1_tick = 0
wins_player2_tick = 0
safari_game_bool = False
safari_prizegame_bool = False
safari_player_tick = 0
safari_player_subtick = 0
safari_shots_left = 0
safari_timer = 0
safari_subtimer = 0
safari_jump_tick = 0
safari_jump_tick_pos = 0
safari_zebra_lives = 2
safari_kaban_lives = 4
safari_kaban_ct_count = 0
safari_zebra_ct_count = 0
safari_nosorog_ct_count = 0
pamat_game_bool = False
pamat_ask = ""
pamat_right_ans = (0,0)
pamat_pos = (0,0)
pamat_wrong_tick = 0
pamat_right_tick = 0
pamat_vrema_timer = 0
pamat_timer = 0
pamat_subtimer = 0
pamat_correct = 0
pamat_incorrect = 0
pamat_prizegame_bool = False
pamat_fake_roll = 0
ralli_game_bool = False
ralli_prizegame_bool = False
ralli_f = False
ralli_b = False
ralli_l = False
ralli_r = False
ralli_nontex = pygame.Surface((22,22)); ralli_nontex.set_colorkey((0,0,0))
ralli_subtimer = 0
ralli_timer = 0
ralli_target_x, ralli_target_y = -1, -1
ralli_flags_pos = [0]*9
ralli_points = 0
ralli_points2 = 0
ralli_start_pos = (0,0)
ralli_II_game_bool = False
ralli_p1_start_pos, ralli_p2_start_pos = (0,0),(0,0)
ralli_II_1_f = False
ralli_II_1_b = False
ralli_II_1_l = False
ralli_II_1_r = False
ralli_II_2_f = False
ralli_II_2_b = False
ralli_II_2_l = False
ralli_II_2_r = False
ralli_is_crash = False
ralli_is_crash_II = False
resetprogress_bool = False
resetprogress_select = 0

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

palitra = [[(  0,  0,  0),(  0,  0,  0),(  0,  0,  0)],
           [(  0,  0,255),(  0,  0,191),(  0,  0,127)],
           [(255,255,255),(191,191,191),(127,127,127)],
           [(  0,255,  0),(  0,191,  0),(  0,127,  0)],
           [(127, 63,  0),( 95, 47,  0),( 63, 31,  0)],
           [(127,127,127),( 95, 95, 95),( 63, 63, 63)],
           [(  0,255,255),(  0,191,191),(  0,127,127)],
           [(  0,  0,127),(  0,  0, 95),(  0,  0, 63)],
           [(255,127,  0),(191, 95,  0),(127, 63,  0)],
           [(255,  0,  0),(191,  0,  0),(127,  0,  0)],
           [(127,  0,  0),( 95,  0,  0),( 63,  0,  0)],
           [(  0,127,  0),(  0, 95,  0),(  0,  0, 63)],
           [(255,255,  0),(191,191,  0),(127,127,  0)],
           [(191,191,191),(127,127,127),( 95, 95, 95)],
           [( 63, 63, 63),( 47, 47, 47),( 31, 31, 31)],
           [(255,191,127),(191,143, 95),(127, 95, 63)],
           [(127,127,  0),( 95, 95,  0),( 63, 63,  0)],
           [(255,  0,255),(191,  0,191),(127,  0,127)],
           [(  0, 63,  0),(  0, 47,  0),(  0, 31,  0)],
           [(  0,191,  0),(  0,127,  0),(  0, 95,  0)],
           [(127, 95, 63),( 95, 63, 47),( 63, 47, 31)],
           [( 95, 47,  0),( 63, 31,  0),( 48, 15,  0)],
           [(191,191,  0),(127,127,  0),( 95, 95,  0)],
           [( 63, 31,  0),( 47, 15,  0),( 31,  7,  0)],
           [(159, 95,  0),(127, 63,  0),( 95, 47,  0)]]

def make_retropixel(image,clipcolor):
    x,y = image.get_size()
    newImage = pygame.Surface((x*2,y*2))
    for xs in range (x):
        for ys in range(y):
            pixel = image.get_at((xs,ys))
            pixel = (pixel[0],pixel[1],pixel[2])
            if (pixel != clipcolor):
                for i in range(25):
                    if (pixel == palitra[i][0]):
                        newImage.set_at((xs*2,ys*2),palitra[i][0])
                        newImage.set_at((xs*2+1,ys*2),palitra[i][1])
                        newImage.set_at((xs*2,ys*2+1),palitra[i][1])
                        newImage.set_at((xs*2+1,ys*2+1),palitra[i][2])
                        break
            else:
                newImage.set_at((xs*2,ys*2),(1,0,0,255))
                newImage.set_at((xs*2+1,ys*2),(1,0,0,255))
                newImage.set_at((xs*2,ys*2+1),(1,0,0,255))
                newImage.set_at((xs*2+1,ys*2+1),(1,0,0,255))

    newImage.set_colorkey((1,0,0))
    return newImage 





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

class RL_segm():
    def __init__(self):
        self.type = "empty"
        self.can_generate = True
        self.texture = None
        self.uptex = ralli_nontex
        self.hitbox = CollisionBox()

ralli_segm = []
for i in range(26):
    ralli_segm.append([0]*22)

for i in range(26):
    for j in range(22):
        ralli_segm[i][j] = RL_segm()
        ralli_segm[i][j].hitbox.define(12+22*i,20+22*j,22,22)

ralli_map_hitbox = [0]*4
for i in range(4): ralli_map_hitbox[i] = CollisionBox()
ralli_map_hitbox[0].define(0,0,640,20)
ralli_map_hitbox[1].define(0,460,640,20)
ralli_map_hitbox[2].define(0,20,12,440)
ralli_map_hitbox[3].define(628,20,12,440)

def ralli_map_generate():
    global ralli_segm, ralli_flags_pos, ralli_start_pos, ralli_segm

    ralli_segm = []
    for i in range(26):
        ralli_segm.append([0]*22)

    for i in range(26):
        for j in range(22):
            ralli_segm[i][j] = RL_segm()
            ralli_segm[i][j].hitbox.define(12+22*i,20+22*j,22,22)
    
    R1 = randint(7,18)
    R2 = randint(3,16)

    ralli_player.pos_x = R1*22+13+6
    ralli_player.pos_y = R2*22+13+10

    ralli_start_pos = (R1*22+13+6,R2*22+13+10)

    ralli_segm[R1][R2].type = "start"
    ralli_segm[R1][R2].texture = ralli_nontex

    if (0):

        for i in range(3):
            for j in range(3):
                ralli_segm[R1+i-1][R2+j-1].type = "road"
                ralli_segm[R1+i-1][R2+j-1].can_generate = False
                ralli_segm[R1+i-1][R2+j-1].texture = ralli_segm_road[0]

        if (randint(0,1)):
            ralli_segm[R1-2][R2].type = "road"
            ralli_segm[R1-2][R2].can_generate = True
            ralli_segm[R1-2][R2].texture = ralli_segm_road[0]
            ralli_segm[R1+2][R2].type = "road"
            ralli_segm[R1+2][R2].can_generate = True
            ralli_segm[R1+2][R2].texture = ralli_segm_road[0]

            if (randint(0,1)):
                ralli_segm[R1-1][R2-1].type = "block"
                ralli_segm[R1-1][R2-1].can_generate = False
                ralli_segm[R1-1][R2-1].texture = ralli_segm_stantion_1
                ralli_segm[R1][R2-1].type = "block"
                ralli_segm[R1][R2-1].can_generate = False
                ralli_segm[R1][R2-1].texture = ralli_nontex
                ralli_segm[R1+1][R2-1].type = "block"
                ralli_segm[R1+1][R2-1].can_generate = False
                ralli_segm[R1+1][R2-1].texture = ralli_nontex
            else:
                ralli_segm[R1-1][R2+1].type = "block"
                ralli_segm[R1-1][R2+1].can_generate = False
                ralli_segm[R1-1][R2+1].texture = ralli_segm_stantion_1
                ralli_segm[R1][R2+1].type = "block"
                ralli_segm[R1][R2+1].can_generate = False
                ralli_segm[R1][R2+1].texture = ralli_nontex
                ralli_segm[R1+1][R2+1].type = "block"
                ralli_segm[R1+1][R2+1].can_generate = False
                ralli_segm[R1+1][R2+1].texture = ralli_nontex
                
        else:
            ralli_segm[R1][R2-2].type = "road"
            ralli_segm[R1][R2-2].can_generate = True
            ralli_segm[R1][R2-2].texture = ralli_segm_road[0]
            ralli_segm[R1][R2+2].type = "road"
            ralli_segm[R1][R2+2].can_generate = True
            ralli_segm[R1][R2+2].texture = ralli_segm_road[0]

            if (randint(0,1)):
                ralli_segm[R1-1][R2-1].type = "block"
                ralli_segm[R1-1][R2-1].can_generate = False
                ralli_segm[R1-1][R2-1].texture = ralli_segm_stantion_2
                ralli_segm[R1-1][R2].type = "block"
                ralli_segm[R1-1][R2].can_generate = False
                ralli_segm[R1-1][R2].texture = ralli_nontex
                ralli_segm[R1-1][R2+1].type = "block"
                ralli_segm[R1-1][R2+1].can_generate = False
                ralli_segm[R1-1][R2+1].texture = ralli_nontex
            else:
                ralli_segm[R1+1][R2-1].type = "block"
                ralli_segm[R1+1][R2-1].can_generate = False
                ralli_segm[R1+1][R2-1].texture = ralli_segm_stantion_2
                ralli_segm[R1+1][R2].type = "block"
                ralli_segm[R1+1][R2].can_generate = False
                ralli_segm[R1+1][R2].texture = ralli_nontex
                ralli_segm[R1+1][R2+1].type = "block"
                ralli_segm[R1+1][R2+1].can_generate = False
                ralli_segm[R1+1][R2+1].texture = ralli_nontex


        buffermap = ralli_segm
        for i in range(22+randint(-4,4)):
            for x in range(1,25,1):
                for y in range(1,19,1):
                    if (ralli_segm[x][y].type == "empty"):

                        F1 = (ralli_segm[x+1][y].type == "road" or
                            ralli_segm[x-1][y].type == "road" or
                            ralli_segm[x][y+1].type == "road" or
                            ralli_segm[x][y-1].type == "road")

                        F2 = (ralli_segm[x+1][y+1].type == "road" or
                            ralli_segm[x+1][y-1].type == "road" or
                            ralli_segm[x-1][y+1].type == "road" or
                            ralli_segm[x-1][y-1].type == "road")

                        F3 = (((ralli_segm[x-1][y-1].type == "road" and ralli_segm[x-1][y].type == "road" and ralli_segm[x][y-1].type == "road") or
                            (ralli_segm[x+1][y-1].type == "road" and ralli_segm[x+1][y].type == "road" and ralli_segm[x][y-1].type == "road") or
                            (ralli_segm[x+1][y+1].type == "road" and ralli_segm[x+1][y].type == "road" and ralli_segm[x][y+1].type == "road") or
                            (ralli_segm[x-1][y+1].type == "road" and ralli_segm[x-1][y].type == "road" and ralli_segm[x][y+1].type == "road")) or
                            ((ralli_segm[x-1][y-1].type == "road" and ralli_segm[x-1][y].type != "road" and ralli_segm[x][y-1].type != "road") or
                            (ralli_segm[x+1][y-1].type == "road" and ralli_segm[x+1][y].type != "road" and ralli_segm[x][y-1].type != "road") or
                            (ralli_segm[x+1][y+1].type == "road" and ralli_segm[x+1][y].type != "road" and ralli_segm[x][y+1].type != "road") or
                            (ralli_segm[x-1][y+1].type == "road" and ralli_segm[x-1][y].type != "road" and ralli_segm[x][y+1].type != "road")))

                        F4 = (ralli_segm[x][y-1].can_generate and
                              ralli_segm[x+1][y-1].can_generate and
                              ralli_segm[x+1][y].can_generate and
                              ralli_segm[x+1][y+1].can_generate and
                              ralli_segm[x][y+1].can_generate and
                              ralli_segm[x-1][y+1].can_generate and
                              ralli_segm[x-1][y].can_generate and
                              ralli_segm[x-1][y-1].can_generate)

                        if (F1 and F2): F5 = chascecount(0.0175)
                        else: F5 = True

                        if (F1 and not(F3) and F4 and F5 and randint(0,1) == 0):

                            buffermap[x][y].type = "road"
                            buffermap[x][y].texture = ralli_segm_road[0]

            ralli_segm = buffermap
                    
        for x in range(1,25,1):
            for y in range(1,19,1):

                if (ralli_segm[x][y].can_generate):
                    
                    summ = 0
                    summ += int(ralli_segm[x+1][y].type == "road")
                    summ += int(ralli_segm[x-1][y].type == "road")
                    summ += int(ralli_segm[x][y+1].type == "road")
                    summ += int(ralli_segm[x][y-1].type == "road")

                    if (summ == 1):

                        if   (ralli_segm[x+1][y].type == "road" or ralli_segm[x-1][y].type == "road"): ralli_segm[x][y].texture = ralli_segm_road[1]
                        else: ralli_segm[x][y].texture = ralli_segm_road[2]

                    if (summ == 2):

                        if (ralli_segm[x+1][y].type == "road" and ralli_segm[x-1][y].type == "road"): ralli_segm[x][y].texture = ralli_segm_road[1]
                        if (ralli_segm[x][y+1].type == "road" and ralli_segm[x][y-1].type == "road"): ralli_segm[x][y].texture = ralli_segm_road[2]

                        if (ralli_segm[x][y-1].type == "road" and ralli_segm[x+1][y].type == "road"): ralli_segm[x][y].texture = ralli_segm_road[3]
                        if (ralli_segm[x+1][y].type == "road" and ralli_segm[x][y+1].type == "road"): ralli_segm[x][y].texture = ralli_segm_road[4]
                        if (ralli_segm[x-1][y].type == "road" and ralli_segm[x][y+1].type == "road"): ralli_segm[x][y].texture = ralli_segm_road[5]
                        if (ralli_segm[x-1][y].type == "road" and ralli_segm[x][y-1].type == "road"): ralli_segm[x][y].texture = ralli_segm_road[6]

        for x in range(25):
            for y in range(21):
                if (ralli_segm[x][y].type == "empty"):
                    summ = 0
                    summ += int(ralli_segm[x+1][y].type == "road")
                    summ += int(ralli_segm[x-1][y].type == "road")
                    summ += int(ralli_segm[x][y+1].type == "road")
                    summ += int(ralli_segm[x][y-1].type == "road")
                    summ += int(ralli_segm[x-1][y-1].type == "road")
                    summ += int(ralli_segm[x-1][y+1].type == "road")
                    summ += int(ralli_segm[x+1][y-1].type == "road")
                    summ += int(ralli_segm[x+1][y+1].type == "road")

                    if (chascecount((summ)/12)):
                        ralli_segm[x][y].type = "house_buliding"
                        ralli_segm[x][y].can_generate = True
                            
        for x in range(25):
            for y in range(21):
                    if (ralli_segm[x][y].type == "house_buliding"):
                        if (ralli_segm[x+1][y].type == "house_buliding" or ralli_segm[x][y+1].type == "house_buliding"):
                                if (ralli_segm[x+1][y].type == "house_buliding"):
                                    ralli_segm[x][y].texture = ralli_segm_house[0][1]
                                    ralli_segm[x+1][y].texture = ralli_nontex
                                    ralli_segm[x][y].type = "house"
                                    ralli_segm[x+1][y].type = "house"
                                else:
                                    ralli_segm[x][y].texture = ralli_segm_house[0][2]
                                    ralli_segm[x][y+1].texture = ralli_nontex
                                    ralli_segm[x][y].type = "house"
                                    ralli_segm[x][y+1].type = "house"
                        else:
                            ralli_segm[x][y].texture = ralli_segm_house[0][0]
                            ralli_segm[x][y].type = "house"

    else:

        for i in range(9):
            while True:
                RX = randint(0,25)
                RY = randint(0,19)
                can_plase = True
                for x in range(-4,5,1):
                    for y in range(-4,5,1):
                        TRX = RX + x
                        TRY = RY + y
                        if (TRX >= 0 and TRX <= 25 and TRY >= 0 and TRY <= 21):
                            if (ralli_segm[TRX][TRY].type != "empty" and TRX != R1 and TRY != R2):
                                can_plase = False
                if (can_plase):
                    ralli_flags_pos[i] = (RX,RY)
                    ralli_segm[RX][RY].type = "flag_"+str(i%3+1)
                    ralli_segm[RX][RY].texture = ralli_segm_flag_base
                    ralli_segm[RX][RY].uptex = ralli_segm_flag_R
                    break

        for i in range(22+randint(-4,4)):
            RX = randint(0,25)
            RY = randint(0,19)
            acs = False
            for j in range(9):
                acs = acs or (ralli_flags_pos[j][0] == RX and ralli_flags_pos[j][1] == RY)
            if (RX != R1 and RY != R2 and not(acs)):
                ralli_segm[RX][RY].texture = ralli_segm_house[3][0]
                ralli_segm[RX][RY].type = "house_buliding"

        for x in range(25):
            for y in range(21):
                    if (ralli_segm[x][y].type == "house_buliding"):
                        if (ralli_segm[x+1][y].type == "house_buliding" or ralli_segm[x][y+1].type == "house_buliding"):
                                if (ralli_segm[x+1][y].type == "house_buliding"):
                                    ralli_segm[x][y].texture = ralli_segm_house[3][1]
                                    ralli_segm[x+1][y].texture = ralli_nontex
                                    ralli_segm[x][y].type = "house"
                                    ralli_segm[x+1][y].type = "house"
                                else:
                                    ralli_segm[x][y].texture = ralli_segm_house[3][2]
                                    ralli_segm[x][y+1].texture = ralli_nontex
                                    ralli_segm[x][y].type = "house"
                                    ralli_segm[x][y+1].type = "house"
                        else:
                            ralli_segm[x][y].texture = ralli_segm_house[3][0]
                            ralli_segm[x][y].type = "house"

def ralli_prizegame_map_gen():
    for i in range(8 + randint(-3,3)):
        while True:
            RX = randint(0,24)
            RY = randint(0,18)
            if (ralli_segm[RX][RY].type == "empty" and
                ralli_segm[RX+1][RY].type == "empty" and
                ralli_segm[RX][RY+1].type == "empty" and
                ralli_segm[RX+1][RY+1].type == "empty"):
                    ralli_segm[RX][RY].texture = ralli_segm_house[3][3]
                    ralli_segm[RX+1][RY].texture = ralli_nontex
                    ralli_segm[RX][RY+1].texture = ralli_nontex
                    ralli_segm[RX+1][RY+1].texture = ralli_nontex
                    ralli_segm[RX][RY].type = "house"
                    ralli_segm[RX+1][RY].type = "house"
                    ralli_segm[RX][RY+1].type = "house"
                    ralli_segm[RX+1][RY+1].type = "house"
                    break

def ralli_II_map_gen():
    global ralli_segm, ralli_flags_pos, ralli_p1_start_pos, ralli_p2_start_pos, ralli_segm

    ralli_segm = []
    for i in range(26):
        ralli_segm.append([0]*22)

    for i in range(26):
        for j in range(22):
            ralli_segm[i][j] = RL_segm()
            ralli_segm[i][j].hitbox.define(12+22*i,20+22*j,22,22)
    
    R1 = randint(7,18)
    R2 = randint(3,16)

    ralli_player.pos_x = R1*22+13+6
    ralli_player.pos_y = R2*22+13+10

    ralli_p1_start_pos = (R1*22+13+6,R2*22+13+10)

    ralli_segm[R1][R2].type = "start"
    ralli_segm[R1][R2].texture = ralli_nontex    
                
    R1 = randint(7,18)
    R2 = randint(3,16)

    ralli_player2.pos_x = R1*22+13+6
    ralli_player2.pos_y = R2*22+13+10

    ralli_p2_start_pos = (R1*22+13+6,R2*22+13+10)

    ralli_segm[R1][R2].type = "start"
    ralli_segm[R1][R2].texture = ralli_nontex

    for i in range(9):
            while True:
                RX = randint(0,25)
                RY = randint(0,19)
                can_plase = True
                for x in range(-4,5,1):
                    for y in range(-4,5,1):
                        TRX = RX + x
                        TRY = RY + y
                        if (TRX >= 0 and TRX <= 25 and TRY >= 0 and TRY <= 21):
                            if (ralli_segm[TRX][TRY].type != "empty" and TRX != R1 and TRY != R2):
                                can_plase = False
                if (can_plase):
                    ralli_flags_pos[i] = (RX,RY)
                    ralli_segm[RX][RY].type = "flag_"+str(i%3+1)
                    ralli_segm[RX][RY].texture = ralli_segm_flag_base
                    ralli_segm[RX][RY].uptex = ralli_segm_flag_R
                    break

    for i in range(16+randint(-4,4)):
            RX = randint(0,25)
            RY = randint(0,19)
            acs = False
            for j in range(9):
                acs = acs or (ralli_flags_pos[j][0] == RX and ralli_flags_pos[j][1] == RY)
            if (RX != R1 and RY != R2 and not(acs)):
                ralli_segm[RX][RY].texture = ralli_segm_house[3][0]
                ralli_segm[RX][RY].type = "house_buliding"

    for x in range(25):
            for y in range(21):
                    if (ralli_segm[x][y].type == "house_buliding"):
                        if (ralli_segm[x+1][y].type == "house_buliding" or ralli_segm[x][y+1].type == "house_buliding"):
                                if (ralli_segm[x+1][y].type == "house_buliding"):
                                    ralli_segm[x][y].texture = ralli_segm_house[3][1]
                                    ralli_segm[x+1][y].texture = ralli_nontex
                                    ralli_segm[x][y].type = "house"
                                    ralli_segm[x+1][y].type = "house"
                                else:
                                    ralli_segm[x][y].texture = ralli_segm_house[3][2]
                                    ralli_segm[x][y+1].texture = ralli_nontex
                                    ralli_segm[x][y].type = "house"
                                    ralli_segm[x][y+1].type = "house"
                        else:
                            ralli_segm[x][y].texture = ralli_segm_house[3][0]
                            ralli_segm[x][y].type = "house"

    for i in range(4 + randint(-2,2)):
        while True:
            RX = randint(0,24)
            RY = randint(0,18)
            if (ralli_segm[RX][RY].type == "empty" and
                ralli_segm[RX+1][RY].type == "empty" and
                ralli_segm[RX][RY+1].type == "empty" and
                ralli_segm[RX+1][RY+1].type == "empty"):
                    ralli_segm[RX][RY].texture = ralli_segm_house[3][3]
                    ralli_segm[RX+1][RY].texture = ralli_nontex
                    ralli_segm[RX][RY+1].texture = ralli_nontex
                    ralli_segm[RX+1][RY+1].texture = ralli_nontex
                    ralli_segm[RX][RY].type = "house"
                    ralli_segm[RX+1][RY].type = "house"
                    ralli_segm[RX][RY+1].type = "house"
                    ralli_segm[RX+1][RY+1].type = "house"
                    break
            
class RL_car():
    def __init__(self):
        self.pos_x = -1
        self.pos_y = -1
        self.speed = 0
        self.turn = 0
        self.hitbox = CollisionBox()
        self.texture = None

    def draw(self):
        rect = self.texture.get_rect(center=(int(self.pos_x),int(self.pos_y))) 
        txr, pos = rot_center(self.texture, rect, (self.turn))

        txr = make_retropixel(txr,(255,0,255))

        Window.blit(txr,(pos[0] + int(round(pos[0])%2 == 1),pos[1] + int(round(pos[1])%2 == 1)))

ralli_player = RL_car()
ralli_player.hitbox.define(0,0,14,14)
ralli_player.texture = ralli_car
ralli_player2 = RL_car()
ralli_player2.hitbox.define(0,0,14,14)
ralli_player2.texture = ralli_car_2

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
            self.speed = randint(300-100*int(gonky_prizegame_bool or gonky_II_game_bool),500+50*int(gonky_prizegame_bool or gonky_II_game_bool))/100
            self.texture = gonky_brown_car
            self.hitbox.define(0,0,36,58)
        if (cartype == "grey"):
            self.speed = randint(350-100*int(gonky_prizegame_bool or gonky_II_game_bool),700+50*int(gonky_prizegame_bool or gonky_II_game_bool))/100
            self.texture = gonky_grey_car
            self.hitbox.define(0,0,36,60)
        if (cartype == "red"):
            self.speed = randint(400-100*int(gonky_prizegame_bool or gonky_II_game_bool),800+50*int(gonky_prizegame_bool or gonky_II_game_bool))/100
            self.texture = gonky_red_car
            self.hitbox.define(0,0,36,64)
        if (cartype == "vio"):
            self.speed = randint(200-100*int(gonky_prizegame_bool or gonky_II_game_bool),400+50*int(gonky_prizegame_bool or gonky_II_game_bool))/100
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

for i in range(8):
    gonky_II_car[i+2] = car()
    gonky_II_car[i+2].control = False
    gonky_II_car[i+2].pos_y = -999

gonky_II_car[2].way = False
gonky_II_car[2].pos_x = 64
gonky_II_car[3].way = False
gonky_II_car[3].pos_x = 116
gonky_II_car[4].way = True
gonky_II_car[4].pos_x = 168
gonky_II_car[5].way = True
gonky_II_car[5].pos_x = 220
gonky_II_car[6].way = False
gonky_II_car[6].pos_x = 384
gonky_II_car[7].way = False
gonky_II_car[7].pos_x = 436
gonky_II_car[8].way = True
gonky_II_car[8].pos_x = 488
gonky_II_car[9].way = True
gonky_II_car[9].pos_x = 540   

class PM_figure():
    def __init__(self):
        self.code = "0"*16

    def random_code(self):
        while True:
            gcode = ""
            for i in range(16): gcode += str(randint(0,1))
            if (gcode.count("0") >= 6 and gcode.count("1") >= 6):
                self.code = gcode
                break

    def get_reverse(self):
        return ((self.code.replace("0","a")).replace("1","0")).replace("a","1")


    def draw(self,x,y,ch):
        if (ch):
            Window.blit(pamat_ans_l,(x,y))
            if (self.code[0] == "1"): Window.blit(pamat_ans_b_l[1],(x+6,y+2)); Window.blit(pamat_ans_f_d[1],(x+6,y+2))
            if (self.code[1] == "1"): Window.blit(pamat_ans_b_l[1],(x+28,y+2)); Window.blit(pamat_ans_f_d[1],(x+28,y+2))
            if (self.code[2] == "1"): Window.blit(pamat_ans_b_l[0],(x+46,y+6)); Window.blit(pamat_ans_f_d[0],(x+46,y+6))
            if (self.code[3] == "1"): Window.blit(pamat_ans_b_l[0],(x+46,y+28)); Window.blit(pamat_ans_f_d[0],(x+46,y+28))
            if (self.code[4] == "1"): Window.blit(pamat_ans_b_l[1],(x+28,y+46)); Window.blit(pamat_ans_f_d[1],(x+28,y+46))
            if (self.code[5] == "1"): Window.blit(pamat_ans_b_l[1],(x+6,y+46)); Window.blit(pamat_ans_f_d[1],(x+6,y+46))
            if (self.code[6] == "1"): Window.blit(pamat_ans_b_l[0],(x+2,y+28)); Window.blit(pamat_ans_f_d[0],(x+2,y+28))
            if (self.code[7] == "1"): Window.blit(pamat_ans_b_l[0],(x+2,y+6)); Window.blit(pamat_ans_f_d[0],(x+2,y+6))
            if (self.code[8] == "1"): Window.blit(pamat_ans_b_l[2],(x+6,y+6)); Window.blit(pamat_ans_f_d[2],(x+6,y+6))
            if (self.code[9] == "1"): Window.blit(pamat_ans_b_l[0],(x+24,y+6)); Window.blit(pamat_ans_f_d[0],(x+24,y+6))
            if (self.code[10]== "1"): Window.blit(pamat_ans_b_l[3],(x+28,y+6)); Window.blit(pamat_ans_f_d[3],(x+28,y+6))
            if (self.code[11]== "1"): Window.blit(pamat_ans_b_l[1],(x+28,y+24)); Window.blit(pamat_ans_f_d[1],(x+28,y+24))
            if (self.code[12]== "1"): Window.blit(pamat_ans_b_l[2],(x+28,y+28)); Window.blit(pamat_ans_f_d[2],(x+28,y+28))
            if (self.code[13]== "1"): Window.blit(pamat_ans_b_l[0],(x+24,y+28)); Window.blit(pamat_ans_f_d[0],(x+24,y+28))
            if (self.code[14]== "1"): Window.blit(pamat_ans_b_l[3],(x+6,y+28)); Window.blit(pamat_ans_f_d[3],(x+6,y+28))
            if (self.code[15]== "1"): Window.blit(pamat_ans_b_l[1],(x+6,y+24)); Window.blit(pamat_ans_f_d[1],(x+6,y+24))
        else:
            if (self.code[0] == "1"): Window.blit(pamat_ans_b_d[1],(x+6,y+2)); Window.blit(pamat_ans_f_d[1],(x+6,y+2))
            if (self.code[1] == "1"): Window.blit(pamat_ans_b_d[1],(x+28,y+2)); Window.blit(pamat_ans_f_d[1],(x+28,y+2))
            if (self.code[2] == "1"): Window.blit(pamat_ans_b_d[0],(x+46,y+6)); Window.blit(pamat_ans_f_d[0],(x+46,y+6))
            if (self.code[3] == "1"): Window.blit(pamat_ans_b_d[0],(x+46,y+28)); Window.blit(pamat_ans_f_d[0],(x+46,y+28))
            if (self.code[4] == "1"): Window.blit(pamat_ans_b_d[1],(x+28,y+46)); Window.blit(pamat_ans_f_d[1],(x+28,y+46))
            if (self.code[5] == "1"): Window.blit(pamat_ans_b_d[1],(x+6,y+46)); Window.blit(pamat_ans_f_d[1],(x+6,y+46))
            if (self.code[6] == "1"): Window.blit(pamat_ans_b_d[0],(x+2,y+28)); Window.blit(pamat_ans_f_d[0],(x+2,y+28))
            if (self.code[7] == "1"): Window.blit(pamat_ans_b_d[0],(x+2,y+6)); Window.blit(pamat_ans_f_d[0],(x+2,y+6))
            if (self.code[8] == "1"): Window.blit(pamat_ans_b_d[2],(x+6,y+6)); Window.blit(pamat_ans_f_d[2],(x+6,y+6))
            if (self.code[9] == "1"): Window.blit(pamat_ans_b_d[0],(x+24,y+6)); Window.blit(pamat_ans_f_d[0],(x+24,y+6))
            if (self.code[10]== "1"): Window.blit(pamat_ans_b_d[3],(x+28,y+6)); Window.blit(pamat_ans_f_d[3],(x+28,y+6))
            if (self.code[11]== "1"): Window.blit(pamat_ans_b_d[1],(x+28,y+24)); Window.blit(pamat_ans_f_d[1],(x+28,y+24))
            if (self.code[12]== "1"): Window.blit(pamat_ans_b_d[2],(x+28,y+28)); Window.blit(pamat_ans_f_d[2],(x+28,y+28))
            if (self.code[13]== "1"): Window.blit(pamat_ans_b_d[0],(x+24,y+28)); Window.blit(pamat_ans_f_d[0],(x+24,y+28))
            if (self.code[14]== "1"): Window.blit(pamat_ans_b_d[3],(x+6,y+28)); Window.blit(pamat_ans_f_d[3],(x+6,y+28))
            if (self.code[15]== "1"): Window.blit(pamat_ans_b_d[1],(x+6,y+24)); Window.blit(pamat_ans_f_d[1],(x+6,y+24))


pamat_figures=[]
for i in range(10):
    pamat_figures.append([0]*(4))

for i in range(10):
    for j in range(4):
        pamat_figures[i][j] = PM_figure()
        pamat_figures[i][j].random_code()


class SF_bullet():
    def __init__(self):
        self.pos_x = -999
        self.pos_y = -999
        self.texture = safari_bullet
        self.active = False
        self.hitbox = CollisionBox()

    def spawn(self,y):
        self.pos_x = 88
        self.pos_y = 382+y
        self.active = True
        
    def update(self):
        self.pos_x += 2.5
        self.pos_y -= 2.5

class SF_palma():
    def __init__(self):
        self.pos_x = -999
        self.pos_y = -999
        self.texture = safari_palma[0]
        self.speed = 0
        self.border = 0
        self.hitbox = CollisionBox()

    def update(self):
        self.pos_x -= self.speed
        if (self.pos_x <= -self.border): self.pos_x = 640 + self.border

class SF_animal():
    
    def __init__(self):
        self.pos_x = -999
        self.pos_y = -999
        self.texture = safari_kaban
        self.speed = 0
        self.border = 0
        self.hitbox = CollisionBox()
        self.active = True

    def update(self,szl,skl):
        self.pos_x -= self.speed
        if (self.pos_x <= -self.border):
            self.pos_x = 640 + self.border
            if (self.pos_y == 210):
                if (szl >= 0):
                    szl -= 1
                    self.active = True
            if (self.pos_y == 300):
                if (skl >= 0):
                    skl -= 1
                    self.active = True

        return szl, skl

class SF_oblako():
    def __init__(self):
        self.pos_x = -999
        self.pos_y = -999
        self.texture = safari_oblako[0]
        self.speed = 0.0

    def update(self):
        self.pos_x += self.speed
        if (self.pos_x <= -100.0):
            self.pos_x = 740.0
            self.pos_y = randint(-4,30)
            self.speed = -(randint(1,16)/10.0)
            self.texture = safari_oblako[randint(0,2)]

safari_Coblakos = [0]*6
for i in range(6):
    safari_Coblakos[i] = SF_oblako()
    safari_Coblakos[i].pos_x = randint(-100,740)
    safari_Coblakos[i].pos_y = randint(-4,30)
    safari_Coblakos[i].speed = -(randint(1,16)/10.0)
    safari_Coblakos[i].texture = safari_oblako[randint(0,2)]


safari_Cpalmas = [0]*16
for i in range(16): safari_Cpalmas[i] = SF_palma()

safari_Canimals = [0]*10
for i in range(10): safari_Canimals[i] = SF_animal()

def safari_reset_subf():
    global safari_Cpalmas, safari_Canimals

    R1 = randint(-10,10)/100.0
    R2 = randint(-10,10)/100.0
    R3 = randint(-10,10)/100.0
    R4 = randint(-10,10)/100.0

    safari_Cpalmas[0].pos_y = 390
    safari_Cpalmas[0].pos_x = -40
    safari_Cpalmas[0].border = 400
    safari_Cpalmas[0].speed = 1.0 + R1
    safari_Cpalmas[0].texture = safari_palma[0]
    safari_Cpalmas[1].pos_y = 390
    safari_Cpalmas[1].pos_x = 320
    safari_Cpalmas[1].border = 400
    safari_Cpalmas[1].speed = 1.0 + R1
    safari_Cpalmas[1].texture = safari_palma[1]
    safari_Cpalmas[2].pos_y = 390
    safari_Cpalmas[2].pos_x = 680
    safari_Cpalmas[2].border = 400
    safari_Cpalmas[2].speed = 1.0 + R1
    safari_Cpalmas[2].texture = safari_palma[2]
    safari_Cpalmas[3].pos_y = 390
    safari_Cpalmas[3].pos_x = 1040
    safari_Cpalmas[3].border = 400
    safari_Cpalmas[3].speed = 1.0 + R1
    safari_Cpalmas[3].texture = safari_palma[3]

    safari_Cpalmas[4].pos_y = 300
    safari_Cpalmas[4].pos_x = 10
    safari_Cpalmas[4].border = 300
    safari_Cpalmas[4].speed = 0.75 + R2
    safari_Cpalmas[4].texture = safari_palma[3]
    safari_Cpalmas[5].pos_y = 300
    safari_Cpalmas[5].pos_x = 320
    safari_Cpalmas[5].border = 300
    safari_Cpalmas[5].speed = 0.75 + R2
    safari_Cpalmas[5].texture = safari_palma[0]
    safari_Cpalmas[6].pos_y = 300
    safari_Cpalmas[6].pos_x = 630
    safari_Cpalmas[6].border = 300
    safari_Cpalmas[6].speed = 0.75 + R2
    safari_Cpalmas[6].texture = safari_palma[1]
    safari_Cpalmas[7].pos_y = 300
    safari_Cpalmas[7].pos_x = 940
    safari_Cpalmas[7].border = 300
    safari_Cpalmas[7].speed = 0.75 + R2
    safari_Cpalmas[7].texture = safari_palma[2]

    safari_Cpalmas[8].pos_y = 210
    safari_Cpalmas[8].pos_x = 60
    safari_Cpalmas[8].border = 200
    safari_Cpalmas[8].speed = 0.50 + R3
    safari_Cpalmas[8].texture = safari_palma[2]
    safari_Cpalmas[9].pos_y = 210
    safari_Cpalmas[9].pos_x = 320
    safari_Cpalmas[9].border = 200
    safari_Cpalmas[9].speed = 0.50 + R3
    safari_Cpalmas[9].texture = safari_palma[3]
    safari_Cpalmas[10].pos_y = 210
    safari_Cpalmas[10].pos_x = 580
    safari_Cpalmas[10].border = 200
    safari_Cpalmas[10].speed = 0.50 + R3
    safari_Cpalmas[10].texture = safari_palma[0]
    safari_Cpalmas[11].pos_y = 210
    safari_Cpalmas[11].pos_x = 840
    safari_Cpalmas[11].border = 200
    safari_Cpalmas[11].speed = 0.50 + R3
    safari_Cpalmas[11].texture = safari_palma[1]

    safari_Cpalmas[12].pos_y = 120
    safari_Cpalmas[12].pos_x = 110
    safari_Cpalmas[12].border = 100
    safari_Cpalmas[12].speed = 0.25 + R4
    safari_Cpalmas[12].texture = safari_palma[1]
    safari_Cpalmas[13].pos_y = 120
    safari_Cpalmas[13].pos_x = 320
    safari_Cpalmas[13].border = 100
    safari_Cpalmas[13].speed = 0.25 + R4
    safari_Cpalmas[13].texture = safari_palma[2]
    safari_Cpalmas[14].pos_y = 120
    safari_Cpalmas[14].pos_x = 530
    safari_Cpalmas[14].border = 100
    safari_Cpalmas[14].speed = 0.25 + R4
    safari_Cpalmas[14].texture = safari_palma[3]
    safari_Cpalmas[15].pos_y = 120
    safari_Cpalmas[15].pos_x = 740
    safari_Cpalmas[15].border = 100
    safari_Cpalmas[15].speed = 0.25 + R4
    safari_Cpalmas[15].texture = safari_palma[0]

    for i in range(10): safari_Canimals[i].active = True
    
    safari_Canimals[0].pos_y = 120
    safari_Canimals[0].pos_x = 195
    safari_Canimals[0].border = 100
    safari_Canimals[0].speed = 0.25 + R4
    safari_Canimals[0].texture = safari_nosorog
    safari_Canimals[1].pos_y = 120
    safari_Canimals[1].pos_x = 615
    safari_Canimals[1].border = 100
    safari_Canimals[1].speed = 0.25 + R4
    safari_Canimals[1].texture = safari_nosorog

    safari_Canimals[2].pos_y = 210
    safari_Canimals[2].pos_x = 172
    safari_Canimals[2].border = 200
    safari_Canimals[2].speed = 0.50 + R3
    safari_Canimals[2].texture = safari_zebra
    safari_Canimals[3].pos_y = 210
    safari_Canimals[3].pos_x = 432
    safari_Canimals[3].border = 200
    safari_Canimals[3].speed = 0.50 + R3
    safari_Canimals[3].texture = safari_zebra
    safari_Canimals[4].pos_y = 210
    safari_Canimals[4].pos_x = 692
    safari_Canimals[4].border = 200
    safari_Canimals[4].speed = 0.50 + R3
    safari_Canimals[4].texture = safari_zebra
    safari_Canimals[5].pos_y = 210
    safari_Canimals[5].pos_x = 952
    safari_Canimals[5].border = 200
    safari_Canimals[5].speed = 0.50 + R3
    safari_Canimals[5].texture = safari_zebra

    safari_Canimals[6].pos_y = 300
    safari_Canimals[6].pos_x = 153 
    safari_Canimals[6].border = 300
    safari_Canimals[6].speed = 0.75 + R2
    safari_Canimals[6].texture = safari_kaban
    safari_Canimals[7].pos_y = 300
    safari_Canimals[7].pos_x = 463
    safari_Canimals[7].border = 300
    safari_Canimals[7].speed = 0.75 + R2
    safari_Canimals[7].texture = safari_kaban
    safari_Canimals[8].pos_y = 300
    safari_Canimals[8].pos_x = 773
    safari_Canimals[8].border = 300
    safari_Canimals[8].speed = 0.75 + R2
    safari_Canimals[8].texture = safari_kaban
    safari_Canimals[9].pos_y = 300
    safari_Canimals[9].pos_x = 1083
    safari_Canimals[9].border = 300
    safari_Canimals[9].speed = 0.75 + R2
    safari_Canimals[9].texture = safari_kaban

def safari_prizegame_reset_subf():
    global safari_Cpalmas, safari_Canimals

    R1 = randint(-10,10)/100.0
    R2 = randint(-10,10)/100.0
    R3 = randint(-10,10)/100.0
    R4 = randint(-10,10)/100.0

    safari_Cpalmas[0].pos_y = 390
    safari_Cpalmas[0].pos_x = -40
    safari_Cpalmas[0].border = 400
    safari_Cpalmas[0].speed = 1.2 + R1
    safari_Cpalmas[0].texture = safari_palma[0]
    safari_Cpalmas[1].pos_y = 390
    safari_Cpalmas[1].pos_x = 320
    safari_Cpalmas[1].border = 400
    safari_Cpalmas[1].speed = 1.2 + R1
    safari_Cpalmas[1].texture = safari_palma[1]
    safari_Cpalmas[2].pos_y = 390
    safari_Cpalmas[2].pos_x = 680
    safari_Cpalmas[2].border = 400
    safari_Cpalmas[2].speed = 1.2 + R1
    safari_Cpalmas[2].texture = safari_palma[2]
    safari_Cpalmas[3].pos_y = 390
    safari_Cpalmas[3].pos_x = 1040
    safari_Cpalmas[3].border = 400
    safari_Cpalmas[3].speed = 1.2 + R1
    safari_Cpalmas[3].texture = safari_palma[3]

    safari_Cpalmas[4].pos_y = 300
    safari_Cpalmas[4].pos_x = 10
    safari_Cpalmas[4].border = 300
    safari_Cpalmas[4].speed = 0.95 + R2
    safari_Cpalmas[4].texture = safari_palma[3]
    safari_Cpalmas[5].pos_y = 300
    safari_Cpalmas[5].pos_x = 320
    safari_Cpalmas[5].border = 300
    safari_Cpalmas[5].speed = 0.95 + R2
    safari_Cpalmas[5].texture = safari_palma[0]
    safari_Cpalmas[6].pos_y = 300
    safari_Cpalmas[6].pos_x = 630
    safari_Cpalmas[6].border = 300
    safari_Cpalmas[6].speed = 0.95 + R2
    safari_Cpalmas[6].texture = safari_palma[1]
    safari_Cpalmas[7].pos_y = 300
    safari_Cpalmas[7].pos_x = 940
    safari_Cpalmas[7].border = 300
    safari_Cpalmas[7].speed = 0.95 + R2
    safari_Cpalmas[7].texture = safari_palma[2]

    safari_Cpalmas[8].pos_y = 210
    safari_Cpalmas[8].pos_x = 60
    safari_Cpalmas[8].border = 200
    safari_Cpalmas[8].speed = 0.70 + R3
    safari_Cpalmas[8].texture = safari_palma[2]
    safari_Cpalmas[9].pos_y = 210
    safari_Cpalmas[9].pos_x = 320
    safari_Cpalmas[9].border = 200
    safari_Cpalmas[9].speed = 0.70 + R3
    safari_Cpalmas[9].texture = safari_palma[3]
    safari_Cpalmas[10].pos_y = 210
    safari_Cpalmas[10].pos_x = 580
    safari_Cpalmas[10].border = 200
    safari_Cpalmas[10].speed = 0.70 + R3
    safari_Cpalmas[10].texture = safari_palma[0]
    safari_Cpalmas[11].pos_y = 210
    safari_Cpalmas[11].pos_x = 840
    safari_Cpalmas[11].border = 200
    safari_Cpalmas[11].speed = 0.70 + R3
    safari_Cpalmas[11].texture = safari_palma[1]

    safari_Cpalmas[12].pos_y = 120
    safari_Cpalmas[12].pos_x = 110
    safari_Cpalmas[12].border = 100
    safari_Cpalmas[12].speed = 0.45 + R4
    safari_Cpalmas[12].texture = safari_palma[1]
    safari_Cpalmas[13].pos_y = 120
    safari_Cpalmas[13].pos_x = 320
    safari_Cpalmas[13].border = 100
    safari_Cpalmas[13].speed = 0.45 + R4
    safari_Cpalmas[13].texture = safari_palma[2]
    safari_Cpalmas[14].pos_y = 120
    safari_Cpalmas[14].pos_x = 530
    safari_Cpalmas[14].border = 100
    safari_Cpalmas[14].speed = 0.45 + R4
    safari_Cpalmas[14].texture = safari_palma[3]
    safari_Cpalmas[15].pos_y = 120
    safari_Cpalmas[15].pos_x = 740
    safari_Cpalmas[15].border = 100
    safari_Cpalmas[15].speed = 0.45 + R4
    safari_Cpalmas[15].texture = safari_palma[0]

    for i in range(10): safari_Canimals[i].active = True
    
    safari_Canimals[0].pos_y = 120
    safari_Canimals[0].pos_x = 195
    safari_Canimals[0].border = 100
    safari_Canimals[0].speed = 0.45 + R4
    safari_Canimals[0].texture = safari_nosorog
    safari_Canimals[1].pos_y = 120
    safari_Canimals[1].pos_x = 615
    safari_Canimals[1].border = 100
    safari_Canimals[1].speed = 0.45 + R4
    safari_Canimals[1].texture = safari_nosorog

    safari_Canimals[2].pos_y = 210
    safari_Canimals[2].pos_x = 172
    safari_Canimals[2].border = 200
    safari_Canimals[2].speed = 0.70 + R3
    safari_Canimals[2].texture = safari_zebra
    safari_Canimals[3].pos_y = 210
    safari_Canimals[3].pos_x = 432
    safari_Canimals[3].border = 200
    safari_Canimals[3].speed = 0.70 + R3
    safari_Canimals[3].texture = safari_zebra
    safari_Canimals[4].pos_y = 210
    safari_Canimals[4].pos_x = 692
    safari_Canimals[4].border = 200
    safari_Canimals[4].speed = 0.70 + R3
    safari_Canimals[4].texture = safari_zebra
    safari_Canimals[5].pos_y = 210
    safari_Canimals[5].pos_x = 952
    safari_Canimals[5].border = 200
    safari_Canimals[5].speed = 0.70 + R3
    safari_Canimals[5].texture = safari_zebra

    safari_Canimals[6].pos_y = 300
    safari_Canimals[6].pos_x = 153 
    safari_Canimals[6].border = 300
    safari_Canimals[6].speed = 0.95 + R2
    safari_Canimals[6].texture = safari_kaban
    safari_Canimals[7].pos_y = 300
    safari_Canimals[7].pos_x = 463
    safari_Canimals[7].border = 300
    safari_Canimals[7].speed = 0.95 + R2
    safari_Canimals[7].texture = safari_kaban
    safari_Canimals[8].pos_y = 300
    safari_Canimals[8].pos_x = 773
    safari_Canimals[8].border = 300
    safari_Canimals[8].speed = 0.95 + R2
    safari_Canimals[8].texture = safari_kaban
    safari_Canimals[9].pos_y = 300
    safari_Canimals[9].pos_x = 1083
    safari_Canimals[9].border = 300
    safari_Canimals[9].speed = 0.95 + R2
    safari_Canimals[9].texture = safari_kaban



safari_reset_subf()


safari_Cbullets = [0]*16
for i in range(16): safari_Cbullets[i] = SF_bullet()

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
        missed.play()
    
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
    global Window, retropixel_bool

    if (1):

        if (not(retropixel_bool)): Window.blit(pygame.transform.scale((pygame.transform.scale(Window, (320,240))),(640,480)),(0,0))

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
        dist_coeffs[0, 0] = linza_effect * 10.0
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

def game_select_update(select):
    
    if (game_select_button == 0):
        Window.blit(play_button_2,(456,80))
        Window.blit(back_button_1,(468,32))
        if (game_select == "gonky" or game_select == "ralli"): Window.blit(p2p_button_2,(420,128))  
    if (game_select_button == 1):
        Window.blit(play_button_1,(456,80))
        Window.blit(back_button_2,(468,32))
        if (game_select == "gonky" or game_select == "ralli"):Window.blit(p2p_button_2,(420,128))  
    if (game_select_button == 2):
        Window.blit(play_button_2,(456,80))
        Window.blit(back_button_2,(468,32))
        if (game_select == "gonky" or game_select == "ralli"): Window.blit(p2p_button_1,(420,128))  

    if (languare == "RUS"): 
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

        if (game_select == "safari"):
            text_print("Сафари",1,32,32)
            text_print("- Поразите как можно,",1,32,84)
            text_print("  больше животных.",1,32,110)
            text_print("- Цельтись с упреждением,",1,32,136)
            text_print("  чтобы поразить цель.",1,32,162)
            text_print("- Пальмы останавливают пули.",1,32,188)
            text_print("- Иногда вы будете подпрыгивать.",1,32,214)
            text_print("  Учитывайте это при стрельбе.",1,32,240)
            text_print("- у вас будет только 16 выстрелов.",1,32,266)      
            text_print("- время игры - 2 минуты.",1,32,292)
            text_print("- поразите хотя бы 13 животных,",1,32,318)
            text_print("  чтобы получить призовую игру.",1,32,344)        
            text_print("- поразите хотя бы 13 животных в",1,32,370)
            text_print("  призовой игре, чтобы получить",1,32,396)
            text_print("  золотую монету.",1,32,422)

        if (game_select == "pamat"):
            text_print("Память",1,32,32)
            text_print("- Вам будет показана неполная",1,32,84)
            text_print("  фигура и несколько вариантов",1,32,110)
            text_print("  ответов. укажите, какую фигуру",1,32,136)
            text_print("  нужно добавить, чтобы",1,32,162)
            text_print("  получилась полная фигура.",1,32,188)
            text_print("- Вам будет задано 20 вопросов.",1,32,214)
            text_print("- время игры - 3 минуты.",1,32,240)
            text_print("- Ответье хотя бы на 16 вопросов,",1,32,266)      
            text_print("  чтобы получить призовую игру.",1,32,292)
            text_print("- Ответье хотя бы на 16 вопросов",1,32,318)        
            text_print("  в призовой игре, чтобы получить",1,32,344)
            text_print("  золотую монету",1,32,370)

        if (game_select == "ralli"):
            text_print("Ралл-и",1,32,32)
            text_print("- Приедте на указанный флажок,",1,32,84)
            text_print("  чтобы получить очки, указанные",1,32,110)
            text_print("  на нём.",1,32,136)
            text_print("- время игры - 2 минуты.",1,32,162)            
            text_print("- Столкновения замедляют вас.",1,32,188)        
            text_print("- Наберите 50 очков до",1,32,214)
            text_print("  конца игры, чтобы",1,32,240)
            text_print("  получить призовую игру.",1,32,266)
            text_print("- Наберите 50 очков до",1,32,292)
            text_print("  конца призовой игры, чтобы",1,32,318)
            text_print("  получить золотую монету.",1,32,344)

        if (game_select == "ralli_II"):
            text_print("Ралл-и II",1,32,32)
            text_print("- Игра для двоих игроков,",1,32,84)
            text_print("  используйте WASD + Q и",1,32,110)
            text_print("  стрелочки + правый CTRL.",1,32,136)
            text_print("- Первый игрок, приехавший",1,32,162)
            text_print("  на указаный флаг, получит",1,32,188)
            text_print("  очки, указаные на флаге.",1,32,214)
            text_print("- Столкновения замедляют вас.",1,32,240)
            text_print("- время игры - 2 минуты.",1,32,266)      
            text_print("- Наберите 50 очков для победы.",1,32,292)
            text_print("- По истечении времени",1,32,318)
            text_print("  игрок с большим количеством",1,32,344)
            text_print("  очков поюеждает.",1,32,370)
            text_print("- В этой игре нельзя",1,32,396)
            text_print("  получить золотую монету.",1,32,422)

    if (languare == "ENG"): 
        if (game_select == "morskaya_ohota"):
            text_print("Sea hunt",1,32,32)
            text_print("- hit as many as possible",1,32,84)
            text_print("  ships with torpedoes.",1,32,110)
            text_print("- aim ahead to",1,32,136)
            text_print("  hit the target.",1,32,162)
            text_print("- you will only have 10 torpedoes.",1,32,188)      
            text_print("- game time is 2 minutes.",1,32,214)
            text_print("- hit at least 8 ships",1,32,240)
            text_print("  to get a bonus game.",1,32,266)        
            text_print("- Hit at least 8 ships",1,32,292)
            text_print("  in the bonus game to",1,32,318)
            text_print("  get a gold coin.",1,32,344)

        if (game_select == "gonky"):
            text_print("Races",1,32,32)
            text_print("- Get to the finish",1,32,84)
            text_print("  as fast as possible.",1,32,110)
            text_print("- Collisions with other",1,32,136)
            text_print("  cars slow you down.",1,32,162)
            text_print("- game time is 2 minutes.",1,32,188)      
            text_print("- Get to the finish",1,32,214)
            text_print("  to get the prize game.",1,32,240)
            text_print("- Get to the finish",1,32,266)        
            text_print("  in the bonus game",1,32,292)
            text_print("  to get a gold coin.",1,32,318)

        if (game_select == "gonky_II"):
            text_print("Races II",1,32,32)
            text_print("- A game for two players,",1,32,84)
            text_print("  use WASD + Q and",1,32,110)
            text_print("  arrows + right CTRL.",1,32,136)
            text_print("- Get to the finish",1,32,162)
            text_print("  as fast as possible.",1,32,188)
            text_print("- Collisions with other",1,32,214)
            text_print("  cars slow you down.",1,32,240)
            text_print("- game time is 2 minutes.",1,32,266)      
            text_print("- After the time has elapsed,",1,32,292)
            text_print("  the player with the greater",1,32,318)
            text_print("  distance wins.",1,32,344)        
            text_print("- You can't get a",1,32,370)
            text_print("  gold coin in this game.",1,32,396)

        if (game_select == "safari"):
            text_print("Safari",1,32,32)
            text_print("- Hit as many",1,32,84)
            text_print("  animals as possible.",1,32,110)
            text_print("- Aim ahead to",1,32,136)
            text_print("  hit the target.",1,32,162)
            text_print("- Palm trees stop bullets.",1,32,188)
            text_print("- Sometimes you will jump.",1,32,214)
            text_print("  Keep this in mind when shooting.",1,32,240)
            text_print("- you will only have 16 shots.",1,32,266)      
            text_print("- game time is 2 minutes.",1,32,292)
            text_print("- hit at least 13 animals",1,32,318)
            text_print("  to get the bonus game.",1,32,344)        
            text_print("- Hit at least 13 animals ",1,32,370)
            text_print("  in the bonus game",1,32,396)
            text_print("  to get a gold coin.",1,32,422)

        if (game_select == "pamat"):
            text_print("Memory",1,32,32)
            text_print("- You will be shown an incomplete",1,32,84)
            text_print("  figure and several possible",1,32,110)
            text_print("  answers. specify which figure",1,32,136)
            text_print("  you need to add to",1,32,162)
            text_print("  get a complete figure.",1,32,188)
            text_print("- You will be asked 20 questions.",1,32,214)
            text_print("- game time is 3 minutes.",1,32,240)
            text_print("- Answer at least 16 questions",1,32,266)      
            text_print("  to get a bonus game.",1,32,292)
            text_print("- Answer at least 16 questions",1,32,318)        
            text_print("  in the bonus game",1,32,344)
            text_print("  to get a gold coin",1,32,370)

        if (game_select == "ralli"):
            text_print("Rally",1,32,32)
            text_print("- Drive on the specified flag",1,32,84)
            text_print("  to get the points indicated",1,32,110)
            text_print("  on it.",1,32,136)
            text_print("- game time is 2 minutes.",1,32,162)            
            text_print("- Collisions slow you down.",1,32,188)        
            text_print("- Score 50 points before",1,32,214)
            text_print("  the end of the game",1,32,240)
            text_print("  to get a bonus game.",1,32,266)
            text_print("- Score 50 points before",1,32,292)
            text_print("  the end of the bonus game",1,32,318)
            text_print("  to get a gold coin.",1,32,344)

        if (game_select == "ralli_II"):
            text_print("Rally II",1,32,32)
            text_print("- A game for two players,",1,32,84)
            text_print("  use WASD + Q and",1,32,110)
            text_print("  arrows + right CTRL.",1,32,136)
            text_print("- The first player to drive",1,32,162)
            text_print("  to the specified flag will",1,32,188)
            text_print("  receive the points indicated on it.",1,32,214)
            text_print("- Collisions slow you down.",1,32,240)
            text_print("- game time is 2 minutes.",1,32,266)      
            text_print("- Score 50 points to win.",1,32,292)
            text_print("- After the time has elapsed,",1,32,318)
            text_print("  the player with the most",1,32,344)
            text_print("  points wins.",1,32,370)
            text_print("- You can't get a",1,32,396)
            text_print("  gold coin in this game.",1,32,422)    

def ralli_II_game_update():
    global ralli_subtimer, ralli_timer, ralli_target_x, ralli_target_y, ralli_points, ralli_points2, ralli_II_game_bool, gamemenu_bool, blackscreen_timer, wins_player1_tick , wins_player2_tick, ralli_is_crash, ralli_is_crash_II

    if (ralli_points >= 50):
        ralli_II_game_bool = False
        gamemenu_bool = True
        wins_player1_tick = 240

    elif (ralli_points2 >= 50):
        ralli_II_game_bool = False
        gamemenu_bool = True
        wins_player2_tick = 240
        
    elif (ralli_timer <= 0):
        if (ralli_points == ralli_points2):
            ralli_II_game_bool = False
            gamemenu_bool = True
            blackscreen_timer = 120
        else:
            if (ralli_points > ralli_points2):
                ralli_II_game_bool = False
                gamemenu_bool = True
                wins_player1_tick = 240
            else:
                ralli_II_game_bool = False
                gamemenu_bool = True
                wins_player2_tick = 240
        
    Window.blit(ralli_map,(0,0))


    for x in range(26):
        for y in range(22):
            if (ralli_segm[x][y].type != "empty"):
                Window.blit(ralli_segm[x][y].texture,(12+x*22,20+y*22))

    for x in range(26):
        for y in range(22):
            if (ralli_segm[x][y].type[:4] == "flag"):
                if (ralli_target_x == x and ralli_target_y == y): ralli_segm[x][y].uptex = ralli_segm_flag_G
                else: ralli_segm[x][y].uptex = ralli_segm_flag_R

                Window.blit(ralli_segm[x][y].uptex[int(ralli_segm[x][y].type[5])-1][(ralli_subtimer//15+x%4)%4],(12+x*22+10,20+y*22-14))

    if (ralli_II_1_f): ralli_player.speed += 0.0625
    if (ralli_II_1_b): ralli_player.speed -= 0.125

    if   (ralli_II_1_l): RT = ralli_player.turn + 0.5 * (ralli_player.speed)**2
    elif (ralli_II_1_r): RT = ralli_player.turn - 0.5 * (ralli_player.speed)**2
    else: RT = ralli_player.turn
    
    hbx = (ralli_player.pos_x - ralli_player.speed * math.sin(math.radians(RT)))
    hby = (ralli_player.pos_y - ralli_player.speed * math.cos(math.radians(RT)))
    ralli_player.hitbox.define(hbx-0,hby-0,14,14)
    map_cheak = False
    on_road = False
    
    for i in range(4): map_cheak = map_cheak or cheak_BoxC(ralli_player.hitbox,ralli_map_hitbox[i])
    
    for x in range(26):
        for y in range(22):
            if   (ralli_segm[x][y].type == "block"):
                ralli_segm[x][y].hitbox.define(12+x*22,20+y*22,22,22)
                map_cheak = map_cheak or cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type == "house" or ralli_segm[x][y].type == "house_buliding"):
                ralli_segm[x][y].hitbox.define(12+x*22+2,20+y*22+2,18,18)
                map_cheak = map_cheak or cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type == "road"):
                ralli_segm[x][y].hitbox.define(12+x*22,20+y*22,22,22)
                on_road = on_road or cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type[:4] == "flag"):
                ralli_segm[x][y].hitbox.define(12+x*22+4,20+y*22+4,14,14)
                if (cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)):
                    if (ralli_target_x == x and ralli_target_y == y):
                        ralli_points += int(ralli_segm[x][y].type[5])
                        hit.play()
                        while True:
                            r = randint(0,8)
                            if (not(ralli_target_x == ralli_flags_pos[r][0] and ralli_target_y == ralli_flags_pos[r][1])):
                                ralli_target_x = ralli_flags_pos[r][0]
                                ralli_target_y = ralli_flags_pos[r][1]
                                break
    
    if (ralli_II_1_f): ralli_player.speed += 0.125
    if (ralli_II_1_b): ralli_player.speed -= 0.125
    if (map_cheak):
        ralli_player.speed = 0
        if (not(ralli_is_crash)): crash.play()
        ralli_is_crash = True
    else: ralli_is_crash = False
    if (ralli_II_1_l): ralli_player.turn += 0.5 * (ralli_player.speed)**2
    if (ralli_II_1_r): ralli_player.turn -= 0.5 * (ralli_player.speed)**2

    if (ralli_player.speed > 3.5): ralli_player.speed = 3.5
    if (ralli_player.speed < -1): ralli_player.speed = -1

    if (on_road): add_speed = 1.0
    else: add_speed = 1.0

    ralli_player.pos_x -= ralli_player.speed * math.sin(math.radians(ralli_player.turn)) * add_speed
    ralli_player.pos_y -= ralli_player.speed * math.cos(math.radians(ralli_player.turn)) * add_speed

    ralli_player.draw()

    

    if (ralli_II_2_f): ralli_player2.speed += 0.0625
    if (ralli_II_2_b): ralli_player2.speed -= 0.125
    
    if   (ralli_II_2_l): RT = ralli_player2.turn + 0.5 * (ralli_player2.speed)**2
    elif (ralli_II_2_r): RT = ralli_player2.turn - 0.5 * (ralli_player2.speed)**2
    else: RT = ralli_player2.turn

    hbx = (ralli_player2.pos_x - ralli_player2.speed * math.sin(math.radians(RT)))
    hby = (ralli_player2.pos_y - ralli_player2.speed * math.cos(math.radians(RT)))
    ralli_player2.hitbox.define(hbx-0,hby-0,14,14)
    map_cheak = False
    on_road = False
    
    for i in range(4): map_cheak = map_cheak or cheak_BoxC(ralli_player2.hitbox,ralli_map_hitbox[i])
    
    for x in range(26):
        for y in range(22):
            if   (ralli_segm[x][y].type == "block"):
                ralli_segm[x][y].hitbox.define(12+x*22,20+y*22,22,22)
                map_cheak = map_cheak or cheak_BoxC(ralli_player2.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type == "house" or ralli_segm[x][y].type == "house_buliding"):
                ralli_segm[x][y].hitbox.define(12+x*22+2,20+y*22+2,18,18)
                map_cheak = map_cheak or cheak_BoxC(ralli_player2.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type == "road"):
                ralli_segm[x][y].hitbox.define(12+x*22,20+y*22,22,22)
                on_road = on_road or cheak_BoxC(ralli_player2.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type[:4] == "flag"):
                ralli_segm[x][y].hitbox.define(12+x*22+4,20+y*22+4,14,14)
                if (cheak_BoxC(ralli_player2.hitbox,ralli_segm[x][y].hitbox)):
                    if (ralli_target_x == x and ralli_target_y == y):
                        ralli_points2 += int(ralli_segm[x][y].type[5])
                        hit.play()
                        while True:
                            r = randint(0,8)
                            if (not(ralli_target_x == ralli_flags_pos[r][0] and ralli_target_y == ralli_flags_pos[r][1])):
                                ralli_target_x = ralli_flags_pos[r][0]
                                ralli_target_y = ralli_flags_pos[r][1]
                                break
    
    if (ralli_II_2_f): ralli_player2.speed += 0.125
    if (ralli_II_2_b): ralli_player2.speed -= 0.125
    if (map_cheak):
        ralli_player2.speed = 0
        if (not(ralli_is_crash_II)): crash.play()
        ralli_is_crash_II = True
    else: ralli_is_crash_II = False
    if (ralli_II_2_l): ralli_player2.turn += 0.5 * (ralli_player2.speed)**2
    if (ralli_II_2_r): ralli_player2.turn -= 0.5 * (ralli_player2.speed)**2

    if (ralli_player2.speed > 3.5): ralli_player2.speed = 3.5
    if (ralli_player2.speed < -1): ralli_player2.speed = -1

    if (on_road): add_speed = 1.0
    else: add_speed = 1.0

    ralli_player2.pos_x -= ralli_player2.speed * math.sin(math.radians(ralli_player2.turn)) * add_speed
    ralli_player2.pos_y -= ralli_player2.speed * math.cos(math.radians(ralli_player2.turn)) * add_speed

    ralli_player2.draw()

    Window.blit(ralli_board_time,(298,452))
    Window.blit(ralli_board_points,(134,452))
    Window.blit(ralli_board_points,(480,452))

    ralli_subtimer += 1
    if (ralli_subtimer >= 59):
        ralli_subtimer = 0
        ralli_timer -= 1

    Window.blit(ralli_green_num[ralli_points//10],(138,456))
    Window.blit(ralli_green_num[ralli_points%10],(150,456))

    Window.blit(ralli_blue_num[ralli_points2//10],(484,456))
    Window.blit(ralli_blue_num[ralli_points2%10],(496,456))

    text_print(str(ralli_timer//60),1,302,452)
    ss = str(ralli_timer%60)
    if (len(ss)==1): ss = "0" + ss
    text_print(ss,1,302+16,452)
    Window.blit(morskaya_ohota_dd,(302+14,452+6))
    
def ralli_prizegame_update():
    global ralli_subtimer, ralli_timer, ralli_target_x, ralli_target_y, ralli_points, ralli_prizegame_bool, gamemenu_bool, goldcoin_get_timer, goldencoins, blackscreen_timer, ralli_is_crash

    if (ralli_points >= 50):
        ralli_prizegame_bool = False
        gamemenu_bool = True
        goldencoins += 1
        progress_output()
        goldcoin_get_timer = 240

        r = randint(0,8)
        ralli_target_x = (ralli_flags_pos[r])[0]
        ralli_target_y = (ralli_flags_pos[r])[1]

    elif (ralli_timer <= 0):
        ralli_game_bool = False
        gamemenu_bool = True
        blackscreen_timer = 120
    
    Window.blit(ralli_map,(0,0))

    for x in range(26):
        for y in range(22):
            if (ralli_segm[x][y].type != "empty"):
                Window.blit(ralli_segm[x][y].texture,(12+x*22,20+y*22))

    if (ralli_f): ralli_player.speed += 0.0625
    if (ralli_b): ralli_player.speed -= 0.125
    
    if   (ralli_l): RT = ralli_player.turn + 0.5 * (ralli_player.speed)**2
    elif (ralli_r): RT = ralli_player.turn - 0.5 * (ralli_player.speed)**2
    else: RT = ralli_player.turn
    
    hbx = (ralli_player.pos_x - ralli_player.speed * math.sin(math.radians(RT)))
    hby = (ralli_player.pos_y - ralli_player.speed * math.cos(math.radians(RT)))
    ralli_player.hitbox.define(hbx-0,hby-0,14,14)
    map_cheak = False
    on_road = False
    
    for i in range(4): map_cheak = map_cheak or cheak_BoxC(ralli_player.hitbox,ralli_map_hitbox[i])
    
    for x in range(26):
        for y in range(22):
            if   (ralli_segm[x][y].type == "block"):
                ralli_segm[x][y].hitbox.define(12+x*22,20+y*22,22,22)
                map_cheak = map_cheak or cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type == "house" or ralli_segm[x][y].type == "house_buliding"):
                ralli_segm[x][y].hitbox.define(12+x*22+2,20+y*22+2,18,18)
                map_cheak = map_cheak or cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type == "road"):
                ralli_segm[x][y].hitbox.define(12+x*22,20+y*22,22,22)
                on_road = on_road or cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type[:4] == "flag"):
                ralli_segm[x][y].hitbox.define(12+x*22+4,20+y*22+4,14,14)
                if (cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)):
                    if (ralli_target_x == x and ralli_target_y == y):
                        ralli_points += int(ralli_segm[x][y].type[5])
                        hit.play()
                        while True:
                            r = randint(0,8)
                            if (not(ralli_target_x == ralli_flags_pos[r][0] and ralli_target_y == ralli_flags_pos[r][1])):
                                ralli_target_x = ralli_flags_pos[r][0]
                                ralli_target_y = ralli_flags_pos[r][1]
                                break
    
    if (ralli_f): ralli_player.speed += 0.125
    if (ralli_b): ralli_player.speed -= 0.125
    if (map_cheak):
        ralli_player.speed = 0
        if (not(ralli_is_crash)): crash.play()
        ralli_is_crash = True
    else: ralli_is_crash = False
    if (ralli_l): ralli_player.turn += 0.5 * (ralli_player.speed)**2
    if (ralli_r): ralli_player.turn -= 0.5 * (ralli_player.speed)**2

    if (ralli_player.speed > 3.5): ralli_player.speed = 3.5
    if (ralli_player.speed < -1): ralli_player.speed = -1

    if (on_road): add_speed = 1.0
    else: add_speed = 1.0

    ralli_player.pos_x -= ralli_player.speed * math.sin(math.radians(ralli_player.turn)) * add_speed
    ralli_player.pos_y -= ralli_player.speed * math.cos(math.radians(ralli_player.turn)) * add_speed

    ralli_player.draw()

    for x in range(26):
        for y in range(22):
            if (ralli_segm[x][y].type[:4] == "flag"):
                if (ralli_target_x == x and ralli_target_y == y): ralli_segm[x][y].uptex = ralli_segm_flag_G
                else: ralli_segm[x][y].uptex = ralli_segm_flag_R

                Window.blit(ralli_segm[x][y].uptex[int(ralli_segm[x][y].type[5])-1][(ralli_subtimer//15+x%4)%4],(12+x*22+10,20+y*22-14))

    Window.blit(ralli_board_time,(298,452))
    Window.blit(ralli_board_points,(134,452))

    ralli_subtimer += 1
    if (ralli_subtimer >= 59):
        ralli_subtimer = 0
        ralli_timer -= 1

    Window.blit(ralli_green_num[ralli_points//10],(138,456))
    Window.blit(ralli_green_num[ralli_points%10],(150,456))

    text_print(str(ralli_timer//60),1,302,452)
    ss = str(ralli_timer%60)
    if (len(ss)==1): ss = "0" + ss
    text_print(ss,1,302+16,452)
    Window.blit(morskaya_ohota_dd,(302+14,452+6))
    
def ralli_game_update():
    global ralli_subtimer, ralli_timer, ralli_target_x, ralli_target_y, ralli_points, ralli_game_bool, ralli_prizegame_bool, gamemenu_bool, blackscreen_timer, prizegame_timer, ralli_is_crash

    if (ralli_points >= 50):
        ralli_game_bool = False
        ralli_prizegame_bool = True
        ralli_player.pos_x = ralli_start_pos[0]
        ralli_player.pos_y = ralli_start_pos[0]
        ralli_player.turn = 0
        ralli_player.speed = 0
        prizegame_timer = 240
        ralli_timer = 120
        ralli_points = 0
        ralli_prizegame_map_gen()

        r = randint(0,8)
        ralli_target_x = (ralli_flags_pos[r])[0]
        ralli_target_y = (ralli_flags_pos[r])[1]

    elif (ralli_timer <= 0):
        ralli_game_bool = False
        gamemenu_bool = True
        blackscreen_timer = 120
    
    Window.blit(ralli_map,(0,0))

    for x in range(26):
        for y in range(22):
            if (ralli_segm[x][y].type != "empty"):
                Window.blit(ralli_segm[x][y].texture,(12+x*22,20+y*22))

    if (ralli_f): ralli_player.speed += 0.0625
    if (ralli_b): ralli_player.speed -= 0.125
    
    if   (ralli_l): RT = ralli_player.turn + 0.5 * (ralli_player.speed)**2
    elif (ralli_r): RT = ralli_player.turn - 0.5 * (ralli_player.speed)**2
    else: RT = ralli_player.turn
    
    hbx = (ralli_player.pos_x - ralli_player.speed * math.sin(math.radians(RT)))
    hby = (ralli_player.pos_y - ralli_player.speed * math.cos(math.radians(RT)))
    ralli_player.hitbox.define(hbx-0,hby-0,14,14)
    map_cheak = False
    on_road = False
    
    for i in range(4): map_cheak = map_cheak or cheak_BoxC(ralli_player.hitbox,ralli_map_hitbox[i])
    
    for x in range(26):
        for y in range(22):
            if   (ralli_segm[x][y].type == "block"):
                ralli_segm[x][y].hitbox.define(12+x*22,20+y*22,22,22)
                map_cheak = map_cheak or cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type == "house" or ralli_segm[x][y].type == "house_buliding"):
                ralli_segm[x][y].hitbox.define(12+x*22+2,20+y*22+2,18,18)
                map_cheak = map_cheak or cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type == "road"):
                ralli_segm[x][y].hitbox.define(12+x*22,20+y*22,22,22)
                on_road = on_road or cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)
            elif (ralli_segm[x][y].type[:4] == "flag"):
                ralli_segm[x][y].hitbox.define(12+x*22+4,20+y*22+4,14,14)
                if (cheak_BoxC(ralli_player.hitbox,ralli_segm[x][y].hitbox)):
                    if (ralli_target_x == x and ralli_target_y == y):
                        ralli_points += int(ralli_segm[x][y].type[5])
                        hit.play()
                        while True:
                            r = randint(0,8)
                            if (not(ralli_target_x == ralli_flags_pos[r][0] and ralli_target_y == ralli_flags_pos[r][1])):
                                ralli_target_x = ralli_flags_pos[r][0]
                                ralli_target_y = ralli_flags_pos[r][1]
                                break
    
    if (ralli_f): ralli_player.speed += 0.125
    if (ralli_b): ralli_player.speed -= 0.125
    if (map_cheak):
        ralli_player.speed = 0
        if (not(ralli_is_crash)): crash.play()
        ralli_is_crash = True
    else: ralli_is_crash = False
    if (ralli_l): ralli_player.turn += 0.5 * (ralli_player.speed)**2
    if (ralli_r): ralli_player.turn -= 0.5 * (ralli_player.speed)**2

    if (ralli_player.speed > 3.5): ralli_player.speed = 3.5
    if (ralli_player.speed < -1): ralli_player.speed = -1

    if (on_road): add_speed = 1.0
    else: add_speed = 1.0

    ralli_player.pos_x -= ralli_player.speed * math.sin(math.radians(ralli_player.turn)) * add_speed
    ralli_player.pos_y -= ralli_player.speed * math.cos(math.radians(ralli_player.turn)) * add_speed

    ralli_player.draw()

    for x in range(26):
        for y in range(22):
            if (ralli_segm[x][y].type[:4] == "flag"):
                if (ralli_target_x == x and ralli_target_y == y): ralli_segm[x][y].uptex = ralli_segm_flag_G
                else: ralli_segm[x][y].uptex = ralli_segm_flag_R

                Window.blit(ralli_segm[x][y].uptex[int(ralli_segm[x][y].type[5])-1][(ralli_subtimer//15+x%4)%4],(12+x*22+10,20+y*22-14))

    Window.blit(ralli_board_time,(298,452))
    Window.blit(ralli_board_points,(134,452))

    ralli_subtimer += 1
    if (ralli_subtimer >= 59):
        ralli_subtimer = 0
        ralli_timer -= 1

    Window.blit(ralli_green_num[ralli_points//10],(138,456))
    Window.blit(ralli_green_num[ralli_points%10],(150,456))

    text_print(str(ralli_timer//60),1,302,452)
    ss = str(ralli_timer%60)
    if (len(ss)==1): ss = "0" + ss
    text_print(ss,1,302+16,452)
    Window.blit(morskaya_ohota_dd,(302+14,452+6))

def pamat_prizegame_update():
    global pamat_ask, pamat_right_ans, pamat_pos, pamat_wrong_tick, pamat_right_tick, pamat_vrema_timer, pamat_timer, pamat_subtimer, pamat_correct, pamat_incorrect, pamat_game_bool, gamemenu_bool, blackscreen_timer
    global pamat_prizegame_bool, prizegame_timer, pamat_fake_roll

    if (pamat_correct+pamat_incorrect >= 20):
        if (pamat_correct >= 16):
            pamat_prizegame_bool = False
            gamemenu_bool = True
            goldencoins += 1
            progress_output()
            goldcoin_get_timer = 240
        else:
            pamat_prizegame_bool = False
            gamemenu_bool = True
            blackscreen_timer = 120
    
    Window.blit(pamat_base,(0,0))

    if (pamat_ask == ""):
        pamat_right_ans = (randint(0,9),randint(0,3))
        pamat_ask = pamat_figures[pamat_right_ans[0]][pamat_right_ans[1]].get_reverse()

    for i in range(7):
        if (pamat_vrema_timer - 60*i > 60): Window.blit(pamat_vrema[0],(228+28*i,218))
        elif (pamat_vrema_timer - 60*i < 0): Window.blit(pamat_vrema[3],(228+28*i,218))
        else: Window.blit(pamat_vrema[3-((pamat_vrema_timer)%60)//15],(228+28*i,218))
    
    if (pamat_wrong_tick == 0 and pamat_right_tick == 0 and pamat_vrema_timer > 0): pamat_vrema_timer -= 1

    if (pamat_wrong_tick == 0 and pamat_right_tick == 0 and pamat_vrema_timer == 0):
        pamat_wrong_tick = 120
        pamat_right_ans = (-1,-1)
        pamat_fake_roll = -1

    if (pamat_right_tick > 0):
        pamat_right_tick -= 1
        Window.blit(pamat_right, (262,64))
        if (pamat_right_tick == 0):
            pamat_right_ans = (randint(0,9),randint(0,3))
            while True:
                pamat_fake_roll = randint(0,3)
                if (pamat_fake_roll != pamat_right_ans[1]): break
            pamat_ask = pamat_figures[pamat_right_ans[0]][pamat_right_ans[1]].get_reverse()
            pamat_vrema_timer = 420
            pamat_correct += 1
    elif (pamat_wrong_tick > 0):
        pamat_wrong_tick -= 1
        Window.blit(pamat_wrong, (262,64))
        if (pamat_wrong_tick == 0):
            pamat_right_ans = (randint(0,9),randint(0,3))
            while True:
                pamat_fake_roll = randint(0,3)
                if (pamat_fake_roll != pamat_right_ans[1]): break
            pamat_ask = pamat_figures[pamat_right_ans[0]][pamat_right_ans[1]].get_reverse()
            pamat_vrema_timer = 420
            pamat_incorrect += 1
            
    elif (pamat_ask != ""):
        if (pamat_ask[0] == "1"): Window.blit(pamat_ask_1[0],(244, 34));Window.blit(pamat_ask_2[0],(244, 34));Window.blit(pamat_ask_3[0],(244, 34))
        if (pamat_ask[1] == "1"): Window.blit(pamat_ask_1[0],(324, 34));Window.blit(pamat_ask_2[0],(324, 34));Window.blit(pamat_ask_3[0],(324, 34))
        if (pamat_ask[2] == "1"): Window.blit(pamat_ask_1[1],(392, 46));Window.blit(pamat_ask_2[1],(392, 46));Window.blit(pamat_ask_3[1],(392, 46))
        if (pamat_ask[3] == "1"): Window.blit(pamat_ask_1[1],(392,126));Window.blit(pamat_ask_2[1],(392,126));Window.blit(pamat_ask_3[1],(392,126))
        if (pamat_ask[4] == "1"): Window.blit(pamat_ask_1[0],(324,194));Window.blit(pamat_ask_2[0],(324,194));Window.blit(pamat_ask_3[0],(324,194))
        if (pamat_ask[5] == "1"): Window.blit(pamat_ask_1[0],(244,194));Window.blit(pamat_ask_2[0],(244,194));Window.blit(pamat_ask_3[0],(244,194))
        if (pamat_ask[6] == "1"): Window.blit(pamat_ask_1[1],(232,126));Window.blit(pamat_ask_2[1],(232,126));Window.blit(pamat_ask_3[1],(232,126))
        if (pamat_ask[7] == "1"): Window.blit(pamat_ask_1[1],(232, 46));Window.blit(pamat_ask_2[1],(232, 46));Window.blit(pamat_ask_3[1],(232, 46))
        if (pamat_ask[8] == "1"): Window.blit(pamat_ask_1[2],(244, 46));Window.blit(pamat_ask_2[2],(244, 46));Window.blit(pamat_ask_3[2],(244, 46))
        if (pamat_ask[9] == "1"): Window.blit(pamat_ask_1[1],(312, 46));Window.blit(pamat_ask_2[1],(312, 46));Window.blit(pamat_ask_3[1],(312, 46))
        if (pamat_ask[10]== "1"): Window.blit(pamat_ask_1[3],(324, 46));Window.blit(pamat_ask_2[3],(324, 46));Window.blit(pamat_ask_3[3],(324, 46))
        if (pamat_ask[11]== "1"): Window.blit(pamat_ask_1[0],(324,114));Window.blit(pamat_ask_2[0],(324,114));Window.blit(pamat_ask_3[0],(324,114))
        if (pamat_ask[12]== "1"): Window.blit(pamat_ask_1[2],(324,126));Window.blit(pamat_ask_2[2],(324,126));Window.blit(pamat_ask_3[2],(324,126))
        if (pamat_ask[13]== "1"): Window.blit(pamat_ask_1[1],(312,126));Window.blit(pamat_ask_2[1],(312,126));Window.blit(pamat_ask_3[1],(312,126))
        if (pamat_ask[14]== "1"): Window.blit(pamat_ask_1[3],(244,126));Window.blit(pamat_ask_2[3],(244,126));Window.blit(pamat_ask_3[3],(244,126))
        if (pamat_ask[15]== "1"): Window.blit(pamat_ask_1[0],(244,114));Window.blit(pamat_ask_2[0],(244,114));Window.blit(pamat_ask_3[0],(244,114))
        
    for i in range(10):
        for j in range(4):
            pamat_figures[i][j].draw(32+58*i,248+58*j,(pamat_right_ans[1] == j or pamat_fake_roll == j) and pamat_right_ans[1] != -1)

    Window.blit(pamat_choise,(30+58*pamat_pos[0],246+58*pamat_pos[1]))

    pamat_subtimer += 1
    if (pamat_subtimer >= 59):
        pamat_subtimer = 0
        pamat_timer -= 1

    text_print(str(pamat_timer//60),1,444,218)
    ss = str(pamat_timer%60)
    if (len(ss)==1): ss = "0" + ss
    text_print(ss,1,444+16,218)
    Window.blit(morskaya_ohota_dd,(444+14,218+6))
    
def pamat_game_update():
    global pamat_ask, pamat_right_ans, pamat_pos, pamat_wrong_tick, pamat_right_tick, pamat_vrema_timer, pamat_timer, pamat_subtimer, pamat_correct, pamat_incorrect, pamat_game_bool, gamemenu_bool, blackscreen_timer
    global pamat_prizegame_bool, prizegame_timer, pamat_fake_roll

    if (pamat_correct+pamat_incorrect >= 20):
        if (pamat_correct >= 16):
            pamat_game_bool = False
            pamat_prizegame_bool = True
            prizegame_timer = 240

            pamat_timer = 180
            pamat_correct = 0
            pamat_incorrect = 0
            pamat_vrema_timer = 0
            pamat_fake_roll = -1
            
        else:
            pamat_game_bool = False
            gamemenu_bool = True
            blackscreen_timer = 120
    
    Window.blit(pamat_base,(0,0))

    if (pamat_ask == ""):
        pamat_right_ans = (randint(0,9),randint(0,3))
        pamat_ask = pamat_figures[pamat_right_ans[0]][pamat_right_ans[1]].get_reverse()

    for i in range(7):
        if (pamat_vrema_timer - 60*i > 60): Window.blit(pamat_vrema[0],(228+28*i,218))
        elif (pamat_vrema_timer - 60*i < 0): Window.blit(pamat_vrema[3],(228+28*i,218))
        else: Window.blit(pamat_vrema[3-((pamat_vrema_timer)%60)//15],(228+28*i,218))
    
    if (pamat_wrong_tick == 0 and pamat_right_tick == 0 and pamat_vrema_timer > 0): pamat_vrema_timer -= 1

    if (pamat_wrong_tick == 0 and pamat_right_tick == 0 and pamat_vrema_timer == 0):
        pamat_wrong_tick = 120
        pamat_right_ans = (-1,-1)

    if (pamat_right_tick > 0):
        if (pamat_right_tick == 120): hit.play()
        pamat_right_tick -= 1
        Window.blit(pamat_right, (262,64))
        if (pamat_right_tick == 0):
            pamat_right_ans = (randint(0,9),randint(0,3))
            pamat_ask = pamat_figures[pamat_right_ans[0]][pamat_right_ans[1]].get_reverse()
            pamat_vrema_timer = 420
            pamat_correct += 1
    elif (pamat_wrong_tick > 0):
        if (pamat_wrong_tick == 120): wrong.play()
        pamat_wrong_tick -= 1
        Window.blit(pamat_wrong, (262,64))
        if (pamat_wrong_tick == 0):
            pamat_right_ans = (randint(0,9),randint(0,3))
            pamat_ask = pamat_figures[pamat_right_ans[0]][pamat_right_ans[1]].get_reverse()
            pamat_vrema_timer = 420
            pamat_incorrect += 1
            
    elif (pamat_ask != ""):
        if (pamat_ask[0] == "1"): Window.blit(pamat_ask_1[0],(244, 34));Window.blit(pamat_ask_2[0],(244, 34));Window.blit(pamat_ask_3[0],(244, 34))
        if (pamat_ask[1] == "1"): Window.blit(pamat_ask_1[0],(324, 34));Window.blit(pamat_ask_2[0],(324, 34));Window.blit(pamat_ask_3[0],(324, 34))
        if (pamat_ask[2] == "1"): Window.blit(pamat_ask_1[1],(392, 46));Window.blit(pamat_ask_2[1],(392, 46));Window.blit(pamat_ask_3[1],(392, 46))
        if (pamat_ask[3] == "1"): Window.blit(pamat_ask_1[1],(392,126));Window.blit(pamat_ask_2[1],(392,126));Window.blit(pamat_ask_3[1],(392,126))
        if (pamat_ask[4] == "1"): Window.blit(pamat_ask_1[0],(324,194));Window.blit(pamat_ask_2[0],(324,194));Window.blit(pamat_ask_3[0],(324,194))
        if (pamat_ask[5] == "1"): Window.blit(pamat_ask_1[0],(244,194));Window.blit(pamat_ask_2[0],(244,194));Window.blit(pamat_ask_3[0],(244,194))
        if (pamat_ask[6] == "1"): Window.blit(pamat_ask_1[1],(232,126));Window.blit(pamat_ask_2[1],(232,126));Window.blit(pamat_ask_3[1],(232,126))
        if (pamat_ask[7] == "1"): Window.blit(pamat_ask_1[1],(232, 46));Window.blit(pamat_ask_2[1],(232, 46));Window.blit(pamat_ask_3[1],(232, 46))
        if (pamat_ask[8] == "1"): Window.blit(pamat_ask_1[2],(244, 46));Window.blit(pamat_ask_2[2],(244, 46));Window.blit(pamat_ask_3[2],(244, 46))
        if (pamat_ask[9] == "1"): Window.blit(pamat_ask_1[1],(312, 46));Window.blit(pamat_ask_2[1],(312, 46));Window.blit(pamat_ask_3[1],(312, 46))
        if (pamat_ask[10]== "1"): Window.blit(pamat_ask_1[3],(324, 46));Window.blit(pamat_ask_2[3],(324, 46));Window.blit(pamat_ask_3[3],(324, 46))
        if (pamat_ask[11]== "1"): Window.blit(pamat_ask_1[0],(324,114));Window.blit(pamat_ask_2[0],(324,114));Window.blit(pamat_ask_3[0],(324,114))
        if (pamat_ask[12]== "1"): Window.blit(pamat_ask_1[2],(324,126));Window.blit(pamat_ask_2[2],(324,126));Window.blit(pamat_ask_3[2],(324,126))
        if (pamat_ask[13]== "1"): Window.blit(pamat_ask_1[1],(312,126));Window.blit(pamat_ask_2[1],(312,126));Window.blit(pamat_ask_3[1],(312,126))
        if (pamat_ask[14]== "1"): Window.blit(pamat_ask_1[3],(244,126));Window.blit(pamat_ask_2[3],(244,126));Window.blit(pamat_ask_3[3],(244,126))
        if (pamat_ask[15]== "1"): Window.blit(pamat_ask_1[0],(244,114));Window.blit(pamat_ask_2[0],(244,114));Window.blit(pamat_ask_3[0],(244,114))
        
    for i in range(10):
        for j in range(4):
            pamat_figures[i][j].draw(32+58*i,248+58*j,pamat_right_ans[1] == j)

    Window.blit(pamat_choise,(30+58*pamat_pos[0],246+58*pamat_pos[1]))

    pamat_subtimer += 1
    if (pamat_subtimer >= 59):
        pamat_subtimer = 0
        pamat_timer -= 1

    text_print(str(pamat_timer//60),1,444,218)
    ss = str(pamat_timer%60)
    if (len(ss)==1): ss = "0" + ss
    text_print(ss,1,444+16,218)
    Window.blit(morskaya_ohota_dd,(444+14,218+6))

def safari_prizegame_update():
    global safari_player_tick, safari_player_subtick, safari_shots_left, safari_Cbullets, safari_timer, safari_subtimer, safari_jump_tick, safari_jump_tick_pos, safari_zebra_lives, safari_kaban_lives, goldencoins
    global safari_kaban_ct_count, safari_zebra_ct_count, safari_nosorog_ct_count, safari_game_bool, gamemenu_bool, blackscreen_timer, prizegame_timer, safari_Coblakos, goldcoin_get_timer, safari_prizegame_bool

    F = False
    for i in range(16): F = F or safari_Cbullets[i].active
    if ((not(F) and safari_shots_left == 0) or safari_timer <= 0):

        summ = safari_kaban_ct_count + safari_zebra_ct_count + safari_nosorog_ct_count

        if (summ >= 13):
            safari_prizegame_bool = False
            gamemenu_bool = True
            goldencoins += 1
            progress_output()
            goldcoin_get_timer = 240

        else:
            safari_prizegame_bool = False
            gamemenu_bool = True
            blackscreen_timer = 120
        

    Window.blit(safari_map,(0,0))

    for i in range(6):
        safari_Coblakos[i].update()
        Window.blit(safari_Coblakos[i].texture,(round(safari_Coblakos[i].pos_x) + int(round(safari_Coblakos[i].pos_x)%2 == 1),round(safari_Coblakos[i].pos_y) + int(round(safari_Coblakos[i].pos_y)%2 == 1)))
        

    Window.blit(safari_piramid,((round((round(-safari_subtimer/15.0 - -safari_timer/0.25)/2.0)*4))%1000-200,110))

    
    Window.blit(safari_player[safari_player_tick],(56,380-(round(safari_jump_tick_pos) + int(round(safari_jump_tick_pos)%2 == 1))))
    safari_player_subtick += 1
    if (safari_player_subtick == 10):
        safari_player_subtick = 0
        safari_player_tick = (safari_player_tick + 1)%4

    Window.blit(safari_shots_base,(4,424))
    
    Window.blit(safari_animals_cathc,(334,424))

    if (safari_kaban_ct_count <= 4):
        for i in range(safari_kaban_ct_count): Window.blit(safari_kaban[0],(336+32*i,414))
    else:
        for i in range(4): Window.blit(safari_kaban[0],(336+32*i,414))
        for i in range(safari_kaban_ct_count-4): Window.blit(safari_kaban[0],(336+32*i,440))

    if (safari_zebra_ct_count <= 3):
        for i in range(safari_zebra_ct_count): Window.blit(safari_zebra[3],(464+44*i,418))
    else:
        for i in range(3): Window.blit(safari_zebra[3],(464+44*i,418))
        for i in range(safari_zebra_ct_count-3): Window.blit(safari_zebra[3],(464+44*i,444))

    if (safari_nosorog_ct_count > 0): Window.blit(safari_nosorog[1],(594,416))
    if (safari_nosorog_ct_count > 1): Window.blit(safari_nosorog[1],(594,444))

    if (safari_shots_left <= 8):
        for i in range(safari_shots_left): Window.blit(safari_shots_unysed,(6+18*i,426))
    else:
        for i in range(8): Window.blit(safari_shots_unysed,(6+18*i,426))
        for i in range(safari_shots_left-8): Window.blit(safari_shots_unysed,(6+18*i,454))

    for i in range(16):
        if (safari_Cbullets[i].active):
            safari_Cbullets[i].update()
            safari_Cbullets[i].hitbox.define(safari_Cbullets[i].pos_x,safari_Cbullets[i].pos_y,6,6)
            if (safari_Cbullets[i].pos_y < -6):
                safari_Cbullets[i].active = False
                missed.play()
            for j in range(16):
                if (cheak_BoxC(safari_Cbullets[i].hitbox,safari_Cpalmas[j].hitbox)):
                    safari_Cbullets[i].active = False
                    missed.play()
            else: Window.blit(safari_Cbullets[i].texture,(round(safari_Cbullets[i].pos_x) + int(round(safari_Cbullets[i].pos_x)%2 == 1),round(safari_Cbullets[i].pos_y) + int(round(safari_Cbullets[i].pos_y)%2 == 1)))

    for i in range(16):
        safari_Cpalmas[i].hitbox.define(safari_Cpalmas[i].pos_x + 4,safari_Cpalmas[i].pos_y + 4,14,22)
        if (i < 4):
            if (safari_jump_tick_pos == 0.0 and safari_Cpalmas[i].pos_x >= 121.5 and safari_Cpalmas[i].pos_x <= 123):
                safari_jump_tick = 2.3
                jump.play()
        safari_Cpalmas[i].update()
        Window.blit(safari_Cpalmas[i].texture,(round(safari_Cpalmas[i].pos_x) + round(round(safari_Cpalmas[i].pos_x)%2 == 1),safari_Cpalmas[i].pos_y))

    for i in range(10):
        safari_zebra_lives, safari_kaban_lives = safari_Canimals[i].update(safari_zebra_lives, safari_kaban_lives)
        if (safari_Canimals[i].pos_y ==  120): safari_Canimals[i].hitbox.define(safari_Canimals[i].pos_x+4,safari_Canimals[i].pos_y+14,32,10)
        if (safari_Canimals[i].pos_y ==  210): safari_Canimals[i].hitbox.define(safari_Canimals[i].pos_x+2,safari_Canimals[i].pos_y+14,32,8)
        if (safari_Canimals[i].pos_y ==  300): safari_Canimals[i].hitbox.define(safari_Canimals[i].pos_x+2,safari_Canimals[i].pos_y+20,20,6)
        if (safari_Canimals[i].active): Window.blit(safari_Canimals[i].texture[safari_subtimer//15],(round(safari_Canimals[i].pos_x) + int(round(safari_Canimals[i].pos_x)%2 == 1),safari_Canimals[i].pos_y))

    for i in range(10):
        for j in range(16):
            if (safari_Canimals[i].active and safari_Cbullets[j].active):
                if (cheak_BoxC(safari_Canimals[i].hitbox,safari_Cbullets[j].hitbox)):
                    safari_Canimals[i].active = False
                    safari_Cbullets[j].active = False
                    hit.play()
                    if (safari_Canimals[i].pos_y ==  120): safari_nosorog_ct_count += 1
                    if (safari_Canimals[i].pos_y ==  210): safari_zebra_ct_count += 1
                    if (safari_Canimals[i].pos_y ==  300): safari_kaban_ct_count += 1
            
        
    if (safari_jump_tick >= -2.3):
        safari_jump_tick_pos += safari_jump_tick
        safari_jump_tick -= 0.05
    else: safari_jump_tick_pos = 0.0

    safari_subtimer += 1
    if (safari_subtimer >= 59):
        safari_subtimer = 0
        safari_timer -= 1

    text_print(str(safari_timer//60),1,148,420)
    ss = str(safari_timer%60)
    if (len(ss)==1): ss = "0" + ss
    text_print(ss,1,164,420)
    Window.blit(morskaya_ohota_dd,(162,426))
    
def safari_game_update():
    global safari_player_tick, safari_player_subtick, safari_shots_left, safari_Cbullets, safari_timer, safari_subtimer, safari_jump_tick, safari_jump_tick_pos, safari_zebra_lives, safari_kaban_lives
    global safari_kaban_ct_count, safari_zebra_ct_count, safari_nosorog_ct_count, safari_game_bool, gamemenu_bool, blackscreen_timer, prizegame_timer, safari_Coblakos, safari_prizegame_bool

    F = False
    for i in range(16): F = F or safari_Cbullets[i].active
    if ((not(F) and safari_shots_left == 0) or safari_timer <= 0):

        summ = safari_kaban_ct_count + safari_zebra_ct_count + safari_nosorog_ct_count

        if (summ >= 13):
            safari_game_bool = False
            safari_prizegame_bool = True
            prizegame_timer = 240

            safari_shots_left = 16
            safari_timer = 120
            safari_jump_tick = -32
            safari_jump_tick_pos = 0
            safari_nosorog_ct_count = 0
            safari_zebra_ct_count = 0
            safari_kaban_ct_count = 0
            safari_zebra_lives = 2
            safari_kaban_lives = 4
            for i in range(6):
                safari_Coblakos[i] = SF_oblako()
                safari_Coblakos[i].pos_x = randint(-100,740)
                safari_Coblakos[i].pos_y = randint(-4,30)
                safari_Coblakos[i].speed = -(randint(1,16)/10.0)
                safari_Coblakos[i].texture = safari_oblako[randint(0,2)]

            safari_prizegame_reset_subf()

        else:
            safari_game_bool = False
            gamemenu_bool = True
            blackscreen_timer = 120
        

    Window.blit(safari_map,(0,0))

    for i in range(6):
        safari_Coblakos[i].update()
        Window.blit(safari_Coblakos[i].texture,(round(safari_Coblakos[i].pos_x) + int(round(safari_Coblakos[i].pos_x)%2 == 1),round(safari_Coblakos[i].pos_y) + int(round(safari_Coblakos[i].pos_y)%2 == 1)))
        

    Window.blit(safari_piramid,((round((round(-safari_subtimer/15.0 - -safari_timer/0.25)/2.0)*4))%1000-200,110))

    
    Window.blit(safari_player[safari_player_tick],(56,380-(round(safari_jump_tick_pos) + int(round(safari_jump_tick_pos)%2 == 1))))
    safari_player_subtick += 1
    if (safari_player_subtick == 10):
        safari_player_subtick = 0
        safari_player_tick = (safari_player_tick + 1)%4

    Window.blit(safari_shots_base,(4,424))
    
    Window.blit(safari_animals_cathc,(334,424))

    if (safari_kaban_ct_count <= 4):
        for i in range(safari_kaban_ct_count): Window.blit(safari_kaban[0],(336+32*i,414))
    else:
        for i in range(4): Window.blit(safari_kaban[0],(336+32*i,414))
        for i in range(safari_kaban_ct_count-4): Window.blit(safari_kaban[0],(336+32*i,440))

    if (safari_zebra_ct_count <= 3):
        for i in range(safari_zebra_ct_count): Window.blit(safari_zebra[3],(464+44*i,418))
    else:
        for i in range(3): Window.blit(safari_zebra[3],(464+44*i,418))
        for i in range(safari_zebra_ct_count-3): Window.blit(safari_zebra[3],(464+44*i,444))

    if (safari_nosorog_ct_count > 0): Window.blit(safari_nosorog[1],(594,416))
    if (safari_nosorog_ct_count > 1): Window.blit(safari_nosorog[1],(594,444))

    if (safari_shots_left <= 8):
        for i in range(safari_shots_left): Window.blit(safari_shots_unysed,(6+18*i,426))
    else:
        for i in range(8): Window.blit(safari_shots_unysed,(6+18*i,426))
        for i in range(safari_shots_left-8): Window.blit(safari_shots_unysed,(6+18*i,454))

    for i in range(16):
        if (safari_Cbullets[i].active):
            safari_Cbullets[i].update()
            safari_Cbullets[i].hitbox.define(safari_Cbullets[i].pos_x,safari_Cbullets[i].pos_y,6,6)
            if (safari_Cbullets[i].pos_y < -6):
                safari_Cbullets[i].active = False
                missed.play()
            for j in range(16):
                if (cheak_BoxC(safari_Cbullets[i].hitbox,safari_Cpalmas[j].hitbox)):
                    safari_Cbullets[i].active = False
                    missed.play()
            else: Window.blit(safari_Cbullets[i].texture,(round(safari_Cbullets[i].pos_x) + int(round(safari_Cbullets[i].pos_x)%2 == 1),round(safari_Cbullets[i].pos_y) + int(round(safari_Cbullets[i].pos_y)%2 == 1)))

    for i in range(16):
        safari_Cpalmas[i].hitbox.define(safari_Cpalmas[i].pos_x + 4,safari_Cpalmas[i].pos_y + 4,14,22)
        if (i < 4):
            if (safari_jump_tick_pos == 0.0 and safari_Cpalmas[i].pos_x >= 121.5 and safari_Cpalmas[i].pos_x <= 123):
                safari_jump_tick = 2.3
                jump.play()
        safari_Cpalmas[i].update()
        Window.blit(safari_Cpalmas[i].texture,(round(safari_Cpalmas[i].pos_x) + round(round(safari_Cpalmas[i].pos_x)%2 == 1),safari_Cpalmas[i].pos_y))

    for i in range(10):
        safari_zebra_lives, safari_kaban_lives = safari_Canimals[i].update(safari_zebra_lives, safari_kaban_lives)
        if (safari_Canimals[i].pos_y ==  120): safari_Canimals[i].hitbox.define(safari_Canimals[i].pos_x+4,safari_Canimals[i].pos_y+14,32,10)
        if (safari_Canimals[i].pos_y ==  210): safari_Canimals[i].hitbox.define(safari_Canimals[i].pos_x+2,safari_Canimals[i].pos_y+14,32,8)
        if (safari_Canimals[i].pos_y ==  300): safari_Canimals[i].hitbox.define(safari_Canimals[i].pos_x+2,safari_Canimals[i].pos_y+20,20,6)
        if (safari_Canimals[i].active): Window.blit(safari_Canimals[i].texture[safari_subtimer//15],(round(safari_Canimals[i].pos_x) + int(round(safari_Canimals[i].pos_x)%2 == 1),safari_Canimals[i].pos_y))

    for i in range(10):
        for j in range(16):
            if (safari_Canimals[i].active and safari_Cbullets[j].active):
                if (cheak_BoxC(safari_Canimals[i].hitbox,safari_Cbullets[j].hitbox)):
                    safari_Canimals[i].active = False
                    safari_Cbullets[j].active = False
                    hit.play()
                    if (safari_Canimals[i].pos_y ==  120): safari_nosorog_ct_count += 1
                    if (safari_Canimals[i].pos_y ==  210): safari_zebra_ct_count += 1
                    if (safari_Canimals[i].pos_y ==  300): safari_kaban_ct_count += 1
            
        
    if (safari_jump_tick >= -2.3):
        safari_jump_tick_pos += safari_jump_tick
        safari_jump_tick -= 0.05
    else: safari_jump_tick_pos = 0.0

    safari_subtimer += 1
    if (safari_subtimer >= 59):
        safari_subtimer = 0
        safari_timer -= 1

    text_print(str(safari_timer//60),1,148,420)
    ss = str(safari_timer%60)
    if (len(ss)==1): ss = "0" + ss
    text_print(ss,1,164,420)
    Window.blit(morskaya_ohota_dd,(162,426))
    
def gonky_II_game_update():
    global gonky_II_player1_viev_pos, gonky_II_player2_viev_pos, gonky_II_time, gonky_II_subtime, wins_player1_tick, wins_player2_tick, gonky_II_game_bool, gamemenu_bool
    
    Window.blit(gonky_II_roadsegment,(0,int(gonky_II_player1_viev_pos%480) + int(int(gonky_II_player1_viev_pos)%2 == 1)))
    Window.blit(gonky_II_roadsegment,(0,int(gonky_II_player1_viev_pos%480)-480 + int(int(gonky_II_player1_viev_pos)%2 == 1)))
    
    Window.blit(gonky_II_roadsegment,(320,int(gonky_II_player2_viev_pos%480) + int(int(gonky_II_player2_viev_pos)%2 == 1)))
    Window.blit(gonky_II_roadsegment,(320,int(gonky_II_player2_viev_pos%480)-480 + int(int(gonky_II_player2_viev_pos)%2 == 1)))

    Window.blit(gonky_info_player_1_go,(304,438))
    Window.blit(gonky_info_timer_go,(316,438))
    Window.blit(gonky_info_player_2_go,(328,438))
    Window.blit(gonky_II_info_finish,(302,22))

    if (round(gonky_II_player1_viev_pos/1000) > 50):
        gonky_II_game_bool = False
        gamemenu_bool = True
        wins_player1_tick = 240

    elif (round(gonky_II_player2_viev_pos/1000) > 50):
        gonky_II_game_bool = False
        gamemenu_bool = True
        wins_player2_tick = 240
        
    elif (round((120-gonky_II_time)/240*100) > 50):
        gonky_II_game_bool = False
        gamemenu_bool = True
        if (gonky_II_player1_viev_pos > gonky_II_player2_viev_pos):
            wins_player1_tick = 240
        else:
            wins_player2_tick = 240

    for i in range(round(gonky_II_player1_viev_pos/1000)):
        Window.blit(gonky_info_player_1_go,(304,438-((i+1)*8)))

    for i in range(round((120-gonky_II_time)/240*100)):
        Window.blit(gonky_info_timer_go,(316,438-((i+1)*8)))  

    for i in range(round(gonky_II_player2_viev_pos/1000)):
        Window.blit(gonky_info_player_2_go,(328,438-((i+1)*8)))

    gonky_II_player1_viev_pos += gonky_II_car[0].speed

    if (gonky_II_car[0].distract == 0 and gonky_II_F1_bool): gonky_II_car[0].speed += 0.0625
    if (gonky_II_B1_bool): gonky_II_car[0].speed -= 0.0625

    if (gonky_II_car[0].speed < 0): gonky_II_car[0].speed = 0
    if (gonky_II_car[0].speed > 12): gonky_II_car[0].speed = 12

    if (gonky_II_R1_bool and gonky_II_car[0].speed != 0): gonky_II_car[0].pos_x += 2
    if (gonky_II_L1_bool and gonky_II_car[0].speed != 0): gonky_II_car[0].pos_x -= 2

    if (gonky_II_car[0].pos_x < 38): gonky_II_car[0].pos_x = 38
    if (gonky_II_car[0].pos_x > 246): gonky_II_car[0].pos_x = 246

    if (gonky_II_car[0].distract > 0): gonky_II_car[0].distract -= 1
            
    if ((gonky_II_car[0].distract/2)%2 == 0):Window.blit(gonky_II_car[0].texture[int(gonky_II_B1_bool or gonky_II_car[0].speed == 0)],(gonky_II_car[0].pos_x,374))

    Boxs = CollisionBox()
    Boxt = CollisionBox()

    Boxs.define(gonky_II_car[0].pos_x,374,gonky_II_car[0].hitbox.size_x,gonky_II_car[0].hitbox.size_y)
    for i in range(4):
        if (gonky_II_car[i+2].hitbox.size_y > 64): S = gonky_II_car[i+2].hitbox.size_y-64
        else: S = 0
        Boxt.define(gonky_II_car[i+2].pos_x,gonky_II_car[i+2].pos_y+S,gonky_II_car[i+2].hitbox.size_x,gonky_II_car[i+2].hitbox.size_y)
        if (gonky_II_car[0].distract == 0 and cheak_BoxC(Boxs,Boxt)):
            gonky_II_car[0].distract = 60
            crash.play()
            gonky_II_car[0].speed = round((gonky_II_car[0].speed*0.25)*16)/16
            
        gonky_II_car[i+2].update()
        gonky_II_car[i+2].pos_y += gonky_II_car[0].speed
            
        Window.blit(gonky_II_car[i+2].texture[not(gonky_II_car[i+2].way)],(gonky_II_car[i+2].pos_x,round(gonky_II_car[i+2].pos_y)+int(round(gonky_II_car[i+2].pos_y)%2 == 1)))
        
    gonky_II_player2_viev_pos += gonky_II_car[1].speed

    if (gonky_II_car[1].distract == 0 and gonky_II_F2_bool): gonky_II_car[1].speed += 0.0625
    if (gonky_II_B2_bool): gonky_II_car[1].speed -= 0.0625

    if (gonky_II_car[1].speed < 0): gonky_II_car[1].speed = 0
    if (gonky_II_car[1].speed > 12): gonky_II_car[1].speed = 12

    if (gonky_II_R2_bool and gonky_II_car[1].speed != 0): gonky_II_car[1].pos_x += 2
    if (gonky_II_L2_bool and gonky_II_car[1].speed != 0): gonky_II_car[1].pos_x -= 2

    if (gonky_II_car[1].pos_x < 358): gonky_II_car[1].pos_x = 358
    if (gonky_II_car[1].pos_x > 566 ): gonky_II_car[1].pos_x = 566

    if (gonky_II_car[1].distract > 0): gonky_II_car[1].distract -= 1
            
    if ((gonky_II_car[1].distract/2)%2 == 0):Window.blit(gonky_II_car[1].texture[int(gonky_II_B2_bool or gonky_II_car[1].speed == 0)],(gonky_II_car[1].pos_x,374))

    Boxs.define(gonky_II_car[1].pos_x,374,gonky_II_car[1].hitbox.size_x,gonky_II_car[1].hitbox.size_y)
    for i in range(4):
        if (gonky_II_car[i+6].hitbox.size_y > 64): S = gonky_II_car[i+6].hitbox.size_y-64
        else: S = 0
        Boxt.define(gonky_II_car[i+6].pos_x,gonky_II_car[i+6].pos_y+S,gonky_II_car[i+6].hitbox.size_x,gonky_II_car[i+6].hitbox.size_y)
        if (gonky_II_car[1].distract == 0 and cheak_BoxC(Boxs,Boxt)):
            gonky_II_car[1].distract = 60
            crash.play()
            gonky_II_car[1].speed = round((gonky_II_car[1].speed*0.25)*16)/16
            
        gonky_II_car[i+6].update()
        gonky_II_car[i+6].pos_y += gonky_II_car[1].speed
            
        Window.blit(gonky_II_car[i+6].texture[not(gonky_II_car[i+6].way)],(gonky_II_car[i+6].pos_x,round(gonky_II_car[i+6].pos_y)+int(round(gonky_II_car[i+6].pos_y)%2 == 1)))

    gonky_II_subtime += 1
    if (gonky_II_subtime >= 59):
        gonky_II_subtime = 0
        gonky_II_time -= 1

def gonky_game_update():
    global gonky_viev_pos, gonky_R_bool, gonky_L_bool, gonky_F_bool, gonky_B_bool, gonky_time, gonky_subtime, gonky_prizegame_bool, gonky_game_bool, prizegame_timer, blackscreen_timer,gamemenu_bool
    
    Window.blit(gonky_roadsegment,(0,int(gonky_viev_pos%480) + int(int(gonky_viev_pos)%2 == 1)))
    Window.blit(gonky_roadsegment,(0,int(gonky_viev_pos%480)-480 + int(int(gonky_viev_pos)%2 == 1)))

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
            crash.play()
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
    
    Window.blit(gonky_roadsegment,(0,int(gonky_viev_pos%480) + int(int(gonky_viev_pos)%2 == 1)))
    Window.blit(gonky_roadsegment,(0,int(gonky_viev_pos%480)-480 + int(int(gonky_viev_pos)%2 == 1)))

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
            crash.play()
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
                        expl.play()
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
                        expl.play()
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
    global effect_2_tick, effect_4_tick, coinfalls_tick,blackscreen_timer, prizegame_timer, goldcoin_get_timer, effect_6_tick, wins_player1_tick, wins_player2_tick
    
    Window.fill((0,0,0))

    if (blackscreen_timer > 0):
        blackscreen.set_alpha(255)
        blackscreen_timer -= 1
        Window.blit(blackscreen,(0,0))

    elif (prizegame_timer > 0):
        prizegame_timer -= 1
        if (prizegame_timer >= 60 and prizegame_timer <= 180):
            Window.blit(prizegame[3-prizegame_timer//10%4],(164,168))
        if (prizegame_timer == 210): prizegame_sound.play()

    elif (goldcoin_get_timer > 0):
        goldcoin_get_timer -= 1
        if (goldcoin_get_timer >= 60 and goldcoin_get_timer <= 180):
            Window.blit(goldcoin_get,(270,190))
        if (goldcoin_get_timer == 210): win.play()

    elif (wins_player1_tick > 0):
        wins_player1_tick -= 1
        if (wins_player1_tick >= 60 and wins_player1_tick <= 180):
            Window.blit(wins_player1,(0,0))
        if (wins_player1_tick == 210): win.play()

    elif (wins_player2_tick > 0):
        wins_player2_tick -= 1
        if (wins_player2_tick >= 60 and wins_player2_tick <= 180):
            Window.blit(wins_player2,(0,0))
        if (wins_player2_tick == 210): win.play()
        
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

                Window.blit(version_text,(250,458))

            if (settmenu_bool):
                if (settmenu_select == 0): Window.blit(back_button_1,(32,32))
                else: Window.blit(back_button_2,(32,32))

                if (settmenu_select == 1):
                    Window.blit(settmenu_fullscreen_1,(62,100))
                    if (fullscreen_bool): Window.blit(settmenu_fullscreen_cheak_1,(62,100))
                else:
                    Window.blit(settmenu_fullscreen_2,(62,100))
                    if (fullscreen_bool): Window.blit(settmenu_fullscreen_cheak_2,(62,100))

                if (settmenu_select == 2):  Window.blit(settmenu_grahigs_1,(62,160))
                else:   Window.blit(settmenu_grahigs_2,(62,160))

                if (settmenu_select == 3):  Window.blit(settmenu_audio_1,(62,220))
                else:   Window.blit(settmenu_audio_2,(62,220))

                if (settmenu_select == 4):  Window.blit(settmenu_languare_1,(62,280))
                else:   Window.blit(settmenu_languare_2,(62,280))

                if (settmenu_select == 5):  Window.blit(settmenu_resetprogress_1,(62,340))
                else:   Window.blit(settmenu_resetprogress_2,(62,340))

            if (grafmenu_bool):
                if (grafmenu_select == 0): Window.blit(back_button_1,(32,32))
                else: Window.blit(back_button_2,(32,32))

                Window.blit(grafmenu_merzanie_str[grafmenu_select == 1],(62,100))
                Window.blit(grafmenu_merzanie[merzanie_bool][grafmenu_select == 1],(62,100))

                Window.blit(grafmenu_lostpixel_str[grafmenu_select == 2],(10,160))
                Window.blit(grafmenu_lostpixel[effect_2_int][grafmenu_select == 2],(10,160))

                Window.blit(grafmenu_linza_str[grafmenu_select == 3],(10,220))
                Window.blit(grafmenu_linza[linza_effect][grafmenu_select == 3],(10,220))

                Window.blit(grafmenu_defects_str[grafmenu_select == 4],(62,280))
                Window.blit(grafmenu_defects[defects_bool][grafmenu_select == 4],(62,280))

                Window.blit(grafmenu_retropixel_str[grafmenu_select == 5],(62,340))
                Window.blit(grafmenu_retropixel[retropixel_bool][grafmenu_select == 5],(62,340))

                Window.blit(grafmenu_setdefents[grafmenu_select == 6],(62,400))

            if (audimenu_bool):
                if (audimenu_select == 0): Window.blit(back_button_1,(32,32))
                else: Window.blit(back_button_2,(32,32))

                if (audimenu_select == 1):  Window.blit(volumenu_general_1,(56,100))
                else: Window.blit(volumenu_general_2,(56,100))

                if (audimenu_select == 2):  Window.blit(volumenu_white_noise_1,(56,160))
                else: Window.blit(volumenu_white_noise_2,(56,160))

                if (audimenu_select == 3):  Window.blit(volumenu_effects_1,(56,220))
                else: Window.blit(volumenu_effects_2,(56,220))

                if (audimenu_select == 4):  Window.blit(volumenu_music_1,(56,280))
                else: Window.blit(volumenu_music_2,(56,280))

                if (languare == "RUS"):
                    if (audimenu_select == 1): Window.blit(volume_pr_S[int(volume_GN/5)],(468,108))
                    else: Window.blit(volume_pr_U[int(volume_GN/5)],(468,108))

                    if (audimenu_select == 2): Window.blit(volume_pr_S[int(volume_WN/5)],(394,168))
                    else: Window.blit(volume_pr_U[int(volume_WN/5)],(394,168))

                    if (audimenu_select == 3): Window.blit(volume_pr_S[int(volume_EF/5)],(370,228))
                    else: Window.blit(volume_pr_U[int(volume_EF/5)],(370,228))

                    if (audimenu_select == 4): Window.blit(volume_pr_S[int(volume_MS/5)],(358,288))
                    else: Window.blit(volume_pr_U[int(volume_MS/5)],(358,288))

                if (languare == "ENG"):
                    if (audimenu_select == 1): Window.blit(volume_pr_S[int(volume_GN/5)],(454,108))
                    else: Window.blit(volume_pr_U[int(volume_GN/5)],(454,108))

                    if (audimenu_select == 2): Window.blit(volume_pr_S[int(volume_WN/5)],(418,168))
                    else: Window.blit(volume_pr_U[int(volume_WN/5)],(418,168))

                    if (audimenu_select == 3): Window.blit(volume_pr_S[int(volume_EF/5)],(370,228))
                    else: Window.blit(volume_pr_U[int(volume_EF/5)],(370,228))

                    if (audimenu_select == 4): Window.blit(volume_pr_S[int(volume_MS/5)],(346,288))
                    else: Window.blit(volume_pr_U[int(volume_MS/5)],(346,288))

            if (langmenu_bool):
                if (langmenu_select == 0): Window.blit(back_button_1,(32,32))
                else: Window.blit(back_button_2,(32,32))

                if (langmenu_select == 1): Window.blit(settmenu_languare_rus_1,(62,100))
                else: Window.blit(settmenu_languare_rus_2,(62,100))
                
                if (langmenu_select == 2): Window.blit(settmenu_languare_eng_1,(62,160))
                else: Window.blit(settmenu_languare_eng_2,(62,160))

            if (resetprogress_bool):
                if(resetprogress_select == 0): Window.blit(resetprogress_1,(0,0))
                else: Window.blit(resetprogress_2,(0,0))

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
                        Window.blit(safary_banner,(448,208))
                        if (gamemenu_select == 3): Window.blit(safary_gamename_1,(444,178))
                        else: Window.blit(safary_gamename_2,(444,178))

                        Window.blit(pamat_banner,( 32,368))
                        if (gamemenu_select == 4): Window.blit(pamat_gamename_1,(28,338))
                        else: Window.blit(pamat_gamename_2,(28,338))
                        Window.blit(ralli_banner,(240,368))
                        if (gamemenu_select == 5): Window.blit(ralli_gamename_1,(236,338))
                        else: Window.blit(ralli_gamename_2,(236,338))
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

                    if (safari_game_bool): safari_game_update()
                    elif (safari_prizegame_bool): safari_prizegame_update()

                    if (pamat_game_bool): pamat_game_update()
                    elif (pamat_prizegame_bool): pamat_prizegame_update()

                    if (ralli_game_bool): ralli_game_update()
                    elif (ralli_prizegame_bool): ralli_prizegame_update()

                    if (ralli_II_game_bool): ralli_II_game_update()
                        

                    
            
    if (effect_2_tick > 0):

            for i in range(effect_2_int+randint(-1,1)):
                R = randint(1,60)
                Window.blit(pygame.transform.scale(effect_3_1,(R,480)),(randint(0,639-R),0))
            for i in range(effect_2_int+randint(-1,1)):
                R = randint(1,60)
                Window.blit(pygame.transform.scale(effect_3_2,(640,R)),(0,randint(0,479-R)))

    for i in range(((effect_2_int + 5*int(bool(effect_2_tick)))**2 * 3)):
            lpx = randint(0,319); lpy = randint(0,239)
            pygame.draw.rect(Window, (0,0,0),(lpx*2,lpy*2, 2, 2))

    if (merzanie_bool): Window.blit(effect_1[mainmenu_subtick%3],(0,0))

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

white_noise.play(-1)
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

                if (blackscreen_timer <= 0 and prizegame_timer <= 0 and goldcoin_get_timer <= 0 and wins_player1_tick <= 0 and wins_player2_tick <= 0):
            
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
                                menu_button_click.play()
                            if (mainmenu_select == 2):
                                mainmenu_bool = False
                                settmenu_bool = True
                                settmenu_select = 0
                                menu_button_click.play()
                            if (mainmenu_select == 3):
                                Run = False

                    elif (settmenu_bool):
                        if (event.key == pygame.K_UP or event.key == pygame.K_w):
                            if (settmenu_select > 0): settmenu_select -= 1
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                            if (settmenu_select < 5): settmenu_select += 1
                            
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                                if (settmenu_select == 0):
                                    settmenu_bool = False
                                    mainmenu_bool = True
                                    mainmenu_select = 2
                                    menu_button_click.play()
                                if (settmenu_select == 1):
                                    fullscreen_bool = not(fullscreen_bool)
                                    pygame.display.toggle_fullscreen()
                                    settings_output()
                                    menu_button_click.play()
                                if (settmenu_select == 2):
                                    settmenu_bool = False
                                    grafmenu_bool = True
                                    menu_button_click.play()
                                if (settmenu_select == 3):
                                    settmenu_bool = False
                                    audimenu_bool = True
                                    menu_button_click.play()
                                if (settmenu_select == 4):
                                    settmenu_bool = False
                                    langmenu_bool = True
                                    menu_button_click.play()
                                if (settmenu_select == 5):
                                    settmenu_bool = False
                                    resetprogress_bool = True
                                    menu_button_click.play()

                    elif (grafmenu_bool):
                        if (event.key == pygame.K_UP or event.key == pygame.K_w):
                            if (grafmenu_select > 0): grafmenu_select -= 1
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                            if (grafmenu_select < 6): grafmenu_select += 1

                        if (grafmenu_select == 0 and event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            grafmenu_bool = False
                            settmenu_bool = True
                            audimenu_select = 2
                            menu_button_click.play()
                            
                        if (grafmenu_select == 1 and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL or
                            (event.key == pygame.K_RIGHT or event.key == pygame.K_d) or
                            (event.key == pygame.K_LEFT or event.key == pygame.K_a))):
                            merzanie_bool = not(merzanie_bool)
                            settings_output()
                            menu_button_click.play()

                        if (grafmenu_select == 2):
                            if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL or (event.key == pygame.K_RIGHT or event.key == pygame.K_d)):
                                effect_2_int = (effect_2_int+1)%5
                                settings_output()
                                menu_button_click.play()
                            if ((event.key == pygame.K_LEFT or event.key == pygame.K_a)):
                                effect_2_int = (effect_2_int-1)%5
                                settings_output()
                                menu_button_click.play()

                        if (grafmenu_select == 3):
                            if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL or (event.key == pygame.K_RIGHT or event.key == pygame.K_d)):
                                linza_effect = (linza_effect+1)%13
                                settings_output()
                                menu_button_click.play()
                            if ((event.key == pygame.K_LEFT or event.key == pygame.K_a)):
                                linza_effect = (linza_effect-1)%13
                                settings_output()
                                menu_button_click.play()

                        if (grafmenu_select == 4 and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL or
                            (event.key == pygame.K_RIGHT or event.key == pygame.K_d) or
                            (event.key == pygame.K_LEFT or event.key == pygame.K_a))):
                            defects_bool = not(defects_bool)
                            settings_output()
                            menu_button_click.play()

                        if (grafmenu_select == 5 and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL or
                            (event.key == pygame.K_RIGHT or event.key == pygame.K_d) or
                            (event.key == pygame.K_LEFT or event.key == pygame.K_a))):
                            retropixel_bool = not(retropixel_bool)
                            settings_output()
                            menu_button_click.play()

                        if (grafmenu_select == 6 and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL)):
                            merzanie_bool = True
                            effect_2_int = 2
                            linza_effect = 3
                            defects_bool = True
                            retropixel_bool = True
                            settings_output()
                            menu_button_click.play()

                            

                    elif (audimenu_bool):
                        if (event.key == pygame.K_UP or event.key == pygame.K_w):
                            if (audimenu_select > 0): audimenu_select -= 1
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                            if (audimenu_select < 4): audimenu_select += 1

                        if (audimenu_select == 0 and event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            audimenu_bool = False
                            settmenu_bool = True
                            settmenu_select = 3
                            menu_button_click.play()

                        if (audimenu_select == 1 and ((event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL) or (event.key == pygame.K_RIGHT or event.key == pygame.K_d))):
                            volume_GN += 5
                            if (volume_GN > 100): volume_GN = 0
                            settings_output()
                            volume_choise(volume_GN,volume_WN,volume_EF,volume_MS)
                            menu_button_click.play()
                        if (audimenu_select == 1 and ((event.key == pygame.K_LEFT or event.key == pygame.K_a))):
                            volume_GN -= 5
                            if (volume_GN < 0): volume_GN = 100
                            settings_output()
                            volume_choise(volume_GN,volume_WN,volume_EF,volume_MS)
                            menu_button_click.play()

                        if (audimenu_select == 2 and ((event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL) or (event.key == pygame.K_RIGHT or event.key == pygame.K_d))):
                            volume_WN += 5
                            if (volume_WN > 100): volume_WN = 0
                            settings_output()
                            volume_choise(volume_GN,volume_WN,volume_EF,volume_MS)
                            menu_button_click.play()
                        if (audimenu_select == 2 and ((event.key == pygame.K_LEFT or event.key == pygame.K_a))):
                            volume_WN -= 5
                            if (volume_WN < 0): volume_WN = 100
                            settings_output()
                            volume_choise(volume_GN,volume_WN,volume_EF,volume_MS)
                            menu_button_click.play()

                        if (audimenu_select == 3 and ((event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL) or (event.key == pygame.K_RIGHT or event.key == pygame.K_d))):
                            volume_EF += 5
                            if (volume_EF > 100): volume_EF = 0
                            settings_output()
                            volume_choise(volume_GN,volume_WN,volume_EF,volume_MS)
                            menu_button_click.play()
                        if (audimenu_select == 3 and ((event.key == pygame.K_LEFT or event.key == pygame.K_a))):
                            volume_EF -= 5
                            if (volume_EF < 0): volume_EF = 100
                            settings_output()
                            volume_choise(volume_GN,volume_WN,volume_EF,volume_MS)
                            menu_button_click.play()

                        if (audimenu_select == 4 and ((event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL) or (event.key == pygame.K_RIGHT or event.key == pygame.K_d))):
                            volume_MS += 5
                            if (volume_MS > 100): volume_MS = 0
                            settings_output()
                            volume_choise(volume_GN,volume_WN,volume_EF,volume_MS)
                            menu_button_click.play()
                        if (audimenu_select == 4 and ((event.key == pygame.K_LEFT or event.key == pygame.K_a))):
                            volume_MS -= 5
                            if (volume_MS < 0): volume_MS = 100
                            settings_output()
                            volume_choise(volume_GN,volume_WN,volume_EF,volume_MS)
                            menu_button_click.play()

                    elif (langmenu_bool):
                        if (event.key == pygame.K_UP or event.key == pygame.K_w):
                            if (langmenu_select > 0): langmenu_select -= 1
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                            if (langmenu_select < 2): langmenu_select += 1

                        if (langmenu_select == 0 and event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            langmenu_bool = False
                            settmenu_bool = True
                            settmenu_select = 4
                            menu_button_click.play()

                        if (langmenu_select == 1 and event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            languare = "RUS"
                            languare_choise(languare)
                            settings_output()
                            menu_button_click.play()

                        if (langmenu_select == 2 and event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            languare = "ENG"
                            languare_choise(languare)
                            settings_output()
                            menu_button_click.play()

                    elif (resetprogress_bool): 
                        if (event.key == pygame.K_LEFT or event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_a):
                            resetprogress_select = int(not(bool(resetprogress_select)))

                        if (resetprogress_select == 0 and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL)):
                                resetprogress_bool = False
                                settmenu_bool = True
                                menu_button_click.play()

                        if (resetprogress_select == 1 and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL)):
                                resetprogress_bool = False
                                mainmenu_bool = True
                                resetprogress_select = 0
                                goldencoins = 0
                                progress_output()
                                menu_button_click.play()                            
                                
                            
                    elif (gamemenu_bool):
                        if (event.key == pygame.K_UP or event.key == pygame.K_w): gamemenu_select = gamemenu_map(gamemenu_select,1)
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s): gamemenu_select = gamemenu_map(gamemenu_select,3)
                        if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): gamemenu_select = gamemenu_map(gamemenu_select,2)
                        if (event.key == pygame.K_LEFT or event.key == pygame.K_a): gamemenu_select = gamemenu_map(gamemenu_select,4)

                        if (gamemenu_select > 6): gamemenu_select = 6

                        if   (gamemenu_select >= 0 and gamemenu_select <= 6): gamemenu_razdel = 0
                        elif (gamemenu_select >= 7 and gamemenu_select <= 15): gamemenu_razdel = 1
                        elif (gamemenu_select >= 16 and gamemenu_select <= 21): gamemenu_razdel = 2
                            
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                                if (gamemenu_select == 0):
                                    gamemenu_bool = False
                                    mainmenu_bool = True
                                    mainmenu_select = 1
                                    menu_button_click.play()
                                if (gamemenu_select == 1):
                                    gamemenu_bool = False
                                    game_select = "morskaya_ohota"
                                    mainmenu_select = 0
                                    menu_button_click.play()
                                if (gamemenu_select == 2):
                                    gamemenu_bool = False
                                    game_select = "gonky"
                                    mainmenu_select = 0
                                    menu_button_click.play()
                                if (gamemenu_select == 3):
                                    gamemenu_bool = False
                                    game_select = "safari"
                                    mainmenu_select = 0
                                    menu_button_click.play()
                                if (gamemenu_select == 4):
                                    gamemenu_bool = False
                                    game_select = "pamat"
                                    mainmenu_select = 0
                                    menu_button_click.play()
                                if (gamemenu_select == 5):
                                    gamemenu_bool = False
                                    game_select = "ralli"
                                    mainmenu_select = 0
                                    menu_button_click.play()

                    elif (game_select != "none"):
                        if (event.key == pygame.K_UP or event.key == pygame.K_w):
                            if (game_select_button > 0): game_select_button -= 1
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                            if (game_select_button < 1 + int(game_select == "gonky" or game_select == "ralli")): game_select_button += 1
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            if (game_select_button == 0):
                                if   (game_select == "gonky_II"): game_select = "gonky"
                                elif (game_select == "ralli_II"): game_select = "ralli"
                                else:
                                    game_select = "none"
                                    gamemenu_bool = True
                                menu_button_click.play()
                            if (game_select_button == 1):

                                menu_button_click.play()
                                
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
                                    gonky_II_time = 120

                                    gonky_II_player1_viev_pos = 0
                                    gonky_II_car[0].distract = 0
                                    gonky_II_car[0].type = "green"
                                    gonky_II_car[0].control = True
                                    gonky_II_car[0].pos_x = 168
                                    gonky_II_car[0].pos_y = -1
                                    gonky_II_car[0].speed = 5
                                    gonky_II_car[0].texture = gonky_green_car
                                    gonky_II_car[0].hitbox.define(0,0,36,64)
                                    gonky_II_car[0].way = True

                                    gonky_II_player2_viev_pos = 0
                                    gonky_II_car[1].type = "blue"
                                    gonky_II_car[1].control = True
                                    gonky_II_car[1].pos_x = 488
                                    gonky_II_car[1].pos_y = -1
                                    gonky_II_car[1].speed = 5
                                    gonky_II_car[1].texture = gonky_blue_car
                                    gonky_II_car[1].hitbox.define(0,0,36,64)
                                    gonky_II_car[1].way = True

                                if (game_select == "safari"):
                                    safari_game_bool = True
                                    
                                    safari_shots_left = 16
                                    safari_timer = 120
                                    safari_jump_tick = -32
                                    safari_jump_tick_pos = 0
                                    safari_nosorog_ct_count = 0
                                    safari_zebra_ct_count = 0
                                    safari_kaban_ct_count = 0
                                    safari_zebra_lives = 2
                                    safari_kaban_lives = 4
                                    for i in range(6):
                                        safari_Coblakos[i] = SF_oblako()
                                        safari_Coblakos[i].pos_x = randint(-100,740)
                                        safari_Coblakos[i].pos_y = randint(-4,30)
                                        safari_Coblakos[i].speed = -(randint(1,16)/10.0)
                                        safari_Coblakos[i].texture = safari_oblako[randint(0,2)]

                                    safari_reset_subf()

                                if (game_select == "pamat"):
                                    pamat_game_bool = True

                                    pamat_timer = 180
                                    pamat_correct = 0
                                    pamat_incorrect = 0
                                    pamat_vrema_timer = 0

                                    for i in range(10):
                                        for j in range(4):
                                            pamat_figures[i][j].random_code()

                                if (game_select == "ralli"):
                                    ralli_game_bool = True

                                    ralli_map_generate()
                                    ralli_timer = 120
                                    ralli_points = 0
                                    ralli_player.turn = 0
                                    ralli_player.speed = 0

                                    r = randint(0,8)
                                    ralli_target_x = (ralli_flags_pos[r])[0]
                                    ralli_target_y = (ralli_flags_pos[r])[1]

                                if (game_select == "ralli_II"):
                                    ralli_II_game_bool = True

                                    ralli_II_map_gen()
                                    ralli_timer = 120
                                    ralli_points = 0
                                    ralli_points2 = 0
                                    r = randint(0,8)
                                    ralli_target_x = (ralli_flags_pos[r])[0]
                                    ralli_target_y = (ralli_flags_pos[r])[1]
                                    

                                game_start.play()
                                game_select = "none"
                                gamemenu_bool = False
                                coinfalls_tick = 120
                                game_select_button = 0

                            if (game_select_button == 2):
                                if (game_select == "gonky"):
                                    game_select = "gonky_II"
                                if (game_select == "ralli"):
                                    game_select = "ralli_II"
                                game_select_button = 0

                                menu_button_click.play()
                                

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

                    elif (gonky_II_game_bool):
                        if (event.key == pygame.K_d): gonky_II_R1_bool = True
                        if (event.key == pygame.K_a): gonky_II_L1_bool = True
                        if (event.key == pygame.K_w): gonky_II_F1_bool = True
                        if (event.key == pygame.K_s): gonky_II_B1_bool = True
                        if (event.key == pygame.K_RIGHT):  gonky_II_R2_bool = True
                        if (event.key == pygame.K_LEFT):   gonky_II_L2_bool = True
                        if (event.key == pygame.K_UP):     gonky_II_F2_bool = True
                        if (event.key == pygame.K_DOWN):   gonky_II_B2_bool = True

                    elif (safari_game_bool or safari_prizegame_bool):
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            if (safari_shots_left > 0):
                                safari_shots_left -= 1
                                safari_Cbullets[safari_shots_left].spawn(-safari_jump_tick_pos)

                    elif (pamat_game_bool or pamat_prizegame_bool):
                        if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): pamat_pos = ((pamat_pos[0]+1)%10,pamat_pos[1])
                        if (event.key == pygame.K_LEFT or event.key == pygame.K_a): pamat_pos = ((pamat_pos[0]-1)%10,pamat_pos[1])
                        if (event.key == pygame.K_UP or event.key == pygame.K_w): pamat_pos = (pamat_pos[0],(pamat_pos[1]-1)%4)
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s): pamat_pos = (pamat_pos[0],(pamat_pos[1]+1)%4)
                        if(event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_q or event.key == pygame.K_RCTRL):
                            if(pamat_right_ans == pamat_pos): pamat_right_tick = 120
                            else: pamat_wrong_tick = 120
                            pamat_right_ans = (-1,-1)

                    elif (ralli_game_bool or ralli_prizegame_bool):
                        if (event.key == pygame.K_UP or event.key == pygame.K_w): ralli_f = True
                        if (event.key == pygame.K_DOWN or event.key == pygame.K_s): ralli_b = True
                        if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): ralli_r = True
                        if (event.key == pygame.K_LEFT or event.key == pygame.K_a): ralli_l = True

                    elif (ralli_II_game_bool):
                        if (event.key == pygame.K_w): ralli_II_1_f = True
                        if (event.key == pygame.K_s): ralli_II_1_b = True
                        if (event.key == pygame.K_d): ralli_II_1_r = True
                        if (event.key == pygame.K_a): ralli_II_1_l = True
                        if (event.key == pygame.K_UP): ralli_II_2_f = True
                        if (event.key == pygame.K_DOWN): ralli_II_2_b = True
                        if (event.key == pygame.K_RIGHT): ralli_II_2_r = True
                        if (event.key == pygame.K_LEFT): ralli_II_2_l = True
                            
                    
                    

        if (event.type == pygame.KEYUP):
                if (morskaya_ohota_game_bool or morskaya_ohota_prizegame_bool):
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): morskaya_ohota_R_bool = False
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a): morskaya_ohota_L_bool = False
                elif (gonky_game_bool or gonky_prizegame_bool):
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): gonky_R_bool = False
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a): gonky_L_bool = False
                    if (event.key == pygame.K_UP or event.key == pygame.K_w): gonky_F_bool = False
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s): gonky_B_bool = False
                elif (gonky_II_game_bool):
                        if (event.key == pygame.K_d): gonky_II_R1_bool = False
                        if (event.key == pygame.K_a): gonky_II_L1_bool = False
                        if (event.key == pygame.K_w): gonky_II_F1_bool = False
                        if (event.key == pygame.K_s): gonky_II_B1_bool = False
                        if (event.key == pygame.K_RIGHT):  gonky_II_R2_bool = False
                        if (event.key == pygame.K_LEFT):   gonky_II_L2_bool = False
                        if (event.key == pygame.K_UP):     gonky_II_F2_bool = False
                        if (event.key == pygame.K_DOWN):   gonky_II_B2_bool = False
                elif (ralli_game_bool or ralli_prizegame_bool):
                    if (event.key == pygame.K_UP or event.key == pygame.K_w): ralli_f = False
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s): ralli_b = False
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): ralli_r = False
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a): ralli_l = False
                elif (ralli_II_game_bool):
                    if (event.key == pygame.K_w): ralli_II_1_f = False
                    if (event.key == pygame.K_s): ralli_II_1_b = False
                    if (event.key == pygame.K_d): ralli_II_1_r = False
                    if (event.key == pygame.K_a): ralli_II_1_l = False
                    if (event.key == pygame.K_UP): ralli_II_2_f = False
                    if (event.key == pygame.K_DOWN): ralli_II_2_b = False
                    if (event.key == pygame.K_RIGHT): ralli_II_2_r = False
                    if (event.key == pygame.K_LEFT): ralli_II_2_l = False   
                    
    if (defects_bool and chascecount(0.0025) and effect_4_tick == 0):
        effect_4_tick = 20
        effect_4_pos = randint(0,234)*2

    if (defects_bool and chascecount(0.0001) and effect_6_tick == 0):
        effect_6_tick = randint(12,48)

    if (loadtick < 420):
        loadtick += 1
        if (loadtick == 50 or loadtick == 170 or loadtick == 290): effect_2_tick = 20; intro_sound.play()
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
