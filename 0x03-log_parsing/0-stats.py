#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys

total_lines = 0
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
                     500: 0}

try:
    for line in sys.stdin:
        parts = line.strip().split(' ')
        if len(parts) < 7:
            continue

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except ValueError:
            continue

        if status_code in status_code_count:
            status_code_count[status_code] += 1

        total_file_size += file_size
        total_lines += 1

        if total_lines == 10:
            print(f"File size: {total_file_size}")
            for code, value in sorted(status_code_count.items()):
                if value > 0:
                    print(f"{code}: {value}")
            total_lines = 0

except KeyboardInterrupt:
    pass

finally:
    print(f"File size: {total_file_size}")
    for code, value in sorted(status_code_count.items()):
        if value > 0:
            print(f"{code}: {value}")
