# src/preprocessing.py
import re
import string
import emoji
import pandas as pd

class TunisianTextCleaner:
    def __init__(self):
        # A heuristic map to normalize Arabizi numbers to Latin letters
        # This helps the model treat "3aslema" and "aaslema" as the same word.
        self.arabizi_map = {
            '3': 'a',  # 3in -> a (e.g., 3aslema -> aaslema)
            '7': 'h',  # 7a -> h (e.g., 7lowa -> hlowa)
            '5': 'kh', # 5a -> kh (e.g., 5ouya -> khouya)
            '9': 'q',  # 9af -> q (e.g., 9al -> qal)
            '8': 'gh', # 8in -> gh
            '2': 'a',  # Hamza -> a
        }
        
    def normalize_arabizi(self, text):
        """Replaces Arabizi numbers with their Latin equivalents."""
        for num, char in self.arabizi_map.items():
            text = text.replace(num, char)
        return text

    def clean_text(self, text):
        """Main cleaning function pipeline."""
        if not isinstance(text, str):
            return ""
            
        # 1. Lowercase everything
        text = text.lower()
        
        # 2. Remove Emojis (We focus on words for now)
        text = emoji.replace_emoji(text, replace='')
        
        # 3. Apply Arabizi Normalization (The "Secret Sauce")
        text = self.normalize_arabizi(text)
        
        # 4. Remove Punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # 5. Remove repeated characters (e.g., "nuuuuuul" -> "nuul")
        # We limit repetitions to max 2 characters
        text = re.sub(r'(.)\1+', r'\1\1', text)
        
        # 6. Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

# Simple test block if you run this file directly
if __name__ == "__main__":
    cleaner = TunisianTextCleaner()
    examples = [
        "L'application et trop nuuuuuuul 😡",
        "T3adi rou7ha, reseau 5ayeb barcha !!!",
        "C'est toppppppp ❤️"
    ]
    
    print("--- TESTING CLEANER ---")
    for ex in examples:
        print(f"Original: {ex}")
        print(f"Cleaned : {cleaner.clean_text(ex)}")
        print("-" * 20)