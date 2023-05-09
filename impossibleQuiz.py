"""
NOTE: This program ONLY works with a display of size 1920x1080
To set up environment to run program, follow this link "https://shorturl.at/hmxEP" (without the quotes)
or, if you don't trust the link, search "The Impossible Quiz" on the website Poki.com
Once loaded, maximize your window and zoom to 200%, making sure you are at the top of the page
You will have to press "Begin" and "Start" manually.
You may run the program once you have followed all instructions thus far and are on the first question

Enjoy!

julius-alexander 9 May 2023
"""
import pyautogui as pg
import time

MOVE = pg.moveTo
TOP = -580
BOTTOM = -410
LEFT = 605
RIGHT = 1050

# Begin
MOVE(RIGHT, BOTTOM)

# Question 1
pg.leftClick()
pg.leftClick()
MOVE(LEFT, BOTTOM)

# Question 2
pg.leftClick()
MOVE(LEFT, TOP)

# Question 3
pg.leftClick()
pg.moveTo(865, -760)

# Question 4
pg.mouseDown()
time.sleep(0.2)
pg.mouseUp()

# Question 5
pg.moveTo(1280, -440)
pg.move(1, 1)
pg.moveTo(415, -550)
pg.leftClick()
MOVE(LEFT, BOTTOM)

# Question 6
pg.leftClick()
MOVE(RIGHT, BOTTOM)

# Question 7
pg.moveTo(1050, -410)
pg.leftClick()

# Question 8
pg.moveTo(650, -570)
pg.leftClick()
MOVE(RIGHT, TOP)

# Question 9
pg.leftClick()
pg.moveTo(710, -430)

# Question 10
pg.leftClick()
MOVE(RIGHT, TOP)
time.sleep(2)

# Question 11
pg.leftClick()
pg.moveTo(759, -838)

# Question 12
pg.leftClick()
MOVE(RIGHT, TOP)

# Question 13
pg.leftClick()

# Question 14
pg.leftClick()

# Question 15
pg.moveTo(930, -485)
pg.leftClick()
pg.moveTo(1087, -604)
pg.leftClick()
pg.moveTo(733, -603)
pg.leftClick()
pg.moveTo(621, -489)
pg.leftClick()
pg.moveTo(652, -602)
pg.leftClick()
MOVE(RIGHT, TOP)

# Question 16
pg.leftClick()
pg.moveTo(420, -838)
time.sleep(0.2)

# Question 17
pg.mouseDown()

pg.mouseUp()
pg.moveTo(702, -540)

# Question 18
pg.leftClick()

# Question 19
pg.moveTo(840, -458)
pg.leftClick()
pg.moveTo(944, -605)
pg.leftClick()
pg.moveTo(1235, -607)
pg.leftClick()
pg.leftClick()
pg.moveTo(1098, -610)
pg.leftClick()
pg.moveTo(1213, -343)
pg.leftClick()
MOVE(LEFT, BOTTOM)

# Question 20
pg.leftClick()
MOVE(LEFT, TOP)
time.sleep(2)

# Question 21
pg.leftClick()
MOVE(RIGHT, BOTTOM)

# Question 22
pg.leftClick()
MOVE(RIGHT, BOTTOM)

# Question 23
pg.leftClick()
pg.moveTo(456, -252)

# Question 24
pg.leftClick()
MOVE(LEFT, TOP)

# Question 25
pg.leftClick()
pg.moveTo(786, -595)

# Question 26
pg.leftClick()
MOVE(RIGHT, BOTTOM)

# Question 27
pg.leftClick()
pg.moveTo(560, -485)

# Question 28
pg.leftClick()
MOVE(LEFT, BOTTOM)

# Question 29
pg.leftClick()

# Question 30
pg.moveTo(460, -438)
pg.moveTo(987, -610)
pg.leftClick()
MOVE(LEFT, BOTTOM)

# Question 31
pg.leftClick()
MOVE(RIGHT, TOP)

# Question 32
pg.leftClick()
MOVE(LEFT, TOP)

# Question 33
pg.leftClick()
time.sleep(0.2)

# Question 34
pg.moveTo(50, -440)     # elephants
time.sleep(6)

# Question 35
pg.moveTo(850, -500)
time.sleep(5)           # game over button
pg.leftClick()
MOVE(RIGHT, TOP)
time.sleep(2.5)

