import re
from typing import Counter

def remove_harakat(text):
    # Remove harakat (diacritics)
    harakat_pattern = re.compile(r'[\u0610-\u061A\u064B-\u065F\u06D6-\u06ED]')
    text = harakat_pattern.sub('', text)

    

    # handle hamza for Arabic letters with re
    # Normalize all Alif variants to bare Alif (ا)
    text = re.sub(r'[آأإٱا]', 'ا', text)

    # Optionally normalize yaa variants: ى → ي
    text = re.sub(r'[ى]', 'ي', text)

    # Remove hamza (ء) if it appears alone
    text = re.sub(r'[ء]', '', text)

    # remove dagger alif (أ)
    text = re.sub(r'\u0670', '', text)

    # # remove hamza variations
    hamza_chars = re.compile(r'[ءآأؤٱإئى]')
    text = hamza_chars.sub('', text)

    # Keep only Arabic letters
    arabic_letters_pattern = re.compile(r'[^\u0621-\u063A\u0641-\u064A\u066E-\u06D3\u06FA-\u06FF\u0020]')
    text = arabic_letters_pattern.sub('', text)

    return text

## This function completely removes characters that appear more than once in a string
def remove_global_duplicates(strings):
    # Combine all strings into one to count total occurrences
    all_chars = re.findall(r'.', ''.join(strings))
    char_counts = Counter(all_chars)
    
    # Characters that appear only once in total
    unique_chars = {char for char, count in char_counts.items() if count == 1}
    
    # For each string, keep only the characters that are globally unique
    result = [''.join([char for char in s if char in unique_chars]) for s in strings]
    
    return result