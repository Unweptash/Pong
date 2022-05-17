paddles = {
#paddle positions
"left_y" : 260,
"right_y" : 260,
#powerup1 paddles
"leftp_y" : 260,
"rightp_y" : 260,
"leftp_x" : 1000,
"rightp_x" : 1000,
#paddle keys
"left_key" : "",
"right_key" : "",
#powerup2 causing change in size in paddles
"powerup2_left_paddle_height" : 80,
"powerup2_right_paddle_height" : 80
}

powerup1 = {
#powerup1 position & velocity
"powerup1_x" : 440,
"powerup1_y" : 270,
"powerup1_dx" : 2,
"powerup1_dy" : 2
}

powerup2 = {
#powerup2 position & velocity
"powerup2_x" : 440,
"powerup2_y" : 270,
"powerup2_dx" : -2,
"powerup2_dy" : -2
}

ball = {
#ball position & velocity
"ball_x" : 390,
"ball_y" : 290,
"ball_dx" : -2,
"ball_dy" : -2
}

other = {
#starting values for everything
#scores
"left_score" : 0,
"right_score" : 0,
#last hit between powerup1 and ball & powerup2 and ball
"last_hit1" : 0,
"last_hit2" : 0,
#counting variable to prevent first auto-reset of powerup
"counter1" : 0,
"counter2" : 0
}

main = {
"paddles" : paddles,
"powerup1" : powerup1,
"powerup2" : powerup2,
"ball" : ball,
"paddles" : paddles,
"other" : other
}
