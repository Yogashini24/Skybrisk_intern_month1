import csv


def remove_duplicates(rows, key):
    seen = set()
    out = []
    for r in rows:
        k = r.get(key)
        if k in seen:
            continue
        seen.add(k)
        out.append(r)
    return out


def read_csv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fieldnames):
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    rows = read_csv('..\\week3\\sample_data.csv')
    cleaned = remove_duplicates(rows, 'id')
    print(f'Read {len(rows)} rows, {len(cleaned)} after duplicates removed')
