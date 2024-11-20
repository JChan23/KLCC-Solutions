array = [['Gastly', 50], ['Haunter', 65], ['Gengar', 130], ['Misdreavus', 60], ['Mismagius', 105], ['Shuppet', 75], ['Banette', 115], ['Drifloon', 90], ['Drifblim', 150], ['Spiritomb', 108], ['Golett', 74], ['Golurk', 140], ['Phantump', 50], ['Trevenant', 110], ['Pumpkaboo', 49], ['Gourgeist', 90], ['Froslass', 110], ['Sableye', 100], ['Cofagrigus', 140], ['Runerigus', 145], ['Cursola', 130], ['Chandelure', 145], ['Mimikyu', 96], ['Yamask', 38], ['Galarian Yamask', 38], ['Polteageist', 90], ['Calyrex (Shadow Rider)', 160], ['Froslass', 110], ['Gengar (Mega)', 170], ['Banette (Mega)', 165], ['Toxtricity (Amped)', 98], ['Toxtricity (Low Key)', 98], ['Cacturne', 105], ['Shedinja', 20], ['Drifloon (Galarian)', 90], ['Spiritomb', 108], ['Duskull', 25], ['Dusclops', 40], ['Dusknoir', 150], ['Creepy Crawler', 75], ['Shuppet', 75], ['Spiritomb', 108], ['Litwick', 50], ['Lampent', 60], ['Chandelure', 145], ['Dusknoir', 150], ['Marshadow', 125], ['Sableye (Mega)', 120], ['Gengar (Mega)', 170], ['Banette (Mega)', 165], ['Zarude (Dada)', 120], ['Chandelure', 145], ['Gorebyss', 100], ['Lunala', 113]]

for i in range(len(array)):
    for j in range(0, len(array)-i-1):
        if array[j][1] > array[j+1][1]:
            temp = array[j+1]
            array[j+1] = array[j]
            array[j] = temp

print(array[((len(array)+1)//2)-1][0])