# Question 36
pg.leftClick()

# Question 37
pg.leftClick()

# Question 38
pg.leftClick()
MOVE(LEFT, TOP)

# Question 39
pg.leftClick()

# Question 40
pg.moveTo(632, -570)
pg.moveTo(900, -570)
pg.leftClick()

# Question 41
pg.moveTo(589, -847)
pg.leftClick()

# Question 42
pg.moveTo(526, -350)
pg.leftClick()
MOVE(RIGHT, BOTTOM)

# Question 43
pg.leftClick()

# Question 44
pg.moveTo(1064, -745)
pg.mouseDown()
pg.moveTo(859, -571)
pg.mouseUp()
pg.moveTo(1139, -799)
pg.leftClick()
MOVE(RIGHT, TOP)

# Question 45
pg.leftClick()
MOVE(LEFT, BOTTOM)

# Question 46
pg.leftClick()
time.sleep(5)

# Question 47
pg.moveTo(908, -661)
pg.leftClick()
MOVE(RIGHT, TOP)

# Question 48
pg.leftClick()
MOVE(RIGHT, BOTTOM)

# Question 49
pg.leftClick()
MOVE(LEFT, TOP)

# Question 50
pg.leftClick()
time.sleep(0.2)

# Question 51
pg.moveTo(807, -544)
for i in range(20):
    pg.leftClick()
time.sleep(2.5)           # fight

# Question 52
pg.moveTo(942, -559)
pg.leftClick()
time.sleep(4)           # carrot

# Question 53
MOVE(LEFT, BOTTOM)
pg.leftClick()

# Question 54
MOVE(RIGHT, BOTTOM)
pg.leftClick()

# Question 55
MOVE(RIGHT, TOP)
pg.leftClick()
time.sleep(6)

# Question 56
pg.moveTo(718, -755)
pg.leftClick()
pg.moveTo(1109, -410)
pg.leftClick()
pg.moveTo(703, -755)
pg.leftClick()
pg.moveTo(761, -375)
pg.leftClick()
MOVE(LEFT, TOP)

# Question 57
pg.leftClick()
MOVE(RIGHT, BOTTOM)

# Question 58
pg.leftClick()

# Question 59
pg.moveTo(497, -366)
start_time = time.time()
while (time.time() - start_time) < 13:
    pg.leftClick()
time.sleep(2)

# Question 60
pg.moveTo(602, -485)
pg.leftClick()
MOVE(LEFT, TOP)

# Question 61
pg.leftClick()
pg.moveTo(495, -465)

# Question 62
pg.leftClick()
MOVE(RIGHT, TOP)

# Question 63
pg.leftClick()
MOVE(RIGHT, BOTTOM)

# Question 64
pg.leftClick()

# Question 65
pg.moveTo(827, -702)
pg.leftClick()

# Question 66
pg.moveTo(1113, -727)
pg.leftClick()

# Question 67
pg.moveTo(550, -700)
pg.leftClick()

# Question 68
pg.moveTo(574, -478)
time.sleep(2)

for i in range(13):
    pg.moveTo(894, -834, 1, pg.easeInQuad)
    pg.moveTo(574, -478, 1, pg.easeInQuad)
MOVE(RIGHT, BOTTOM)
time.sleep(2)

# Question 69
pg.leftClick()
MOVE(LEFT, BOTTOM)

# Question 70
pg.leftClick()
MOVE(RIGHT, TOP)

# Question 71
pg.leftClick()

# Question 72
pg.moveTo(401, -587)
pg.leftClick()
MOVE(RIGHT, TOP)
time.sleep(3)

# Question 73
pg.leftClick()
MOVE(LEFT, BOTTOM)

# Question 74
pg.leftClick()
pg.moveTo(416, -742)
time.sleep(1)

# Question 75
for i in range(20):
    pg.leftClick()

# Question 76
pg.moveTo(507, -464)
pg.leftClick()
pg.moveTo(1144, -457)
pg.leftClick()
pg.leftClick()

# Question 77
pg.moveTo(555, -372)
pg.leftClick()
MOVE(LEFT, TOP)

# Question 78
pg.leftClick()

# Question 79
pg.moveTo(542, -366)        # answer is a horseshoe
pg.leftClick()
MOVE(LEFT, TOP)

