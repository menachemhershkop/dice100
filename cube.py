import random

def roll_two_d6() -> tuple[int, int]:
    first_cube=random.randint(1,7)
    second_cube=random.randint(1,7)
    print(f'the result of the two cube is {first_cube},{second_cube}')
    return first_cube, second_cube
def is_bust(score: int) -> bool:
    if score > 100:
        return True
def is_exact_100(score: int) -> bool:
    if score==100:
        return True
def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    player1=target-a
    player2=target-b
    if player1 < player2:
        return 1
    elif player1 > player2:
        return 2
    else:
        return None
def tie_breaker(roller) -> int:
    while True:
        player1=sum(roll_two_d6())
        player2=sum(roll_two_d6())
        if player1 > player2:
            return 1
        elif player1 < player2:
            return 2
def turn_decision(input_fn) -> str:
    while True:
        if input_fn =="r":
            return "roll"
        elif input_fn=="p":
            return "pass"
        else:
            continue
def play_game():
    def play_mengment():
        choice=turn_decision(input("Press 'r' to play or 'p' to pass: "))
        passing=0
        if choice=="roll":
            return sum(roll_two_d6())
        elif choice == 'p'
            return 'r'
    def chek_victory(player):
        if is_exact_100(player):
            return f'{player} is win!'
        if is_bust(player):
            return f'{player} is los because is over the 100 score... '

    player1=0
    player2=0
    while True:
        player1+=play_mengment()
        player2+=play_mengment()
        close_to_win=closer_to_target(player1,player2)
        if close_to_win == 1:
            print("player 1 is closer")
        elif close_to_win == 2:
            print("player 2 is closer")
        else:
            print("tie")
        print(f'p1={player1}, p2={player2}')

play_game()