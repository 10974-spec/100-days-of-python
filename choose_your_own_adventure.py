name = input("What is your name? ")
print("welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across.").lower()

if answer == "swim":
    print("You get attacked by an alligator and you lose.")
elif answer == "walk":
    print("You were bit by a snake and you lose.")




elif answer == "right":        
    answer = input("You come to a bridge, it looks wobbly, do you cross it or head back (cross/back)? ").lower()

if answer == "back":
    print("You go back and lose.")
elif answer == "cross":
    answer = input("You cross the bridge and reach the other side and you see a house, a cave, or an island. Which do you go to (house/cave/island)? ").lower()

if answer == "house":
    print("You go to the house and it is dark and full of monsters. You die.")
elif answer == "cave":
    print("You peer into the cave, you see a wizard and he gives you gold. You win!")
elif answer == "island":
    print("You arrive at the island unharmed. You win!")
else:
    print("Not a valid option. You lose.")