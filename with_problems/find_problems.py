from pathlib import Path


all_files = [p.stem.replace('_final', '') for p in Path('../').glob('*.txt')]
big_pb = []
small_pb = []
for line in Path('similarity.csv').read_text().splitlines()[1:]:
    parts = line.split(',')
    name, sim = parts[0], int(parts[1])
    if sim <= 70 and name in all_files:
        big_pb.append(name)
    elif 70 < sim < 82 and name in all_files:
        small_pb.append(name)
    elif sim == 82 and name in all_files:
        print(name)

for n in big_pb:
    n += '_final.txt'
    Path(n).replace(Path('big_differences/' + str(n)))

for n in small_pb:
    n += '_final.txt'
    Path(n).replace(Path('small_differences/' + str(n)))
