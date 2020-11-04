whole_deck = "abcdefg"
my_card = "h"

print('Looking for card', my_card,'among', whole_deck)

top = len(whole_deck)
bottom = 0
while bottom < top:
    print('bottom =', bottom, 'top =', top,
          '- remaining cards', whole_deck[bottom:top])
    middle = (top+bottom)//2
    if whole_deck[middle] == my_card:
        break
    elif my_card < whole_deck[middle]:
        top = middle-1;
    else:
        # my_card > whole_deck[middle]
        bottom = middle+1       
print('Card', my_card, 'is at position', middle)


