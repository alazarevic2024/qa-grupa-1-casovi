notes = {
    "C":"Do",
    "D":"Re",
    "E":"Mi",
    "F":"Fa",
    "G":"Sol",
    "A":"La",
    "H":"Si",
}

# Na osnovu oznake note vraca njen naziv
def note(note):
    return notes[note]
# Na osnovu naziva note vraca njenu oznaku
def letter(letter):
    return dict(map(reversed, notes.items()))[letter]

print(note("C"))
print(note("D"))
print(note("E"))
