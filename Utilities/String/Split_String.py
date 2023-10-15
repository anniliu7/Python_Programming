str1 = 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
str1.split(sep=' ')
# ['Cysteine', 'helps', 'prevent', 'side', 'effects', 'due', 'to', 'drug', 'reactions', 'and', 'toxic', 'chemicals']

str1.split(sep=' ', maxsplit=2) # left split
# ['Cysteine', 'helps', 'prevent side effects due to drug reactions and toxic chemicals']

str1.rsplit(sep=' ', maxsplit=2) # right split
# ['Cysteine helps prevent side effects due to drug reactions and', 'toxic', 'chemicals']
