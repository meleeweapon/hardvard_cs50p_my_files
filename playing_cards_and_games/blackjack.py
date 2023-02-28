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
    self.players = [Player(self.dealer) for _ in range(number_of_players)]

    self.playing = False
  
  def start_game(self) -> None:
    self.playing = True
    self.dealer.shuffle_deck()
    self.game_loop()
  
  def game_loop(self) -> None:
    print("starting sequence")
    self.starting_sequence()
    print(" dealer: ", self.dealer.hand)
    print("players: ", *[*self.all_hands()], sep="\n")
    print(self.dealer.deck.cards)
    while True:
      print("\n")
      print("first round")
      for index, player in enumerate(self.players):
        while True:
          player_input = input(f"player {index + 1}, enter action: ")
          try:
            success = player.dealer.request_action(player.hand, player_action_to_int[player_input])
          except KeyError:
            print("enter a valid action")
            continue
          if success:
            break
        print(self.dealer.deck.cards)
        print(player.hand)

    self.end_game()
  
  def starting_sequence(self) -> None:
    self.dealer.deal_cards(self.dealer.hand, 1)
    self.dealer.deal_cards_to_all(self.all_hands(), 2)

  
  def end_game(self) -> None:
    self.playing = False
  
  def all_hands(self) -> list[Card_Cluster]:
    return (player.hand for player in self.players)


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
  
  def deal_cards_to_all(self, destinations: list[Card_Cluster], number_of_cards: int=1) -> None:
    for destination in destinations:
      self.deal_cards(destination, number_of_cards)
  
  def request_action(self, requestors_hand: Card_Cluster, action: int) -> bool:
    match action:
      case Player_Actions.Hit:
        if self.hand_is_over_21(requestors_hand):
          return False
        self.deal_cards(requestors_hand)
        return True
      case Player_Actions.Stand:
        return True
      case Player_Actions.Double_Down:
        if self.hand_is_over_21(requestors_hand):
          return False
        self.deal_cards(requestors_hand)
        return True
      case Player_Actions.Split:
        ...
      case Player_Actions.Surrender:
        ...
  
  def hand_is_over_21(self, hand: Card_Cluster) -> bool:
    all_hands_are_over_21 = (possible_value > 21 for possible_value in self.all_possible_hand_values(hand))
    return all(all_hands_are_over_21)
    # return all(map(lambda possible_value: possible_value > 21, self.all_possible_hand_values(hand)))
  
  def all_possible_hand_values(self, hand: Card_Cluster) -> list[int]:
    has_ace = any(card.number == Numbers.Ace for card in hand)
    if has_ace:
      ...
    return [sum(card.number for card in hand)]

  

  # try if {number: 1, suit: Any} in hand



class Player:
  def __init__(self, dealer: Dealer) -> None:
    self.dealer = dealer
    self.hand = Card_Cluster()

  class Player_Actions:
    Hit = 1
    Stand = 2
    Double_Down = 3
    Split = 4
    Surrender = 5
  
  def hit(self) -> None:
    """
    Take another card.
    """
    ...
  
  def stand(self) -> None:
    """
    Take no more cards.
    """
    ...

  def double_down(self) -> None:
    """
    Take no more cards.
    """
    ...

  def split_hand(self) -> None:
    """
    Take no more cards.
    """
    ...

  def surrender(self) -> None:
    """
    Take no more cards.
    """
    ...


if __name__ == '__main__':
  main()