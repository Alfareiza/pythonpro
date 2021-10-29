"""
950. Reveal Cards In Increasing Order
https://leetcode.com/problems/reveal-cards-in-increasing-order/

You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1. Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

Note that the first entry in the answer is considered to be the top of the deck.
"""
from typing import List
import random


def reveals_cards(lista: List[int]):
    """
    @param lista:
    @return: Nothing
    """
    while lista:
        card_revealed = lista.pop(0)
        try:
            card_to_bottom = lista.pop(0)
            lista.append(card_to_bottom)
        except IndexError:
            break
        print(f'We reveal {card_revealed}, and move {card_to_bottom} to the bottom. The deck is now {lista}.')


if __name__ == '__main__':
    reveals_cards([2, 13, 3, 11, 5, 17, 7])
