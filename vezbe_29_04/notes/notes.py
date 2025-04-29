notes = {
    "C":"Do",
    "D":"Re",
    "E":"Mi",
    "F":"Fa",
    "G":"Sol",
    "A":"La",
    "H":"Si",
}

def note(note):
    return notes[note]

def letter(letter):
    return dict(map(reversed, notes.items()))[letter]


