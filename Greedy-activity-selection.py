
def greedy_activity_selection(activities, start_times, end_times):

    result = []
    blocked_times = 0
    n = len(activities)
    for i in range(n):
        if (start_times[i] >= blocked_times):
            result.append(activities[i])
            blocked_times = end_times[i]

    return result

test_activities = ["Play Golf", "Paint", "Cook", "Sleep", "Jog", "Code", "Eat"]
test_start_times = [1, 3, 1, 3, 4, 6, 8] 
test_end_times = [3, 4, 4, 6, 6, 9, 9]

print(f"Best activities to maximize the number of activities in a day: {greedy_activity_selection(test_activities, test_start_times, test_end_times)}")