from random import randrange


class Pet(object):

    """A virtual pet"""
    excitement_reduce = 3  # reduces the the pets excitement by 3
    excitement_max = 10  # max amount allowed for pet to be satisfied
    excitement_warning = 3  # lowest amount allowed for pet tells you he's bored
    food_reduce = 2  # reduces the food amount by 2
    food_max = 10  # max amount allowed for pet to be full
    food_warning = 3  # lowest amount allowed for pet to be hungry
    # List of vocabulary that user can add to by teaching pet a new word
    # currently only know how to "Grr" until player teaches new word
    vocab = ['"Grrrr..."']

    # Constructor with parameters name and animal type
    def __init__(self, name, animal_type):
        self.name = name  # defining arguments being passed
        self.animal_type = animal_type  # defining arguments being passed
        # randrange is used to change the food_max value during game at random pet to respond with hunger satisfaction
        self.food = randrange(self.food_max)
        # randrange is used to change the excitement_max value for pet to respond with excitement satisfaction
        self.excitement = randrange(self.excitement_max)
        self.vocab = self.vocab[:]  # method to add vocab to vocab list

    # this method was created to add at end of other methods to change excitement and food levels over "time"
    def __clock_tick(self):
        self.excitement -= 1  # decrements exitement by 1
        self.food -= 1  # decrements food by 1

    def mood(self):
        # if food level is greater than 3 and excitement level is greater than 3
        if self.food > self.food_warning and self.excitment > self.excitement_warning:
            return "happy"
        elif self.food <= self.food_warning:  # else if food level is less than or equal to 3
            return "hungry"
        else:
            return "bored"  # else pet is bored since it has been fed and is content

    def __str__(self):
        # returns the pets name and how it feels
        return "\nI'm " + self.name + "." + "\nI feel " + self.mood() + "."

    def teach(self, word):
        self.vocab.append(word)  # appends word to vocab list
        self.__clock_tick()  # decrements exitement and food by 1

    def talk(self):
        print("I am a " + self.animal_type + " named " + self.name +
              ". I feel " + self.mood() + " now.\n")
        # gets a random object off the length of the vocab list (including new words)
        print(self.vocab[randrange(len(self.vocab))])
        self.__clock_tick()  # decrements exitement and food by 1

    def feed(self):
        print("***crunch***\n mmm. Thank you!")
        # initially had self.food as the start point, but I kept getting an "empty range for randrange() error" because it wasnt retrieving updated food- so set it to 0
        meal = randrange(0, self.food_max)
        self.food += meal

        if self.food < 0:
            self.food = 0
            print("I am still hungry!")
        elif self.food >= self.food_max:
            self.food = self.food_max
            print("I'm full!")
        self.__clock_tick()  # decrements exitement and food by 1

    def play(self):
        print("Woohoo!")
        # initially had self.excitment as the start point, but I kept getting an "empty range for randrange() error" because it wasnt retrieving updated excitement- so set it to 0
        fun = randrange(0, self.excitement_max)
        self.excitement += fun
        if self.excitement < 0:
            self.excitment = 0
            print("I am bored")
        elif self.excitement >= self.excitement_max:
            self.excitement = self.excitement_max
            print("I am really happy!")
        self.__clock_tick()


def main():
    pet_name = input("What do you want to name your pet? ")
    pet_type = input("What type of animal is your pet? ")

    my_pet = Pet(pet_name, pet_type)

    input("\nHello! I am " + my_pet.name +
          " and I am new here!" + "\nPress enter to start.")

    while True:
        print(
            """
            ***Interact With Your Pet***

            1 - Feed your pet
            2 - Talk with your pet
            3 - Teach your pet a new word
            4 - Play with your pet
            0 - Quit
            """)
        choice = input("Choice: ")

        if choice == '0':
            print("Goodbye!")
            exit()
        elif choice == '1':
            my_pet.feed()
        elif choice == '2':
            my_pet.talk()
        elif choice == '3':
            new_word = input("What do you want to teach your pet to say?")
            my_pet.teach(new_word)
        elif choice == '4':
            my_pet.play()
        else:
            print("Sorry, that isn't a valid option")


main()
