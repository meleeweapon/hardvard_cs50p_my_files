# TODO: implement split

from cards import *

def main() -> None:
  my_dealer = Dealer(2000, 2, True)
  my_players = [Player(f"Player {index}", 10_000) for index in range(4)]
  my_game = Blackjack_Game(my_dealer, my_players, 500)
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
  def __init__(self, player_name: str, total_money: int=0) -> None:
    self.player_name = player_name
    self.hand = Card_Cluster()
    self.state = Player_States.Idle
    self.hand_state = Player_Hand_States.Not_Playing
    self.total_money = total_money
    self.hand_bet = 0
  
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



class Dealer:
  def __init__(self, total_money:int, number_of_decks: int=1, reshuffle_when_deck_is_empty: bool=False) -> None:
    # self.deck = Deck()
    # self.hand = Card_Cluster()
    # self.used_cards = Card_Cluster()
    self.reshuffle_when_deck_is_empty = reshuffle_when_deck_is_empty
    self.deck = Deck(number_of_decks)
    self.hand = Card_Cluster()
    self.used_cards = Card_Cluster()
    self.total_money = total_money
  
  def resolve_bet(self, player: Player):
    player_bet = player.hand_bet
    player.hand_bet = 0
    match player.state:
      case Player_States.Won:
        # check if house has enough money
        # if not
        if player_bet > self.total_money:
          remaining_money = self.total_money
          self.total_money = 0
          player.total_money += remaining_money + player_bet
          # returning true means house ran out of money
          return True
        else: # has enough money
          self.total_money -= player_bet
          player.total_money += player_bet * 2
      case Player_States.Lost:
        self.total_money += player_bet
      case Player_States.Pushed:
        player.total_money += player_bet
    return False


  def ask_for_bet(self, player: Player, min_bet) -> None:
    print("")
    while True:
      bet_amount = input(f"player {player.player_name}, enter bet amount: ").strip().title()
      try:
        # success = self.dealer.request_action(player.hand, player_action_to_int[player_input])
        bet_amount = int(bet_amount)
      except ValueError:
        print("enter a valid bet amount, must be an integer")
        continue
      if bet_amount < min_bet:
        print(f"enter at least {min_bet}")
        continue
      player.total_money -= bet_amount
      player.hand_bet = bet_amount
      print(player.hand_bet)
      break
  
  def shuffle_deck(self) -> None:
    self.deck.shuffle_deck()
  
  def used_cards_to_deck(self) -> None:
    self.deck.cards.add_cards(self.used_cards.remove_cards_from_top(len(self.used_cards)))
    self.deck.shuffle_deck()
    # burn card
    burn_card = self.deck.cards.remove_from_top()
    self.used_cards.add_card(burn_card)

  
  def enough_cards_check(func):
    def ooga(self, source, destination, number_of_cards: int=1) -> None:
      if len(source) < number_of_cards:
        if source == self.deck.cards:
          self.used_cards_to_deck()
          print("NO CARDS LEFT, RESHUFFLING THE DECK")
          print("")
      func(self, source, destination, number_of_cards)
    return ooga

  # @enough_cards_check
  def move_cards(self, source: Card_Cluster, destination: Card_Cluster, number_of_cards: int=1) -> None:
    if self.reshuffle_when_deck_is_empty:
      if len(source) < number_of_cards:
        if source == self.deck.cards:
          print("NO CARDS LEFT, RESHUFFLING THE DECK")
          print("")
          self.used_cards_to_deck()
    destination.add_cards(source.remove_cards_from_top(number_of_cards))
  
  def deal_cards(self, destination: Card_Cluster, number_of_cards: int=1) -> None:
    self.move_cards(self.deck.cards, destination, number_of_cards)
  
  def deal_cards_to_all(self, destinations: list[Card_Cluster], number_of_cards: int=1) -> None:
    for destination in destinations:
      self.deal_cards(destination, number_of_cards)
  
  # def request_action(self, requestors_hand: Card_Cluster, action: int) -> bool:
  def request_action(self, requesting_player: Player, action: int) -> bool:
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
          print("can't double down")
          return False
        if requesting_player.hand_bet > requesting_player.total_money:
          print("you don't have enough money")
          return False
        self.deal_cards(requesting_player.hand)
        player_bet = requesting_player.hand_bet
        requesting_player.total_money -= player_bet
        requesting_player.hand_bet += player_bet
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




