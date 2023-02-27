import pytest
from cards import *

def test_Card():
  assert Card(number=Numbers.Ace, suit=Suits.Club).get_card() == {"number": Numbers.Ace, "suit": Suits.Club, "color": Colors.Black}
  assert Card(number=Numbers.Ace, suit=Suits.Diamond).get_card() == {"number": Numbers.Ace, "suit": Suits.Diamond, "color": Colors.Red}
  assert Card(number=Numbers.Ace, suit=Suits.Heart).get_card() == {"number": Numbers.Ace, "suit": Suits.Heart, "color": Colors.Red}
  assert Card(number=Numbers.Ace, suit=Suits.Spade).get_card() == {"number": Numbers.Ace, "suit": Suits.Spade, "color": Colors.Black}

  assert Card(number=None, suit=Suits.Joker, color=Colors.Red).get_card() == {"number": None, "suit": Suits.Joker, "color": Colors.Red}
  assert Card(number=None, suit=Suits.Joker, color=Colors.Black).get_card() == {"number": None, "suit": Suits.Joker, "color": Colors.Black}

  with pytest.raises(ValueError):
    Card(number=None, suit=Suits.Club)
    Card(number=None, suit=Suits.Diamond)
    Card(number=None, suit=Suits.Heart)
    Card(number=None, suit=Suits.Spade)

    Card(number=None, suit=Suits.Joker) # without color
    Card(number=Numbers.Ace, suit=Suits.Joker) # without color

    Card(number=Numbers.Ace, suit=Suits.Joker, color=Colors.Black)

    Card(number=0, suit=Suits.Club)
    Card(number=14, suit=Suits.Club)

    Card(number=Numbers.Ace, suit=0)
    Card(number=Numbers.Ace, suit=6)

    Card(number=Numbers.Ace, suit=Suits.Club, color=0)
    Card(number=Numbers.Ace, suit=Suits.Club, color=3)


def test_Deck():
  ...