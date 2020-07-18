#Jimmy B 4-13-20 Blackjack
#Version 1.0: add betting

import games, cards

class BJ_Card(cards.Card):
    """ A blackjack card."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """ A blackjack Deck."""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    """ A Blackjack Hand."""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # If a card in the hand has a value of None, then total is None.
        for card in self.cards:
            if not card.value:
                return None

        # Add up card values, treating Ace as 1.
        t = 0
        for card in self.cards:
            t += card.value

        # Determine if hand contains and Ace.
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for Ace
            t += 10

        return t

    def is_busted(self):
        return self.total > 21  # Returns True or False.


class BJ_Player(BJ_Hand):
    """ a Blackjack Player."""
    def __init__(self, name):
        super(BJ_Player, self).__init__(name)
        self.stack = 100  # initialize player's stack of chips.
        self.bet = 0  # initialize player's bet.

    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N):  ")
        return response == "y"  # Returns True or False

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")
        self.stack -= self.bet
        print(self.name + ":", "$" + str(self.stack))

    def win(self):
        print(self.name, "wins")
        self.stack += self.bet
        print(self.name + ":", "$" + str(self.stack))

    def push(self):
        print(self.name, "pushes.")
        print(self.name + ":", "$" + str(self.stack))

class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

        # another deck used to top off the shoe when it gets low.
        self.deck1 = BJ_Deck()
    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        for player in self.players:
            player.bet = int(input(player.name +"," + " How many $ would you like to bet? "))

        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()  # hide dealer's first card.
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()  # reveal dealer's first card

        if not self.still_playing:
            # Since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins.
                for player in self.still_playing:
                    player.win()
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("\t\tWelcome to Blackjack!\n")

    names = []
    number = games.ask_number("How many players (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()  #print a blank line to space out the display.

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        # add another shuffled deck to back of shoe when it gets low.
        print(len(game.deck.cards))
        if len(game.deck.cards) < 30:
            print("Cards getting low... Adding another shuffled deck in the shoe behind most recent deck.")
            game.deck1.populate()
            game.deck1.shuffle()
            game.deck1.deal([game.deck], 52)

        again = games.ask_yes_no("\nDo you want to play again?: ")



main()

