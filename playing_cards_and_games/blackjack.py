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
    self.players = [Player(f"Player {index}") for index in range(number_of_players)]

    self.playing = False

  
  def start_game(self) -> None:
    self.playing = True
    self.dealer.shuffle_deck()
    self.game_loop()
  
  def game_loop(self) -> None:
    print("starting sequence")
    self.starting_sequence()
    print(" dealer: ", self.dealer.hand)
    print("players: ", *self.all_hands(), sep="\n")
    # print(self.dealer.deck.cards)
    while True:
      print("\n")
      print("first round")


      self.update_player_states()
      if len(list(self.playing_players())) < 1:
        break

      for player in self.players:
        print(player.player_name, int_to_player_state[player.state], self.dealer.all_possible_hand_values(player.hand))

      
      for player in self.playing_players():
        while True:
          player_input = input(f"player {player.player_name}, enter action: ").strip().title()
          try:
            success = self.dealer.request_action(player.hand, player_action_to_int[player_input])
          except KeyError:
            print("enter a valid action")
            continue
          if success:
            break
        print(player.hand)

    self.end_game()


  def starting_sequence(self) -> None:
    self.dealer.deal_cards(self.dealer.hand, 1)
    self.dealer.deal_cards_to_all(self.all_hands(), 2)
    for player in self.players:
      player.state = Player_States.Playing
    
  def end_game(self) -> None:
    self.playing = False
  
  def all_hands(self) -> list[Card_Cluster]:
    return (player.hand for player in self.players)
  
  def playing_players(self) -> list:
    return (player for player in self.players if player.state == Player_States.Playing)
  
  def update_player_states(self) -> None:
    for player in self.playing_players():
      comparison_to_21 = self.dealer.compare_to_21(player.hand)
      match comparison_to_21:
        case Hand_Comparison_To_21.Smaller_Than_21:
          player.state = Player_States.Playing
        case Hand_Comparison_To_21.Greater_Than_21:
          player.state = Player_States.Lost
        case Hand_Comparison_To_21.Equal_To_21:
          player.state = Player_States.Won

      # if self.dealer.hand_is_over_21(player.hand):
      #   player.state = Player_States.Lost


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
        # if self.hand_is_over_21(requestors_hand):
        #   return False
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
  
  def hand_is_21(self, hand: Card_Cluster) -> bool:
    is_21_list = (possible_value == 21 for possible_value in self.all_possible_hand_values(hand))
    return any(is_21_list)

  def compare_to_21(self, hand: Card_Cluster) -> int:
    if self.hand_is_21(hand):
      return Hand_Comparison_To_21.Equal_To_21
    if self.hand_is_over_21(hand):
      return Hand_Comparison_To_21.Greater_Than_21
    return Hand_Comparison_To_21.Smaller_Than_21
  
  def all_possible_hand_values(self, hand: Card_Cluster) -> list[int]:
    aces = [card for card in hand if card.number == Numbers.Ace]
    if len(aces) > 0:
      return [
        sum(self.card_value(card) if card.number != Numbers.Ace else value for card in hand)
        for ace in aces
        for value in (Numbers.Ace, Numbers.Ten)
      ]
    return [sum(self.card_value(card) for card in hand)]
  
  def card_value(self, card: Card) -> int:
    return card.number if card.number <= 10 else 10


class Hand_Comparison_To_21:
  Smaller_Than_21 = 1
  Equal_To_21 = 2
  Greater_Than_21 = 3

class Player_States:
  Idle = 1
  Playing = 2
  Lost = 3
  Won = 4
player_state_to_int = {
  "Idle": 1,
  "Playing": 2,
  "Lost": 3,
  "Won": 4,
}
int_to_player_state = {value: key for key, value in player_state_to_int.items()}

# class Player_Playing_States:
#   Playing = 1
#   Standing = 2
#   Doubled_Down = 3
#   Won = 4
# player_state_to_int = {
#   "Idle": 1,
#   "Playing": 2,
#   "Lost": 3,
#   "Won": 4,
# }
# int_to_player_state = {value: key for key, value in player_state_to_int.items()}


class Player:
  def __init__(self, player_name: str) -> None:
    self.player_name = player_name
    self.hand = Card_Cluster()
    self.state = Player_States.Idle
    # self.playing_state = 
  
  # def hit(self) -> None:
  #   """
  #   Take another card.
  #   """
  #   ...
  
  # def stand(self) -> None:
  #   """
  #   Take no more cards.
  #   """
  #   ...

  # def double_down(self) -> None:
  #   """
  #   Take no more cards.
  #   """
  #   ...

  # def split_hand(self) -> None:
  #   """
  #   Take no more cards.
  #   """
  #   ...

  # def surrender(self) -> None:
  #   """
  #   Take no more cards.
  #   """
  #   ...


if __name__ == '__main__':
  main()