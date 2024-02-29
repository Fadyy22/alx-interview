#!/usr/bin/python3
"""module for makeChange"""


def makeChange(coins, total):
    """returns fewest number of coins needed to meet a given amount total"""
    no_coins = 0
    sorted_coins = sorted(coins, reverse=True)
    if total > 0:
        for i in range(len(sorted_coins)):
            while total >= sorted_coins[i]:
                total -= sorted_coins[i]
                no_coins += 1
        if total != 0:
            return -1
        return no_coins
    return 0
