# A UNO inspired card game, not the actual game (don't sue me thx xD)
import random
from pprint import pprint


def roll(lst: list, n: int = 1, right: bool = True) -> None:
    """Rolls the referenced list to the right by one index or left by the given number of indices."""
    temp = lst[-n:] + lst[:-n] if right else lst[n:] + lst[:n]
    lst.clear()
    lst.extend(temp)


class Card:
    VALID_COLORS = ('red', 'green', 'blue', 'yellow', 'wild')
    VALID_VALUES = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'skip', 'reverse', 'draw2', 'wild', 'wild4')
    VALID_POINTS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'skip': 20,
                    'reverse': 20, 'draw2': 20, 'wild': 50, 'wild4': 50}

    def __init__(self, color: int, value: int):
        """Initialize a card with a color and a value using the given integers as indices for the VALID_COLORS
        and VALID_VALUES tuples of this Class."""
        self.__color: str = Card.VALID_COLORS[color]
        self.__value: str = Card.VALID_VALUES[value]
        self.__points: int = Card.VALID_POINTS[self.__value]

    def get_color(self) -> str:
        return self.__color

    def get_value(self) -> str:
        return self.__value

    def get_points(self) -> int:
        return self.__points

    def __str__(self):
        return f'{self.__color} {self.__value}'

    def __repr__(self):
        return f'Card({self.__color}, {self.__value}, {self.__points})'


def create_deck():
    generated_deck = []
    for color in range(4):
        generated_deck.append(Card(color, 0))
        generated_deck.append(Card(4, 13))
        generated_deck.append(Card(4, 14))
        for value in range(1, 13):
            generated_deck.append(Card(color, value))
            generated_deck.append(Card(color, value))
    return generated_deck


class CardPile:
    def __init__(self):
        self.__deck = []

    def add_to_pile(self, card: Card) -> None:
        self.__deck.append(card)

    def get_card_pile(self, amount: int = 0) -> list[Card]:
        return self.__deck[-amount:]

    def pop_all_cards_without_top(self) -> list[Card]:
        cards = self.__deck[:-1]
        del self.__deck[:-1]
        return cards


class DrawPile:
    def __init__(self, deck: list[Card]):
        self.__deck = deck

    def shuffle_cards(self) -> None:
        for _ in range(2):
            random.shuffle(self.__deck)

    def pop_from_draw_pile(self) -> Card:
        return self.__deck.pop()

    def get_draw_pile(self) -> list[Card]:
        return self.__deck


class Hand:
    def __init__(self):
        self.__inventory = []

    def add_cards(self, cards: list[Card]) -> None:
        self.__inventory.extend(cards)

    def remove_card(self, index: int) -> Card:
        return self.__inventory.pop(index)

    def get_hand(self) -> list[Card]:
        return self.__inventory


class Player(Hand):
    def __init__(self, id_num: int):
        Hand.__init__(self)
        self._id = id_num
        ...


class Game(DrawPile, CardPile):
    def __init__(self, deck: list[Card], players: int):
        if players < 2 or players > 10:
            raise ValueError('Number of players must be between 2 and 10')
        self.__player_order = [Player(i) for i in range(players)]
        self.__players = {player: player._id for player in self.__player_order}  # NOQA it's my code, I can do what I want

        DrawPile.__init__(self, deck.copy())
        CardPile.__init__(self)

    def give_starting_hand(self, num_cards: int) -> None:
        for _ in range(num_cards):
            for player in self.__player_order:
                player.add_cards([self.pop_from_draw_pile()])
        self.add_to_pile(self.pop_from_draw_pile())

    def draw(self):
        ...  # TODO: Implement draw method and CardPile class

    def setup(self):
        ...

    def round(self) -> dict | None:
        """
        The main game loop, where the game is played.
        it needs to be called in a loop until the game is over.
        it returns the winner and Points of the Players or None if the game is not over.
        """
        ...


if __name__ == '__main__':
    new_deck = create_deck()
    # pprint(new_deck)
    game = Game(new_deck, 2)
    game.shuffle_cards()
    game.give_starting_hand(7)


    # a = CardPile()
    # for example in range(10):
    #     a.add_to_pile(new_deck[example])
    # print(a.get_card_pile(3))
    # print(a.get_card_pile())
    # print(a.pop_all_cards_without_top())
    # print(a.get_card_pile())
