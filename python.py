import pyautogui as pag
import time
import os
import sys

print(''' before run the code read readme file or help file. otherwise It happens disaster
''')
Que =input("Newly installed Corel draw?(Settings have not changed) [(yes) or (no)]")
for i in range (1,6):
    time.sleep(1)
    print(i)
if Que == 'yes':
    #create new windows in corel draw (its to work if Newly installed Corel draw and Settings have not changed)   
    pag.click(x=77, y=153)
    time.sleep(1)
    pag.press('backspace')
    pag.typewrite('python_backgrand',interval=0)
    pag.click(x=990, y=442)
    pag.doubleClick(x=931, y=553,interval = 0.25)
    pag.typewrite('90')
    pag.doubleClick(x=925, y=585,interval= 0.25)
    pag.typewrite('50',interval=0.25)
    pag.click(x=960, y=618,interval=.025)
    pag.click(x=1001, y=659)
    pag.typewrite('300',interval=0.25)
    pag.click()
    pag.click(x=1025, y=735,interval= 0.25)
elif Que == 'no' :
    print('continuee')
else :
    sys.exit
    
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#ADD COLOR
pag.click(x=80, y=970,interval=0.5)
pag.click(x=80, y=926,interval=0.5)
pag.click(x=55, y=974,interval=0.5)
pag.click(x=65, y=706,interval=0.5)
#add yello color
pag.click(x=1131, y=329,interval=0.5)
pag.moveTo(1003,518,2)
pag.doubleClick()
pag.typewrite('#FFD140',interval=0.5)
pag.click(x=1133, y=763,interval=0.5)
pag.moveTo(1133,327,1)
pag.click()
#add red color
pag.moveTo(1000, 518,2)
pag.doubleClick()
pag.typewrite('#ff0066',interval=0.5)
pag.click(x=1133, y=763,interval=0.5)
pag.moveTo(1133,327,0.5)
pag.click()
#add blue color
pag.moveTo(1000, 518,2)
pag.doubleClick()
pag.typewrite('#4A89BE',interval=0.5)
pag.click(x=1133, y=763,interval=0.5)
#complate press ok
pag.moveTo(1073, 788)
pag.click()

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



#creation backgrand

pag.click(x=18, y=373,interval=0.5)
pag.moveTo(x=479, y=304)
time.sleep(0.5)
pag.dragTo(1448,836,2, button='left')
pag.click(1422,824)
pag.click(x=1174, y=111,interval=0.5)
pag.click(x=1128, y=137)
pag.click(x=188, y=976) #color backgrand
pag.moveTo(20,703,0.5)
pag.click()
time.sleep(1)
pag.click(76,764)
pag.moveTo(x=206, y=976) #blue color
time.sleep(0.5)
pag.dragTo(562,428,2, button='left')

pag.moveTo(x=165, y=975) #yello color
time.sleep(0.5)
pag.dragTo(1323,701,2, button='left')

pag.click(x=58, y=102)
pag.click(x=58, y=120)

#create python lego
    
pag.click(x=20, y=373)
pag.moveTo(x=718, y=522)
time.sleep(0.5)
pag.dragTo(900,601,2, button='left')
time.sleep(0.25)
pag.moveTo(x=755, y=104)
pag.doubleClick()
time.sleep(0.25)
pag.typewrite('2')
time.sleep(0.25)
pag.click(x=759, y=392)
time.sleep(0.25)
pag.click(x=17, y=157) #this line is for take copy of object
pag.click(x=854, y=561)
##pag.rightClick() #laso ths line (copy of object)
##pag.click(x=889, y=482)
pag.keyDown('ctrl')
pag.press('c')
pag.keyUp('ctrl')
time.sleep(1)
pag.keyDown('ctrl')
pag.press('v')
pag.keyUp('ctrl')
##print(pag.position())
time.sleep(0.5)
pag.dragTo(815,524,2, button='left')
##pag.press(['right','right','right','right','right','right','right','right','right','right'])
pag.keyDown('shift')
pag.click(x=862, y=578)
pag.keyUp('shift')
time.sleep(0.25)
pag.click(x=788, y=112)
time.sleep(1)
pag.press('esc')
pag.moveTo(x=806, y=531)
pag.dragTo(837,635,2, button='left')
time.sleep(0.25)
pag.doubleClick(461,114,interval=0.5)
time.sleep(0.25)
pag.typewrite('90')
time.sleep(0.25)
pag.press('enter')
pag.moveTo(x=798, y=529)
pag.dragTo(798,624,2, button='left')
pag.dragTo(818,560,2, button='left')

##pag.press([])

pag.keyDown('shift')
pag.click(x=881, y=561)
pag.keyUp('shift')
time.sleep(0.25)
pag.click(x=788, y=112)
time.sleep(0.25)
pag.press('esc')
pag.click(x=750, y=576)
time.sleep(0.25)
pag.click(x=1197, y=111)
pag.press('esc')
time.sleep(1)
pag.click(x=757, y=578)
pag.press('del')
pag.click(x=818, y=615)
time.sleep(0.25)
pag.moveTo(x=817, y=656)
time.sleep(0.25)
pag.dragTo(817,645,2, button='left')

