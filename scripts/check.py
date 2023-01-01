import csv
import glob

VALUES_LENGTH = 6


def main():
    csv_paths = glob.glob('../csv/*.csv', recursive=True)
    for csv_path in csv_paths:
        with open(csv_path) as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) != VALUES_LENGTH:
                    print(f"{row} is not the specified length {VALUES_LENGTH}.")


if __name__ == '__main__':
    main()
