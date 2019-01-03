from pathlib import Path

for f in Path('.').glob('*.txt'):
    print(f.name)
    content = f.read_text()
    idx = content[:content.find(':')].rfind('\n') -1
    no_notes, notes = content[:idx], content[idx:]
    no_notes = no_notes.replace(' ', ' \n')
    content = no_notes + notes
    f.write_text(content)
