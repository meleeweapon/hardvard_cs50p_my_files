from cards import *

def main() -> None:
  my_game = Blackjack_Game(4)
  my_game.start_game()


class Player_Actions:
  Hit = 1
  Stand = 2
  Double_Down = 3
  Split = 4
  Surrender = 5
player_action_to_int = {
  "Hit": 1,
  "Stand": 2,
  "Double Down": 3,
  "Split": 4,
  "Surrender": 5,
}
int_to_player_action = {value: key for key, value in player_action_to_int.items()}


class Blackjack_Game:
  def __init__(self, number_of_players: int) -> None:
    self.dealer = Dealer()
    self.players = [Player() for _ in range(number_of_players)]

    self.playing = False
  
  def start_game(self) -> None:
    self.playing = True
    self.dealer.shuffle_deck()
    self.game_loop()
  
  def game_loop(self) -> None:
    while True:
      self.dealer.deal_cards(self.dealer.hand, 1)
      for player in self.players:
        self.dealer.deal_cards(player.hand, 2)
      print(self.dealer.hand)
      print(self.players[0].hand)
      print(self.players[1].hand)
      print(self.players)
      input()
  
  def end_game(self) -> None:
    ...



class Dealer:
  def __init__(self) -> None:
    self.deck = Deck()
    self.hand = Card_Cluster()
    self.used_cards = Card_Cluster()
  
  def shuffle_deck(self) -> None:
    self.deck.shuffle_deck()
  
  def move_cards(self, source: Card_Cluster, destination: Card_Cluster, number_of_cards: int=1) -> None:
    destination.add_cards(source.remove_cards_from_top(number_of_cards))

  def deal_cards(self, destination: Card_Cluster, number_of_cards: int=1) -> None:
    self.move_cards(self.deck.cards, destination, number_of_cards)

  

class Player:
  def __init__(self) -> None:
    self.hand = Card_Cluster()

if __name__ == '__main__':
  main()