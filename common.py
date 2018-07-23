# INSERT CONSTANTS AND FUNCTIONS USED ACROSS ALL QUESTIONS HERE

#what numeric value each value symbol corresponds to
real_values = {'A': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}

#what colour each suit is
suit_colour = {'S': 'Black', 'C': 'Black', 'D': 'Red', 'H': 'Red'}

def value(card):
    '''Returns the value symbol of the card'''
    return card[0]

def suit(card):
    '''Returns the suit of the card'''
    return card[1]

def same_colour(card1, card2):
    '''
    Returns True if card1 and card2 are of same colour and False otherwise
    '''
    return suit_colour[suit(card1)] == suit_colour[suit(card2)]
      
def adjacent(card1, card2, pile_type):
    '''
    (str, str, str) --> (bool)
    
    pile_type takes the value 'D' or 'B' if either of card1 or card 2 is from a
    discard pile or build pile respectively. Returns True if card1 and card2 
    are adjacent according to adjacency rules for pile_type'''
    
    if pile_type == 'B':
        #Cant loop between '2' and 'K' in build pile
        return abs(real_values[value(card1)] - real_values[value(card2)]) == 1
    elif pile_type == 'D':
        #Can loop between '2' and 'K' in discard pile
        return abs(real_values[value(card1)] - real_values[value(card2)]) == 1\
               or (value(card1), value(card2)) == ('2', 'K') \
               or (value(card1), value(card2)) == ('K', '2')
    
def top_card(pile):
    '''Returns the string representation of the top card of pile if the pile
       is non-empty. Returns None otherwise.'''
    if len(pile) == 0:
        return None
    else:
        return pile[-1]
    
def comp10001bo_match_build(play_card, build_pile):
    """
    Returns True if 'play_card' can be legally placed on 'build_pile' and 
    False otherwise.
    """
    
    #Check if build pile empty
    if len(build_pile) == 0:
        build_empty = True
    else:
        build_empty = False
        
    #only '2' and 'K' can initiate empty build pile
    if build_empty:
        return value(play_card) == '2' or value(play_card) == 'K'
    
    #if build pile not empty
    else:
        
        #can play same colour ace on build pile regardless of value of top card
        #of build pile
        if value(play_card) == 'A':
            return same_colour(play_card, top_card(build_pile))
        
        #for non-ace cards
        else:
            #cant play non-adjacent card
            if not(adjacent(play_card, top_card(build_pile), 'B')):
                return False
            
            #cant play different colour card
            elif not(same_colour(play_card, top_card(build_pile))):
                return False
            
            #can play same colour adjacent value card
            return True

        
# build pile play types
INVALID_PLAY = 0
VALID_NONFINAL_PLAY = 1
VALID_FINAL_PLAY = 2


def comp10001bo_match_discard(play_card, discard_pile, player_no, to_player_no,
                              from_hand=True):
    """
    (str, list, int, int, bool) --> (int)
    
    Returns 0 if the play is invalid, 1 if the play is a valid non-turn-ending
    play, 2 if the play is a valid turn-ending play.
    """
        
    #Aces cant be played on discard pile
    if value(play_card) == 'A':
        return INVALID_PLAY
    
    #check if or if not pile is empty
    pile_empty = (len(discard_pile) == 0)
    
    #check if playing to own discard pile or not
    own_pile = (player_no == to_player_no)
    
    #only starting own discard pile possible if discard_pile is empty
    if pile_empty:
        
        #Check if starting own discard pile
        if own_pile and from_hand:
            return VALID_FINAL_PLAY
    
    #illegal move and placing card on discard pile possible if discard_pile
    #is not empty
    else:
        
        #Check if illegal move (placing same colour card)
        if same_colour(play_card, top_card(discard_pile)):
            if from_hand:
                return VALID_FINAL_PLAY
           
        else:
            #Check if illegal move (placing non-adjacent value card)
            if not adjacent(play_card, top_card(discard_pile), 'D'):
                if from_hand:
                    return VALID_FINAL_PLAY
            
            #alternate colour and adjacent value mean placing card on
            #discard_pile possbile without terminating turn
            else:
                return VALID_NONFINAL_PLAY
    
    #if none of the above, no valid play is possible
    return INVALID_PLAY


# build pile play types
INVALID_PLAY = 0
VALID_NONFINAL_PLAY = 1
VALID_FINAL_PLAY = 2
NO_PLAY = 3

#constants to use with 'play_type'
PLAY_FROM_HAND = 0
PLAY_FROM_DISCARD_PILE = 1
PLAY_FROM_STOCKPILE = 2
NO_POSSIBLE_PLAY = 3

#constants to use with 'play'
PLAY_TYPE = 0
SOURCE = 1
DESTINATION = 2

#Constatns to use with play[DESTINATION]
PILE_TYPE = 0
BP = 0 
DP = 1
BP_NO = 1
DP_SPECS = 1
DP_OWNER_NO = 0
DP_NO = 1

#Constants to use with play[SOURCE]
CARD = 0
DP_SPECS = 1
DP_OWNER_NO = 0
DP_NO = 1

#constants to use with stockpiles
STOCKPILE_TOP_CARD = 0
STOCKPILE_CARD_NO = 1

def valid_play_to_discard_piles(card, discard_piles, player_no, 
                                from_hand=True):
    '''Returns if card is playable to any discard pile in the game'''
    for player in discard_piles:
        for end_pile in player:
            if comp10001bo_match_discard(card, end_pile, player_no,
                                         player, from_hand):
                return True
    return False
    