class Blackjack_Game:
  def __init__(self, dealer: Dealer, players: list[Player], min_bet: int=0) -> None:
    self.dealer = dealer
    self.players = players

    self.playing = False
    self.play_forever = dealer

    self.min_bet = min_bet

    self.play_forever = self.dealer.reshuffle_when_deck_is_empty

  
  def start_game(self) -> None:
    self.playing = True
    self.dealer.shuffle_deck()
    # print(self.dealer.deck.cards)
    # print(len(self.dealer.deck.cards))
    self.game_loop()
  
  def game_loop(self) -> None:
    round_number = 0
    total_number_of_cards = self.dealer.deck.number_of_decks * 52

    # round cycle
    # continue the game until there are less than 25% of all cards
    while True:
      current_number_of_cards = len(self.dealer.deck.cards)
      if not self.play_forever:
        if not (current_number_of_cards / total_number_of_cards > 0.25):
          break
      else:
        if not (current_number_of_cards / total_number_of_cards > 0.25):
          print("reshuffling cards")
          print("deck", len(self.dealer.deck.cards))
          print("used", len(self.dealer.used_cards))
          self.dealer.used_cards_to_deck()
          print("deck", len(self.dealer.deck.cards))
          print("used", len(self.dealer.used_cards))



      round_number += 1
      continue_game = self.starting_sequence()
      if not continue_game:
        break
      print("")
      print("")
      # print(" round cycle")
      print(f"round {round_number}")
      # for player in self.players:
      #   print(
      #     player.player_name, 
      #     int_to_player_state[player.state], 
      #     player.hand, 
      #     self.dealer.all_possible_hand_values(player.hand)
      #   )
      self.update_player_states()

      # player cycle
      while True:
        if len(list(self.playing_players())) < 1:
          break
        if len(list(self.playing_and_card_receiving_players())) < 1:
          break
        
        print("")
        print(
          f"dealer",
          # self.dealer.all_possible_hand_values(self.dealer.hand), 
          [self.dealer.hand[0], "Hidden Card"],
          
        )
        for player in self.players:
          print(
            player.player_name, 
            int_to_player_state[player.state], 
            player.hand, 
            self.dealer.all_possible_hand_values(player.hand)
          )
        print("")


        # check if dealer got blackjack before asking players
        if self.dealer.hand_is_21(self.dealer.hand):
          dealer_hand = 21
          for player in self.playing_players():
            # if player hand equals to dealer hand
            if any(
              hand_value == dealer_hand and hand_value <= 21 
              for hand_value in self.dealer.all_possible_hand_values(player.hand)
            ):
              # check if dealer has 21, also should mean player has 21
              # blackjack > 21
              if dealer_hand == 21:
                if len(self.dealer.hand) == 2: # dealer has blackjack
                  if len(player.hand) == 2: # player has blackjack
                    player.state = Player_States.Pushed
                  else:
                    player.state = Player_States.Lost # dealer blackjack player no blackjack
                else:
                  if len(player.hand) == 2: # player has blackjack
                    player.state = Player_States.Won # dealer no blackjack player blackjack
                  else:
                    player.state = Player_States.Pushed # dealer no blackjack player no blackjack
              else:
                # otherwise they push
                player.state = Player_States.Pushed
            else:
              player.state = Player_States.Lost

        else: # if dealer hasn't got blackjack
          for player in self.playing_and_card_receiving_players():
            while True:
              player_input = input(f"player {player.player_name}, enter action: ").strip().title()
              try:
                # success = self.dealer.request_action(player.hand, player_action_to_int[player_input])
                success = self.dealer.request_action(player, player_action_to_int[player_input])
              except KeyError:
                print("enter a valid action")
                continue
              if success:
                # self.update_player_states()
                print(player.hand)
                self.update_player_state(player)
                if player not in self.playing_and_card_receiving_players():
                  break
                # break
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
            # if player hand bigger than dealer hand
            if any(
              hand_value > dealer_hand and hand_value <= 21 
              for hand_value in self.dealer.all_possible_hand_values(player.hand)
            ):
              player.state = Player_States.Won
            # if player hand equals to dealer hand
            elif any(
              hand_value == dealer_hand and hand_value <= 21 
              for hand_value in self.dealer.all_possible_hand_values(player.hand)
            ):
              # check if dealer has 21, also should mean player has 21
              # blackjack > 21
              if dealer_hand == 21:
                if len(self.dealer.hand) == 2: # dealer has blackjack
                  if len(player.hand) == 2: # player has blackjack
                    player.state = Player_States.Pushed
                  else:
                    player.state = Player_States.Lost # dealer blackjack player no blackjack
                else:
                  if len(player.hand) == 2: # player has blackjack
                    player.state = Player_States.Won # dealer no blackjack player blackjack
                  else:
                    player.state = Player_States.Pushed # dealer no blackjack player no blackjack
              else:
                # otherwise they push
                player.state = Player_States.Pushed
            else:
              player.state = Player_States.Lost

      # resolve all bets
      for player in self.players:
        dealer_ran_out_of_money = self.dealer.resolve_bet(player)
        if dealer_ran_out_of_money:
          break

      print("")
      print(self.dealer.total_money)
      print(" result")
      print(f"round {round_number} results")
      print(
        f"dealer {self.dealer.all_possible_hand_values(self.dealer.hand)}", 
        self.dealer.hand
      )
      for player in self.players:
        print(
          f"{player.player_name} {int_to_player_state[player.state]}", 
          player.hand, 
          self.dealer.all_possible_hand_values(player.hand),
          player.total_money
        )

      self.collect_all_hands()

      if dealer_ran_out_of_money:
        print("house ran out of money")
        break

      # end of round
      print("")

    # end of game
    self.end_game()


  def starting_sequence(self) -> None:
    # print(" starting sequence")
    # reset all hands after a round
    self.collect_all_hands()
    for player in self.players:
      # also reset player states
      player.state = Player_States.Playing
      player.hand_state = Player_Hand_States.Receiving_Cards
    
    # disqualify player without enough money
    for player in self.players:
      if player.total_money < self.min_bet:
        print(f"player {player.player_name} disqualified")
        player.state = Player_States.Idle
    
    # if there are no players end game
    if len(list(self.playing_players())) < 1:
      print("all players are disqualified")
      return False

    # ask for bets
    print("asking for bets")
    print(f"minimum bet amount: {self.min_bet}")
    for player in self.playing_players():
      self.dealer.ask_for_bet(player, self.min_bet)

    self.dealer.deal_cards_to_all([
      player.hand
      for player in self.playing_players()
    ], 1)
    # hidden card
    self.dealer.deal_cards(self.dealer.hand, 1)
    self.dealer.deal_cards_to_all([
      player.hand
      for player in self.playing_players()
    ], 1)
    # open card (hole card)
    self.dealer.deal_cards(self.dealer.hand, 1)
    return True
  
  def collect_all_hands(self) -> None:
    if len(self.dealer.hand) > 0:
      self.dealer.move_cards(self.dealer.hand, self.dealer.used_cards, len(self.dealer.hand))
    for player in self.players:
      if len(player.hand) > 0:
        self.dealer.move_cards(player.hand, self.dealer.used_cards, len(player.hand))

    
  def end_game(self) -> None:
    self.playing = False
    for player in self.players:
      player.state = Player_States.Idle

    print(f" end game")
    # print(self.dealer.deck.cards)
    # print(f"end game results")
    # print(
    #   f"dealer {self.dealer.all_possible_hand_values(self.dealer.hand)}", 
    #   self.dealer.hand
    # )
    # for player in self.players:
    #   print(
    #     f"{player.player_name} {int_to_player_state[player.state]}", 
    #     player.hand, 
    #     self.dealer.all_possible_hand_values(player.hand)
    #   )
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
          if len(player.hand) == 2:
            player.hand_state = Player_Hand_States.Hit_Blackjack
          else:
            player.hand_state = Player_Hand_States.Standing
          # player.state = Player_States.Won

      # if self.dealer.hand_is_over_21(player.hand):
      #   player.state = Player_States.Lost

  @property
  def play_forever(self) -> bool:
    return self._play_forever
  @play_forever.setter
  def play_forever(self, value):
    self._play_forever = value
    self.dealer.reshuffle_when_deck_is_empty = value




if __name__ == '__main__':
  main()