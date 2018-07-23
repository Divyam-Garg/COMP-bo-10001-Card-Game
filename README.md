# COMP-10001-bo-Card-Game

1 Game Description
In this project, you will implement a program that plays a game called “Comp10001-Bo”, which is a variant
of Skip-Bo.

In the standard version of the game, we will play Comp10001-Bo with two standard decks of 52 cards each (i.e.
104 cards in total). Each card has a “suit” (Spades, Clubs, Hearts, Diamonds) as well as a “value” (numbers 2
to 10, as well as Jack, Queen, King and Ace). For the purposes of this game, Aces are considered to have value
1, Jacks 11, Queens 12 and Kings 13. The game makes strong use of the notion of the “colour” of a card, where
Spades and Clubs are black, and Hearts and Diamonds are red.

2 The Rules of Comp10001-Bo
2.1 Overview
Comp10001-Bo is a 4-player game, where the objective is to be the first to empty out the “stockpile” that you
are dealt at the start of the game.
The primary components of the game, as depicted in Figure 1, are:
• a “hand” of 1–5 cards, that is replenished at the start of each turn or when the hand is exhausted during a
turn
• a “draw pile” (face down) that players draw cards from to make up their hand
• a “stockpile” of cards (face down, except for the top card that is revealed) — one for each player — that
they are seeking to exhaust by playing the cards onto one of the build or discard piles
1
In a moment of weakness, Tim may have entertained the possibility of naming the game “Tim-Bo”, and equally may have selfvetoed
the name.
• four “build piles”, shared between the four players (face up), that are initially empty and used to build up
sequences of cards.
The only cards that can be used to start build piles are 2s and Kings (of any colour).
Cards on build piles must all be of the same colour (i.e. all red or all black, based on the colour of the
starting card for that pile), and be adjacent in value. For example, if the top card of a build pile was a 4
of Hearts, cards that could be placed on it are a 3 of Hearts or Diamonds, a 5 of Hearts or Diamonds, or
an Ace of Hearts or Diamonds (see below). It is not possible to loop around from a King to a 2 (or vice
versa) in the case of build piles.
A non-empty build pile can be “completed” by placing a 2, King or Ace of the appropriate colour on it.
In the case of an Ace, the card does not have to be adjacent in value to the card it is placed on (as the only
exception to the adjacent value rule). Immediately on completion, build piles are cleared from the table
and shuffled into the draw pile.
• four “discard piles” per player (16 in total; face up) that are initially empty and used to discard cards from
the hand and stockpile, as well as to move (single) cards around between discard piles.
A discard pile can be started with any card other than an Ace by the owning player (it is not possible
to start the discard pile of any other player), by playing any card from the player’s hand onto the empty
discard pile. Note that it is not possible for a player to start the discard pile of another player, and equally
it is not possible to start a discard pile from the stockpile or another discard pile. Starting a new discard
pile automatically ends the player’s turn (see below).
Once a discard pile has been started any player may discard cards onto it, from their hand, stockpile or
the top card from other discard piles. Cards on discard piles must alternate in colour (between red and
black), with adjacent cards being adjacent in value, including the possibility of looping around from a
King to a 2 or vice versa (unlike build piles). For example, if the top card is a Jack of Clubs (value =
11, colour = black), cards that can be placed on it are the 10 of Hearts or Diamonds (value = 10, colour
= red), or Queen of Hearts or Diamonds (value = 12, colour = red). Note that Aces cannot be played on
discard piles under any circumstances.
In addition to starting a new discard pile, it is possible to “restart” a non-empty discard pile of any player
by illegally placing a (non-Ace) card on top of the discard pile from the hand (and only the hand). An
“illegal” placement is simply one which does not follow the rule that adjacent cards must alternate in
colour and be adjacent in value. Starting a new discard pile or “restarting” a discard pile ends the player’s
turn, whereas if a player places a card from their hand, stockpile or another discard pile (of their own or
another player) onto a non-empty discard pile counts as a single play but does not automatically end the
player’s turn (see below).
Note that the values of cards within either a discard pile or a build pile may alternate in direction (i.e. they do
not have to be monotonically increasing or decreasing). For example, if a 3 is placed on a 2, a 2 can then be
placed on the 3.
A single turn proceeds as follows. First, the player draws cards from the draw pile to make their hand up to 5
cards. They can then make any of the following plays, with up to 5 plays allowed within a single turn:
• (legally) play a card from their hand (i.e. alternating in colour and adjacent in value), their stockpile, or
the top card from a discard pile of any player onto a non-empty discard pile of any player; in the case of
taking a card from a discard pile and playing it to a discard pile, the destination cannot be the original
discard pile (i.e. it must move between piles)
• play a card from their hand, the top card from the discard pile of any player, or the top card from their
stockpile (players can only play from their own stockpile) onto a build pile
In the instance that the draw pile is exhausted, play continues based on the current composition of cards in each
player’s hand until no player can play any card, in which case, the game is abandoned.
Any of the following terminate a player’s turn:
1. placing a card from their hand onto one of their empty discard piles;
draw
pile
four build piles
four discard piles
handstockpile
Figure 1: An overview of the key components of Comp10001-Bo
2. illegally discarding a card from their hand onto any non-empty discard pile, violating the sequence of
value/colour, e.g. by placing a 2 of Spades onto a discard pile with a top card of 4 of Hearts (sequence
not followed) or 3 of Clubs (alternating colour not followed);
3. completing 5 (legal) plays;
4. being unable to make any more plays (through not holding any cards in their hand and the draw pile being
empty, and there being no legal moves between discard piles, or from a discard pile/stockpile to a build
pile);
5. emptying out their stockpile, in which case that player wins the game.
Note that a player must complete at least one play per turn if there is a legal play they can make. The only
context where a turn can consist of no plays is where the hand is empty at the start of the turn (because the draw
pile is empty), and there are no legal plays from the stockpile or any of the draw piles.
Players take it in turns to play, rotating play clockwise around the table.
2.2 Sequence of Play
The sequence of play is fixed throughout the game (based on clockwise sequence between the players). The
dealer shuffles the combined deck, deals out 8 cards to each of the 4 players face down to make up their
stockpile, and turns up the top card (the 8th card). The remainder of the cards are placed face down in the
middle of the table to form the draw pile.
2.3 The End of the Game
A game ends when: (a) a player has exhausted their stockpile; (b) the draw pile has been exhausted, and no
player can play any card; or (c) each player has completed a total of 20 turns, with no winner. In case (a), the
player who has exhausted their pile is declared the winner, and all other players are equal losers; in case (b) or
(c) all players are equal losers.

