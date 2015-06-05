# Petals around the rose game
import random

class Die:

    def __init__(self):
        self.value = int(random.random() * 6 + 1)
    
    def roll(self):
        self.value = int(random.random() * 6 + 1)

    def show(self):
        if self.value == 1:
            return("---------\n|       |\n|   *   |\n|       |\n---------")
        elif self.value == 2:
            return("---------\n|*      |\n|       |\n|      *|\n---------")
        elif self.value == 3:
            return("---------\n|*      |\n|   *   |\n|      *|\n---------")
        elif self.value == 4:
            return("---------\n|*     *|\n|       |\n|*     *|\n---------")
        elif self.value == 5:
            return("---------\n|*     *|\n|   *   |\n|*     *|\n---------")
        else:
            return("---------\n|*     *|\n|*     *|\n|*     *|\n---------")


class Dice:
    
    def __init__(self, n):
        self.dice_array =  [Die() for _ in range(n)]

    def roll(self):
        for i in xrange(self.dice_array):
            self.dice_array[i].roll()

    def answer(self):
        sum = 0
        for dice in self.dice_array:
            if (dice.value == 5 or dice.value == 3):
                sum += dice.value - 1
        return sum

    def show_dice(self):
        for dice in self.dice_array:
            print(dice.show())


class PetalsGame:

    def __init__(self):
        self.dice = Dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0
        self.consecutive_wins = 0

    def game_over(self):
        self.consecutive_wins == 6
    
    @staticmethod
    def play_game():
        # Needs some cleanup
        while True:
            pg = PetalsGame()
            print("Round " + str(pg.round) + " :")
            
            pg.dice.show_dice()

            print("")
            guess = input("What is your guess?: ")

            while guess.isdigit() is False:
                guess = input('Please enter a number: ')

            guess = int(guess)
            answer = pg.dice.answer()

            if guess == answer:
                print("Hooray!")
                pg.wins += 1
                pg.consecutive_wins += 1
            else:
                print("Sorry that's wrong")
                print('The answer is: ' + str(answer))
                pg.loses += 1
                pg.consecutive_wins = 0
            print("Wins: " + str(pg.wins) + " Loses: " + str(pg.loses))
            pg.round += 1
               
            if pg.game_over():
                print("You have figured it out, congrats!")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt.lower() == 'y' or prompt == '':
                continue
            else:
                break

        
def main():
    print("Petals around the rose. There are three rules:")
    print("1. The name of the game is important \n2. The answer is always even \n3. If you figure it out, do not let anyone else know")

    PetalsGame.play_game()


if __name__ == "__main__":
    main()
