#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
if __name__ == "__main__":
    counter = 0
    total_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
    }
    try:
        while True:
            counter += 1
            log = input().split()
            file_size = int(log[-1])
            status_code = log[-2]
            try:
                status_codes[status_code] += 1
            except Exception:
                pass

            total_size += file_size

            if counter % 10 == 0:
                print(f"Files size: {total_size}")

                for key, value in status_codes.items():
                    if value != 0:
                        print(f"{key}: {value}")
                        status_codes[key] = 0

                total_size = 0
    except (KeyboardInterrupt, EOFError):
        print(f"Files size: {total_size}")

        for key, value in status_codes.items():
            if value != 0:
                print(f"{key}: {value}")
                status_codes[key] = 0

        total_size = 0
