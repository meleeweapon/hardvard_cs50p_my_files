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
    self.starting_sequence()
    print(" dealer: ", self.dealer.hand)
    for player in self.players:
      print(
        player.player_name, 
        int_to_player_state[player.state], 
        player.hand, 
        self.dealer.all_possible_hand_values(player.hand)
      )
    self.update_player_states()

    # player cycle
    while True:
      print("\n")
      print("first round")


      if len(list(self.playing_players())) < 1:
        break

      print(
        f"dealer {self.dealer.all_possible_hand_values(self.dealer.hand)}", 
        self.dealer.hand
      )
      for player in self.players:
        print(
          player.player_name, 
          int_to_player_state[player.state], 
          player.hand, 
          self.dealer.all_possible_hand_values(player.hand)
        )
      
      if len(list(self.playing_and_card_receiving_players())) < 1:
        break
      
      # for player in self.playing_players():
      for player in self.playing_and_card_receiving_players():
        while True:
          player_input = input(f"player {player.player_name}, enter action: ").strip().title()
          # player_input = "Stand"
          try:
            # success = self.dealer.request_action(player.hand, player_action_to_int[player_input])
            success = self.dealer.request_action(player, player_action_to_int[player_input])
          except KeyError:
            print("enter a valid action")
            continue
          if success:
            # self.update_player_states()
            self.update_player_state(player)
            if player not in self.playing_and_card_receiving_players():
              break
            # break
          print(player.hand)
        # print(player.hand)
    
    # dealer hand cycle
    while (
      not any(
        hand_value >= 17 and hand_value <= 21 
        for hand_value in self.dealer.all_possible_hand_values(self.dealer.hand)
      )
      and min(self.dealer.all_possible_hand_values(self.dealer.hand)) < 21
    ):
      self.dealer.deal_cards(self.dealer.hand)
    
    dealer_hand = max(
      (
        hand_value 
        for hand_value in self.dealer.all_possible_hand_values(self.dealer.hand) 
        if hand_value <= 21
      )
      , default= max(self.dealer.all_possible_hand_values(self.dealer.hand))
    )
    if dealer_hand > 21:
      for player in self.playing_players():
        player.state = Player_States.Won
    else:
      for player in self.playing_players():
        if any(
          hand_value > dealer_hand and hand_value <= 21 
          for hand_value in self.dealer.all_possible_hand_values(player.hand)
        ):
          player.state = Player_States.Won
        elif any(
          hand_value == dealer_hand and hand_value <= 21 
          for hand_value in self.dealer.all_possible_hand_values(player.hand)
        ):
          player.state = Player_States.Pushed
        else:
          player.state = Player_States.Lost


    self.end_game()


  def starting_sequence(self) -> None:
    print("starting sequence")
    self.dealer.deal_cards(self.dealer.hand, 2)
    self.dealer.deal_cards_to_all(self.all_hands(), 2)
    for player in self.players:
      player.state = Player_States.Playing
      player.hand_state = Player_Hand_States.Receiving_Cards
    
  def end_game(self) -> None:
    self.playing = False

    print(f"\n")
    print(f"end game results")
    print(
      f"dealer {self.dealer.all_possible_hand_values(self.dealer.hand)}", 
      self.dealer.hand
    )
    for player in self.players:
      print(
        f"{player.player_name} {int_to_player_state[player.state]}", 
        player.hand, 
        self.dealer.all_possible_hand_values(player.hand)
      )
  
  def all_hands(self) -> list[Card_Cluster]:
    return (player.hand for player in self.players)
  
  def playing_players(self) -> list:
    return (
      player for player in self.players 
      if player.state == Player_States.Playing
    )
  
  def playing_and_card_receiving_players(self) -> list:
    return (
      player for player in self.playing_players() 
      if (
        player.hand_state == Player_Hand_States.Receiving_Cards 
        or player.hand_state == Player_Hand_States.Took_A_Card
      )
    )
  
  def update_player_states(self) -> None:
    for player in self.playing_players():
      self.update_player_state(player)

  def update_player_state(self, player) -> None:
      comparison_to_21 = self.dealer.compare_to_21(player.hand)
      # print("comparing to 21", player.hand, comparison_to_21)
      match comparison_to_21:
        case Hand_Comparison_To_21.Smaller_Than_21:
          player.state = Player_States.Playing
        case Hand_Comparison_To_21.Greater_Than_21:
          player.state = Player_States.Lost
        case Hand_Comparison_To_21.Equal_To_21:
          player.state = Player_States.Playing
          player.hand_state = Player_Hand_States.Hit_Blackjack
          # player.state = Player_States.Won

      # if self.dealer.hand_is_over_21(player.hand):
      #   player.state = Player_States.Lost