# Question 80
pg.leftClick()

# Question 81 - Lightning rod
pg.moveTo(831, -460)
for i in range(8):
    pg.moveTo(831, -620, 1, pg.easeInQuad)
    pg.moveTo(831, -460, 1, pg.easeInQuad)

pg.moveTo(1177, -525)
pg.leftClick()
time.sleep(0.2)

# Question 82 - Toenail/ Bomb
pg.moveTo(1240, -632)
pg.leftClick()
pg.moveTo(1217, -565)
pg.leftClick()
pg.moveTo(1173, -494)
pg.leftClick()
pg.moveTo(1095, -447)
pg.leftClick()
pg.moveTo(975, -408)
pg.leftClick()
pg.moveTo(774, -396)
pg.leftClick()
pg.moveTo(651, -415)
pg.leftClick()
pg.moveTo(568, -455)
pg.leftClick()
pg.moveTo(517, -519)
pg.leftClick()
pg.moveTo(482, -584)
pg.leftClick()
MOVE(RIGHT, BOTTOM)


# Question 83
pg.leftClick()
time.sleep(0.2)

# Question 84
pg.moveTo(829, -500)        # press button to start minigame

pg.moveTo(650, -727)        # first safety, under star
time.sleep(8)
pg.moveTo(513, -841)        # top corner safety
time.sleep(5)
pg.moveTo(502, -550)        # grab first skip
time.sleep(3)
pg.moveTo(1201, -660)        # skip from top right
time.sleep(1)               # 3 seconds was too slow
pg.moveTo(1164, -449)        # shooting star from bottom left
time.sleep(3)

# Question 85 - assume 84 is correct...
MOVE(RIGHT, TOP)
pg.leftClick()


# Question 86
MOVE(LEFT, BOTTOM)
pg.leftClick()


# Question 87
pg.moveTo(456, -807)
pg.leftClick()
time.sleep(0.2)

# Question 88
pg.moveTo(800, -485)
for i in range(60):
    pg.leftClick()
time.sleep(2)

# Question 89
MOVE(RIGHT, TOP)
pg.leftClick()


# Question 90
MOVE(RIGHT, BOTTOM)
pg.leftClick()


# Question 91 - tear the paper
pg.moveTo(633, -492)
pg.moveTo(704, -524, 1)
pg.moveTo(760, -522, 1)     # ap^p in appeared
pg.moveTo(800, -512, 1)     # r^ed in appeared
pg.moveTo(869, -509, 1)     # t^he
pg.moveTo(918, -514, 1)     # t^op
pg.moveTo(944, -528, 1)     # below the o in most likely
pg.moveTo(1000, -549, 1)    # above the e in likely
time.sleep(2.5)

# Question 92
pg.moveTo(961, -367)        # 6
pg.leftClick()
pg.moveTo(404, -411)        # 1
pg.leftClick()
pg.moveTo(759, -326)        # 4
pg.leftClick()
pg.moveTo(1153, -398)       # 8
pg.leftClick()
pg.moveTo(849, -374)        # 5
pg.leftClick()
pg.moveTo(511, -343)        # 2
pg.leftClick()
pg.moveTo(1065, -387)       # 7
pg.leftClick()
pg.moveTo(1272, -389)       # 9
pg.leftClick()
pg.moveTo(648, -380)        # 3
pg.leftClick()
time.sleep(8)

# Question 93 - click and drag bomb
pg.moveTo(1249, -853)
pg.mouseDown()
pg.moveTo(1095, -700)
pg.mouseUp()
pg.moveTo(1245, -855)
pg.leftClick()


# Question 94 - do nothing
time.sleep(19)

# Question 95 - distracted cat
pg.moveTo(1020, -257)
time.sleep(8)
pg.moveTo(831, -544)
pg.leftClick()

# Question 96
MOVE(LEFT, BOTTOM)
pg.leftClick()

# Question 97
MOVE(RIGHT, BOTTOM)
pg.leftClick()

# Question 98
pg.moveTo(1086, -510)
pg.leftClick()
pg.moveTo(568, -646)
pg.leftClick()
pg.moveTo(1085, -509)
pg.leftClick()
pg.moveTo(1083, -640)
pg.leftClick()

# Question 99 and 100
pg.moveTo(1095, -595)
time.sleep(13)
pg.leftClick()
pg.leftClick()
pg.leftClick()
time.sleep(14)

