
import time

import pyautogui as pg

from selection import *
from tools import *

#glabal varibles
screen_path = "imgs\screen.jpg"



def fight(screen,energy,coord):
    print("--------------------{0}-------------------".format(inspect.currentframe().f_code.co_name))
    #set place of button
    time.sleep(1)
    button = find_coord_to_click(screen, r"imgs\button_cacar_chefe.jpg" )

    #fight 3 times with the same team
    for i in range(0,energy):
        for i in range(45): #range try:          
            time.sleep(1) 
            try:      
                print("Click: button_cacar_chefe")
                pg.moveTo(button)
                pg.click()
                time.sleep(1)
                screen = myscreen()

                #check if 
                # perceber = find_coord_to_click(screen, r"imgs\perceber.jpg")
                # if perceber:
                
                #     print("No energy in fight!")
                      #close perceber
                #     time.sleep(3)#try
                        #deselect_person(coord)
                #     return False
                # print("Continue .... 38 ")
                           
            except Exception as e:                
                print(e, "in fight")
                time.sleep(3)#try
                continue
            break

    #click 
        time.sleep(6)
        print("----Start fight!")
        pg.moveTo(button[0]-350, button[1]-25)
        pg.click()       
       
        #cheking screen for 45 secs
                              
        print("Fighting...")
        for i in range(45): #range try screen: 
            time.sleep(1) 
            screen = myscreen()
            toque_para = find_coord_to_click(screen, r"imgs\button_toque_para.jpg")
            caçar_chefe = find_coord_to_click(screen, r"imgs\button_cacar_chefe.jpg")
            banner_boss = find_coord_to_click(screen, r"imgs\banner_boss.jpg")
            toque_para_continuar = find_coord_to_click(screen, r"imgs\button_toque_para_continuar.jpg",.7)
            toque_para_abrir = find_coord_to_click(screen, r"imgs\button_toque_para_abrir.jpg")
            toque_para_assistir = find_coord_to_click(screen, r"imgs\button_toque_para_assistir.jpg")
            derrota = find_coord_to_click(screen, r"imgs\banner_derrota.jpg")
            vitoria = find_coord_to_click(screen, r"imgs\banner_vitoria.jpg")  
               

            #make time stops            
            if toque_para:                
                click(screen,toque_para)
            
            if toque_para_abrir:                
                click(screen, toque_para_abrir)
            
            if toque_para_continuar:                
                click(screen,toque_para_continuar)
            
            if derrota or vitoria:
                print("------Stop fight!")
                ref = find_coord_to_click(screen, r"imgs\ref_toque.jpg")                 
                click(screen,(int(ref[0]),int(ref[1]-100)))                                                 

            if caçar_chefe:                
                break  

            if banner_boss:
                print("------Change boss!")
                boss = select_boss(screen)
                for i in range(0,3):
                    time.sleep(2)
                if boss:                    
                    break 

            if i % 3 == 0:          
                print("Fighting...")     
    return True
    

def old_fight():
    time.sleep(2)
    button = find_coord_to_click(screen, r"imgs\button_cacar_chefe.jpg" )

    #play 3 times
    for i in range(0,3):
        #caçar       
        print("Click:1")
        pg.moveTo(button)
        pg.click()
        time.sleep(3)#try

        #move to midle
        print("Click:2")
        pg.moveTo(button[0]-350, button[1])
        pg.click()       
       
        #clik in the midle
        for i in range(45):#range try screen:
            time.sleep(1)            
            pg.click()

    return True

