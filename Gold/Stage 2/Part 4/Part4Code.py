SECONDS_IN_A_DAY = 24 * 60 * 60
DAY_TO_SECONDS = {
    "Monday": 0,
    "Tuesday": 1 * SECONDS_IN_A_DAY,
    "Wednesday": 2 * SECONDS_IN_A_DAY,
    "Thursday": 3 * SECONDS_IN_A_DAY,
    "Friday": 4 * SECONDS_IN_A_DAY,
    "Saturday": 5 * SECONDS_IN_A_DAY,
    "Sunday": 6 * SECONDS_IN_A_DAY
}

def time_to_seconds(day, time, period): #Converts day and time in AM/PM format to seconds since Monday.
    hours, minutes, seconds = map(int, time.split(":"))
    if period == "PM" and hours != 12:
        hours += 12
    if period == "AM" and hours == 12:
        hours = 0
    return DAY_TO_SECONDS[day] + hours * 3600 + minutes * 60 + seconds

# Read the file and convert each row into [start, end, profit]:
tasks = []
with open("tasks.txt", 'r') as file:
    for line in file:
        parts = line.split()
        start_day = parts[0]
        start_time = parts[1]
        start_period = parts[2]
        end_day = parts[3]
        end_time = parts[4]
        end_period = parts[5]
        profit = int(parts[6])
        start_seconds = time_to_seconds(start_day, start_time, start_period)
        end_seconds = time_to_seconds(end_day, end_time, end_period)
        tasks.append([start_seconds, end_seconds, profit])

tasks.sort(key=lambda x: x[1]) #sort by increasing end_seconds to find non overlapping jobs
n = len(tasks)
dp = [0] * (n + 1)

def find_previous(index):
    low = 0
    high = index - 1
    while low <= high:
        mid = (low + high) // 2
        if tasks[mid][1] <= tasks[index][0]:
            if tasks[mid + 1][1] <= tasks[index][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

for i in range(1, n + 1):
    prev = find_previous(i - 1)
    dp[i] = max(dp[i - 1], tasks[i - 1][2] + (dp[prev + 1] if prev != -1 else 0))

print(dp[n])
