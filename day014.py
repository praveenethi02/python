import random
import day014_game_data

print(day014_game_data.LOGO)

def game():
    run = True
    chance = 5
    score = 0
    while run:
        rand_int1 = random.randint(0,33)
        rand_int2 = random.randint(0,33)
        if rand_int1 == rand_int2:
            rand_int2 = random.randint(0,33)



        print(f"Compare A : {day014_game_data.data[rand_int1]['name']} , a {day014_game_data.data[rand_int1]['description']} , from {day014_game_data.data[rand_int1]['country']}.")

        print(day014_game_data.vs)

        print(f"Compare B : {day014_game_data.data[rand_int2]['name']} , a {day014_game_data.data[rand_int2]['description']} , from {day014_game_data.data[rand_int2]['country']}.")

        ans = input("Enter the answer A or B : ").lower()

        if ans == 'a':
            if day014_game_data.data[rand_int1]['follower_count'] > day014_game_data.data[rand_int2]['follower_count']:
                print("You are correct")
                score = score + 1
                print(score)


            else:
                print("You are wrong")
                print(score)

        else:
            if day014_game_data.data[rand_int1]['follower_count'] < day014_game_data.data[rand_int2]['follower_count']:
                    print("You are correct")
                    score = score + 1
                    print(score)
            
            else:
                print("You are wrong")
                print(score)

        chance = chance - 1
        if chance <= 0:
            run = False

    print(f"Final mark = {score}")


game()
