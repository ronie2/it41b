import psutil
import shutil
import os
import time
import operator
import argparse
import sys

# Shows biggest values at the top
reverse_keys = {'cpu_percent', 'memory_info_ex'}

# Shows smallest values at the top
normal_keys = {'name', 'pid', 'username'}

# All allowed keys
allowed_keys = reverse_keys | normal_keys

parser = argparse.ArgumentParser()
parser.add_argument("-s",
                    "--sort",
                    help="sorting key 'cpu_percent' (default), 'name', 'pid', 'username', 'memory_info_ex'",
                    action="store")

parser.add_argument("-i",
                    "--interval",
                    help="refresh interval of data (default: 5 sec)",
                    type=int,
                    action="store")

args = parser.parse_args()

# Time interval
if args.interval:
    delay = args.interval
else:
    delay = 5

# Sorting key
if args.sort and (args.sort in allowed_keys):
    sort_key = args.sort
    if sort_key in reverse_keys:
        reversed_order = True
    elif sort_key in normal_keys:
        reversed_order = False

elif args.sort and (args.sort not in allowed_keys):
    print("ERROR!!!\nOnly this keys are allowed: {keys}".format(keys=allowed_keys))
    sys.exit()
elif not args.sort:
    sort_key = "cpu_percent"
    reversed_order = True

initial = sorted([pid.as_dict() for pid in psutil.process_iter()],
                 key=operator.itemgetter(sort_key), reverse=reversed_order)


def print_screen(delay=1, sort_key="cpu_percent"):
    # Get total available memory
    total_memory = psutil.virtual_memory().total

    # Get terminal width and height
    columns, lines = shutil.get_terminal_size()

    z = sorted([pid.as_dict() for pid in psutil.process_iter()],
               key=operator.itemgetter(sort_key), reverse=reversed_order)

    if os.name == "posix":
        _ = os.system("clear")
    elif os.name == "nt":
        _ = os.system("cls")

    print("Total memory: {total} bytes\tFree memory: {free} bytes".format(total=psutil.virtual_memory()[0],
                                                                          free=psutil.virtual_memory()[1]))
    print("Total swap: {total} bytes\tFree swap: {free} bytes".format(total=psutil.swap_memory()[0],
                                                                      free=psutil.swap_memory()[1]))

    # Print table header:
    print("=" * columns)
    print("PID\t\tUSER\t\t%CPU\t\t%MEM\t\tSTATUS\t\tNAME")
    print("=" * columns)

    # Lines counter (first line is header)
    printed_lines = 6

    pattern = "{id}\t\t{user}\t\t{cpu:.2f}\t\t{memory:.2f}\t\t{status}\t\t{name}"

    for pid in z:
        printed_lines += 1
        p = pid
        print(pattern.format(id=pid["pid"],
                             name=pid["name"][:int(columns * 0.5)],
                             user=pid["username"],
                             cpu=pid["cpu_percent"],
                             status=pid["status"],
                             memory=pid["memory_info_ex"][0] / total_memory))
        if printed_lines == lines:
            break

    time.sleep(delay)

while True:
    print_screen(delay=delay, sort_key=sort_key)
