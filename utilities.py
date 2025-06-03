import re
from typing import Counter
import streamlit as st

# def remove_harakat(text):
#     # Remove harakat (diacritics)
#     harakat_pattern = re.compile(r'[\u0610-\u061A\u064B-\u065F\u06D6-\u06ED]')
#     text = harakat_pattern.sub('', text)

    

#     # handle hamza for Arabic letters with re
#     # Normalize all Alif variants to bare Alif (ا)
#     text = re.sub(r'[آأإٱائء]', 'ا', text)

#     # Optionally normalize yaa variants: ى → ي
#     text = re.sub(r'[ى]', 'ي', text)

#     # Remove hamza (ء) if it appears alone
#     # text = re.sub(r'[ء]', '', text)

#     # remove dagger alif (أ)
#     text = re.sub(r'\u0670', '', text)

#     # # remove hamza variations
#     hamza_chars = re.compile(r'[ءآأؤٱإئى]')
#     text = hamza_chars.sub('', text)

#     # Keep only Arabic letters
#     arabic_letters_pattern = re.compile(r'[^\u0621-\u063A\u0641-\u064A\u066E-\u06D3\u06FA-\u06FF\u0020]')
#     text = arabic_letters_pattern.sub('', text)

#     return text

def remove_harakat(text):
    """
    Removes Arabic diacritics (harakāt) such as fatḥa, kasra, ḍamma, sukun, shadda, etc.
    """
    harakat_pattern = re.compile(r'[\u0610-\u061A\u064B-\u065F\u06D6-\u06ED]')
    return harakat_pattern.sub('', text)

def normalize_arabic_letters(text):
    """
    Normalizes Arabic letters:
    - Converts all forms of Alif to bare Alif (ا)
    - Converts Yaa with no dots (ى) to normal Yaa (ي)
    - Removes standalone hamza and its variants
    - Keeps only Arabic letters and spaces
    """
    # Normalize all Alif variants to bare Alif (ا)
    text = re.sub(r'[آأإٱائ]', 'ا', text)

    # Normalize yaa variant (ى to ي)
    text = re.sub(r'[ى]', 'ي', text)

    # Remove dagger Alif (ٰ)
    text = re.sub(r'\u0670', '', text)

    # Remove hamza and variants
    text = re.sub(r'[ء]', '', text)

    # Keep only Arabic letters and space
    arabic_letters_pattern = re.compile(r'[^\u0621-\u063A\u0641-\u064A\u066E-\u06D3\u06FA-\u06FF\u0020]')
    text = arabic_letters_pattern.sub('', text)

    return text

def count_arabic_letters(text):
    text = remove_harakat(text)
    # Only keep Arabic letters (ignore spaces, etc.)
    arabic_letters = get_arabic_letters(text)
    return len(arabic_letters)

def get_arabic_letters(text):
    text = remove_harakat(text)
    arabic_letters = re.findall(r'[\u0621-\u063A\u0641-\u064A\u0671\u06CC\u06D5]', text)
    return arabic_letters

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




def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return num > 1

def get_primes_up_to(n):
    """Returns a list of prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def find_nth_prime(n):
    """Returns the nth prime number."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

def calculate_total_prime_number_verses(quran):
    """Calculates the total number of verses that are prime numbers."""
    total_prime_verses = 0
    unique_verses = quran[['surah_name_ar', 'total_ayah_surah']].drop_duplicates()
    prime_verses = []
    prime_verse_numbers = []
    for _, row in unique_verses.iterrows():
        if is_prime(row['total_ayah_surah']):
            prime_verses.append(row['surah_name_ar'])
            prime_verse_numbers.append(row['total_ayah_surah'])
            total_prime_verses += 1

    return prime_verses, prime_verse_numbers, total_prime_verses

def find_nth_prime_list(n_list):
    prime_list = []
    for ele in n_list:
        prime_list.append(find_nth_prime(ele))
    
    return prime_list


def get_prime_nums_upto_nth(n):
    """ Find Sum of prime numbers upto nth prime number"""
    nth_prime = find_nth_prime(n)
    return get_primes_up_to(nth_prime)


def find_surah_no(quran, n):
    quran = quran[quran['surah_no'] == n]
    ar_name = quran['surah_name_ar'].iloc[0]
    roman_name = quran['surah_name_roman'].iloc[0]
    en_name = quran['surah_name_en'].iloc[0]

    return ar_name, roman_name, en_name

def get_ayah_by_surah_and_ayah_no(quran, surah_no, ayah_no):
    surah = quran[quran['surah_no'] == surah_no]
    ayah = surah[surah['ayah_no_surah'] == ayah_no]

    return ayah

def get_word_count(ayah):
    ayah = remove_harakat(ayah)
    ayah_list = ayah.split(' ')
    ayah_list = [word for word in ayah_list if word.strip() != '']
    return ayah_list


def find_words_count_in_range(quran, surah, start, end, startword=0, skip_first_words=0, skip_last_words=0):
    # start and stop words allow to count from specific word in first ayah to specific word in last ayah
    words_count_sum = 0
    for i in range(start, end + 1):
        ayah = get_ayah_by_surah_and_ayah_no(quran, surah, i)['ayah_ar'].iloc[0]
        st.info(f"{get_word_count(ayah), len(get_word_count(ayah))}")
        word_count = len(get_word_count(ayah))
        words_count_sum += word_count

    return words_count_sum - skip_first_words - skip_last_words

def find_letters_count_in_range(quran, surah, start, end):
    letter_count_sum = 0
    for i in range(start, end+1):
        ayah = get_ayah_by_surah_and_ayah_no(quran, surah, i)['ayah_ar'].iloc[0]
        letter_count = len(get_arabic_letters(ayah))
        letter_count_sum += letter_count
    return letter_count_sum


def sum_of_sur_and_verses():
    # finding sum using sum up to n formula
    n = 114
    surahs_sum = n*(n+1) / 2
    ayah_no_sum = 6236
    return  surahs_sum, ayah_no_sum