import argparse
import pandas as pd


def clean_and_aggregate(path):
    df = pd.read_csv(path)
    df = df.drop_duplicates(subset=['id'])
    df['temp'] = pd.to_numeric(df['temp'], errors='coerce')
    df['humidity'] = pd.to_numeric(df['humidity'], errors='coerce')
    df = df.dropna(subset=['temp'])
    agg = df.groupby('city').agg(
        avg_temp=('temp', 'mean'),
        avg_humidity=('humidity', 'mean'),
        count=('id', 'count')
    ).reset_index()
    return agg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    args = parser.parse_args()
    result = clean_and_aggregate(args.file)
    print(result)
    result.to_csv('week3_aggregated.csv', index=False)


if __name__ == '__main__':
    main()
