#!/usr/bin/env python3

import argparse
import random
import re


def roll(max_roll):
    return random.randint(1, max_roll)

def full_throw(die_list):
    total = []
    for die in die_list:
        (num_dice, max_roll) = die.split('d')
        (num_dice, max_roll) = (int(num_dice), int(max_roll))

        for y in range(0, num_dice):
            face = ('d{}'.format(max_roll), roll(max_roll))
            total.append(face)

    return total

def ensure_input(dice_req):
    dice_good = []

    for die in dice_req:
        good_format = re.match('\d+d\d+', die)

        if good_format:
            dice_good.append(die)
        else:
            continue

    if dice_good:
        return dice_good
    else:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple dice roller')
    parser.add_argument('dice', nargs='+',
                        help='Number and Type of Dice in the form NdX')
    args = parser.parse_args()

    print(type(args.dice))
    print(args.dice)

    throw = full_throw(ensure_input(args.dice))
    for i in throw:
        print(type(i))

    print(throw)

    total = 0
    for die in throw:
        total += die[1]

    print("The total is {}.".format(total))
