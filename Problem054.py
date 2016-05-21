hand = "KD KH KC 7S 8S"
hand = hand.replace("A","14")
hand = hand.replace("K","13")
hand = hand.replace("Q","12")
hand = hand.replace("J","11")
hand = hand.replace("T","10")
for i in hand:
	if any(i == x for x in ["S", "H", "C", "D"]):
		hand = hand.replace(i," "+i)
print(hand)
hand_list = []
for i in ([int(s) for s in hand.split() if s.isdigit()]):
	hand_list.append(i)
for i in ([s for s in hand.split() if s.isalpha()]):
	hand_list.append(i)
print(hand_list)
#Make a list entry for every part of the hand
"""
hand_list = []
for i in hand:
	if i != " ":
		hand_list.append(i)
"""
card_value = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0}
color = {"S":0,"H":0,"C":0,"D":0}

#Increase database with card values + colors
for i in hand_list:
	try:
		color[i] += 1
	except:
		continue
for i in hand_list:	
	try:
		card_value[int(i)] += 1
	except:
		continue

#card_value = {card:0 for card in range(2,15)}
Flush = False
Straight = False
StraightFlush = False
FourOfAKind = False
ThreeOfAKind = False
FullHouse = False
Pair = False
TwoPairs = False

#Check for Flush
if any([color[x] == 5 for x in color]):
	Flush = True

#Check for Straight
for i in range(2,11):
	if all([card_value[i+x] == 1 for x in [0,1,2,3,4]]):
		Straight = True
if all([card_value[x] == 1 for x in [14,2,3,4,5]]):
	Straight = True

#Check for StraightFlush
if Flush and Straight:
	StraightFlush = True

#Check 4 of a Kind
if any([card_value[x] == 4 for x in card_value]):
	FourOfAKind = True

#Check 3 of a Kind
if any([card_value[x] == 3 for x in card_value]):
	ThreeOfAKind = True

#Check Full House
if any([card_value[x] == 3 for x in card_value]) and any([card_value[x] == 2 for x in card_value]):
	FullHouse = True

#Check Pair
if any([card_value[x] == 2 for x in card_value]):
	Pair = True

#Check TwoPair
TwoPairCheck = []
if any([card_value[x] == 2 for x in card_value]):
	for i in card_value:
		if card_value[i] == 2:
			TwoPairCheck.append(i)
	if len(TwoPairCheck) == 2:
		TwoPairs = True



print(card_value,color)
#FullResultOverview = FullResultOverview.fromkeys(FullResultOverview, False)

#Pick out result
if StraightFlush == True:
	result = "Straight Flush"
	result_num = 8
elif FourOfAKind == True:
	result = "Four of a Kind"
	result_num = 7
elif FullHouse == True:
	result = "Full House"
	result_num = 6
elif Flush == True:
	result = "Flush"
	result_num = 5
elif Straight == True:
	result = "Straight"
	result_num = 4
elif ThreeOfAKind == True:
	result = "Three of a Kind"
	result_num = 3
elif TwoPairs == True:
	result = "Two Pairs"
	result_num = 2
elif Pair == True:
	result = "Pair"
	result_num = 1
else:
	result = "High Card"
	result_num = 0

print(result)

judge = []

if result == "High Card" or result == "Straight" or result == "Flush" or result == "Straight Flush":
	for i in range(2,15):
		if card_value[i] == 1:
			print(i)
			judge.append(i)
			judge.sort(reverse=True)

if result == "Pair":
	for i in range(2,15):
		if card_value[i] == 1:
			judge.append(i)
			judge.sort(reverse=True)
	for i in range(2,15):
		if card_value[i] == 2:
			judge.insert(0,i)

if result == "Two Pairs":
	for i in TwoPairCheck:
		judge.append(i)
		judge.sort(reverse=True)
	for i in range(2,15):
		if card_value[i] == 1:
			judge.append(i)

if result == "Three of a Kind":
	for i in range(2,15):
		if card_value[i] == 1:
			judge.append(i)
			judge.sort(reverse=True)
	for i in range(2,15):
		if card_value[i] == 3:
			judge.insert(0,i)

if result == "Full House":
	for i in range(2,15):
		if card_value[i] == 3:
			judge.append(i)
	for i in range(2,15):
		if card_value[i] == 2:
			judge.append(i)

if result == "Four of a Kind":
	for i in range(2,15):
		if card_value[i] == 1:
			judge.append(i)
			judge.sort(reverse=True)
	for i in range(2,15):
		if card_value[i] == 4:
			judge.insert(0,i)


print(result,judge)



"""
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
"""



"""
#Create list with all possible results
FullResultOverview = {"High Card":False,
"One Pair":False,
"Two Pair":False,
"Three of a Kind":False,
"Straight":False,
"Flush":False,
"Full House":False,
"Four of a Kind":False,
"Straight Flush":False,
"Royal Flush":False}
"""
