import unittest
from hangman import choose_word, display_word

class TestHangman(unittest.TestCase):
    def test_choose_word(self):
        words = ["python", "hangman", "challenge", "developer", "keyboard"]
        self.assertIn(choose_word(), words)

    def test_display_word(self):
        word = "python"
        guessed_letters = {"p", "y"}
        self.assertEqual(display_word(word, guessed_letters), "p y _ _ _ _")

if __name__ == "__main__":
    unittest.main()