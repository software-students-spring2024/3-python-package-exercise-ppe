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
        print("5. Exit")

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
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()