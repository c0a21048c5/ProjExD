import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
import time

def check_bound(rect,scr_rect):
    # rect: こうかとんか爆弾のrect
    # scr_rect: スクリーンのrect
    yoko, tate = +1,+1
    if rect.left < scr_rect.left or scr_rect.right < rect.right:
        yoko = -1
    
    if rect.top < scr_rect.top or scr_rect.bottom < rect.bottom:
        tate = -1
    return yoko,tate

def main():
    time_start = time.time()
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rect = screen_sfc.get_rect()

    bgimage_sfc = pg.image.load("ex03/fig/pg_bg.jpg")
    bgimage_rect = bgimage_sfc.get_rect()
    screen_sfc.blit(bgimage_sfc,bgimage_rect)

    kkimg_sfc = pg.image.load("ex03/fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0)
    kkimg_rect = kkimg_sfc.get_rect()
    kkimg_rect.center = 900,400

    bombimg_sfc = pg.Surface((20,20))
    bombimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bombimg_sfc,(255,0,0),(10,10),10)
    bombimg_rect = bombimg_sfc.get_rect()
    bombimg_rect.centerx = random.randint(0,screen_rect.width)
    bombimg_rect.centery = random.randint(0,screen_rect.height)
    vx,vy = +1,+1


    bombimg_sfc2 = pg.Surface((20,20))
    bombimg_sfc2.set_colorkey((0,0,0))
    pg.draw.circle(bombimg_sfc2,(255,0,0),(10,10),10)
    bombimg_rect2 = bombimg_sfc2.get_rect()
    bombimg_rect2.centerx = bombimg_rect.width
    bombimg_rect2.centery = bombimg_rect.height
    vx2,vy2 = +1,+1


    while True:
        screen_sfc.blit(bgimage_sfc,bgimage_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True or key_states[pg.K_w] == True :
            kkimg_rect.centery -= 1
        if key_states[pg.K_DOWN] == True or key_states[pg.K_s] == True:
            kkimg_rect.centery += 1
        if key_states[pg.K_LEFT] == True or key_states[pg.K_a] == True:
            kkimg_rect.centerx -= 1
        if key_states[pg.K_RIGHT] == True or key_states[pg.K_d] == True:
            kkimg_rect.centerx += 1
        
        if check_bound(kkimg_rect,screen_rect) != (1,1):
            if key_states[pg.K_UP] == True or key_states[pg.K_w] == True :
                kkimg_rect.centery += 1
            if key_states[pg.K_DOWN] == True or key_states[pg.K_s] == True:
                kkimg_rect.centery -= 1
            if key_states[pg.K_LEFT] == True or key_states[pg.K_a] == True:
                kkimg_rect.centerx += 1
            if key_states[pg.K_RIGHT] == True or key_states[pg.K_d] == True:
                kkimg_rect.centerx -= 1

        screen_sfc.blit(kkimg_sfc,kkimg_rect)


        bombimg_rect.move_ip(vx,vy)
        bombimg_rect2.move_ip(-vx2,vy2)

        screen_sfc.blit(bombimg_sfc,bombimg_rect)
        screen_sfc.blit(bombimg_sfc2,bombimg_rect2)

        yoko,tate = check_bound(bombimg_rect,screen_rect)
        yoko2,tate2 = check_bound(bombimg_rect2,screen_rect)

        vx2 *= yoko2 
        vy2 *= tate2
        vx *= yoko 
        vy *= tate

        if kkimg_rect.colliderect(bombimg_rect) or kkimg_rect.colliderect(bombimg_rect2):
            time_end = time.time()
            tkm.showinfo("残念！",f"また挑戦しよう！ 経過時間{int(abs(time_start-time_end))}秒")
            return

        pg.display.update()
        clock.tick(1000)





if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()    