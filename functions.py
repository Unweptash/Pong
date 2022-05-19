from dictionaries import *
import math as math


def powerup_resets(powerup1, powerup2, paddles):
    #reset powerup1        
    if 8000 < millis() - main["other"]["last_hit1"] < 9000 and main["other"]["counter1"] == 1:
        main["other"]["last_hit1"] = 0
        powerup1_reset(powerup1, paddles)

    #reset powerup2        
    if 8000 < millis() - main["other"]["last_hit2"] < 9000 and main["other"]["counter2"] == 1:
        main["other"]["last_hit2"] = 0
        powerup2_reset(powerup2, paddles)

def powerup1_reset(powerup1, paddles):
   
    powerup1["powerup1_x"] = 390
    powerup1["powerup1_y"] = 290
    paddles["leftp_x"] = -100  
    paddles["rightp_x"] = -100

def powerup2_reset(powerup2, paddles):
   
    #paddle height dependent of powerup2
    paddles["powerup2_left_paddle_height"] = 80
    paddles["powerup2_right_paddle_height"] = 80
    if paddles["powerup2_left_paddle_height"] == 160:
        paddles["left_y"] += 40        
        paddles["leftp_y"] += 40
        paddles["powerup2_left_paddle_height"] = 80
    elif paddles["powerup2_right_paddle_height"] == 160:
        paddles["right_y"] += 40
        paddles["rightp_y"] += 40
        paddles["powerup2_right_paddle_height"] = 80
    powerup2["powerup2_x"] = 390
    powerup2["powerup2_y"] = 290

def ball_reset(ball):
    #ball position
    ball["ball_x"] = 390
    ball["ball_y"] = 290
   
def continous_movement_paddles(paddles):
    #moving paddles
    #move left paddles
    if paddles["left_key"] == "w":
        paddles["left_y"] += -2
        paddles["leftp_y"] += 2
    if paddles["left_key"] == "s":
        paddles["left_y"] += 2  
        paddles["leftp_y"] += -2
    #move right paddles
    if paddles["right_key"] == "i":
        paddles["right_y"] += -2
        paddles["rightp_y"] += 2
    if paddles["right_key"] == "k":
        paddles["right_y"] += 2  
        paddles["rightp_y"] += -2
       
def auto_object_movements(powerup1, powerup2, ball):
   
    #moving powerups
    powerup1["powerup1_x"] += powerup1["powerup1_dx"]
    powerup1["powerup1_y"] += powerup1["powerup1_dy"]
    powerup2["powerup2_x"] += powerup2["powerup2_dx"]
    powerup2["powerup2_y"] += powerup2["powerup2_dy"]

    #moving ball    
    ball["ball_x"] = ball["ball_x"] + ball["ball_dx"]
    ball["ball_y"] = ball["ball_y"] + ball["ball_dy"]
   
def auto_object_area_boundaries(ball, powerup1, powerup2):
   
        #bounce off bottom/top screen
    if ball["ball_y"] < 0 or ball["ball_y"] > 580:
        ball["ball_dy"] = ball["ball_dy"] * -1
       
        #bounce off bottom/top screen
    if powerup1["powerup1_y"] >= 560 or powerup1["powerup1_y"] <= 0:
        powerup1["powerup1_dy"] = powerup1["powerup1_dy"] * -1
    if powerup2["powerup2_y"] >= 560 or powerup2["powerup2_y"] <= 0:
        powerup2["powerup2_dy"] = powerup2["powerup2_dy"] * -1
       
        #bounce in yellow rectangle
    if powerup1["powerup1_x"] >= 560 or powerup1["powerup1_x"] <= 200:
        powerup1["powerup1_dx"] = powerup1["powerup1_dx"] * -1
    if powerup2["powerup2_x"] >= 560 or powerup2["powerup2_x"] <= 200:
        powerup2["powerup2_dx"] = powerup2["powerup2_dx"] * -1

