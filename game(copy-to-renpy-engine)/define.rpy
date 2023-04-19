#角色定義#########################
define sl_full = Character("蘇凜", color="#c8ffc8")

##################################
define sl = Character("我")
define sa = Character("???")
define oldman = Character("老爺子")


define noname_1 = Character("???")

define rando_1 = Character("平民")
define rando_2 = Character("平民")
define rando_3 = Character("平民")
define rando_4 = Character("平民")


define crew_1 = Character("船員")
define crew_2 = Character("船員")
define crew_3 = Character("船員")

#背景定義###########################
image ship_1 = "background/ship/bg ship 1.png"
image ship_2 = "background/ship/bg ship 2.png"
image ship_3 = "background/ship/bg ship 3.png"

image ship_lobby = "background/ship/bg ship lobby.png"
image ship_hallway = "background/ship/bg ship hallway.png"

#劇情值定義#####################
default dont_open_door_saya = False
default persistent.vp_appear = False
default persistent.know_name = False

# 轉場定義 ####################
define slowdissolve = Dissolve(1.0)
