from rng_package.functions import *

def test_coin_flip_defaults():
    # Test default behavior with one coin flip
    result = coin_flip()
    assert len(result) == 1
    assert result[0] in ['heads', 'tails']

def test_coin_flip_multiple_coins():
    # Test flipping multiple coins
    num_coins = 5
    result = coin_flip(num_coins)
    assert len(result) == num_coins
    assert all(coin in ['heads', 'tails'] for coin in result)

def test_coin_flip_invalid_input():
    # Test with invalid input (negative number of coins)
    num_coins = -1
    result = coin_flip(num_coins)
    assert len(result) == 0  # Expect an empty list for negative input

def test_dice_roll_defaults():
    # Test default behavior with one die and six sides
    result = dice_roll()
    assert len(result) == 1
    assert 1 <= result[0] <= 6

def test_dice_roll_multiple_dice():
    # Test rolling multiple dice
    num_dice = 3
    result = dice_roll(num_dice)
    assert len(result) == num_dice
    assert all(1 <= die <= 6 for die in result)

def test_dice_roll_custom_sides():
    # Test rolling dice with custom number of sides
    num_dice = 5
    sides = 10
    result = dice_roll(num_dice, sides)
    assert len(result) == num_dice
    assert all(1 <= die <= sides for die in result)

def test_dice_roll_invalid_input():
    # Test with invalid input (negative number of dice)
    num_dice = -1
    sides = 6
    result = dice_roll(num_dice, sides)
    assert len(result) == 0  # Expect an empty list for negative input

def test_draw_cards_defaults():
    # Test default behavior with one hand and one card
    result = draw_cards()
    assert len(result) == 1
    assert len(result[0]) == 1

def test_draw_cards_multiple_hands():
    # Test drawing multiple hands
    num_hands = 3
    result = draw_cards(num_hands)
    assert len(result) == num_hands
    assert all(len(hand) == 1 for hand in result)

def test_draw_cards_multiple_cards():
    # Test drawing multiple cards in each hand
    num_cards = 5
    result = draw_cards(num_cards=num_cards)
    assert len(result) == 1
    assert len(result[0]) == num_cards

def test_draw_cards_invalid_input():
    # Test with invalid input (negative number of hands)
    num_hands = -1
    num_cards = 5
    result = draw_cards(num_hands, num_cards)
    assert len(result) == 0  # Expect an empty list for negative input

def test_generate_powerball_defaults():
    # Test default behavior
    result = generate_powerball()
    assert len(result) == 6
    assert all(1 <= num <= 69 for num in result[:5])
    assert 1 <= result[5] <= 26

def test_generate_powerball_multiple_times():
    # Test generating multiple powerball combinations
    num_times = 10
    results = [generate_powerball() for _ in range(num_times)]
    assert all(len(result) == 6 for result in results)
    assert all(1 <= num <= 69 for result in results for num in result[:5])
    assert all(1 <= result[5] <= 26 for result in results)

def test_generate_powerball_unique_combinations():
    # Test generating multiple powerball combinations and ensure uniqueness
    num_times = 1000
    results = [generate_powerball() for _ in range(num_times)]
    unique_results = set(tuple(result) for result in results)
    assert len(results) == len(unique_results)

def test_draw_from_bag_defaults():
    # Test default behavior
    result = draw_from_bag()
    assert len(result) == 1
    assert result[0] in ['red', 'blue', 'green']

def test_draw_from_bag_custom_items():
    # Test drawing from a bag with custom items
    itemTypes = ['apple', 'banana', 'cherry']
    result = draw_from_bag(itemTypes)
    assert len(result) == 1
    assert result[0] in itemTypes

def test_draw_from_bag_custom_item_nums():
    # Test drawing from a bag with custom item numbers
    itemTypes = ['apple', 'banana', 'cherry']
    itemNums = [3, 2, 1]
    result = draw_from_bag(itemTypes, itemNums)
    assert len(result) == 1
    assert result[0] in itemTypes

def test_draw_from_bag_multiple_draws():
    # Test drawing multiple items from the bag
    itemTypes = ['apple', 'banana', 'cherry']
    itemNums = [3, 2, 1]
    drawNum = 5
    result = draw_from_bag(itemTypes, itemNums, drawNum)
    assert len(result) == drawNum
    assert all(item in itemTypes for item in result)

def test_prob_simulator_defaults():
    # Test default behavior
    result = prob_simulator()
    assert len(result) == 1
    assert result[0] in ['yes', 'no']

def test_prob_simulator_custom_outcomes():
    # Test custom outcomes
    outcomes = ['win', 'lose', 'draw']
    probabilities=[]
    prob = 1/len(outcomes)
    for i in range(len(outcomes)):
        probabilities.append(prob)
    result = prob_simulator(outcomes)
    assert len(result) == 1
    assert result[0] in outcomes

def test_prob_simulator_custom_probabilities():
    # Test custom probabilities
    outcomes = ['win', 'lose', 'draw']
    probabilities = [0.2, 0.5, 0.3]
    result = prob_simulator(outcomes, probabilities)
    assert len(result) == 1
    assert result[0] in outcomes

def test_prob_simulator_multiple_trials():
    # Test multiple trials
    num_trials = 10
    result = prob_simulator(num_trials=num_trials)
    assert len(result) == num_trials
    assert all(outcome in ['yes', 'no'] for outcome in result)

def test_prob_simulator_invalid_probabilities():
    # Test with invalid probabilities (not summing to 1)
    outcomes = ['win', 'lose', 'draw']
    probabilities = [0.2, 0.5, 0.4]
    result = prob_simulator(outcomes, probabilities)
    assert len(result) == 0  # Expect an empty list for invalid probabilities

def test_prob_simulator_invalid_input():
    # Test with invalid input (negative number of trials)
    num_trials = -1
    result = prob_simulator(num_trials=num_trials)
    assert len(result) == 0  # Expect an empty list for negative input

def test_prob_simulator_custom_outcomes_probabilities():
    # Test with custom outcomes and probabilities
    outcomes = ['win', 'lose', 'draw']
    probabilities = [0.3, 0.4, 0.3]
    num_trials = 1000
    result = prob_simulator(outcomes, probabilities, num_trials)
    assert len(result) == num_trials
    assert all(outcome in outcomes for outcome in result)

