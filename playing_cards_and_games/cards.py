import random

suits_to_int = {
  "Club":    1,
  "Diamond": 2,
  "Heart":   3,
  "Spade":   4,
  "Joker":   5,
}
int_to_suits = {value: key for key, value in suits_to_int.items()}
class Suits:
  Club    = 1
  Diamond = 2
  Heart   = 3
  Spade   = 4
  Joker   = 5


int_to_number = {
  1:  "Ace",
  2:  "2",
  3:  "3",
  4:  "4",
  5:  "5",
  6:  "6",
  7:  "7",
  8:  "8",
  9:  "9",
  10: "10",
  11: "Jack",
  12: "Queen",
  13: "King",
}
number_to_int = {value: key for key, value in int_to_number.items()}
class Numbers:
  Ace   = 1
  Two   = 2
  Three = 3
  Four  = 4
  Five  = 5
  Six   = 6
  Seven = 7
  Eight = 8
  Nine  = 9
  Ten   = 10
  Jack  = 11
  Queen = 12
  King  = 13


color_to_int = {
  "Red": 1,
  "Black": 2,
}
int_to_color = {value: key for key, value in color_to_int.items()}
class Colors:
  Red = 1
  Black = 2


class Card:
  def __init__(self, suit: int, number: int | None=None, color: int | None=None) -> None:
    self.suit = suit
    self.number = number
    self.color = color
  
  def __str__(self) -> str:
    if self.suit == Suits.Joker:
      return f"{int_to_color[self.get_color()]} Joker"
    return f"{int_to_number[self.get_number()]} of {int_to_suits[self.get_suit()]}s"
  def __repr__(self) -> str:
    return self.__str__()
  
  @property
  def number(self) -> int:
    return self._number
  
  @number.setter
  def number(self, value: int | None):
    if value == None:
      if self.suit == Suits.Joker:
        self._number = value
        return
      else:
        raise ValueError
    else:
      if value < 1 or value > 13:
        raise ValueError
      self._number = value

    if value < 1 or value > 13:
      raise ValueError
    self._number = value
  
  def get_number(self):
    return self.number

  @property
  def suit(self) -> int:
    return self._suit
  
  @suit.setter
  def suit(self, value: int):
    if value < 1 or value > 5:
      raise ValueError
    self._suit = value
    if value == Suits.Joker:
      self.number = None

  def get_suit(self):
    return self.suit
  
  @property
  def color(self) -> int:
    return self._color
  
  @color.setter
  def color(self, value: int | None):
    if value == None:
      match self.suit:
        case Suits.Club | Suits.Spade:
          self._color = Colors.Black
          return
        case Suits.Heart | Suits.Diamond:
          self._color = Colors.Red
          return
        case _:
          raise ValueError
    if value < 1 or value > 2:
      raise ValueError
    self._color = value

  def get_color(self) -> int:
    return self.color
  
  def get_card(self) -> dict[int, int]:
    return {"number": self.number, "suit": self.suit, "color": self.color}



class Deck:
  def __init__(self, has_joker:bool=False) -> None:
    """
    Last card in the list is the card on top of the deck
    """

    self.cards: list[Card] = []

    for suit in (Suits.Club, Suits.Heart, Suits.Diamond, Suits.Spade):
      for number in range(1, 14):
        # self.cards.append(Card(suit, number))
        self.add_card(Card(suit, number))
    
    if has_joker:
      # self.cards.append(Card(Suits.Joker, color=Colors.Black))
      # self.cards.append(Card(Suits.Joker, color=Colors.Red))
      self.add_card(Card(Suits.Joker, color=Colors.Black))
      self.add_card(Card(Suits.Joker, color=Colors.Red))
  
  def __str__(self) -> str:
    return str(self.cards)
  def __repr__(self) -> str:
    return self.__str__()
  
  @property
  def cards(self) -> list[Card]:
    return self._cards
  
  @cards.setter
  def cards(self, value):
    self._cards = value
  
  def add_card(self, card: Card) -> None:
    self.cards.append(card)
  
  def has_card(self, card: Card) -> bool:
    return card in self.cards
  
  def remove_card(self, card: Card) -> None:
    self.cards.remove(card)
  
  def remove_from_top(self) -> Card:
    return self.cards.pop()
  
  def peek_at_top(self) -> Card:
    return self.cards[-1]
  
  def shuffle_deck(self) -> None:
    random.shuffle(self.cards)
  
  def split_deck(self, number_of_cards_from_top: int):
    top_part = self.cards[-number_of_cards_from_top:]
    print("top part:", top_part, end="\n\n")
    bottom_part = self.cards[:-number_of_cards_from_top]
    print("bottom part:", bottom_part, end="\n\n")
    # self.cards = bottom_part.extend(top_part)
    self.cards = top_part
    self.cards.extend(bottom_part)



my_deck = Deck()
my_deck.shuffle_deck()
print(my_deck, end="\n\n")

my_deck.split_deck(3)
print(my_deck, end="\n\n")