pag.keyDown('shift')
pag.click(x=881, y=561)
pag.keyUp('shift')
time.sleep(0.25)
pag.click(x=689, y=112)
time.sleep(0.25)
pag.press('f6')
time.sleep(0.25)
pag.moveTo(x=874, y=600)
time.sleep(0.25)
pag.dragTo(817,604,2, button='left')
pag.press('esc')
time.sleep(0.25)
pag.click(x=13, y=156)
pag.keyDown('shift')
pag.click(x=859, y=601,interval=0.5)
pag.click(x=791, y=568,interval=0.5)
pag.keyUp('shift')
pag.click(x=789, y=110)
pag.press('esc')
pag.click(x=859, y=601)
pag.press('del')
#create a circle
pag.click(x=14, y=405,interval=0.25)
pag.moveTo(x=477, y=303)
pag.dragTo(490,316,2, button='left')
pag.dragTo(845,627,2, button='left')
pag.click(x=16, y=160)
pag.click(x=839, y=621)
pag.keyDown('shift')
pag.click(x=802, y=594,interval=0.25)
pag.keyUp('shift')
pag.click(x=788, y=112)
pag.press('esc')
pag.click(x=841, y=621)
pag.press('del')
#create a new python
pag.click(808,614)
time.sleep(0.25)
##pag.click()
pag.keyDown('ctrl')
pag.press('c')
pag.keyUp('ctrl')
time.sleep(0.5)
pag.keyDown('ctrl')
pag.press('v')
pag.keyUp('ctrl')
#drag the new python
pag.moveTo(x=808, y=614)
pag.dragTo(729,552,2, button='left')

pag.doubleClick(x=457, y=113)
pag.typewrite('180')
pag.press('enter')
pag.moveTo(x=810, y=532)
pag.dragTo(845,549,2, button='left')


pag.click(x=207, y=975)
pag.click(x=881, y=572)
pag.click(x=163, y=977)

pag.click(x=751, y=538)
pag.click(x=745, y=113)
pag.click(x=733, y=134)

pag.click(x=879, y=574)
pag.click(x=745, y=113)
pag.click(x=733, y=134)
pag.keyDown('shift')
pag.click(x=755, y=551)
pag.keyUp('shift')
time.sleep(0.25)
pag.click(x=1201, y=113)
time.sleep(0.25)
pag.click(x=399, y=112)
time.sleep(0.25)
pag.doubleClick(x=210, y=104)
time.sleep(0.25)
pag.typewrite('13')
time.sleep(0.25)
pag.doubleClick(x=211, y=122)
time.sleep(0.25)
pag.typewrite('13')
time.sleep(0.25)
pag.press('enter')
time.sleep(0.25)

pag.keyDown('shift')
pag.click(x=610, y=445)
pag.keyUp('shift')
time.sleep(0.25)
pag.press('c')
pag.press('e')

time.sleep(0.25)
pag.click(x=17, y=406)
pag.moveTo(x=184, y=402)
pag.dragTo(345,541,2, button='left')
pag.doubleClick(x=211, y=105)

time.sleep(0.25)
pag.typewrite('17')
pag.doubleClick(x=209, y=122)
time.sleep(0.25)
pag.typewrite('17')
pag.press('enter')
time.sleep(0.25)
pag.doubleClick(x=939, y=112)
time.sleep(0.25)
pag.typewrite('24')
time.sleep(0.25)
pag.press('enter')
time.sleep(0.25)

time.sleep(1.5)
pag.keyDown('shift')
pag.click(x=667, y=550)
pag.keyUp('shift')
time.sleep(0.25)
pag.press('c')
pag.press('e')
time.sleep(0.5)
pag.click(x=19, y=477)
time.sleep(0.25)
pag.click(x=950, y=446)
pag.doubleClick(x=667, y=111)
time.sleep(0.25)
pag.typewrite('Morohashi')
time.sleep(0.25)
pag.doubleClick(x=870, y=113)
time.sleep(0.25)
pag.typewrite('350')
time.sleep(0.25)
pag.press('enter')
time.sleep(0.25)
pag.typewrite('Python/Naser')
time.sleep(0.25)
pag.doubleClick(x=175, y=114)
time.sleep(0.25)
pag.typewrite('-0.5')
pag.press('enter')
pag.doubleClick(x=316, y=112)
time.sleep(0.25)
pag.typewrite('0')
pag.press('enter')
pag.click(x=17, y=158)
#delet circle 
##time.sleep(0.25)
##pag.doubleClick(x=951, y=603)
##time.sleep(0.25)
##pag.press('del')
pag.click(x=16, y=595)
time.sleep(0.25)
pag.click(x=942, y=431)
time.sleep(0.25)
pag.moveTo(x=950, y=518)
time.sleep(0.25)
pag.dragTo(947,400,2, button='left')
time.sleep(0.25)