FAQ

Can we assume that all card inputs will be valid?
Yes.

How do I capture game state in my player, to use as part of my strategy?
If you are wanting to store game state in some way, or data about your player strategy (many of you won't, but for those doing more involved things, this will be relevant, to avoid redundancy of computation), you are permitted to create a SINGLE (that's right, just one ... five is right out) global variable to store this information (noting that this could be a dictionary or an instance of a class, and embed arbitrarily complex objects).

How will tournament marks be calculated?
The tournament is based on running players off against each other randomly (noting that "custom games" don't get counted in the tournament statistics). If your player makes an invalid play at any point, it will be disqualified from the whole game. If your player is disqualified enough times, it will be disqualified from the entire tournament (which is a good reason to submit your player sooner rather than later, to confirm that it is robust over different game states). The marking of the game will be based on your final submission to the tournament, which you can do from Q4 once you pass the test case (noting that we don't do this automatically — it is up to you to enter your player yourself, as we don't know what what players you want entered or not entered — and also that there's a 10 minute exclusion to entering players after each submission ... another reason not to be last minute with the project, did I hear?). Marking will be based on: (1) confirming that your player is not disqualified from the tournament (you will receive 0 marks for the tournament if you are disqualified); and (2) the ranking of the version of the player you submit last to the tournament (so make sure your final submission is the one you want marked!).

