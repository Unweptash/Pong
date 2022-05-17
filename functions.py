from dictionaries import *
import math as math


def powerup_resets():
    #reset powerup1        
    if 8000 < millis() - main["other"]["last_hit1"] < 9000 and main["other"]["counter1"] == 1:
        main["other"]["last_hit1"] = 0
        powerup1_reset()

    #reset powerup2        
    if 8000 < millis() - main["other"]["last_hit2"] < 9000 and main["other"]["counter2"] == 1:
        main["other"]["last_hit2"] = 0
        powerup2_reset()

def powerup1_reset():
   
    main["powerup1"]["powerup1_x"] = 390
    main["powerup1"]["powerup1_y"] = 290
    main["paddles"]["leftp_x"] = -100  
    main["paddles"]["rightp_x"] = -100

def powerup2_reset():
   
    #paddle height dependent of powerup2
    main["paddles"]["powerup2_left_paddle_height"] = 80
    main["paddles"]["powerup2_right_paddle_height"] = 80
    if main["paddles"]["powerup2_left_paddle_height"] == 160:
        main["paddles"]["left_y"] += 40        
        main["paddles"]["leftp_y"] += 40
        main["paddles"]["powerup2_left_paddle_height"] = 80
    elif main["paddles"]["powerup2_right_paddle_height"] == 160:
        main["paddles"]["right_y"] += 40
        main["paddles"]["rightp_y"] += 40
        main["paddles"]["powerup2_right_paddle_height"] = 80
    main["powerup2"]["powerup2_x"] = 390
    main["powerup2"]["powerup2_y"] = 290

def ball_reset():
    #ball position
    main["ball"]["ball_x"] = 390
    main["ball"]["ball_y"] = 290
   
def continous_movement_paddles():
    #moving paddles
    #move left paddles
    if main["paddles"]["left_key"] == "w":
        main["paddles"]["left_y"] += -2
        main["paddles"]["leftp_y"] += 2
    if main["paddles"]["left_key"] == "s":
        main["paddles"]["left_y"] += 2  
        main["paddles"]["leftp_y"] += -2
    #move right paddles
    if main["paddles"]["right_key"] == "i":
        main["paddles"]["right_y"] += -2
        main["paddles"]["rightp_y"] += 2
    if main["paddles"]["right_key"] == "k":
        main["paddles"]["right_y"] += 2  
        main["paddles"]["rightp_y"] += -2
       
def auto_object_movements():
   
    #moving powerups
    main["powerup1"]["powerup1_x"] += main["powerup1"]["powerup1_dx"]
    main["powerup1"]["powerup1_y"] += main["powerup1"]["powerup1_dy"]
    main["powerup2"]["powerup2_x"] += main["powerup2"]["powerup2_dx"]
    main["powerup2"]["powerup2_y"] += main["powerup2"]["powerup2_dy"]

    #moving ball    
    main["ball"]["ball_x"] = main["ball"]["ball_x"] + main["ball"]["ball_dx"]
    main["ball"]["ball_y"] = main["ball"]["ball_y"] + main["ball"]["ball_dy"]
   
def auto_object_area_boundaries():
   
        #bounce off bottom/top screen
    if main["ball"]["ball_y"] < 0 or main["ball"]["ball_y"] > 580:
        main["ball"]["ball_dy"] = main["ball"]["ball_dy"] * -1
       
        #bounce off bottom/top screen
    if main["powerup1"]["powerup1_y"] >= 560 or main["powerup1"]["powerup1_y"] <= 0:
        main["powerup1"]["powerup1_dy"] = main["powerup1"]["powerup1_dy"] * -1
    if main["powerup2"]["powerup2_y"] >= 560 or main["powerup2"]["powerup2_y"] <= 0:
        main["powerup2"]["powerup2_dy"] = main["powerup2"]["powerup2_dy"] * -1
       
        #bounce in yellow rectangle
    if main["powerup1"]["powerup1_x"] >= 560 or main["powerup1"]["powerup1_x"] <= 200:
        main["powerup1"]["powerup1_dx"] = main["powerup1"]["powerup1_dx"] * -1
    if main["powerup2"]["powerup2_x"] >= 560 or main["powerup2"]["powerup2_x"] <= 200:
        main["powerup2"]["powerup2_dx"] = main["powerup2"]["powerup2_dx"] * -1

def score_counter():
    #scoring
        #going off left or right edge of screen
        #check right edge/left point
    if main["ball"]["ball_x"] > 780:
        main["other"]["left_score"] += 1
        ball_reset()
           
        #check left edge/right point
    elif main["ball"]["ball_x"] < 0:
        main["other"]["right_score"] += 1
        ball_reset()
       
