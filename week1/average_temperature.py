import argparse
import csv


def average_from_list(values):
    return sum(values) / len(values) if values else None


def average_from_csv(path, column='temp'):
    temps = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            v = r.get(column)
            if v is None or v == '':
                continue
            try:
                temps.append(float(v))
            except ValueError:
                pass
    return average_from_list(temps)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='CSV file with a numeric "temp" column')
    args = parser.parse_args()

    if args.file:
        avg = average_from_csv(args.file, 'temp')
        if avg is None:
            print('No valid temperatures found')
        else:
            print(f'Average temperature: {avg:.2f}')
    else:
        values = [23.5, 22.0, 21.8, 24.1]
        print(f'Sample temps: {values}')
        print(f'Average: {average_from_list(values):.2f}')


if __name__ == '__main__':
    main()
