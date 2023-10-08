times = list(map(float, input().split()))
finish_line = len(times) // 2
left_total_time = sum(times[:finish_line])
right_total_time = sum(times[finish_line + 1:])

if 0 in times:
    zero_index = times.index(0)
    if zero_index < finish_line:
        left_total_time -= (left_total_time / len(times))
    else:
        right_total_time -= (right_total_time / len(times))

winner = ""
total_time = 0

if left_total_time < right_total_time:
    winner = "left"
    total_time = left_total_time
else:
    winner = "right"
    total_time = right_total_time

print(f"The winner is {winner} with total time: {total_time:.1f}")