# Question 101 - spell chihuahua
pg.moveTo(775, -390)
pg.leftClick()
pg.moveTo(871, -439)
pg.leftClick()
pg.moveTo(922, -496)
pg.leftClick()
pg.moveTo(871, -439)
pg.leftClick()
pg.moveTo(887, -503)
pg.leftClick()
pg.moveTo(655, -430)
pg.leftClick()
pg.moveTo(871, -439)
pg.leftClick()
pg.moveTo(887, -503)
pg.leftClick()
pg.moveTo(655, -430)
pg.leftClick()
time.sleep(8)

# Question 102 -  touch the dots

pg.moveTo(470, -732)
pg.moveTo(789, -360)
pg.moveTo(1016, -753)
pg.moveTo(410, -456)
pg.moveTo(1214, -400)
pg.moveTo(1129, -811)
pg.moveTo(801, -549)
pg.moveTo(1211, -536)
pg.moveTo(526, -668)
pg.moveTo(756, -267)
time.sleep(3.5)
pg.moveTo(637, -794)
pg.moveTo(1278, -771)
pg.moveTo(395, -579)
pg.moveTo(831, -584)
time.sleep(8)

# Question 103
pg.moveTo(1010, -500)
for i in range(10):
    pg.leftClick()

time.sleep(7)
pg.moveTo(1200, -400)
pg.leftClick()
time.sleep(6)

# Question 105
pg.moveTo(612, -372)
pg.leftClick()
pg.moveTo(520, -469)
pg.leftClick()
pg.moveTo(691, -575)
pg.leftClick()
pg.moveTo(520, -469)
pg.leftClick()
pg.moveTo(691, -575)
pg.leftClick()
pg.moveTo(520, -469)
pg.leftClick()
time.sleep(5)

# Question 106
pg.moveTo(571, -407)
time.sleep(3)
pg.moveTo(571, -93, 1)
time.sleep(17)
pg.moveTo(511, -446)
pg.leftClick()
time.sleep(5)

# Question 107
for i in range(4):
    MOVE(LEFT, TOP)
    MOVE(RIGHT, TOP)
    MOVE(RIGHT, BOTTOM)
    MOVE(LEFT, BOTTOM)
time.sleep(9)

# Question 108 - 4 8 15 16 23 42 EXECUTE
pg.moveTo(x=710, y=-423)
pg.leftClick()
pg.moveTo(x=766, y=-350)
pg.leftClick()
pg.moveTo(x=1015, y=-421)
pg.leftClick()
pg.moveTo(x=780, y=-353)
pg.leftClick()
pg.moveTo(x=486, y=-424)
pg.leftClick()
pg.moveTo(x=787, y=-427)
pg.leftClick()
pg.moveTo(x=782, y=-349)
pg.leftClick()
pg.moveTo(x=481, y=-426)
pg.leftClick()
pg.moveTo(x=867, y=-425)
pg.leftClick()
pg.moveTo(x=794, y=-354)
pg.leftClick()
pg.moveTo(x=565, y=-421)
pg.leftClick()
pg.moveTo(x=636, y=-422)
pg.leftClick()
pg.moveTo(x=779, y=-356)
pg.leftClick()
pg.moveTo(x=714, y=-421)
pg.leftClick()
pg.moveTo(x=571, y=-419)
pg.leftClick()
pg.moveTo(x=1126, y=-350)
pg.leftClick()
time.sleep(10)

# Question 109
pg.moveTo(828, -527)
for i in range(55):
    pg.leftClick()
pg.moveTo(910, -362)
for i in range(10):
    pg.leftClick()
time.sleep(13)

# Question 110
pg.moveTo(x=1276, y=-258)
pg.mouseDown()
pg.mouseUp()
pg.mouseDown()
pg.mouseUp()
pg.moveTo(x=1201, y=-255)
pg.mouseDown()
pg.mouseUp()
pg.moveTo(x=1137, y=-256)
pg.mouseDown()
pg.mouseUp()
pg.moveTo(x=1062, y=-258)
pg.mouseDown()
pg.mouseUp()
pg.moveTo(x=995, y=-259)
pg.mouseDown()
pg.mouseUp()
pg.moveTo(x=921, y=-257)
pg.mouseDown()
pg.mouseUp()
