import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plots(path='sample_data.csv'):
    df = pd.read_csv(path)
    df['temp'] = pd.to_numeric(df['temp'], errors='coerce')
    df['humidity'] = pd.to_numeric(df['humidity'], errors='coerce')
    df = df.dropna(subset=['temp'])

    plt.figure()
    df['temp'].hist(bins=8)
    plt.title('Temperature distribution')
    plt.savefig('week4_temp_hist.png')

    plt.figure()
    sns.scatterplot(data=df, x='temp', y='humidity', hue='city')
    plt.title('Temp vs Humidity')
    plt.savefig('week4_temp_vs_humidity.png')

    # Heatmap of correlations (simple)
    plt.figure()
    corr = df[['temp', 'humidity']].corr()
    sns.heatmap(corr, annot=True)
    plt.title('Correlation heatmap')
    plt.savefig('week4_heatmap.png')

    # Pairplot (may open a window; saved via seaborn's pairplot figure)
    pair = sns.pairplot(df.dropna(subset=['humidity']), vars=['temp', 'humidity'], hue='city')
    pair.savefig('week4_pairplot.png')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default=None, help='Path to CSV file (default: search common locations)')
    args = parser.parse_args()

    def resolve_file(path_arg):
        # If provided and exists, use it
        if path_arg:
            p = Path(path_arg)
            if p.exists():
                return p

        # Search common locations relative to cwd and repository layout
        candidates = [
            Path.cwd() / 'week3' / 'sample_data.csv',
            Path.cwd() / 'sample_data.csv',
            Path(__file__).resolve().parent.parent / 'week3' / 'sample_data.csv',
            Path(__file__).resolve().parent.parent / 'sample_data.csv',
        ]

        for c in candidates:
            if c.exists():
                return c

        return None

    file_path = resolve_file(args.file)
    if not file_path:
        tried = [str(p) for p in (
            Path(args.file) if args.file else None,
            Path.cwd() / 'week3' / 'sample_data.csv',
            Path.cwd() / 'sample_data.csv',
            Path(__file__).resolve().parent.parent / 'week3' / 'sample_data.csv',
        ) if p]
        raise FileNotFoundError(f"sample_data.csv not found. Tried: {tried}. Provide --file <path-to-csv>.")

    plots(str(file_path))
    print('Saved plots: week4_temp_hist.png, week4_temp_vs_humidity.png, week4_heatmap.png, week4_pairplot.png')


if __name__ == '__main__':
    main()