def valid_play_to_build_piles(card, build_piles):
    '''Returns if card is playable to any build pile in the game'''
    for build_pile in build_piles:
        if comp10001bo_match_build(card, build_pile):
            return True
    return False
    
def comp10001bo_is_valid_play(play, player_no, hand, stockpiles, discard_piles,
                              build_piles):
    """
    Returns:
    -0 if the play is invalid
    -1 if the play is a valid non-turn-ending play
    -2 if the play is a valid turn-ending play
    -3 if there is no possible play
    """    
    
    #When player claims no valid move is possible
    if play[PLAY_TYPE] == NO_POSSIBLE_PLAY:
        
        #Check if any valid move possible with cards in hand
        for card in hand:
            #Checking for play to other discard piles
            if valid_play_to_discard_piles(card, discard_piles, player_no):
                return INVALID_PLAY
            
            #Checking for play to build_piles    
            if valid_play_to_build_piles(card, build_piles):
                return INVALID_PLAY
            
        #List of all non-hand cards that can be played. i.e own stockpile top
        #card and top cards of all discard piles
        all_other_playable_cards = []
        
        #Add top card of own stockpile to 'all_playable_cards'
        stockpile_card = stockpiles[player_no][STOCKPILE_TOP_CARD]
        all_other_playable_cards.append(stockpile_card)
        
        #Add top cards of all non empty discard piles to 'all_playable_cards'
        for players_piles in discard_piles:
            for pile in players_piles:
                if len(pile) > 0:
                    all_other_playable_cards.append(top_card(pile))
        
        #Check if any valid move possible with non-hand cards
        for card in all_other_playable_cards:    
            #Checking for play to other discard piles
            if valid_play_to_discard_piles(card, discard_piles, player_no,
                                           from_hand=False):
                return INVALID_PLAY
            
            #Checking for play to build_piles    
            if valid_play_to_build_piles(card, build_piles):
                return INVALID_PLAY
        
        #If none of the above plays possible, no valid plays are possible
        return NO_PLAY
    
    #When play is from a card in hand
    elif play[PLAY_TYPE] == PLAY_FROM_HAND:
        
        #Card to be played
        card = play[SOURCE]
        
        #Check that card is actually present in the hand
        card_in_hand = False
        for c in hand:
            if c == card:
                card_in_hand = True
        
        if not card_in_hand:
            return INVALID_PLAY
        
        #If card claimed to be played to a build pile, check if valid
        if play[DESTINATION][PILE_TYPE] == BP:
            bp_no = play[DESTINATION][BP_NO]
            if not 0 <= bp_no <= 3:
                return INVALID_PLAY
            req_bp = build_piles[bp_no]
            if comp10001bo_match_build(card, req_bp):
                return VALID_NONFINAL_PLAY
            else:
                return INVALID_PLAY
        
        #If card claimed to be played to a discard pile, check if valid
        elif play[DESTINATION][PILE_TYPE] == DP:
            final_dp_owner_no = play[DESTINATION][DP_SPECS][DP_OWNER_NO]
            final_dp_no = play[DESTINATION][DP_SPECS][DP_NO]
            final_dp = discard_piles[final_dp_owner_no][final_dp_no]
            return comp10001bo_match_discard(card, final_dp, player_no, 
                                             final_dp_owner_no)
    
    #When play from card on top of a discard pile or own stockpile
    elif (play[PLAY_TYPE] == PLAY_FROM_DISCARD_PILE or 
          play[PLAY_TYPE] == PLAY_FROM_STOCKPILE):
        
        #When play from card on top of a discard pile
        if play[PLAY_TYPE] == PLAY_FROM_DISCARD_PILE:

            #Card to be played
            card = play[SOURCE][CARD] 

            #Check if card to be played exists where it says its coming from
            start_dp_owner_no = play[SOURCE][DP_SPECS][DP_OWNER_NO]
            start_dp_no = play[SOURCE][DP_SPECS][DP_NO]
            start_dp = discard_piles[start_dp_owner_no][start_dp_no]
            card_on_claimed_pile = top_card(start_dp)
            if card != card_on_claimed_pile:
                return INVALID_PLAY  
        
        #When play from a card on top of own stockpile
        elif play[PLAY_TYPE] == PLAY_FROM_STOCKPILE:

            #Card to be played
            card = play[SOURCE]

            #Check if the card to be played is actually the players stockpiles 
            #top card
            top_card_own_stockpile = stockpiles[player_no][STOCKPILE_TOP_CARD]
            if card != top_card_own_stockpile:
                return INVALID_PLAY

        #If card claimed to be played to a build pile, check if valid
        if play[DESTINATION][PILE_TYPE] == BP:
            bp_no = play[DESTINATION][BP_NO]
            if not 0 <= bp_no <= 3:
                return INVALID_PLAY
            req_bp = build_piles[bp_no]
            if comp10001bo_match_build(card, req_bp):
                return VALID_NONFINAL_PLAY
            else:
                return INVALID_PLAY

        #If card claimed to be played to a discard pile, check if valid
        elif play[DESTINATION][PILE_TYPE] == DP:
            final_dp_owner_no = play[DESTINATION][DP_SPECS][DP_OWNER_NO]
            final_dp_no = play[DESTINATION][DP_SPECS][DP_NO]
            final_dp = discard_piles[final_dp_owner_no][final_dp_no]
            return comp10001bo_match_discard(card, final_dp, player_no, 
                                             final_dp_owner_no, 
                                             from_hand=False)
