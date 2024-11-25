from collections import defaultdict
from fractions import Fraction

coords = [(4361, 1383), (5907, 9301), (-8143, 5193), (-1621, 7128), (-7710, 7313), (751, 378), (-8348, -1294), (-8769, -5387), (8882, -4917), (2930, -7248), (6323, 3762), (-1184, 7928), (823, 1076), (-6869, -597), (-6540, -585), (4570, -9044), (6816, 6951), (3908, 2400), (-7282, -3635), (5602, 1461), (5226, 6263), (-2313, -9645), (2411, 7004), (-9508, -6848), (-4802, -7621), (-2618, -4451), (6542, 5531), (6142, 5814), (-7194, -8846), (-5535, -4990), (6161, -4951), (8185, 1370), (-3710, 652), (2389, -437), (4740, 7231), (9830, 3390), (-2152, 2897), (-8681, 9561), (-7997, -8049), (-6548, -6247), (-4029, -7366), (-6145, 9677), (3848, 1870), (3072, -8613), (-5921, 5699), (870, 6190), (4446, 493), (-7907, -3734), (-1926, -2629), (-6665, 8336), (-2529, -5263), (575, -8783), (3651, -4194), (-713, 3534), (9999, 2590), (8047, -5644), (4131, -3426), (-4837, -9247), (-2548, -2064), (2621, 6120), (-5364, 6408), (-1885, -6418), (6299, 7917), (5661, -9704), (3419, 5050), (-4391, 8926), (9718, -2406), (9929, -6320), (4131, -6971), (8065, -7327), (-495, -8948), (-7643, 427), (-6181, -4040), (3699, 8892), (-7296, -1295), (-8843, 8520), (-6334, -2605), (973, 1418), (-4295, 2044), (-3614, 2629), (-5785, -8489), (-7206, -6917), (8939, 2605), (4607, 5217), (-2804, 7154), (-2011, -9678), (-8747, -936), (-7064, 5507), (9061, 6371), (-9686, 9109), (-860, 2085), (-6871, -9375), (2918, 1717), (642, -678), (3604, 6442), (4539, -919), (8281, -3839), (4634, -1326), (-7185, 3032), (-668, -1775), (5871, -9474), (6904, 2341), (3016, -6523), (-3658, 6860), (9592, 8988), (-2711, -3413), (-5048, 4665), (4861, -3144), (-2800, 9396), (-4568, 538), (3840, 5872), (-6687, -9952), (9219, 2816), (-4061, 2071), (7801, 2967), (-6022, -2797), (84, -2568), (-822, 7476), (-4146, 2861), (9176, 3651), (-362, -1288), (-4708, 7680), (5328, -7696), (-5804, 9118), (-6814, -2165), (-8415, 6318), (-5140, 128), (4914, -6814), (-1422, 8681), (7087, 6368), (8647, -7699), (1817, 3200), (2777, 869), (-2862, -5765), (-6263, -487), (3210, 5725), (-6169, 9493), (-9815, -4562), (-3053, 5007), (6826, 6250), (3395, -1471), (635, 6468), (9819, 7786), (-1704, -7475), (3380, -7629), (-4289, 6044), (-88, 4429), (-7156, -225), (5, 3476), (8373, -9811), (4973, 9702), (7333, 4573), (-9454, 4421), (-512, -8285), (-1684, 4719), (9802, -433), (-360, -5252), (-4886, 947), (7322, 5413), (-2411, -3758), (-5165, -3720), (-8415, 4111), (-2236, -1818), (-6660, 567), (-8861, 8596), (4169, 626), (4522, -6851), (1523, -7576), (-3675, -9116), (308, 1694), (-6218, 7776), (8546, 4619), (9024, 1609), (-4705, -5673), (4910, 3083), (-2320, -1609), (7407, -7960), (9350, 4827), (8723, 4890), (-781, 6678), (2411, -5731), (-7548, 1826), (-7579, 3331), (7768, -6052), (1746, 5336), (2147, 6267), (-1383, -6907), (-8865, 9097), (-205, 1222), (7797, 7766), (-9891, -1542), (4094, 1249), (-6428, -9253), (7176, -9828), (5104, 8111), (-7242, -8204), (2601, -3718), (747, 9292), (-1754, 4935), (-8847, -8672), (40549, 35099), (204976, 178079), (62146, 53879), (160011, 138979), (-207276, -180401), (216959, 188499), (207667, 180419), (5589, 4699), (-228183, -198581), (-122866, -107001), (202331, 175779), (-174317, -151741), (-44551, -38901), (-186783, -162581), (186300, 161839), (165094, 143399), (76107, 66019), (-163622, -142441), (182896, 158879), (211830, 184039), (69046, 59879), (-58972, -51441), (-135976, -118401), (67045, 58139), (-33649, -29421), (156147, 135619), (-51727, -45141), (-199778, -173881), (-198904, -173121), (172109, 149499), (208426, 181079), (-78591, -68501), (216637, 188219), (-154100, -134161), (193131, 167779), (-75003, -65381), (-193936, -168801), (191843, 166659), (-204884, -178321), (-8763, -7781), (30268, 26159), (133400, 115839), (-111021, -96701), (14605, 12539), (31326, 27079), (-113229, -98621), (-187082, -162841), (224894, 195399), (-164887, -143541), (77878, 67559), (-16422, -14441), (76452, 66319), (94024, 81599), (121348, 105359), (-47771, -41701), (30061, 25979), (-136988, -119281), (120382, 104519), (-127443, -110981), (177100, 153839), (-134711, -117301), (141220, 122639), (206310, 179239), (-27692, -24241), (221536, 192479), (-143336, -124801), (-81374, -70921), (36961, 31979), (92299, 80099), (-136206, -118601), (159344, 138399), (-173949, -151421), (191728, 166559), (182229, 158299), (61571, 53379), (-42987, -37541), (-163461, -142301), (-121072, -105441), (-133561, -116301), (-57776, -50401), (45310, 39239), (47955, 41539), (-80799, -70421), (-60927, -53141), (-41331, -36101), (-213624, -185921), (-190877, -166141), (57063, 49459), (192901, 167579), (163300, 141839), (-21298, -18681), (-129973, -113181), (141128, 122559), (94507, 82019), (-171580, -149361), (88803, 77059), (-133216, -116001), (113896, 98879), (62652, 54319), (-127259, -110821), (32683, 28259), (152306, 132279), (-227102, -197641), (-37559, -32821), (189037, 164219), (29394, 25399), (-40871, -35701), (87262, 75719), (-8717, -7741), (102327, 88819), (70426, 61079), (-100947, -87941), (79925, 69339), (127420, 110639), (-135240, -117761), (7130, 6039), (148971, 129379), (-119508, -104081), (138276, 120079), (168889, 146699), (12305, 10539), (112861, 97979), (-8119, -7221), (-55568, -48481), (90183, 78259), (8901, 7579), (-216062, -188041), (-168797, -146941), (13294, 11399), (-183655, -159861), (-137287, -119541), (-41193, -35981), (-36662, -32041), (17480, 15039), (26657, 23019), (130042, 112919), (134734, 116999)]
n = len(coords)
max_count = 0
best_line = None

for i in range(n):
    lines = defaultdict(int)
    local_max = 0

    for j in range(n):
        if i == j:
            continue

        x1, y1 = coords[i]
        x2, y2 = coords[j]

        if x1 == x2:
            slope = 'inf'
            intercept = x1
        else:
            slope = Fraction(y2 - y1, x2 - x1)
            intercept = Fraction(y1) - slope * x1

        line = (slope, intercept)
        lines[line] += 1
        local_max = max(local_max, lines[line])

    if local_max > max_count:
        max_count = local_max
        best_line = line
if best_line:
    print(abs(best_line[0]*best_line[1]*(max_count + 1)))
else:
    print("error")
