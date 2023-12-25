#adFarmer2.0
#assets -> folder
#pip3 import OpenCV,PyAutoGUI
#swipe = image(number) -> to last & to 0 

import cv2
import pyautogui
import numpy as np
from time import sleep as s
from os import system
_warning = r'''

                ,.,   '          ;'*¨'`·- .,  ‘            
              ;´   '· .,         \`:·-,. ,   '` ·.  '      
            .´  .-,    ';\        '\:/   ;\:'`:·,  '`·, '   
           /   /:\:';   ;:'\'       ;   ;'::\;::::';   ;\   
         ,'  ,'::::'\';  ;::';       ;  ,':::;  `·:;;  ,':'\' 
     ,.-·'  '·~^*'´¨,  ';::;      ;   ;:::;    ,·' ,·':::; 
     ':,  ,·:²*´¨¯'`;  ;::';      ;  ;:::;'  ,.'´,·´:::::; 
     ,'  / \::::::::';  ;::';     ':,·:;::-·´,.·´\:::::;´'  
    ,' ,'::::\·²*'´¨¯':,'\:;       \::;. -·´:::::;\;·´     
    \`¨\:::/          \::\'        \;'\::::::::;·´'        
     '\::\;'            '\;'  '         `\;::-·´            
       `¨'                                                

                  created by @slide36

'''

warning = r'''

 Для запуска нажмите ENTER.

 Если у вас не указаны изображения,
 то закройте программу и добавьте их в assets/...

'''

def start():
    system("cls")
    print(_warning)
    s(2.3)
    system("cls")
    input(warning)
    system("cls")
    print("Поиск начат...")
start()

def find_and_click(image_path):
    #Установка нулевого изображения
    swipe = 0
    
    # Загрузка изображения для поиска
    target_image = cv2.imread(image_path)

    while True:
        # Получение скриншота текущего экрана
        screen_image = pyautogui.screenshot()

        # Преобразование скриншота в формат OpenCV
        screen_image = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2BGR)

        # Поиск совпадения целевого изображения на экране
        result = cv2.matchTemplate(screen_image, target_image, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= 0.8)  # Используй любое значение порога совпадения здесь

        # Если найдены совпадения, кликни на каждое из них
        if len(locations[0]) > 0:
            print('>> Совпадение найдено!')
            target_width = target_image.shape[1]
            target_height = target_image.shape[0]
            for pt in zip(*locations[::-1]):
                click_point = (pt[0] + target_width // 2, pt[1] + target_height // 2)
                s(0.4)
                pyautogui.click(click_point)
                print('>> Нажатие произведено!\n')
                s(1.5)
                break
            break
        
        #если совпадение не найдено, то меняем фокус на другое изображение
        else:
            swipe+=1
            if swipe == 3 or swipe == 0:
                swipe = 0
                find_and_click(watch_button_path)
            if swipe == 1:
                find_and_click(close_button_path)
            if swipe == 2:
                find_and_click(flipflop_button_path)
            #if swipe == 3:
            #    find_and_click(cinema_button_path)

# Пути к изображениям, которые нужно найти и нажать
watch_button_path    = "assets/watch_button.png"
flipflop_button_path = "assets/flipflop_button.png"
close_button_path    = "assets/close_button.png"
#cinema_button_path   = "assets/cinema_button.png"


# Вызов функции для поиска и нажатия на изображения
find_and_click(watch_button_path)