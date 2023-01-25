# mini_tamagotchi_clone
This is a command line game. 
In order to run this file, you will need to navigate to directory it was downloaded into, then run command python pet.py to start 

Intro 

I initially wanted to design a program that simulated a pet adoption. I decided to simplify this into
a virtual pet interactive game instead of having pre-defined pets to interact with. I believe that in
the near future I can dedicate more time to accomplishing that part of the game.
The game I made was a simple take on the game Tamagotchi. The game begins by prompting
the player to name the pet and determine what kind of animal the pet is. Then it will give a list of
options to select from. The player can then choose between feeding the pet, talking to the pet,
teaching the pet a new word and playing with the pet. Everytime the player selects an option,
the pet will respond with a few predetermined responses that will be determined by the methods
in the class Pet. The player can do this repeatedly to get different responses each time based
on the python randrange built in function.

Design & Implementation

The design of the game started with creating the main function and writing out some of the
prompts that included the options for the user to select. I left empty spaces in between the
choices to fill with the action of the selection later on.
I continued by writing out a list of function names that would then define what the pet could do.
Initially I was thinking of way too many options for the pets mood as independent functions so I
just made a function that would define them all. I ended up making a class named Pet() and
including the functions within it.
By continuing to write out some variables that would calculate the pets excitement, and food
max. Then I added a list that would hold the strings the pet would learn. I can easily add more of
the pets capabilities later on by adding the variables here and creating a new function within the
class and then including it into the user options prompt.
I then started adding in self.food in the constructor. In order to define it, I knew I needed to use
the rand function right off the bat to have the pet provide different(random) responses each time.
So I imported random from randrange and set self.food to randrange(self.food_max). This
means that when the pet is created, it will pick a number between 0 and the food_max (which is
set to 10) and set the food method to be that value. This will later determine if the pet is full or
hungry. Same thing will apply to self.excitement which will later determine if the pet is happy or
bored. Self.vocab was not initially in this step, I ended up tracing back to determine how I would
have input added into the list. Had to do some research and ultimately found that list[:] creates a
copy of a list (technically a shallow copy of an array) so that the original list is not overwritten
