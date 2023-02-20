#Martin Patrouchev 300286634

#Jayden Pyne 300304778


import random

class PokerGame:
    def __init__(self,card_list,number_players = 2):
        random.shuffle(card_list) 
        self.card_list = card_list
        self.number_players = number_players
        self.player_hands = []
        self.table_cards = []
        for i in range(number_players):
            self.player_hands.append([])
    #Adding cards to a players hands
    def add_card(self,player_index):
        top_card = self.card_list[0]
        self.card_list.pop(0)
        return self.player_hands[player_index].append(top_card)
    
    #Add a card to a table
    def add_to_table(self):
        top_card = self.card_list[0]
        self.card_list.pop(0)
        return self.table_cards.append(top_card)
    
    #Checking if its a four of a kind
    def IsFourofaKind(self,player_index):
        player_list = self.table_cards.copy()
        player_list.extend(self.player_hands[player_index])
        four_list = ''.join(player_list)
        four_kind = False
        for i in range(0,len(player_list)):
            x = four_list.count(player_list[i][0])
            if x == 4:
                four_kind = True
        if four_kind == False:
            return False
        return True
    
    #Checking if its a full house
    def IsFullHouse(self,player_index):
        player_list = self.table_cards.copy()
        player_list.extend(self.player_hands[player_index])
        full_list = ''.join(player_list)  
        card_counter = []
        four_kind = False
        for i in range(0,len(player_list)):
            card_counter.append(full_list.count(player_list[i][0]))
        if 3 in card_counter and 2 in card_counter:
            four_kind = True
        if four_kind == False:
            return False
        return True
    
    #Checking if its a flush
    def IsFlush(self,player_index):
        player_list = self.table_cards.copy()
        player_list.extend(self.player_hands[player_index])
        flush_list = ''.join(player_list)
        flush = False
        for i in range(0,len(player_list)):
            x = flush_list.count(player_list[i][1])
            if x == 5:
                flush = True

        if flush == False:
            return False
        return True
    
    #Checking if its a straight
    def IsStraight(self,player_index):
        player_list = self.table_cards.copy()
        player_list.extend(self.player_hands[player_index])
        player_list = ''.join(player_list)
        sort = []
        a=player_list.find('A')
        if a!=(-1):
            sort.append(player_list[a]) 
        a=player_list.find('2')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('3')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('4')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('5')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('6')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('7')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('8')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('9')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('T')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('J')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('Q')
        if a!=(-1):
            sort.append(player_list[a])
        a=player_list.find('K')
        if a!=(-1):
            sort.append(player_list[a])
        c=''.join(sort)
        x='A23456789TJQKA2JQKA234'
        for i in range (0,3):
            y=[]
            for j in range(i,len(c)-(i+1)):
                y.append(c[j])
                if len(y)==5:
                    z=''.join(y)
                    d=x.find(z)
                    if d!=(-1):
                        return True
        wrap=[]
        a=player_list.find('T')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('J')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('Q')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('K')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('A')
        if a!=(-1):
            wrap.append(player_list[a]) 
        a=player_list.find('2')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('3')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('4')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('5')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('6')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('7')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('8')
        if a!=(-1):
            wrap.append(player_list[a])
        a=player_list.find('9')
        if a!=(-1):
            wrap.append(player_list[a])
        c=''.join(wrap)
        x='A23456789TJQKA2JQKA234'
        for i in range (0,3):
            y=[]
            for j in range(i,len(c)-(i+1)):
                y.append(c[j])
                if len(y)==5:
                    z=''.join(y)
                    d=x.find(z)
                    if d!=(-1):
                        return True
        return False

    #Checking if its a 3 of a kind
    def IsThreeofaKind(self,player_index):
        player_list = self.table_cards.copy()
        player_list.extend(self.player_hands[player_index])
        three_list = ''.join(player_list)
        three = False
        for i in range(0,len(player_list)):
            x = three_list.count(player_list[i][0])
            if x == 3:
                three = True
        if three == False:
            return False
        return True
    
    #Checking if there are 2 pairs
    def IsTwoPairs(self,player_index):
        player_list = self.table_cards.copy()
        player_list.extend(self.player_hands[player_index])
        two_list = ''.join(player_list)
        pairs = []
        for i in range(0,len(player_list)):
            pairs.append(two_list.count(player_list[i][0]))
        x = pairs.count(2)
        if x != 4:
            return False
        return True
    
    #Checking if there is a pair
    def IsOnePair(self,player_index):
        player_list = self.table_cards.copy()
        player_list.extend(self.player_hands[player_index])
        two_list = ''.join(player_list)
        pairs = []
        for i in range(0,len(player_list)):
            pairs.append(two_list.count(player_list[i][0]))
        x = pairs.count(2)
        if x != 2:
            return False
        return True


class TexasHoldem(PokerGame):
    def __init__(self,card_list,number_players=2):
        super().__init__(card_list,number_players)
    #Dealing the cards
    def deal(self):
        for i in range(0,self.number_players):
            self.add_card(i)
            self.add_card(i)
        for i in range(5):
            self.add_to_table()
        for i in range(0,len(self.player_hands)):
            print(self.player_hands[i])
        print(self.table_cards)
    #Checking which player has the highest combination
    def checkWinner(self):
        hands = []
        #Checking each method
        for i in range(self.number_players):
            found = False
            if self.IsStraight(i) and self.IsFlush(i):
                hands.append("Straight flush")
                found = True
            if self.IsFourofaKind(i) and found == False:
                hands.append("Four of a kind")
                found = True
            if self.IsFullHouse(i) and found == False:
                hands.append("Full House")
                found = True
            if self.IsFlush(i) and found == False:
                hands.append("Flush")
                found = True
            if self.IsStraight(i) and found == False:
                hands.append("Straight")
                found = True
            if self.IsThreeofaKind(i) and found == False:
                hands.append("Three of a kind")
                found = True
            if self.IsTwoPairs(i) and found == False:
                hands.append("Two pairs")
                found = True
            if self.IsOnePair(i) and found == False:
                hands.append("One pair")
                found = True
            if found == False:
                hands.append("High card")
        return hands


#Print
print("Welcome to poker")
number_players = int(input("Enter the amount of Players: "))
#The list for the deck
card_list=['AD','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD',
'AC','2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC',
'AS','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS',
'AH','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AH']
#Calling the classes and use the methods
a = TexasHoldem(card_list,number_players)
a.deal()
print(a.checkWinner())

