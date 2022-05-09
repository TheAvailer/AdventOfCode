from time import perf_counter_ns
from collections import Counter


def part1():
    start = perf_counter_ns()
    filename = "day 22.txt"
    on_off_lst = []
    reboot_steps = []

    for lines in open(filename):
        on_off, steps = lines[:3].strip(), [lines.replace("\n", "").replace("on ", "").replace("off ", "")]
        on_off_lst += [on_off]
        reboot_steps += steps

    valid_reboot_steps = []
    for i in range(len(reboot_steps)):
        temp_x, temp_y, temp_z = reboot_steps[i].split(",")
        x = temp_x[temp_x.find("=")+1:].split("..")
        y = temp_y[temp_y.find("=") + 1:].split("..")
        z = temp_z[temp_z.find("=") + 1:].split("..")
        if int(x[0]) < -50 or int(x[1]) > 50 or int(y[0]) < -50 or int(y[1]) > 50 or int(z[0]) < -50 or\
                int(z[1]) > 50:
            continue
        else:
            valid_reboot_steps += [[x, y, z]]

    memo = {}
    print(valid_reboot_steps)
    for i in range(len(valid_reboot_steps)):
        print(i)
        for a in range(int(valid_reboot_steps[i][0][0]), int(valid_reboot_steps[i][0][1])+1, 1):  # -14          # -14
            for b in range(int(valid_reboot_steps[i][1][0]), int(valid_reboot_steps[i][1][1])+1, 1):  # -22      # -22
                for c in range(int(valid_reboot_steps[i][2][0]), int(valid_reboot_steps[i][2][1])+1, 1):  # -25  # -24
                    if (a, b, c) in memo:
                        if memo[a, b, c] == "on" and on_off_lst[i] == "off":
                            memo[a, b, c] = "off"
                        elif memo[a, b, c] == "off" and on_off_lst[i] == "on":
                            memo[a, b, c] = "on"
                    else:
                        memo[a, b, c] = on_off_lst[i]

    print(Counter(memo.values()))
    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")


#part1()