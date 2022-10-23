import pygame
from threading import Timer
import random
import sys

x_moving_object = 700
x_moving_object1 = 900
x_moving_object2 = 800
x = 0
y = 0
times = 0

width1 = 20
width2 = 10
width3 = 30

vel1 = 3
vel2 = 7
vel3 = 5

points = 0
lives = 3

xrepeat = 0
x1repeat = 0
x2repeat = 0

speedRepeat = 0
jumpRepeat = 0

speedRewardx = 15000
jumpRewardx = 15000

pause = False

jumpCount = 10
isJump = False

vel = 0
cx, cy = (0,0)

clicked = 0

resetClicked = 0

jumpVariable = 2

timeEachcycle = 0.0000000001

startIntro = True

gameStop = False

startQuit = True

pauseUn = False

playerColor = 150, 200, 20

shape = 1

pointAmount = 1

pygame.init()
def game():
    global x_moving_object
    global x_moving_object1
    global x_moving_object2
    global x
    global y
    global times
    global points
    global width1
    global width2
    global width3
    global lives
    global pause
    global jumpCount
    global isJump
    global speedRewardx
    global jumpRewardx
    global vel
    global cx, cy
    global clicked
    global resetClicked
    global jumpVariable
    global startIntro
    global gameStop
    global startQuit
    global timeEachcycle
    global pauseUn
    global playerColor
    global shape
    global pointAmount

    win = pygame.display.set_mode((640, 575), pygame.RESIZABLE)
   # win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN )
    pygame.display.set_caption("Jumping Game")

    x = 50
    y = 450
    width = 20
    height = 20
    vel = 9
    isJump = False
    jumpCount = 10

    def reset():
        global x_moving_object
        global x_moving_object1
        global x_moving_object2
        global x
        global y
        global points
        global width1
        global width2
        global width3
        global vel1
        global vel2
        global vel3
        global lives
        global xrepeat
        global x1repeat
        global x2repeat
        global times
        global pause
        global jumpCount
        global isJump
        global speedRewardx
        global jumpRewardx
        global vel
        global clicked
        global resetClicked
        global cx, cy
        global jumpVariable
        global timeEachcycle
        global startIntro
        global gameStop
        global shape
        global pointAmount
        x_moving_object = 700
        x_moving_object1 = 900
        x_moving_object2 = 800
        speedRewardx = 20000
        jumpRewardx = 20000
        x = 50
        y = 450
        times = 0
        width1 = 20
        width2 = 10
        width3 = 30
        vel1 = 3
        vel2 = 7
        vel3 = 5
        points = 0
        lives = 3
        xrepeat = 0
        x1repeat = 0
        x2repeat = 0
        vel = 9
        jumpCount = 10
        isJump = False
        pause = False
        resetClicked = 0
        cx, cy = (0, 0)
        jumpVariable = 2
        timeEachcycle = 0.0000000001
        shape = 1
        pointAmount = 1
        startIntro = False
        if gameStop == True:
            cycle()
            gameStop = False
        else:
            game()
    def endScreen():
        global timeEachcycle
        global gameStop
        global vel
        timeEachcycle = 10000
        vel = 0
        gameStop = True

    def cycle():
        global x_moving_object
        global x_moving_object1
        global x_moving_object2
        global x
        global y
        global points
        global width1
        global width2
        global width3
        global vel1
        global vel2
        global vel3
        global lives
        global xrepeat
        global x1repeat
        global x2repeat
        global speedRewardx
        global jumpRewardx
        global speedRepeat
        global jumpRepeat
        global vel
        global jumpVariable
        global timeEachcycle
        global pointAmount
        x_moving_object -= vel1
        x_moving_object1 -= vel2
        x_moving_object2 -= vel3
        speedRewardx -= 5
        jumpRewardx -= 7
        if y == 450:
            if  abs(x - x_moving_object) <= 20:
                if xrepeat == 0:
                    lives -= 1
                    print("You lost a life")
                    xrepeat += 1
            if  abs(x - x_moving_object1) <= 20:
                if x1repeat == 0:
                    lives -= 1
                    print("You lost a life")
                    x1repeat += 1
            if  abs(x - x_moving_object2) <= 20:
                if x2repeat == 0:
                    lives -= 1
                    print("You lost a life")
                    x2repeat += 1
            if abs(y - 375) <= 50 or abs(y - 375) >= 50:
                if  abs(x - speedRewardx) <= 50:
                    if speedRepeat == 0:
                        vel += 1
                        print("You gained extra speed")
                        speedRepeat += 1
                        speedRewardx = 15000
            if abs(y - 375) <= 50 or abs(y - 375) >= 50:
                if  abs(x - jumpRewardx) <= 50:
                    if jumpRepeat == 0:
                        jumpVariable += 1
                        print("You gained extra height when you jump")
                        jumpRepeat += 1
                        jumpRewardx = 15000
        if x_moving_object < 0:
            x_moving_object = 700
            points += pointAmount
            width1 = random.randint(10, 40)
            vel1 = random.randint(3, 8)
            xrepeat = 0
        if x_moving_object1 < 0:
            x_moving_object1 = 900
            points += pointAmount
            width2 = random.randint(10, 40)
            vel2 = random.randint(3, 8)
            x1repeat = 0
        if x_moving_object2 < 0:
            x_moving_object2 = 800
            points += pointAmount
            width3 = random.randint(10, 40)
            vel3 = random.randint(3, 8)
            x2repeat = 0
        if speedRewardx < 0:
            speedRewardx = 15000
            speedRepeat = 0
        if jumpRewardx < 0:
            jumpRewardx = 15000
            jumpRepeat = 0
        Timer(timeEachcycle, cycle).start()

    while pause == False:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
            if event.type == pygame.MOUSEBUTTONUP:
                cx, cy = pygame.mouse.get_pos()
                print(cx, cy)
                print("yes")
        win.fill((40, 40, 40))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 640 - 20 - vel:
            x += vel
        if keys[pygame.K_0]:
            if times == 1:
                pass
            else:
                times += 1
                startIntro = False
                cycle()
        if keys[pygame.K_1]:
            print("Reset")
            reset()
        if not (isJump):
            """if keys[pygame.K_UP] and y > vel:
                y -= vel
            if keys[pygame.K_DOWN] and y < 450 - 20 - vel:
                y += vel"""
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                if gameStop == True:
                    pass
                elif pauseUn == True:
                    pass
                else:
                    isJump = True
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * jumpVariable/10
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False

        if shape == 1:
            pygame.draw.rect(win, (playerColor), (x, y, width, height))
        if shape == 2:
            pygame.draw.circle(win, playerColor, (x+10, y+10), 10, 0)
            pointAmount = 2
        if shape == 3:
            #pygame.draw.polygon(surface=win, color=(playerColor), points=[(x, y + 469), (x + 10,y + 450), (x + 20, y + 469)])
            pygame.draw.polygon(surface=win, color=(playerColor), points=[(x, y + 19), (x + 10, y), (x + 20, y + 19)])
            #pygame.draw.polygon(surface=win, color=(playerColor), points=[(550, 153), (560, 138), (570, 153)])
            pointAmount = 3
        if shape == 4:
            ellipse_rect = pygame.Rect(x, y, 30, 20)
            pygame.draw.ellipse(win, (playerColor), ellipse_rect)
            pointAmount = 4

        font = pygame.font.SysFont("comicsans", 50)
        fontSmall = pygame.font.SysFont("comicsans", 27)
        fontSmaller = pygame.font.SysFont("comicsans", 15)

        green = 150, 200, 20
        darkGreen = 0,128,0
        #0, 100, 0
        # 34,139,34
        startColor = green
        startColorReset = green
        mx, my = pygame.mouse.get_pos()
        if mx > 470 and mx < 625:
            if my > 520 and my < 570:
                startColor = darkGreen
        if mx > 12 and mx < 167:
            if my > 522 and my <  565:
                startColorReset = darkGreen

        #Pause and Settings Image
        image = pygame.image.load('playPause.jfif')
        imageS = pygame.image.load('hjgbjgidpjz.jpeg')
        image = pygame.transform.scale(image, (35, 35))
        imageS = pygame.transform.scale(imageS, (35, 35))

        brighten = 128

        dark = pygame.Surface((image.get_width(), image.get_height()), flags=pygame.SRCALPHA)
        dark.fill((100, 100, 100, 0))
        #image.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD)

        #image.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        if mx > 589 and mx < 625:
            if my > 48 and my < 85:
                imageS.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        win.blit(imageS, (590, 50))
        if mx > 549 and mx < 585:
            if my > 48 and my < 85:
                image.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        win.blit(image, (550, 50))
        if cx > 549 and cx < 585:
            if cy > 48 and cy < 85:
                if startIntro == True:
                    pass
                else:
                    cx, cy = (0, 0)
                    if pauseUn == False:
                        timeEachcycle = 10000
                        vel = 0
                        print(pauseUn)
                        pauseUn = True
                    else:
                        print(pauseUn)
                        timeEachcycle = 0.0000000001
                        vel = 9
                        cycle()
                        pauseUn = False
        if pauseUn == True:
            pauseLabel = font.render("Paused", bool(1), (255, 255, 255))
            win.blit(pauseLabel, (250, 300))

            colorLab = fontSmall.render("Colors -", bool(1), (255, 255, 255))
            win.blit(colorLab, (425, 100))
            shapeLab = fontSmall.render("Shapes -", bool(1), (255, 255, 255))
            win.blit(shapeLab, (415, 135))

            #Choose your color

            greenColor = 150, 200, 20
            blueColor = 67, 84, 255
            orangeColor = 255, 165, 0
            redColor = 250, 0, 0
            purpleColor = 172, 79, 198
            grayColor = 128, 128, 128

            if cx > 500 and cx < 520:
                if cy > 99 and cy < 120:
                    playerColor = greenColor
            if cx > 525 and cx < 545:
                if cy > 99 and cy < 120:
                    playerColor = blueColor
            if cx > 550 and cx < 570:
                if cy > 99 and cy < 120:
                    playerColor = orangeColor
            if cx > 575 and cx < 595:
                if cy > 99 and cy < 120:
                    playerColor = redColor
            if cx > 600 and cx < 620:
                if cy > 99 and cy < 120:
                    playerColor = purpleColor
            if cx > 500 and cx < 545:
                if cy > 135 and cy < 155:
                    shape = 1
            if points >= 50:
                if cx > 525 and cx < 545:
                    if cy > 135 and cy < 155:
                        shape = 2
            if points >= 75:
                if cx > 550 and cx < 565:
                    if cy > 135 and cy < 155:
                        shape = 3
            if points >= 100:
                if cx > 575 and cx < 605:
                    if cy > 135 and cy < 155:
                        shape = 4


            pygame.draw.rect(win, (greenColor), (500, 100, 20, 20))
            pygame.draw.rect(win, (blueColor), (525, 100, 20, 20))
            pygame.draw.rect(win, (orangeColor), (550, 100, 20, 20))
            pygame.draw.rect(win, (redColor), (575, 100, 20, 20))
            pygame.draw.rect(win, (purpleColor), (600, 100, 20, 20))
            pygame.draw.rect(win, (playerColor), (500, 135, 20, 20))
            if points >=  50:
                pygame.draw.circle(win, playerColor, (535, 145), 10, 20)
            if points >= 75:
                pygame.draw.polygon(surface=win, color=(playerColor), points=[(550, 153), (560, 138), (570, 153)])
            if points >= 100:
                ellipse_rect = pygame.Rect(575, 135, 30, 20)
                pygame.draw.ellipse(win, (playerColor), ellipse_rect)


            if points < 50:
                pygame.draw.rect(win, (grayColor), (525, 135, 20, 20))
                circleLabel = fontSmall.render("50", bool(1), (255, 255, 255))
                win.blit(circleLabel, (525, 137))
            if points < 75:
                pygame.draw.rect(win, (grayColor), (550, 135, 20, 20))
                triangleLabel = fontSmall.render("75", bool(1), (255, 255, 255))
                win.blit(triangleLabel, (550, 137))
            if points < 100:
                pygame.draw.rect(win, (grayColor), (575, 135, 20, 20))
                triangleLabel = fontSmaller.render("100", bool(1), (255, 255, 255))
                win.blit(triangleLabel, (576, 140))

        pygame.draw.rect(win, (startColor), (475, 525, 150, 40))
        pygame.draw.rect(win, (startColorReset), (15, 525, 150, 40))
        pygame.draw.rect(win, (255, 0, 0), (x_moving_object, 450, width1, height))
        pygame.draw.rect(win, (250, 0, 0), (x_moving_object1, 450, width2, height))
        pygame.draw.rect(win, (250, 0, 0), (x_moving_object2, 450, width3, height))
        pygame.draw.rect(win, (255, 215, 0), (speedRewardx, 375, 30, 30))
        pygame.draw.rect(win, (192,192,192), (jumpRewardx, 375, 30, 30))
        pointsLabel = font.render(f"Points: {points}", bool(1), (255, 255, 255))
        livesLabel = font.render(f"Lives: {lives}", bool(1), (255, 255, 255))
        speedLabel = font.render(f"Speed: {vel}", bool(1), (255, 255, 255))
        jumpLabel = font.render(f"Jump: {jumpVariable}", bool(1), (255, 255, 255))
        if startQuit == True:
            startButton = font.render("Start", bool(1), (255, 255, 255))
            win.blit(startButton, (510, 530))
            pygame.display.update()
        if startQuit == False:
            quitButton = font.render("Quit", bool(1), (255, 255, 255))
            win.blit(quitButton, (510, 530))
            pygame.display.update()
        resetButton = font.render("Reset", bool(1), (255, 255, 255))
        win.blit(pointsLabel, (10, 10))
        win.blit(livesLabel, (500, 10))
        win.blit(speedLabel, (10, 50))
        win.blit(jumpLabel, (10, 90))
        win.blit(resetButton, (42, 530))
        if startIntro == True:
            pygame.draw.rect(win, (250, 0, 0), (15, 195, 20, 20))
            pygame.draw.rect(win, (192,192,192), (15, 250, 20, 20))
            pygame.draw.rect(win, (255, 215, 0), (15, 305, 20, 20))
            startLabel = font.render("Stay away from red boxes", bool(1), (255, 255, 255))
            startLabel2 = font.render("Silver boxes give you a jump boost", bool(1), (255, 255, 255))
            startLabel3 = font.render("Gold boxes give you a speed boost", bool(1), (255, 255, 255))
            InsLabel = font.render("Press '0' to start - Press '1' to reset", bool(1), (255, 255, 255))
            win.blit(startLabel, (50, 190))
            win.blit(startLabel2, (50, 245))
            win.blit(startLabel3, (50, 300))
            win.blit(InsLabel, (25, 355))
            pygame.display.update()
        if lives <= 0:
            endgameLabel = font.render("Game Over", bool(1), (255, 255, 255))
            endgamePoints = font.render(f"Points: {points}", bool(1), (255, 255, 255))
            win.blit(endgameLabel, (225, 250))
            win.blit(endgamePoints, (225, 300))
            pygame.display.update()
            endScreen()
        if startQuit == False:
            if cx > 470 and cx < 625:
                if cy > 520 and cy < 570:
                    cx, cy = (0, 0)
                    print("quit")
                    pygame.quit()
                    sys.exit()
        if cx > 470 and cx < 625:
            if cy > 520 and cy < 570:
                if clicked == 0:
                    print("Start")
                    clicked += 1
                    startIntro = False
                    startQuit = False
                    print(clicked)
                    cx, cy = (0, 0)
                    cycle()
        if cx > 12 and cx < 167:
            if cy > 522 and cy <  565:
                if startIntro == True:
                    pass
                else:
                    if resetClicked == 0:
                        print("Reset")
                        resetClicked += 1
                        reset()
        pygame.display.update()

    pygame.quit()

game()