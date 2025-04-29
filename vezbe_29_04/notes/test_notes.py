import unittest
import notes 

class NotesTest(unittest.TestCase):
    def test_notes_label(self):
        self.assertEqual(notes.note("C"), "Do")
        self.assertEqual(notes.note("D"), "Re")
        self.assertEqual(notes.note("E"), "Mi")
        self.assertEqual(notes.note("F"), "Fa")
        self.assertEqual(notes.note("G"), "Sol")
        self.assertEqual(notes.note("A"), "La")
        self.assertEqual(notes.note("H"), "Si")
    
    # nova test funkcija testira metod letter
    def test_notes_letter(self):
        self.assertEqual(notes.letter("Do"), "C")
        self.assertEqual(notes.letter("Re"), "D")

unittest.main()