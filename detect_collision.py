def detect_collision_with_car(player, car):
    player_left = player.xcor() - 10
    player_right = player.xcor() + 10
    player_top = player.ycor() + 10
    player_bottom = player.ycor() - 10

    # Car bounding box
    car_left = car.xcor() - 30  # Half of the car's total length
    car_right = car.xcor() + 30
    car_top = car.ycor() + 10   # Half of the car's height
    car_bottom = car.ycor() - 10

    return (player_left < car_right and
        player_right > car_left and
        player_top > car_bottom and
        player_bottom < car_top)