def score_counter(ball, other):
    #scoring
        #going off left or right edge of screen
        #check right edge/left point
    if ball["ball_x"] > 780:
        other["left_score"] += 1
        ball_reset(ball)
           
        #check left edge/right point
    elif ball["ball_x"] < 0:
        other["right_score"] += 1
        ball_reset(ball)
       
def paddle_ball_bounce(ball, paddles):
        #left paddle bounce    
    if ball["ball_x"] <= 40 and ball["ball_y"] > paddles["left_y"] and ball["ball_y"] < (paddles["left_y"] + paddles["powerup2_left_paddle_height"]):
        ball["ball_dx"] = ball["ball_dx"] * -1
        # left powerup1 paddle bounce
    elif ball["ball_x"] <= 40 and ball["ball_y"] > paddles["leftp_y"] and ball["ball_y"] < (paddles["leftp_y"] + paddles["powerup2_left_paddle_height"]):
        ball["ball_dx"] = ball["ball_dx"] * -1
        #right paddle bounce
    if ball["ball_x"] >= 750 and ball["ball_y"] > paddles["right_y"] and ball["ball_y"] < (paddles["right_y"] + paddles["powerup2_right_paddle_height"]):
        ball["ball_dx"] = ball["ball_dx"] * -1
        #right powerup1 paddle bounce
    elif ball["ball_x"] >= 750 and ball["ball_y"] > paddles["rightp_y"] and ball["ball_y"] < (paddles["rightp_y"] + paddles["powerup2_right_paddle_height"]):
         ball["ball_dx"] = ball["ball_dx"] * -1
         
def powerup_ball_collisions(powerup1, ball, paddles, other, powerup2):
    #collision powerup1 and ball
    if abs(powerup1["powerup1_x"] - ball["ball_x"]) <= 30 and abs(powerup1["powerup1_y"] - ball["ball_y"]) <= 30:
        if ball["ball_dx"] > 0:
            paddles["leftp_x"] = 30
        elif ball["ball_dx"] < 0:
            paddles["rightp_x"] = 770
        other["counter1"] = 1
        powerup1["powerup1_x"] = 1000
        other["last_hit1"] = millis()
       
    #collision powerup2
    if abs(powerup2["powerup2_x"] - ball["ball_x"]) <= 30 and abs(powerup2["powerup2_y"] - ball["ball_y"]) <= 30:
        if ball["ball_dx"] > 0:
            paddles["powerup2_left_paddle_height"] = 160
            paddles["left_y"] -= 40
            paddles["leftp_y"] -= 40
        elif ball["ball_dx"] < 0:
            paddles["powerup2_right_paddle_height"] = 160
            paddles["right_y"] -= 40
            paddles["rightp_y"] -= 40
        other["counter2"] = 1
        powerup2["powerup2_x"] = 1000
        other["last_hit2"] = millis()

       
def draw_screen(other, powerup1, powerup2, paddles, ball):
    text("PONG", 350,40)
    text(other["left_score"], 40, 40)
    text(other["right_score"], 760,40)
   
    #powerup area
    fill(255,215,0)
    rect(200, 0, 400, 600)
   
        #Powerups
    fill(255, 0,  0)
    rect(powerup1["powerup1_x"], powerup1["powerup1_y"],40,40)
    fill(0, 0, 255)
    rect(powerup2["powerup2_x"], powerup2["powerup2_y"],40,40)
       
        #paddles
    fill(255, 255, 255)
    rect(30,paddles["left_y"],10,paddles["powerup2_left_paddle_height"]) #left paddle
    fill(255, 255, 255)
    rect(770,paddles["right_y"],10,paddles["powerup2_right_paddle_height"]) #right paddle
   
    #powerup1_paddle
    fill(0, 128, 0)
    rect(paddles["leftp_x"],paddles["leftp_y"],10,paddles["powerup2_left_paddle_height"]) #left paddle
    fill(0, 128, 0)
    rect(paddles["rightp_x"],paddles["rightp_y"],10,paddles["powerup2_right_paddle_height"]) #right paddle
   

    #ball
    fill(255, 255, 255)
    rect(ball["ball_x"],ball["ball_y"],20,20)
