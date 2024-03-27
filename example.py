from rng_package.functions import coin_flip, dice_roll, draw_cards, generate_powerball

def main():
    print("Welcome to the RNG Package Example Program!")
    print("This program demonstrates the functionalities of the RNG Package.")

    while True:
        print("\nChoose an option:")
        print("1. Flip a Coin")
        print("2. Roll a Dice")
        print("3. Draw Cards")
        print("4. Generate Powerball Combination")
        print ("5. Draw from Bag")
        print ("6. Probability Simulator")
        print("7. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            num_coins = int(input("Enter the number of coins to flip: "))
            print("Coin Flip:", coin_flip(num_coins))
        elif choice == '2':
            num_dice = int(input("Enter the number of dice to roll: "))
            sides = int(input("Enter the number of sides for each die: "))
            print("Dice Roll:", dice_roll(num_dice, sides))
        elif choice == '3':
            num_hands = int(input("Enter the number of hands to draw: "))
            num_cards = int(input("Enter the number of cards per hand: "))
            print("Draw Cards:", draw_cards(num_hands, num_cards))
        elif choice == '4':
            print("Powerball Combination:", generate_powerball())
        elif choice == '5':
            itemTypes = input("Enter the types of items in the bag separated by commas: ").split(",")
            itemNums = [int(x) for x in input("Enter the number of each item in the bag separated by commas: ").split(",")]
            drawNum = int(input("Enter the number of items to draw from the bag: "))
            print("Draw from Bag:", draw_from_bag(itemTypes, itemNums, drawNum))
        elif choice == '6':
            outcomes = input("Enter the possible outcomes separated by commas: ").split(",")
            probabilities = [float(x) for x in input("Enter the probabilities of each outcome separated by commas: ").split(",")]
            num_trials = int(input("Enter the number of trials to simulate: "))
            print("Probability Simulator:", prob_simulator(outcomes, probabilities, num_trials))
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