For the bonus question, how is marking going to work?
The bonus question will be marked exclusively based on the bonus tournament (separate to the standard tournament, linked off the bonus question on Grok), following the same criteria as for the standard tournament (i.e. your final player mustn't be disqualified in order to get marks).

Exactly how do "illegal" moves work?
First, there is a distinction between not being able to make any play (e.g. if the hand is made up of only Aces, and none of the build piles have been started), and being able to illegally make a play. The latter takes the form of a play from the hand (and only the hand) to a non-empty discard pile, which does not follow the rules of the discard piles (i.e. it doesn't alternate in colour or the card values are not "adjacent").

Is it right that in order to terminate your turn, you must do one of the terminating plays? (which includes doing 5 legal plays and the possibility that there are no plays you can make). This means that a player can't, for example, make two legal moves and then decide that they're done.
Correct.

Do we have to check whether the turn is valid in terms of whether we are the next player based on our player number and the previous players? And if so does that just make it an invalid illegal move — if for example the previous player number was 0 and the current player number is 2?
No, you can assume that the tournament code will look after this, and not call players out of sequence.

Also do we have to check for invalid piles and inputs and if so do we return that as an invalid illegal move?
Again, you can assume that the tournament code will make sure that all is in order in terms of valid inputs.

-----------------------------------------------------------------------------------------------------------------------------------

Q1

First, we will write functions to validate key play types in COMP10001-Bo, starting with a play to a "build pile". Here, we are validating whether a given card can be legally placed on a given build pile, irrespective of the source of that card. We will come back to consider whether it is legal to play cards in different ways, using this function.

Write the function comp10001bo_match_build(play_card, build_pile) that takes a string argument play_card (a 2-chracter string made up of the card value and suit, as described below) and a list of strings build_pile (each representing a card, also in the form of a 2-character string; the ordering of the cards in the list represents their ordering within the pile, with the first card being at the bottom of the pile and the last card being at the top of the pile). The function should return True if the card can be legally placed on the given build pile and False otherwise. Recall that for build piles:

the first card must be either a 2 ('2') or a King ('K');
the pile must follow colour (i.e. be all red or all black);
adjacent cards in the pile must be adjacent in value (e.g. a '3' can be placed on a '2' or '4' but not a '5') and cannot loop around from '2' to 'K' and vice versa; and
an Ace ('A') of appropriate colour can be placed on a non-empty build pile at any time to complete it (with the other way to complete a build pile being to place a '2' or 'K' on a non-empty pile).
You may assume that all card arguments are valid, and that the pile is also valid.

Cards are formatted as a two-character string, where the first character is the value of the card and the second character is the suit. Card values are as follows (from Ace up to King, noting that a 10 is indicated as '0'): 'A234567890JQK'; card suits are 'SHDC' for Spades, Hearts, Diamonds and Clubs, respectively.

Here are some example calls to the comp10001bo_match_build function:


>>> comp10001bo_match_build('2S', [])
True
>>> comp10001bo_match_build('3C', ['2C'])
True
>>> comp10001bo_match_build('AH', ['2D', '3H'])
True
>>> comp10001bo_match_build('3H', ['2D', '3H'])
False
>>> comp10001bo_match_build('4C', ['2D', '3H'])
False

--------------------------------------------------------------------------------------------------------------------------------------

Q2

Next, we will write a function to validate a play to a "discard pile", to determine whether a given card can be legally placed on a given discard pile, irrespective of the source of that card. We will come back to consider whether it is legal to play cards from different sources, using this function.

Write the function comp10001bo_match_discard(play_card, discard_pile, player_no, to_player_no, from_hand=True): that takes the following arguments:

play_card: a string (a 2-chracter string made up of the card value and suit, as per the previous question) describing the card the player is attempting to place on the discard pile
discard_pile: a list of strings representing the discard pile the card is to be placed on (each string represents a card in the form of a 2-character string; the ordering of the cards in the list represents their ordering within the pile, with the first card being at the bottom of the pile and the last card being at the top of the pile)
player_no: an integer representing the player number of the player attempting the play, with value 0-3, representing Players 0-3, respectively.
to_player_no: an integer representing the player number for the player who owns the discard pile in question
from_hand: a bool indicating whether the card is being played from the player's hand (True) or the stockpile/another discard pile (False), set to True by default
The function should return one of the following values:

0 if the play is invalid (i.e. it is not possible to play the card in that way)
1 if the play is a valid non-turn-ending play (i.e. it is a valid play to a non-empty discard pile)
2 if the play is a valid turn-ending play (i.e. it is an illegal play to a non-empty discard pile OR a valid play to an empty discard pile of that player, to start a new discard pile)
Recall that for discard piles:

a discard pile can be started with any card, but a given player can only start one of their own discard piles (not an empty discard pile of another player);
cards in the pile must alternate in colour (e.g. if the first card is red, the next card must be black, then red again, etc.);
adjacent cards in the pile must be adjacent in value (e.g. a '3' can be placed on a '2' or '4' but not a '5') and can loop around from '2' to 'K' and vice versa (i.e. a 'K' can be placed on a '2' and vice versa); and
Aces ('A') cannot be placed on discard piles.
You may assume that all arguments are valid in value, and that the pile is also valid.

Here are some example calls to the comp10001bo_match_discard function:


>>> comp10001bo_match_discard('4S', [], 2, 2)
2
>>> comp10001bo_match_discard('4S', [], 2, 0)
0
>>> comp10001bo_match_discard('4S', [], 2, 2, False)
0
>>> comp10001bo_match_discard('4S', ['3H'], 2, 2)
1
>>> comp10001bo_match_discard('4S', ['3H'], 2, 3)
1
>>> comp10001bo_match_discard('4S', ['3H'], 2, 3, False)
1
>>> comp10001bo_match_discard('AH', ['KS'], 2, 3)
0
>>> comp10001bo_match_discard('2H', ['KS'], 2, 3)
1

-----------------------------------------------------------------------------------------------------------------------------------

Q3

Time to put the pieces together, in validating a play in the context of the full game context, with full specification of the play type. We have provided reference versions of comp10001bo_match_build and comp10001bo_match_discard to help in testing your function, although for the final version of your player that will be submitted to the tournament, you will need to have implemented all three parts of the project yourself.

Write the function comp10001bo_is_valid_play(play, player_no, hand, stockpiles, discard_piles, build_piles) that takes the following arguments:

play: a 3-tuple specifying the nature of the play, with the following elements:
play_type: an integer, where 0 indicates a play from the hand, 1 indicates a play from a discard pile, 2 indicates a play from the player's stockpile, and 3 indicates that no play is possible
source: a specification of where the card is to be taken from; for a play from the hand, this is the card to be played (a string); for a play from a discard pile, this is a 2-tuple made up of the card and the identity of the discard pile (itself a 2-tuple, made up of the player number and discard pile number, e.g. (2, 1) indicates Player 2, discard pile 1); for a play from the player's stockpile, this is the card to be played (a string); and in the instance of there being no valid play, the value should be None
destination: a specification of where the card is to be played to, in the form of a 2-tuple indicating the destination pile type (0 = build pile; 1 = discard pile), and the identity of the pile (an integer 0-3 in the case of a build pile, and a 2-tuple of the player number and discard pile number in the case of discard pile, e.g. (0, 3) indicates Player 0 discard pile 3); in the instance that there is no valid play, the value should be (None, None)
player_no: an integer representing the player number of the player attempting the play (of value 0-3)
hand: a list of cards held by the current player
stockpiles: a 4-tuple describing the content of the stockpiles for each of the four players, each of which is in the form of a 2-tuple, made up of the top card (a string) and the number of cards in the stockpile (including the top card); note that the stockpiles are indexed according to player number
discard_piles: a 4-tuple describing the content of the discard piles for each of the four players, each of which is in the form of a 4-tuple of lists of cards (with the final card in the list being the top card of that pile); note that the discard piles are indexed according to player number
build_piles: a 4-tuple of lists of cards describing the content of the build piles, each of which is in the form of a list of cards (with the final card in the list being the top card of that pile)
The function should return one of the following values:

0 if the play is invalid
1 if the play is a valid non-turn-ending play (recalling that a turn-ending play takes the form of an illegal play to a non-empty discard pile)
2 if the play is a valid turn-ending play
3 if there is no possible play (legal or illegal)
Note that if a build pile is completed, it will automatically be removed and shuffled in with the draw pile. Similarly, you can assume that the 5 plays for the turn have not been exhausted.

Here are some example calls to the comp10001bo_is_valid_play function:

>>> # NON-FINAL VALID (from hand to build pile 0)
>>> comp10001bo_is_valid_play((0, '2C', (0, 0)), 0, ['2C', 'AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))
1
>>> # INVALID: doesn't hold card
>>> comp10001bo_is_valid_play((0, '2C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))
0
>>> # INVALID: can't play to build pile 0 (can't start with 3)
>>> comp10001bo_is_valid_play((0, '3C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))
0
>>> # NON-FINAL VALID (from hand to non-empty build pile 0)
>>> comp10001bo_is_valid_play((0, '3C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))
1
>>> # NON-FINAL VALID (from stockpile to empty build pile 1)
>>> comp10001bo_is_valid_play((2, '2C', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))
1
>>> # INVALID: attempt to play card that is not top card of own stockpile
>>> comp10001bo_is_valid_play((2, '2H', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))
0
>>> # INVALID: attempt to play card that is not top card of own stockpile (despite being top card of someone else's stockpile)
>>> comp10001bo_is_valid_play((2, '2H', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('2H', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))
0
>>> # NON-FINAL VALID (from stockpile to non-empty build pile)
>>> comp10001bo_is_valid_play((2, 'QC', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('QC', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], ['KS'], [], []))
1
>>> # NON-FINAL VALID (from stockpile to *empty* build pile 1)
>>> comp10001bo_is_valid_play((2, 'KC', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('KC', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))
1
>>> # NON-FINAL VALID (from discard pile to empty build pile 0)
>>> comp10001bo_is_valid_play((1, ('2C', (1, 0)), (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))
1
>>> # INVALID: attempt to access non-top card from discard stack 0 of player 1 
>>> comp10001bo_is_valid_play((1, ('3C', (1, 0)), (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))
0
>>> # INVALID: can't place 2C (from discard stack 0 of Player 1) on 2S (build stack 0)
>>> comp10001bo_is_valid_play((1, ('2C', (1, 0)), (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))
0
>>> # FINAL VALID: can place 9D (from hand) on 5S (discard stack 0 of Player 0), but final play for turn
>>> comp10001bo_is_valid_play((0, '9D', (1, (0, 0))), 0, ['AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))
2
>>> # INVALID: can make a number of different plays
>>> comp10001bo_is_valid_play((3, None, (None, None)), 0, ['AS', '9D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))
0
>>> # NO_PLAY: no move possible (yes, it's an impossible game state, but it proves a point)
>>> comp10001bo_is_valid_play((3, None, (None, None)), 0, [], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))
3
>>> # INVALID (attempt to move card from discard pile back to same discard pile)
>>> comp10001bo_is_valid_play((1, ('2C', (1, 0)), (1, (1, 0))), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))

--------------------------------------------------------------------------------------------------------------------------------------

Q4

Finally now, implement your game-playing strategy, optionally making use of your own implementations of comp10001bo_match_build, comp10001bo_match_discard, and comp10001bo_is_valid_play (in which case, copy your code from the previous questions into common.py along with any constants and helper functions).

Write the function comp10001bo_play(player_no, hand, stockpiles, discard_piles, build_piles, play_history) that takes the following arguments:

player_no: an integer representing the player number of the player attempting the play (of value 0-3)
hand: a list of cards held by the current player
stockpiles: a 4-tuple describing the content of the stockpiles for each of the four players, each of which is in the form of a 2-tuple, made up of the top card (a string) and the number of cards in the stockpile (including the top card); note that the stockpiles are indexed according to player number
discard_piles: a 4-tuple describing the content of the discard piles for each of the four players, each of which is in the form of a 4-tuple of lists of cards (with the final card in the list being the top card of that pile); note that the discard piles are indexed according to player number
build_piles: a 4-tuple of lists of cards describing the content of the build piles, each of which is in the form of a list of cards (with the final card in the list being the top card of that pile)
play_history: a list of 2-tuples specifying the sequence of plays to this point in the game, where each 2-tuple is made up of: (1) the ID of the player making the move, and (2) the play, based on the same structure as comp10001_is_valid_play, namely:
play_type: an integer, where 0 indicates a play from the hand, 1 indicates a play from a discard pile, 2 indicates a play from the player's stockpile, and 3 indicates that no play is possible
source: a specification of where the card is to be taken from; for a play from the hand, this is the card to be played (a string); for a play from a discard pile, this is a 2-tuple made up of the card and the identity of the discard pile (itself a 2-tuple, made up of the player number and discard pile number, e.g. (2, 1) indicates Player 2, discard pile 1); for a play from the player's stockpile, this is the card to be played (a string); and in the instance of there being no valid play, the value should be None
destination: a specification of where the card is to be played to, in the form of a 2-tuple indicating the destination pile type (0 = build pile; 1 = discard pile), and the identity of the pile (an integer 0-3 in the case of a build pile, and a 2-tuple of the player number and discard pile number in the case of discard pile, e.g. (0, 3) indicates Player 0 build pile 3); in the instance that there is no valid play, the value should be (None, None)
The function should return a 3-tuple stipulating the play you wish to make, based on the same play format as for play_history above.

Note that your hand will automatically be replenished to 5 cards before each turn, and that your function will only be called in you haven't exhausted your plays for the turn/explicitly terminated your turn. Additionally, if a build pile is completed, it will automatically be removed and shuffled in with the draw pile.

Here are some example calls to the comp10001bo_play function (noting that these require that there is a single possible play possible for the given game state; to simplify the test cases, we have created an impossible game state, namely that all hands are empty and the draw pile is also empty):

>>> # no possible play
>>> comp10001bo_play(0, [], (('7H', 7), ('3C', 8), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C'], [], [], []), [(0, (2, '2C', (0, 0)))])
(3, None, (None, None))
>>> # play from stockpile to build pile
>>> comp10001bo_play(1, [], (('7H', 7), ('3C', 8), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0)))])
(2, '3C', (0, 0))
>>> # play from stockpile to build pile
>>> comp10001bo_play(1, [], (('7H', 7), ('4S', 7), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C', '3C'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0)))])
(2, '4S', (0, 0))
>>> # play from stockpile to build pile, with example play
>>> comp10001bo_play(1, [], (('7H', 7), ('3S', 6), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C', '3C', '4S'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0))), (1, (2, '4S', (0, 0)))])
(2, '3S', (0, 0))
>>> # no valid play possible
>>> comp10001bo_play(1, [], (('7H', 7), ('0D', 5), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C', '3C', '4S', '3S'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0))), (1, (2, '4S', (0, 0))), (1, (2, '3S', (0, 0)))])

-------------------------------------------------------------------------------------------------------------------------------------
