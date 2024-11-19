equation = [5.5, 60.5] #store m and c of the equation in an array
coordinates =  [[46, 313.5], [10, 115.5], [2, 71.5], [-18, -38.5], [50, 335.5], [23, 187], [7, 99], [-31, -110], [-7, 22], [46, 313.5], [-49, -209], [-34, -126.5], [-8, 16.5], [49, 330], [-14, -16.5], [32, 236.5], [36, 258.5], [1, 66], [-49, -209], [27, 209], [36, 258.5], [34, 247.5], [14, 137.5], [42, 21], [-21, 36.5], [-8, 7], [-45, 60], [-50, 97.5], [-23, -8], [-43, 88.5], [-32, 11], [0, 65], [-14, 11], [-26, 78.5], [3, 39], [-49, 99], [18, -19], [-13, 18.5]]
num_of_valid_coordinates = 0

for i in range(len(coordinates)):
    if coordinates[i][1] == equation[0]*coordinates[i][0] + equation[1]:
        num_of_valid_coordinates = num_of_valid_coordinates + 1

print(num_of_valid_coordinates)