def paddle_ball_bounce():
        #left paddle bounce    
    if main["ball"]["ball_x"] <= 40 and main["ball"]["ball_y"] > main["paddles"]["left_y"] and main["ball"]["ball_y"] < (main["paddles"]["left_y"] + main["paddles"]["powerup2_left_paddle_height"]):
        main["ball"]["ball_dx"] = main["ball"]["ball_dx"] * -1
        # left powerup1 paddle bounce
    elif main["ball"]["ball_x"] <= 40 and main["ball"]["ball_y"] > main["paddles"]["leftp_y"] and main["ball"]["ball_y"] < (main["paddles"]["leftp_y"] + main["paddles"]["powerup2_left_paddle_height"]):
        main["ball"]["ball_dx"] = main["ball"]["ball_dx"] * -1
        #right paddle bounce
    if main["ball"]["ball_x"] >= 750 and main["ball"]["ball_y"] > main["paddles"]["right_y"] and main["ball"]["ball_y"] < (main["paddles"]["right_y"] + main["paddles"]["powerup2_right_paddle_height"]):
        main["ball"]["ball_dx"] = main["ball"]["ball_dx"] * -1
        #right powerup1 paddle bounce
    elif main["ball"]["ball_x"] >= 750 and main["ball"]["ball_y"] > main["paddles"]["rightp_y"] and main["ball"]["ball_y"] < (main["paddles"]["rightp_y"] + main["paddles"]["powerup2_right_paddle_height"]):
         main["ball"]["ball_dx"] = main["ball"]["ball_dx"] * -1
         
def powerup_ball_collisions():
    #collision powerup1 and ball
    if abs(main["powerup1"]["powerup1_x"] - main["ball"]["ball_x"]) <= 30 and abs(main["powerup1"]["powerup1_y"] - main["ball"]["ball_y"]) <= 30:
        if main["ball"]["ball_dx"] > 0:
            main["paddles"]["leftp_x"] = 30
        elif main["ball"]["ball_dx"] < 0:
            main["paddles"]["rightp_x"] = 770
        main["other"]["counter1"] = 1
        main["powerup1"]["powerup1_x"] = 1000
        main["other"]["last_hit1"] = millis()
       
    #collision powerup2
    if abs(main["powerup2"]["powerup2_x"] - main["ball"]["ball_x"]) <= 30 and abs(main["powerup2"]["powerup2_y"] - main["ball"]["ball_y"]) <= 30:
        if main["ball"]["ball_dx"] > 0:
            main["paddles"]["powerup2_left_paddle_height"] = 160
            main["paddles"]["left_y"] -= 40
            main["paddles"]["leftp_y"] -= 40
        elif main["ball"]["ball_dx"] < 0:
            main["paddles"]["powerup2_right_paddle_height"] = 160
            main["paddles"]["right_y"] -= 40
            main["paddles"]["rightp_y"] -= 40
        main["other"]["counter2"] = 1
        main["powerup2"]["powerup2_x"] = 1000
        main["other"]["last_hit2"] = millis()

       
def draw_screen():
    text("PONG", 350,40)
    text(main["other"]["left_score"], 40, 40)
    text(main["other"]["right_score"], 760,40)
   
    #powerup area
    fill(255,215,0)
    rect(200, 0, 400, 600)
   
        #Powerups
    fill(255, 0,  0)
    rect(main["powerup1"]["powerup1_x"], main["powerup1"]["powerup1_y"],40,40)
    fill(0, 0, 255)
    rect(main["powerup2"]["powerup2_x"], main["powerup2"]["powerup2_y"],40,40)
       
        #paddles
    fill(255, 255, 255)
    rect(30,main["paddles"]["left_y"],10,main["paddles"]["powerup2_left_paddle_height"]) #left paddle
    fill(255, 255, 255)
    rect(770,main["paddles"]["right_y"],10,main["paddles"]["powerup2_right_paddle_height"]) #right paddle
   
    #powerup1_paddle
    fill(0, 128, 0)
    rect(main["paddles"]["leftp_x"],main["paddles"]["leftp_y"],10,main["paddles"]["powerup2_left_paddle_height"]) #left paddle
    fill(0, 128, 0)
    rect(main["paddles"]["rightp_x"],main["paddles"]["rightp_y"],10,main["paddles"]["powerup2_right_paddle_height"]) #right paddle
   

    #ball
    fill(255, 255, 255)
    rect(main["ball"]["ball_x"],main["ball"]["ball_y"],20,20)
