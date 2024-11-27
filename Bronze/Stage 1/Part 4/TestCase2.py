equation = [-12, 7] #store m and c of the equation in an array
coordinates = [[38, -449], [-288, 762], [-274, 798], [-415, -1431], [-481, 660], [-25, 307], [302, 1491], [77, -917], [6, -65], [269, -258], [-412, 159], [30, -1437], [311, 225], [460, -6], [297, -1095], [-33, 403], [-435, 417], [-17, 211], [97, -1157], [25, -293], [286, 99], [-202, -147], [-31, 379], [-103, 618], [319, -555], [19, -221], [-11, -999], [32, -377], [-30, 367], [-297, -1089], [-454, -105], [-73, 883], [22, -257], [-140, -126]]
num_of_valid_coordinates = 0

for i in range(len(coordinates)):
    if coordinates[i][1] == equation[0]*coordinates[i][0] + equation[1]:
        num_of_valid_coordinates = num_of_valid_coordinates + 1

print(num_of_valid_coordinates)
