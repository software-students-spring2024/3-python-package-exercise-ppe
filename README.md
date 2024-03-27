# Python Package Exercise

## Description, Instruction & Examples

### Project Description:

The RNG (Random Number Generator) Package is designed to provide an easy-to-use interface for simulating random events. It's perfect for applications in gaming, simulations, and educational purposes to demonstrate probability and randomness.

Our project is a probability package with four main methods: (1) coin flip, (2) dice roll, (3) draw card, (4) generate powerball. The following methods can be tested in our [example program](./example.py). This program allows us to generate and test the output given by our four main methods under [functions file](/rng_package/functions.py).  
<br>

### Installation Instructions:

To install rng_package and its methods, simply run the command:

```bash
pip install rng_package
```
<br>


### Usage:

After installation, you can import rng_package into your Python script as follows:

```py
from rng_package.functions import coin_flip, dice_roll, draw_card, generate_powerball
```
<br>


### Function 1: Coin Flip

```py

def coin_flip(num_coins=1):
    result = ['heads', 'tails']
    return [random.choice(result) for _ in range(num_coins)]

```

Simulate flipping one or more coins. 
* num_coins: The number of coins to flip (default is 1).

Example:

```py
print(coin_flip(3)) # Flips three coins

```
<br>


### Function 2: Dice Roll

```py

def dice_roll(num_dice=1, sides=6):
    return [random.randint(1, sides) for _ in range(num_dice)]

```

Roll one or more dice with a specified number of sides. 
* num_dice: The number of dice to roll (default is 1).
* sides: The number of sides on the dice (default is 6).

Example:

```py
print(dice_roll(2, 6)) # Rolls two six-sided dice

```
<br>


### Function 3: Draw Cards

```py

def draw_cards(num_hands=1, num_cards=1):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    face_cards = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    jokers = ['Big Joker', 'Small Joker']

    deck = [(suit, value) for suit in suits for value in range(1, 14)]

    for joker in jokers:
        deck.append(('Joker', joker))

    random.shuffle(deck)
    
    hands = []
    for _ in range(num_hands):
        hand = []
        for _ in range(num_cards):
            suit, value = deck.pop()
            if suit == 'Joker':
                hand.append(value)
            else:
                if value in face_cards:
                    value = face_cards[value]
                else:
                    value = str(value)
                hand.append(f"{value} of {suit}")
        hands.append(hand)
    return hands

```

Draw a specified number of cards from deck.
* num_hands: The number of hands to draw (default is 1).
* num_cards: The number of cards per hand (default is 1). 

Example:

```py
print(draw_cards(1, 5)) # Draws five cards for one hand

```
<br>


### Function 4: Generate Powerball

```py

def generate_powerball():
    main_numbers = random.sample(range(1, 70), 5)
    powerball_number = random.randint(1, 26)
    powerball_combination = main_numbers + [powerball_number]
    return powerball_combination

```

Generates a Powerball lottery combination. 

Example:

```py
print(generate_powerball()) # Generates a Powerball combination

```
<br>

### Function 5: Draw from bag

```py

def draw_from_bag(itemTypes=["red","blue","green"], itemNums=[3,3,3], drawNum=1):
    bag = []
    drawn=[]
    for i in range(len(itemTypes)):
        for j in range(itemNums[i]):
            bag.append(itemTypes[i])
    for i in range(drawNum):
        draw = random.choice(bag)
        bag.remove(draw)
        drawn.append(draw)
    return drawn

```

Draws a random item from a bag of different numbers of different items. 

Example:

```py
print(draw_from_bag(["red","green","blue"], [1,5,9])) # Pulls one random item from the bag

```
<br>

### Function 6: Probability Simulator

```py

def prob_simulator(outcomes=["yes", "no"], probabilities=[0.5, 0.5], num_trials=1):
    results = []
    for i in range(num_trials):
        result = random.choices(outcomes, probabilities)[0]
        results.append(result)
    return results

```

Creates the action of a generated probability

Example:

```py
print(prob_simulator(["win","lose","draw"], [.6,.2,.2])) # Simulate given probabilities

```
<br>

## Contribution

If you're interested in contributing to the RNG Package, here's how you can set up your development environment:

1. Clone the repository:

```bash
git clone [your repository URL]
```

2. Navigate to the cloned directory and set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # On Windows use 'venv/Scripts/activate'
```

3. Install the development dependencies:

```bash
pip install -r requirements-dev.txt
```
<br>


## Building & Testing

To build and test the RNG Package locally:

1. Build the package:

```bash
python setup.py sdist bdist_wheel
```

2. Run the tests:

```bash
pytest
```

Please ensure all tests pass before submitting a pull request.
<br>


## Badge

[![Build Tests](https://github.com/software-students-spring2024/3-python-package-exercise-ppe/actions/workflows/build_tests.yml/badge.svg)](https://github.com/software-students-spring2024/3-python-package-exercise-ppe/actions/workflows/build_tests.yml)

## Team Members

[Zhongqian Chen (John)](https://github.com/ZhongqianChen) (https://github.com/ZhongqianChen)

[Eric Emmendorfer](https://github.com/ericemmendorfer) (https://github.com/ericemmendorfer)

[Hojong Shim](https://github.com/HojongShim) (https://github.com/HojongShim)

[Ethan Kim](https://github.com/ethanki) (https://github.com/ethanki)

## Package Link

[Package Link](https://pypi.org/project/rng-package/) (https://pypi.org/project/rng-package/)