class Dealer:
  def __init__(self) -> None:
    # self.deck = Deck()
    # self.hand = Card_Cluster()
    # self.used_cards = Card_Cluster()
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
  
  # def request_action(self, requestors_hand: Card_Cluster, action: int) -> bool:
  def request_action(self, requesting_player, action: int) -> bool:
    match action:
      case Player_Actions.Hit:
        if (
          requesting_player.hand_state != Player_Hand_States.Receiving_Cards 
          and requesting_player.hand_state != Player_Hand_States.Took_A_Card
        ):
          return False
        # if self.hand_is_over_21(requestors_hand):
        #   return False
        self.deal_cards(requesting_player.hand)
        requesting_player.hand_state = Player_Hand_States.Took_A_Card
        return True
      case Player_Actions.Stand:
        requesting_player.hand_state = Player_Hand_States.Standing
        return True
      case Player_Actions.Double_Down:
        if requesting_player.hand_state != Player_Hand_States.Receiving_Cards:
          return False
        self.deal_cards(requesting_player.hand)
        requesting_player.hand_state = Player_Hand_States.Doubled_Down
        return True
      case Player_Actions.Split:
        ...
      case Player_Actions.Surrender:
        ...
  
  def hand_is_over_21(self, hand: Card_Cluster) -> bool:
    all_hands_are_over_21 = (
      possible_value > 21 
      for possible_value in self.all_possible_hand_values(hand)
    )
    return all(all_hands_are_over_21)
    # return all(map(lambda possible_value: possible_value > 21, self.all_possible_hand_values(hand)))
  
  def hand_is_21(self, hand: Card_Cluster) -> bool:
    is_21_list = (
      possible_value == 21 
      for possible_value in self.all_possible_hand_values(hand)
    )
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
        sum(
          self.card_value(card) if card.number != Numbers.Ace else value 
          for card in hand
        )
        for ace in aces
        for value in (Numbers.Ace, 11)
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
  Pushed = 5
player_state_to_int = {
  "Idle": 1,
  "Playing": 2,
  "Lost": 3,
  "Won": 4,
  "Pushed": 5,
}
int_to_player_state = {value: key for key, value in player_state_to_int.items()}

class Player_Hand_States:
  Receiving_Cards = 1
  Standing = 2
  Doubled_Down = 3
  Not_Playing = 4
  Took_A_Card = 5
  Hit_Blackjack = 6
player_hand_states_to_int = {
  "Receiving Cards": 1,
  "Standing": 2,
  "Doubled Down": 3,
  "Not Playing": 4,
  "Took A Card": 5,
  "Hit Blackjack": 6,
}
int_to_player_hand_states = {value: key for key, value in player_hand_states_to_int.items()}


class Player:
  def __init__(self, player_name: str) -> None:
    self.player_name = player_name
    self.hand = Card_Cluster()
    self.state = Player_States.Idle
    self.hand_state = Player_Hand_States.Not_Playing
  
  @property
  def state(self) -> int:
    return self._state
  
  @state.setter
  def state(self, value: int) -> None:
    self._state = value
    match value:
      case Player_States.Playing:
        pass
        # self.hand_state = Player_Hand_States.Receiving_Cards
      # case Player_States.Idle | Player_States.Lost | Player_States.Won | Player_States.Pushed:
      case _:
        self.hand_state = Player_Hand_States.Not_Playing

  
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