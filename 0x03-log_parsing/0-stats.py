#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys

# Initialize variables
sum_file_size = 0
status_code = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
i = 0

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            status_line = parts[-2]
            file_size = parts[-1]
            if status_line in status_code:
                status_code[status_line] += 1
            sum_file_size += int(file_size)
            i += 1

            # Print metrics after every 10 lines
            if i == 10:
                print(f"File size: {sum_file_size}")
                sorted_keys = sorted(status_code.keys())
                for key in sorted_keys:
                    if status_code[key] > 0:
                        print(f"{key}: {status_code[key]}")
                i = 0

except KeyboardInterrupt:
    pass

finally:
    # Print final metrics
    print(f"File size: {sum_file_size}")
    sorted_keys = sorted(status_code.keys())
    for key in sorted_keys:
        if status_code[key] > 0:
            print(f"{key}: {status_code[key]}")
