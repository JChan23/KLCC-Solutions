equation = [2024, 100] #store m and c of the equation in an array
coordinates = [[-44, -88956], [1837, -16974], [1975, -26523], [632, 33102], [41, 5256], [-4829, -43893], [-293, 33399], [1516, -35802], [-325, 41463], [-61, -123364], [-539, 40878], [2885, 25524], [3559, 28116], [-3117, 25389], [1454, -12276], [76, -10080], [-163, 39483], [1853, -42570], [-3061, 14508], [366, -11097], [94, 190356], [4575, 26532], [-71, -143604], [-1337, 1530], [-36, -72764], [25, 50700], [-1971, -5895], [-3687, -16632], [79, 159996], [1008, -15714], [1713, -39168], [4747, 5148], [4975, -18153], [-4235, -20142], [-875, 21195], [2269, 38736], [-3016, -40599], [-617, -10872], [-51, -103124], [2308, 17145], [-3588, -38943], [2032, 25164], [2624, -19017], [70, 141780], [-274, 6894], [-1585, 24201], [389, 31653], [-26, -52524], [2998, 22545], [4053, -6768], [-14, -28236], [-76, -153724], [-50, -101100], [2547, -9828], [-98, -198252], [145, -22599], [-3227, 18819], [-2988, -28872], [2828, 28233], [-3967, 1809], [-76, -153724], [-4911, -2961], [-95, -192180], [-2723, -9549], [-10, -20140], [-107, -26811], [4037, -162], [3989, -29457], [-438, -27774], [-4291, 20943], [-2767, -8127], [4650, -26469], [-57, -115268], [4007, 40644], [-2311, 30375], [-2518, 36666], [2239, 7884], [-1228, 4653], [4304, -39051], [2361, -34614], [-49, -99076], [4282, 25542], [-3223, -16146], [-377, 33111], [-856, -31221], [-21, -42404], [80, 162020], [-1270, -6111], [-2532, -19224], [2301, -20997], [-910, -3222], [-58, -117292], [289, -18054], [2401, -15030], [56, 113444], [4054, 12384], [-485, 5382], [-21, -42404], [-1454, -6012], [2948, 17010], [-822, -17937], [3686, 28863], [4184, 36090], [4251, -41346]]
num_of_valid_coordinates = 0

for i in range(len(coordinates)):
    if coordinates[i][1] == equation[0]*coordinates[i][0] + equation[1]:
        num_of_valid_coordinates = num_of_valid_coordinates + 1

print(num_of_valid_coordinates) #unconfirmed output: 24
