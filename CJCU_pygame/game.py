import pygame
import random
import math 
pygame.mixer.init()
pygame.init()


#背景圖bg1範圍
def upclear_bg1(x,y):
    canMove = True

    if m_top_leftwall_bg1 <= x <= m_top_rightwall_bg1 and y-50 < topwall_bg1:
        canMove = True
    elif  y - 1<topwall_bg1:
        canMove = False
    elif(x < leftwall_bg1 or x > rightwall_bg1):
        canMove = False

    if canMove:
        return 1
    else:
        return 0
def downclear_bg1(x,y):
    canMove = True
    if bottomwall_bg1 < y:
        canMove = False
    if canMove:
        return 1
    else:
        return 0

def leftclear_bg1(x,y):
    canMove = True
    if  x < leftwall_bg1:
        canMove = False
    elif  y < topwall_bg1:
        canMove = False
    if canMove:
        return 1
    else:
        return 0

def rightclear_bg1(x,y):
    canMove = True
    if x > rightwall_bg1:
        canMove = False
    elif y<topwall_bg1:
        canMove = False
    if canMove:
        return 1
    else:
        return 0
    
#碰到小怪物
def atk_m():
    global x_c,y_c,x_m,y_m
    global c_reduce
    if -15 < x_c-x_m < 35 and -35 < y_c-y_m <45:

        c_reduce = True

        xDiff = x_c - x_m
        yDiff = y_c-y_m

        #X軸的碰撞
        for dis in range(int(abs(xDiff//2))):
            x_move = leftclear_bg1(x_c,y_c) + rightclear_bg1(x_c,y_c)
            x_m_move = leftclear_bg1(x_m,y_m) + rightclear_bg1(x_m,y_m)
            if xDiff>0:
                x_c += x_move / 2 * xDiff / xDiff
                x_m -= x_m_move / 2 * xDiff / xDiff
                
            else:
                x_c -= x_move / 2 * xDiff/xDiff
                x_m_move += x_m_move / 2 * xDiff/xDiff
                
        #Y軸的碰撞
        for dis in range(int(abs(yDiff//2))):
            y_move = upclear_bg1(x_c,y_c) + downclear_bg1(x_c,y_c)
            y_m_move = upclear_bg1(x_m,y_m) + downclear_bg1(x_m,y_m)
            if yDiff>0:
                y_c += y_move / 2 * yDiff / yDiff
                y_m -= y_m_move / 2 * yDiff / yDiff
                
            else:
                y_c -= y_move / 2 * yDiff/yDiff
                y_m_move += y_m_move / 2 * yDiff/yDiff
                

            if c_reduce:
                return 1
            else:
                return 0
#碰到BOSS
def atk_BOSS():
    global x_c,y_c,x_boss,y_boss
    global c_BOSS_reduce
    if -14 < x_c-x_boss < 230 and -24 < y_c-y_boss <309:

        c_BOSS_reduce = True

        xDiff_B = x_c - x_boss
        yDiff_B= y_c-y_boss

        #X軸的碰撞
        for dis in range(int(abs(xDiff_B//2))):
            x_move = leftclear_bg1(x_c,y_c) + rightclear_bg1(x_c,y_c)
            x_BOSS_move = leftclear_bg1(x_boss,y_boss) + rightclear_bg1(x_boss,y_boss)
            if xDiff_B>0:
                x_c += x_move / 2 * xDiff_B / xDiff_B
                x_boss -= x_BOSS_move / 2 * xDiff_B / xDiff_B
                
            else:
                x_c -= x_move / 2 * xDiff_B/xDiff_B
                x_BOSS_move += x_BOSS_move / 2 * xDiff_B/xDiff_B
                
        #Y軸的碰撞
        for dis in range(int(abs(yDiff_B//2))):
            y_move = upclear_bg1(x_c,y_c) + downclear_bg1(x_c,y_c)
            y_BOSS_move = upclear_bg1(x_boss,y_boss) + downclear_bg1(x_boss,y_boss)
            if yDiff_B>0:
                y_c += y_move / 2 * yDiff_B / yDiff_B
                y_boss -= y_BOSS_move / 2 * yDiff_B / yDiff_B
                
            else:
                y_c -= y_move / 2 * yDiff_B/yDiff_B
                y_BOSS_move += y_BOSS_move / 2 * yDiff_B/yDiff_B
                

            if c_reduce:
                return 1
            else:
                return 0
#走路
def move(image1,image2,image3,count):
    
    if  0< count%10 <=4:
        return image2
    elif 4< count%10 <= 8:
        return image3
    else:
        return image1

#攻擊
def atk(image1_atk,image2_atk,image3_atk,count):
    
    if  0< count%10 <=4:
        return image2_atk
    elif 4< count%10 <= 8:
        return image3_atk
    else:
        return image1_atk

#傳送陣
def trans():
    global TRANS,x_c,y_c,x_trans,y_trans
    if -150 < x_c-x_trans < 150 and -100 < y_c-y_trans <100:
        TRANS = True


windowSize = [1000,700]
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("CJCU的小冒險")
clock = pygame.time.Clock()

#背景圖
bg1 = pygame.image.load("source/bg1.png")
bg1 = pygame.transform.scale(bg1,windowSize)
#背景圖2
bg2 = pygame.image.load("source/bg2.png")
bg2 = pygame.transform.scale(bg2,windowSize)
#站立
#上
standing_F =  pygame.image.load('source/F1.png')
standing_F= pygame.transform.scale2x(standing_F)
#下
standing_B =  pygame.image.load('source/B1.png')
standing_B= pygame.transform.scale2x(standing_B)
#左
standing_L =  pygame.image.load('source/L1.png')
standing_L= pygame.transform.scale2x(standing_L)
#右
standing_R =  pygame.image.load('source/R1.png')
standing_R = pygame.transform.scale2x(standing_R)

#攻擊
#上
atk_F1 = pygame.image.load('source/atk_F1.png')
atk_F2 = pygame.image.load('source/atk_F2.png')
atk_F3 = pygame.image.load('source/atk_F3.png')
atk_F1 = pygame.transform.scale2x(atk_F1)
atk_F2 = pygame.transform.scale2x(atk_F2)
atk_F3 = pygame.transform.scale2x(atk_F3)
#下
atk_B1 = pygame.image.load('source/atk_B1.png')
atk_B2 = pygame.image.load('source/atk_B2.png')
atk_B3 = pygame.image.load('source/atk_B3.png')
atk_B1 = pygame.transform.scale2x(atk_B1)
atk_B2 = pygame.transform.scale2x(atk_B2)
atk_B3 = pygame.transform.scale2x(atk_B3)
#左
atk_L1 = pygame.image.load('source/atk_L1.png')
atk_L2 = pygame.image.load('source/atk_L2.png')
atk_L3 = pygame.image.load('source/atk_L3.png')
atk_L1 = pygame.transform.scale2x(atk_L1)
atk_L2 = pygame.transform.scale2x(atk_L2)
atk_L3 = pygame.transform.scale2x(atk_L3)
#右
atk_R1 = pygame.image.load('source/atk_R1.png')
atk_R2 = pygame.image.load('source/atk_R2.png')
atk_R3 = pygame.image.load('source/atk_R3.png')
atk_R1 = pygame.transform.scale2x(atk_R1)
atk_R2 = pygame.transform.scale2x(atk_R2)
atk_R3 = pygame.transform.scale2x(atk_R3)


#主角
#下
down1 = pygame.image.load('source/B1.png')
down2 = pygame.image.load('source/B2.png')
down3 = pygame.image.load('source/B3.png')
down1 = pygame.transform.scale2x(down1)
down2 = pygame.transform.scale2x(down2)
down3 = pygame.transform.scale2x(down3)
#上
up1 = pygame.image.load('source/F1.png')
up2 = pygame.image.load('source/F2.png')
up3 = pygame.image.load('source/F3.png')
up1 = pygame.transform.scale2x(up1)
up2 = pygame.transform.scale2x(up2)
up3 = pygame.transform.scale2x(up3)
#左
left1 = pygame.image.load('source/L1.png')
left2 = pygame.image.load('source/L2.png')
left3 = pygame.image.load('source/L3.png')
left1 = pygame.transform.scale2x(left1)
left2 = pygame.transform.scale2x(left2)
left3 = pygame.transform.scale2x(left3)
#右
right1 = pygame.image.load('source/R1.png')
right2 = pygame.image.load('source/R2.png')
right3 = pygame.image.load('source/R3.png')
right1 = pygame.transform.scale2x(right1)
right2 = pygame.transform.scale2x(right2)
right3 = pygame.transform.scale2x(right3)
#頭像
title = pygame.image.load('source/title.png')
title = pygame.transform.scale2x(title)
#狀態列背景
green = pygame.image.load('source/green.jpg')
green = pygame.transform.scale2x(green)
#地刺
thron = pygame.image.load('source/thron.png')

# 生命值數字
pointFont = pygame.font.SysFont("Monospace",15)

#主角位置
x_c = 400
y_c = 400

#主角生命值
heart_c = 50

#RANK
rank = 1

#怪物碰撞檢測
Monster_moving = False
Charater_moving = False

#怪物
monster1  = pygame.image.load('source/monster1.png')
#BOSS
BOSS =  pygame.image.load('source/BOSS11.png')
#怪物生命值
heart_m = 10
#BOSS生命值
heart_BOSS = 100
#主角加速
run_clock = False
#主角血量減少
c_reduce = False
c_BOSS_reduce = False
#主角攻擊怪物
c_atk = False
c_atkBOSS = False
j_atk = False
#升級
global levelup
levelup = 'a'
#殺死怪物數量
kill_m = 0
#傳送陣
transfor = pygame.image.load('source/transfor.png')
x_trans = 370
y_trans = 40
#傳送
TRANS = False
#抵達圖1
ari_bg1 = True
#抵達圖2
ari_bg2 = False
#遊戲結束圖檔
game_over = pygame.image.load('source/game_over.png')
game_over = pygame.transform.scale(game_over,windowSize)
#過關
finish = pygame.image.load('source/done.jpg')
finish = pygame.transform.scale(finish,windowSize)
#音樂
pygame.mixer.music.load("source/music.mp3")
pygame.mixer.music.play(-1)

#BOSS階段音效
contrymachine = pygame.mixer.Sound("source/contrymachine.wav")
#攻擊音效
knife = pygame.mixer.Sound("source/knife.wav")
#GAME OVER 音效
GO = pygame.mixer.Sound("source/GO.wav")
#通關音效
win = pygame.mixer.Sound("source/win.wav")
#bg1範圍
leftwall_bg1 = 0
rightwall_bg1 = 970
topwall_bg1 = 300
bottomwall_bg1 = 655
m_top_rightwall_bg1 = 550
m_top_leftwall_bg1 = 420
m_top_topwall_bg1 = 400

#圖片播放計數
count = 0
count_atk=0

#怪物位置
x_m = random.randrange(50,windowSize[0]-50)
y_m = random.randrange(m_top_topwall_bg1,windowSize[1]-50)
#圖一怪物存在
bg1_m = True
#BOSS位置
x_boss = windowSize[0]/3
y_boss = windowSize[1]/2
BOSS_move = 0

side=0



done = False
while not done:
    if TRANS:
        screen.blit(bg2,(0,0))
        ari_bg2 = True
        bg1_m = False
        
    else:
        screen.blit(bg1,(0,0))
        ari_bg1 = False
        bg1_m = True
#主角 上下左右控制    
    Charater_moving = False
    keys = pygame.key.get_pressed()
#下
    if keys[pygame.K_s]:
        y_c += downclear_bg1(x_c,y_c)
        Charater_moving = True
        side="s"

#上
    elif keys[pygame.K_w]:
        y_c -= upclear_bg1(x_c,y_c)
        side="w"
        Charater_moving = True

#左
    elif keys[pygame.K_a]:
        x_c -= leftclear_bg1(x_c,y_c)
        side="a"
        Charater_moving = True

#右
    elif keys[pygame.K_d]:
        x_c += rightclear_bg1(x_c,y_c)
        side="d"
        Charater_moving = True

    
#移動
    if Charater_moving and side=="s":
            count+=1
            pOneImage = move(down1,down2,down3,count)
    elif Charater_moving and side=="w":
            count+=1
            pOneImage = move(up1,up2,up3,count)
    elif Charater_moving and side=="a":
            count+=1
            pOneImage = move(left1,left2,left3,count)
    elif Charater_moving and side=="d":
            count+=1
            pOneImage = move(right1,right2,right3,count)
#攻擊
    elif side=="s" and keys[pygame.K_j]:
            count+=1
            pOneImage=atk(atk_B1,atk_B2,atk_B3,count)
            knife.play()
            if keys[pygame.K_j]:
                j_atk = True
            else:
                j_atk = False
    elif side=="w" and keys[pygame.K_j]:
            count+=1
            pOneImage=atk(atk_F1,atk_F2,atk_F3,count)
            knife.play()
            if keys[pygame.K_j]:
                j_atk = True
            else:
                j_atk = False
    elif side=="a" and keys[pygame.K_j]:
            count+=1
            pOneImage=atk(atk_L1,atk_L2,atk_L3,count)
            knife.play()
            if keys[pygame.K_j]:
                j_atk = True
            else:
                j_atk = False
    elif side=="d" and keys[pygame.K_j]:
            count+=1
            pOneImage=atk(atk_R1,atk_R2,atk_R3,count)
            knife.play()
            if keys[pygame.K_j]:
                j_atk = True
            else:
                j_atk = False
    else:
        if side==0:
           pOneImage = standing_B

#碰撞後生命值減少
    if c_reduce:
        
        heart_c -= 1
        c_reduce = False
        
#攻擊怪物後 怪物生命減少
    c_atk = False

    if -35 < x_c-x_m < 40 and -45 < y_c-y_m <50:
        
        c_atk = True
        
    if c_atk and j_atk:

        heart_m -= 1
        c_atk = False
        j_atk = False
#碰撞到BOSS生命值減少
    if c_BOSS_reduce:
        heart_c -= 10
        c_BOSS_reduce = False
#攻擊BOSS BOSS生命減少
    c_atkBOSS = False
    if -20 < x_c-x_boss < 240 and -40 < y_c-y_boss <320:
        c_atkBOSS = True
    if c_atkBOSS and j_atk and ari_bg2:

        heart_BOSS -= 1
        c_atkBOSS = False
        j_atk = False
    #碰到怪物
    atk_m()
    
    #傳送陣
    trans()
    
    #生命值數字
    heart_c_label = pointFont.render(str(heart_c),1,(255,255,255))
    heart_m_label = pointFont.render(str(heart_m),1,(255,255,255))
    heart_BOSS_label = pointFont.render(str(heart_BOSS),1,(255,255,255))
    #殺死怪物數
    kill_monster = pointFont.render(str(kill_m),1,(255,255,255))
    #等級
    rank_label = pointFont.render(str(rank),1,(255,255,255))
    #狀態列
    HP = pointFont.render(str("HP:"),1,(255,255,255))
    KILL = pointFont.render(str("KILL:"),1,(255,255,255))   
    RANK = pointFont.render(str("RANK:"),1,(255,255,255))
        #RANK上升
    
    if  2<= kill_m <= 3:
        rank = 2
        if rank==2 and levelup=='a':
            heart_c =100
        levelup='b'
    elif 4<=kill_m <= 10:
        rank = 3
        if rank==3 and levelup=='b':
            heart_c =150
        levelup='c'
    elif 11<=kill_m <= 20:
        rank = 4
        if rank==4 and levelup=='c':
            heart_c =220
        levelup='d'
    elif 20<=kill_m:
        rank = 5
        if rank==5 and levelup=='d':
            heart_c =400
        levelup='e'


        
#主角生命> or < 0判斷
    if heart_c >0 and ari_bg1==0 :
            screen.blit(transfor,[x_trans,y_trans])
            screen.blit(pOneImage,[x_c,y_c])
            screen.blit(title,[0,0])
            screen.blit(green,[95,0])
            screen.blit(heart_c_label,[x_c-10,y_c-10])
            screen.blit(heart_m_label,[x_m-10,y_m-10])           
            #狀態列數值
            screen.blit(heart_c_label,[150,0])                          
            screen.blit(HP,[100,0])
            screen.blit(kill_monster,[150,20])
            screen.blit(KILL,[100,20])
            screen.blit(rank_label,[150,40])
            screen.blit(RANK,[100,40])
    elif  ari_bg2 and heart_c >0 :
            screen.blit(heart_BOSS_label,[x_boss,y_boss])
            screen.blit(pOneImage,[500,680])
            screen.blit(title,[0,0])
            screen.blit(green,[95,0])
            screen.blit(heart_c_label,[x_c-10,y_c-10])
            
            
            screen.blit(heart_c_label,[150,0])                          
            screen.blit(HP,[100,0])
            screen.blit(kill_monster,[150,20])
            screen.blit(KILL,[100,20])
    else:
            screen.blit(game_over,(0,0))
            pygame.mixer.music.stop()
            GO.play()
#怪物生命> or < 0判斷
    if heart_m > 0 and ari_bg1 == 0 and bg1_m and heart_c>0:
            screen.blit(monster1,[x_m,y_m])

    elif ari_bg1==0 and heart_m<0:
            kill_m += 1
            heart_m=10
            x_m = random.randrange(50,windowSize[0]-50)
            y_m = random.randrange(m_top_topwall_bg1,windowSize[1]-50)
            screen.blit(monster1,[x_m,y_m])
#BOSS
    if ari_bg2 and heart_c >0:
        if heart_BOSS >0:
            screen.blit(thron,[x_m,y_m])
            #碰到BOSS
            atk_BOSS()
            #BOSS亂動
            x_boss += math.cos(BOSS_move)*10
            y_boss += math.sin(BOSS_move)*10
            screen.blit(BOSS,[x_boss,y_boss])
            screen.blit(heart_BOSS_label,[x_boss,y_boss])
            BOSS_move +=0.1
            if 78<=heart_BOSS <= 80:
                contrymachine.play()
        elif heart_BOSS<0 :
            screen.blit(finish,(0,0))
            pygame.mixer.music.stop()
            win.play()
            

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = True
    pygame.display.flip()
#加速
    if keys[pygame.K_LSHIFT]:
        run_clock = True
        if run_clock:
            clock.tick(100)
            run_clock = False
    else:
        clock.tick(32)
pygame.quit()
    
