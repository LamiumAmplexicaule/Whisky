import csv
import glob
from collections import defaultdict

VALUES_LENGTH = 6
JAN_CODE_POSITION = 1


def main():
    csv_paths = glob.glob('../csv/*.csv', recursive=True)
    jan_codes = defaultdict(int)
    for csv_path in csv_paths:
        with open(csv_path) as f:
            reader = csv.reader(f)
            for row in reader:
                jan_codes[row[JAN_CODE_POSITION]] += 1
                if jan_codes[row[JAN_CODE_POSITION]] > 1:
                    print(f"{row} has a duplicate JAN code.")
                if len(row) != VALUES_LENGTH:
                    print(f"{row} is not the specified length {VALUES_LENGTH}.")


if __name__ == '__main__':
    main()
