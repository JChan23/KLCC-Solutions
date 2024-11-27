n = 10000
guesses = [(7091, False), (8448, False), (3643, False), (8549, False), (8985, False), (792, True), (8844, False), (9428, False), (7614, False), (9394, False), (1175, True), (3340, False), (4804, False), (4378, False), (2705, False), (4227, False), (9268, False), (973, True), (7162, False), (187, True), (4921, False), (3474, False), (2667, False), (673, True), (9849, False), (9682, False), (8045, False), (3475, False), (3067, False), (593, True), (9048, False), (776, True), (6259, False), (9922, False), (2219, False), (8157, False), (747, True), (8467, False), (7632, False), (7039, False), (3719, False), (5299, False), (8761, False), (582, True), (933, True), (3753, False), (2384, False), (4194, False), (7264, False), (9733, False), (8960, False), (5073, False), (699, True), (7077, False), (3191, False), (3500, False), (4062, False), (5671, False), (6018, False), (9662, False), (6882, False), (9332, False), (8632, False), (3119, False), (1583, False), (69, True), (7127, False), (9436, False), (2802, False), (2344, False), (7462, False), (3229, False), (5115, False), (4518, False), (5174, False), (2814, False), (3343, False), (3, True), (923, True), (686, True), (5125, False), (5449, False), (9660, False), (4112, False), (9457, False), (6716, False), (2011, False), (3136, False), (3953, False), (8885, False), (9495, False), (7296, False), (2207, False), (1522, False), (2611, False), (8414, False), (5312, False), (75, True), (6036, False), (1430, False), (9064, False), (3011, False), (2772, False), (6521, False), (4987, False), (8294, False), (2149, False), (4484, False), (9559, False), (4719, False), (2200, False), (4828, False), (1913, False), (5879, False), (6755, False), (7837, False), (7329, False), (4883, False), (938, True), (7231, False), (1276, True), (8274, False), (8273, False), (6025, False), (2636, False), (4575, False), (8444, False), (7928, False), (2996, False), (5055, False), (3252, False), (1775, False), (2223, False), (9087, False), (7689, False), (2524, False), (5684, False), (3469, False), (1082, True), (2721, False), (4862, False), (596, True), (336, True), (2356, False), (3905, False), (3437, False), (8874, False), (2984, False), (1482, False), (5219, False), (1973, False), (6344, False), (9591, False), (5307, False), (6891, False), (4125, False), (9790, False), (3700, False), (8603, False), (3226, False), (3335, False), (7924, False), (1985, False), (8509, False), (9209, False), (4047, False), (3582, False), (8989, False), (5860, False), (9006, False), (689, True), (5422, False), (3811, False), (7599, False), (5481, False), (3501, False), (7949, False), (6563, False), (190, True), (5861, False), (5724, False), (4913, False), (940, True), (5716, False), (1318, False), (7183, False), (6467, False), (9105, False), (1507, False), (8991, False), (3972, False), (4656, False), (9501, False), (1009, True), (8446, False), (3077, False), (3086, False), (4118, False), (779, True), (8929, False), (9197, False), (4106, False), (4745, False), (2013, False), (8027, False), (6339, False), (5941, False), (5733, False), (5637, False), (4614, False), (6134, False), (8651, False), (5229, False), (2500, False), (470, True), (3284, False), (1427, False), (5057, False), (5621, False), (2886, False), (9335, False), (8749, False), (4681, False), (1434, False), (793, True), (7729, False), (3082, False), (5577, False), (9708, False), (9466, False), (5281, False), (2017, False), (5976, False), (9429, False), (6942, False), (9400, False), (5994, False), (5284, False), (521, True), (8285, False), (5012, False), (8793, False), (5360, False), (3789, False), (8151, False), (1336, False), (8570, False), (133, True), (1118, True), (3184, False), (6441, False), (1312, False), (3080, False), (5015, False), (5688, False), (3483, False), (3201, False), (2954, False), (3031, False), (4650, False), (8309, False), (2527, False), (911, True), (1554, False), (1578, False), (6677, False), (5177, False), (489, True), (8765, False), (5158, False), (2044, False), (7026, False), (7520, False), (9034, False), (1910, False), (9983, False), (4110, False), (1508, False), (62, True), (9252, False), (8768, False), (9368, False), (8789, False), (8407, False), (9962, False), (3263, False), (9802, False), (1855, False), (5144, False), (1620, False), (5509, False), (6233, False), (235, True), (3935, False), (3385, False), (838, True), (2812, False), (145, True), (3094, False), (3933, False), (2074, False), (329, True), (268, True), (2959, False), (3202, False), (6904, False), (3421, False), (8959, False), (2093, False), (7948, False), (824, True), (6289, False), (284, True), (2569, False), (5602, False), (5975, False), (8465, False), (195, True), (1052, True), (3609, False), (1972, False), (695, True), (9477, False), (395, True), (3893, False), (1727, False), (9419, False), (8660, False), (8899, False), (4295, False), (7175, False), (3425, False), (5912, False), (4408, False), (1021, True), (4261, False), (6499, False), (1127, True), (8576, False), (3371, False), (7327, False), (7052, False), (2973, False), (4055, False), (1954, False), (44, True), (4500, False), (5755, False), (431, True), (3797, False), (9241, False), (8708, False), (3802, False), (4595, False), (1575, False), (5461, False), (1837, False), (4875, False), (2211, False), (7912, False), (4916, False), (4675, False), (2975, False), (5785, False), (7357, False), (2793, False), (1392, False), (4220, False), (6811, False), (7386, False), (7892, False), (7578, False), (3717, False), (6965, False), (3268, False), (6163, False), (6468, False), (4250, False), (2478, False), (2532, False), (5563, False), (2521, False), (4123, False), (6328, False), (2660, False), (7232, False), (1376, False), (4078, False), (9948, False), (7173, False), (4389, False), (2056, False), (7007, False), (4253, False), (7787, False), (5889, False), (4583, False), (4626, False), (8375, False), (202, True), (1817, False), (3391, False), (3875, False), (3633, False), (2303, False), (6395, False), (6786, False), (7345, False), (935, True), (1732, False), (2832, False), (8349, False), (7640, False), (8007, False), (6266, False), (8883, False), (201, True), (6330, False), (6512, False), (2640, False), (264, True), (4058, False), (3886, False), (6915, False), (3223, False), (6241, False), (4565, False), (633, True), (1051, True), (6869, False), (3092, False), (2431, False), (5240, False), (4606, False), (8639, False), (2205, False), (3203, False), (7001, False), (7550, False), (5314, False), (4053, False), (7023, False), (8512, False), (3795, False), (9853, False), (2946, False), (8193, False), (6418, False), (8851, False), (9658, False), (2507, False), (6559, False), (2430, False), (8331, False), (8040, False), (4329, False), (5609, False), (5241, False), (4282, False), (4403, False), (2002, False), (7126, False), (9653, False), (9146, False), (5123, False), (4820, False), (2690, False), (2625, False), (623, True), (6528, False), (6967, False), (3313, False), (6312, False), (4114, False), (5687, False), (1278, True), (9669, False), (7680, False), (1761, False), (8075, False), (5323, False), (3988, False), (4997, False), (4894, False), (6812, False), (9990, False), (789, True), (3892, False), (7546, False), (6674, False), (3464, False), (7309, False), (1362, False), (6920, False), (448, True), (1133, True), (8830, False), (4653, False), (8363, False), (9068, False), (1131, True), (2019, False), (2026, False), (6899, False), (817, True), (4968, False), (1126, True), (501, True), (3666, False), (740, True), (3707, False), (6928, False), (9328, False), (2723, False), (8118, False), (472, True), (6353, False), (6445, False), (7035, False), (4781, False), (9579, False), (8116, False), (2823, False), (7669, False), (9, True), (4279, False), (8823, False), (887, True), (3329, False), (6432, False), (5330, False), (2140, False), (111, True), (6844, False), (4600, False), (7558, False), (1516, False), (9690, False), (9097, False), (7885, False), (1861, False), (8856, False), (5674, False), (8271, False), (6859, False), (1959, False), (1693, False), (5585, False), (8341, False), (918, True), (8198, False), (7665, False), (4100, False), (5386, False), (2252, False), (7000, False), (1543, False), (5293, False), (9339, False), (8990, False), (4371, False), (783, True), (8559, False), (3433, False), (6421, False), (9524, False), (3386, False), (7285, False), (5214, False), (3990, False), (8277, False), (5990, False), (537, True), (1853, False), (739, True), (8252, False), (6413, False), (6213, False), (6605, False), (9843, False), (87, True), (1128, True), (6870, False), (867, True), (9158, False), (6617, False), (5351, False), (3458, False), (4067, False), (8644, False), (1025, True), (1955, False), (9327, False), (5339, False), (9303, False), (485, True), (8455, False), (2001, False), (5642, False), (5479, False), (8744, False), (6251, False), (3741, False), (9183, False), (8694, False), (492, True), (7504, False), (8592, False), (1124, True), (2846, False), (3367, False), (6130, False), (2580, False), (5788, False), (5699, False), (3214, False), (7726, False), (4785, False), (5175, False), (2197, False), (2326, False), (4434, False), (1204, True), (8783, False), (3846, False), (6391, False), (9783, False), (4116, False), (1394, False), (3697, False), (571, True), (9747, False), (155, True), (7577, False), (7376, False), (9382, False), (8267, False), (1346, False), (6578, False), (8086, False), (3816, False), (6147, False), (1359, False), (7591, False), (2043, False), (6601, False), (3033, False), (1936, False), (7785, False), (4854, False), (5654, False), (7936, False), (4101, False), (8981, False), (3320, False), (7779, False), (771, True), (9237, False), (9967, False), (3276, False), (3845, False), (8270, False), (7818, False), (213, True), (1860, False), (4693, False), (6621, False), (1813, False), (2825, False), (6003, False), (8610, False), (3354, False), (2655, False), (2171, False), (6170, False), (6733, False), (1597, False), (5291, False), (5338, False), (3674, False), (9889, False), (6584, False), (997, True), (7273, False), (1105, True), (8396, False), (6954, False), (4022, False), (1974, False), (4487, False), (4966, False), (2950, False), (6362, False), (4115, False), (9170, False), (48, True), (652, True), (4492, False), (6235, False), (3300, False), (8672, False), (2433, False), (9954, False), (7702, False), (4874, False), (3858, False), (4000, False), (10000, False), (7171, False), (4205, False), (5333, False), (330, True), (261, True), (2347, False), (9014, False), (8939, False), (9083, False), (5403, False), (1012, True), (3051, False), (5581, False), (3969, False), (9174, False), (5639, False), (6384, False), (2730, False), (3745, False), (2394, False), (2816, False), (1286, True), (884, True), (5543, False), (8097, False), (414, True), (3443, False), (4043, False), (9737, False), (1282, True), (2009, False), (33, True), (9215, False), (240, True), (3176, False), (8767, False), (6719, False), (1615, False), (4257, False), (8187, False), (9510, False), (8167, False), (4208, False), (4374, False), (1998, False), (7042, False), (7808, False), (8105, False), (12, True), (9260, False), (7383, False), (6307, False), (8757, False), (6676, False), (8827, False), (4943, False), (143, True), (2704, False), (7852, False), (4008, False), (2083, False), (6863, False), (6748, False), (8485, False), (2213, False), (5105, False), (4701, False), (1781, False), (519, True), (9009, False), (8296, False), (7983, False), (4129, False), (307, True), (121, True), (1804, False), (467, True), (5290, False), (3999, False), (7602, False), (4601, False), (7351, False), (4310, False), (653, True), (1997, False), (6377, False), (3150, False), (4844, False), (2780, False), (1784, False), (7185, False), (2488, False), (8064, False), (4485, False), (9376, False), (300, True), (6291, False), (9026, False), (5978, False), (5464, False), (556, True), (3178, False), (608, True), (6780, False), (8356, False), (8078, False), (4978, False), (6102, False), (3424, False), (8188, False), (3637, False), (4911, False), (7995, False), (6035, False), (8449, False), (2516, False), (3684, False), (6765, False), (5583, False), (7674, False), (7704, False), (7638, False), (2719, False), (9701, False), (1527, False), (9913, False), (7404, False), (2826, False), (3579, False), (1056, True), (8627, False), (1240, True), (2374, False), (360, True), (7598, False), (6832, False), (2343, False), (2018, False), (2070, False), (7910, False), (4690, False), (507, True), (5698, False), (9061, False), (5380, False), (761, True), (4273, False), (2931, False), (6341, False), (8196, False), (8124, False), (9857, False), (2243, False), (5188, False), (6360, False), (2398, False), (2481, False), (8328, False), (1058, True), (3331, False), (9124, False), (6971, False), (3771, False), (913, True), (2697, False), (5655, False), (6286, False), (6081, False), (2503, False), (2796, False), (3457, False), (9307, False), (6125, False), (8361, False), (234, True), (9502, False), (7618, False), (567, True), (5381, False), (1839, False), (6227, False), (4609, False), (1402, False), (9508, False), (2877, False), (643, True), (3993, False), (8333, False), (9266, False), (2713, False), (9914, False), (1567, False), (2342, False), (1945, False), (7709, False), (486, True), (611, True), (9016, False), (9958, False), (2682, False), (5851, False), (6902, False), (2015, False), (3069, False), (9625, False), (9514, False), (5564, False), (7846, False), (5243, False), (7115, False), (2184, False), (5152, False), (6964, False), (1802, False), (6460, False), (4387, False), (1696, False), (388, True), (5518, False), (2901, False), (5433, False), (708, True), (6167, False), (5749, False), (9597, False), (891, True), (3364, False), (1893, False), (5391, False), (9287, False), (9159, False), (1670, False), (1736, False), (345, True), (804, True), (4423, False), (1308, False), (5643, False), (4638, False), (2080, False), (2878, False), (6162, False), (8343, False), (3180, False), (9322, False), (1410, False), (1931, False), (9111, False), (5022, False), (4418, False), (1344, False), (5475, False), (7424, False), (4323, False), (546, True), (1292, False), (624, True), (5916, False), (9041, False), (4381, False), (8067, False), (1698, False), (5367, False), (2905, False), (8937, False), (1821, False), (8582, False), (9323, False), (2828, False), (5079, False), (4586, False), (9556, False), (9545, False), (6760, False), (5762, False), (8447, False), (9091, False), (2746, False), (9565, False), (1030, True), (9098, False), (6622, False), (6849, False), (149, True), (3435, False), (4238, False), (6372, False), (1590, False), (8279, False), (315, True), (9641, False), (5168, False)]
numbers = []
final_numbers = []

for i in range(1, n+1):
    numbers.append(i)

for i in range(len(guesses)):
    if guesses[i][1] == True:
        for i in range(guesses[i][0]-1):
            numbers[i] = -1
    elif guesses[i][1] == False:
        for i in range(n-1, guesses[i][0]-2, -1):
            numbers[i] = -1

for i in range(len(numbers)):
    if numbers[i] != -1:
        final_numbers.append(numbers[i])

print(final_numbers)