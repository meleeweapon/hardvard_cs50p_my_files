# suits_to_int = {
#   "Club":    1,
#   "Diamond": 2,
#   "Heart":   3,
#   "Spade":   4,
#   "Joker":   5,
# }
# int_to_suits = {value: key for key, value in suits_to_int.items()}
class suits:
  club = 1
  diamond = 2
  heart = 3
  spade = 4
  joker = 5


# int_to_number = {
#   1:  "Ace",
#   2:  "2",
#   3:  "3",
#   4:  "4",
#   5:  "5",
#   6:  "6",
#   7:  "7",
#   8:  "8",
#   9:  "9",
#   10: "10",
#   11: "Jack",
#   12: "Queen",
#   13: "King",
# }
# number_to_int = {value: key for key, value in int_to_number.items()}


# color_to_int = {
#   "Red": 1,
#   "Black": 2,
# }
# int_to_color = {value: key for key, value in color_to_int.items()}


class Card:
  def __init__(self, number: int, suit: int, color: int | None) -> None:
    self._suit = suit
    self._number = number
    self._color = color
  
  def __str__(self) -> str:
    pass
  
  @property
  def number(self) -> int:
    return self._number
  
  @number.setter
  def number(self, value: int):
    if self._suit == suits_to_int["Joker"] and self._number != None:
      raise ValueError
    if value < 1 or value > 13:
      raise ValueError
    self._number = value
  
  def get_number(self):
    return self._number

  @property
  def suit(self) -> int:
    return self._suit
  
  @suit.setter
  def suit(self, value: int):
    if value < 1 or value > 5:
      raise ValueError
    if value == suits_to_int["Joker"]:
      self._number = None
    self._suit = value

  def get_suit(self):
    return self._suit
  
  @property
  def color(self) -> int:
    return self._color
  
  @color.setter
  def color(self, value: int | None):
    if value < 1 or value > 2:
      raise ValueError
    if value == None:
      match self._suit:
        # case suits_to_int["Club"] | suits_to_int["Spade"]:
        case suits.club | suits.spade:
          self._color = color_to_int["Black"]
          return
        # case suits_to_int["Heart"] | suits_to_int["Diamond"]:
        case suits.heart | suits.diamond:
          self._color = color_to_int["Red"]
          return
        case _:
          raise ValueError
    self._color = value


class Deck:
  def __init__(self) -> None:
    pass
