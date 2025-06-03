import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from utilities import calculate_total_prime_number_verses, count_arabic_letters, find_letters_count_in_range, find_nth_prime_list, find_surah_no, find_words_count_in_range, get_arabic_letters, get_ayah_by_surah_and_ayah_no, get_prime_nums_upto_nth, get_primes_up_to, get_word_count, remove_harakat


st.header("Prime Numbers & Other Special Number Patterns in the Quran")

quran = pd.read_csv("The Quran Dataset.csv")

surah_names, prime_verse_numbers, total_prime_verses = calculate_total_prime_number_verses(quran)


prime_verses_df = pd.DataFrame({
    "Surah Name (Arabic)": surah_names,
    "Total Verses in Surah": prime_verse_numbers
})


option = option_menu(
    "Navigation",
    ["About Prime Numbers", "Divine Literary Prime Number", "Prime Number 19", "Surah Ar - Rahman"],
    icons=["123", "book", "star", "sun"],
    menu_icon="cast",
    orientation="horizontal",
    default_index=0
)

if option == "About Prime Numbers":
    st.markdown("""
> **Mathematics is the Queen of Sciences, and prime numbers are the Queen of Mathematics.**  
> — *Carl Friedrich Gauss*

---

- **Prime numbers** are the building blocks of all numbers, and they hold a special place in the Quran's numerical structure.

---

- Prime numbers are the basic entities of Mathematics. They serve as the fundamental building blocks of numbers, yet they exhibit fascinating and complex properties.  
- They appear **random** but reveal **interesting** patterns. Some of the simplest, as well as some of the most challenging, problems in Mathematics **revolve** around prime numbers.

---

#### Definition of Prime Numbers :
> A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
For example, 5 is a prime. The only ways of writing it as a product, is 1 X 5 or 5 x 1

> Due to the unique properties of Prime Numbers, some important algorithms are based on prime numbers , 
One of the public key encryption algorithm called RSA actually depends on the factorization of product large primes. 

---
                          
#### Prime Number (Facts) : 

The largest prime number known till now is 2^82589933 —1 and it has 24,862,048 digits.
- 0 and 1 are not considered prime numbers.
- 2 is the only even prime number.
                
---
- 25 primes in 100 ( 25%)
- 168 primes in 1000 ( 16.8%)
- 1229 primes in 10,000 (12.29%) etc. 
                
---
- The formula to spot or predict the next prime is not found yet.
- However there is a formula to predict approximately n numbers before a prime number.
                
#### Prime Number Theorem (PNT) - Carl Gauss

The prime number theorem provides a way
to approximate the number of primes less
than or equal to a given number n.Thisvalue ,
is called π(n), where π the “prime counting
function.” For example, π(10) = 4 since there
are four primes less than or equal to 10 (2, 3, 5,and 7). Similarly, π(100) = 25.

The theorem tells us that π(n) is
“asymptotically equal” to n/log(n), where log
is the natural logarithm.
                     
                """)


    st.markdown("## 🧬 Prime Numbers in Nature and Design")

    st.markdown("""
    ## 🔢 Prime Numbers and the Number 7 in Nature and the Universe

Prime numbers, especially **7**, appear repeatedly in natural structures, biological systems, and even spiritual symbolism. This isn’t just coincidence — it suggests **design, harmony, and mathematical depth** in the universe.

---

### 🌿 Nature and Prime Patterns

- 🐝 **Beehive Structure**  
  The **hexagonal** shape of honeycombs is geometrically efficient — and 6 (a near-prime) fits into **prime-based tiling** when extended to nature's larger structures.

- 🍍 **Pineapple Spirals**  
  Count the spirals on a pineapple — they often follow **Fibonacci numbers** (which are closely linked to **primes**) like **5, 8, 13**.

- 🌻 **Sunflower Seeds**  
  Sunflower heads also show spirals in **Fibonacci counts**, which alternate between **prime-rich ratios**.

- 🌹 **Petals on Roses**  
  Many flowers have a prime number of petals:
  - 3 petals (lilies)
  - 5 petals (wild rose)
  - 13 petals (corn marigold)

---

### 🌈 Symbolism and Universal Constants Involving 7

- 🌈 **7 Colors in the Visible Spectrum (VIBGYOR)**  
  - Violet, Indigo, Blue, Green, Yellow, Orange, Red — the **spectrum divides naturally into 7** categories due to human eye perception.

- ⚛️ **7 Electron Shells in Atoms**  
  - In the **Bohr model**, atoms have up to **7 electron shells** — a limit that defines how the periodic table is structured.

- 📅 **7 Days in a Week**  
  - Used across **nearly all civilizations**, this reflects a deep connection to the **lunar phases** and **Biblical/Islamic cycles** of time.

- 🌍 **7 Continents on Earth**  
  - Earth is naturally divided into 7 major landmasses, even though it's not a man-made structure:
    - Asia, Africa, North America, South America, Antarctica, Europe, Australia

---
    """)


elif option == "Divine Literary Prime Number":
    st.markdown("##### This section focuses on finding out number of verses 6236 through prime surah verse numbers, and prime numbers considering surah verse numbers as indices")
    st.markdown("## Step 1: Total Prime Verses in Quran")
    st.markdown(
        f"### {total_prime_verses} total verse numbers of Surahs in the Quran are prime numbers."
    )

    # Show the dataframe containing prime verses data
    prime_verses_df.index = prime_verses_df.index + 1
    st.dataframe(prime_verses_df, use_container_width=True)

    # Step 3: Explain finding nth prime for verses and adding it as new column
    st.markdown("## Step 2: Calculate nth prime number based on verse numbers")
    st.markdown(
        """
        Finding nth prime number making number of verses as index for those 32 Surahs,
        and adding it as a new column named 'Prime List'. For Example 7th Prime Number is 17, and 109th is 599.
        """
    )

    # Calculate the prime list and add as a new column
    prime_list = find_nth_prime_list(prime_verse_numbers)
    prime_verses_df['Prime List'] = prime_list

    st.markdown("## Step 3: Add sum row for total verses and prime list columns")

    # Create a sum row for the totals
    sum_row = [
        "Sum",
        sum(prime_verses_df['Total Verses in Surah']),
        sum(prime_verses_df['Prime List'])
    ]

    # Convert sum_row to a DataFrame row and append it to the main dataframe
    sum_df = pd.DataFrame([sum_row], columns=prime_verses_df.columns)
    prime_verses_df = pd.concat([prime_verses_df, sum_df], ignore_index=True)

    # Show the updated dataframe with the sum row
    prime_verses_df.index = prime_verses_df.index + 1
    st.dataframe(prime_verses_df, use_container_width=True)

    st.markdown("## Step 4: Final sums and significance")
    total_verses_sum = sum(prime_verses_df['Total Verses in Surah'][:-1])  # exclude sum row
    prime_list_sum = sum(prime_verses_df['Prime List'][:-1])  # exclude sum row
    total_ayat = total_verses_sum + prime_list_sum

    st.markdown(
        f"""
        ##### Sum of 'Total Verses in Surah' column is {total_verses_sum}, and sum of 'Prime List' column is {prime_list_sum}.  
        ###### Adding these up we get **{total_ayat}**, which is the total number of Ayat in the Quran.
        """
    )

    st.markdown("## DLPN Pattern Applications")

    st.markdown(
        """
        This DLPN Pattern protects the Quran from corruption. For example:

        Dr Rashad Khalifa and followers claimed Surah Taubah (chapter 9) has only 127 verses instead of 129. According to the DLPN pattern, this is incorrect because:

        - 129 is **not** a prime number, so it is **not** part of the pattern.
        - If 127 is considered (which is prime), the pattern would output 7072:6234, causing the pattern to collapse.
        - Also, the chapter number sum would be 33 with a total of 2248, deviating from the prime number 2239.

        This shows the pattern's integrity and highlights why 129 verses must be considered correct.
        """
    )

elif option == "Prime Number 19":
    st.markdown("""
    > **“Over it are nineteen [angels]. And We have made the number only a trial for the disbelievers…”**  
    > — Surah Al-Muddathir (74:30–31)
    """)

    st.image("images/numerical/number_19_1.png", use_container_width=True)
    st.image("images/numerical/number_19_2.png", use_container_width=True)

    st.subheader("🔢 Importance of Number 19")    

    titles = [
    "🔥 19 Angels Guard Hell (Surah 74:30)",
    "🧠 19 as a Test for Believers",
    "🚫 19 as a Trial for Disbelievers",
    "📜 19 Letters in Bismillah",
    "📖 Bismillah Appears 114 Times",
    "📘 114 Chapters in the Qur'an",
    "➕ Sum of Chapters = 6555 (19 × 345)",
    "🔢 Sum of Digits in Quran is Multiple of 19",
    "🕊️ 'Allah' Occurs 2698 Times (19 × 142)",
    "📍 Sum of Verse Numbers with 'Allah' is Multiple of 19",
    "🔠 Mysterious Letters Add to a Multiple of 19",
    "🔡 Most Used Letter: Alif (ا)"
]
    
    with st.expander("Miracle of when 19 is mentioned in the Quran"):
        st.markdown("## 📖 Ayahs Mentioning the Number 19 in Surah Al-Muddathir")

        st.markdown("""
There is something very amazing about this number and **where it is mentioned**, which I will tell you later.  
But first, let’s look at the **probability** of any random number being exactly divisible by 19.

---

### 📊 Probability Calculations

- ✅ The probability of a random number being divisible by 19 is approximately **1 in 19 ≈ 5.26%**

- ✅ The probability that **two random numbers** are both divisible by 19 is:

$$
\\frac{1}{19} \\times \\frac{1}{19} = \\frac{1}{361} \\approx 0.2\\%
$$

- ✅ The probability that **three in a row** are divisible by 19 is:

$$
\\frac{1}{19} \\times \\frac{1}{19} \\times \\frac{1}{19} = \\frac{1}{6859} \\approx 0.01\\%
$$

---
                    
Now let's come to the Ijaz of the Quran, in which multiples of 19 is present many times
""")

        # Get Ayah 30 (mentioning 19) and Ayah 31 (its implication)
        ayah_mentioning_19 = get_ayah_by_surah_and_ayah_no(quran, 74, 30)['ayah_ar'].iloc[0]
        ayah_implication_19 = get_ayah_by_surah_and_ayah_no(quran, 74, 31)['ayah_ar'].iloc[0]

        st.markdown("##### 🔹 Ayah 30 (74:30) - Mentions 19")
        st.markdown(f"**Arabic:** {ayah_mentioning_19}")

        st.markdown("##### 🔹 Ayah 31 (74:31) - Explains the Purpose of 19")
        st.markdown(f"**Arabic:** {ayah_implication_19}")

        implication_word_count = get_word_count(ayah_implication_19)
        # st.info(f"Word Count: {implication_word_count}")
        st.markdown("##### 🔹 Word Count of Ayah number 31 explaining implication of 19")
        st.info(f"✔️ 19 × 3 = {19 * 3} = {len(implication_word_count)} ✅")

        st.markdown("##### 🔹 Total Word Count from 74:1 to 74:19 (Up to Ayah 19) is equal to 57 which is a multiple of 19")
        total_words_upto_30 = find_words_count_in_range(quran, 74, 1, 19)
        st.info(f"Total Words: {total_words_upto_30}")
        st.info(f"✔️ 19 × 3 = {19 * 3} = {total_words_upto_30} ✅")

        # Count words from Ayah 1 to Ayah 30
        st.markdown("##### 🔹 Total Word Count from 74:1 to 74:30 where 'عَلَيۡهَا تِسۡعَةَ عَشَرَؕ' is mentioned ")
        words_count_sum = find_words_count_in_range(quran, 74, 1, 30)
        st.info(f"Total Words: {words_count_sum}")
        st.info(f"✔️ 19 × 5 = {19 * 5} = {words_count_sum} ✅")

        # Count letters from 74:1 to 74:29 plus the word "عليها"
        st.markdown("##### 🔹 Total Letter Count from 74:1 up to the word 'عليها' before 'تِسۡعَةَ عَشَرَؕ' in Ayah 30")
        letter_counts_sum = find_letters_count_in_range(quran, 74, 1, 29) + len("عليها")
        st.info(f"Total Letters: {letter_counts_sum}")
        st.info(f"✔️ 19 × 19 = {19 * 19} = {letter_counts_sum} ✅")


    for i in range(len(titles)):
        if i == 0:
            with st.expander(titles[i]):
                st.markdown("Allah says in **Surah Al-Muddathir (74:30)**: _\"Over it are nineteen [angels]\"_, referring to **the guards of Hell**.")

        elif i == 1:
            with st.expander(titles[i]):
                st.markdown("Allah says this number (19) is a **test for believers**, **not just a coincidence**.")
        elif i == 2:
            with st.expander(titles[i]):
                st.markdown("And this number is also a **trial for the disbelievers**, to separate truth from falsehood.")
        elif i == 3:
            with st.expander(titles[i]):
                st.markdown("**Bismillah** (بسم الله الرحمن الرحيم) contains exactly **19 Arabic letters**.")
                bismillah = quran['ayah_ar'][0]
                st.info(f'{get_arabic_letters(bismillah)} : {count_arabic_letters(bismillah)}')
                st.image("images/numerical/19_bismillah_letters.png")
        elif i == 4:
            with st.expander(titles[i]):
                st.markdown(f"**Bismillah** appears **{19 * 6} times** in the Qur’an (19 × 6).")
        elif i == 5:
            with st.expander(titles[i]):
                st.markdown(f"The Qur’an has **{19 * 6} chapters** (114), another multiple of 19.")
        elif i == 6:
            with st.expander(titles[i]):
                st.markdown("The **sum of all chapter numbers** is **6555**, which is **345 × 19**.")
        elif i == 7:
            with st.expander(titles[i]):
                st.markdown("The **sum of all digits** used in the Qur’an (in verse/chapter numbers) is also a **multiple of 19**.")
                        # Helper to sum digits of a number
                def sum_digits(n):
                    return sum(int(d) for d in str(n))

                # Calculate total digit sum
                def calculate_total_digit_sum(surah_verses):
                    total_digit_sum = 0
                    for surah, verse_count in surah_verses.items():
                        for verse in range(1, verse_count + 1):
                            total_digit_sum += sum_digits(surah) + sum_digits(verse)
                    return total_digit_sum

                # Streamlit interface
                st.title("🔢 Divine Digit Sum in the Qur’an")
                st.markdown("""
                This app calculates the **sum of all digits** used in the **chapter and verse numbers** of the entire Qur’an.
                It checks whether the total sum is a **multiple of 19**, related to the concept of **mathematical miracles** in the Qur'an.
                """)

                surah_nos = [i for i in range(1,115)]
                ayah_nos = [quran[quran['surah_no'] == i]['total_ayah_surah'].iloc[0] for i in surah_nos]
                
                surah_verses = dict(zip(surah_nos, ayah_nos))

                if st.button("🔍 Calculate Digit Sum"):
                    total = calculate_total_digit_sum(surah_verses)
                    is_divisible = total % 19 == 0

                    st.subheader("📊 Results")
                    st.write(f"**Total Digit Sum**: `{total}`")
                    st.write(f"**Is it divisible by 19?**: {'✅ Yes' if is_divisible else '❌ No'}")

                    if is_divisible:
                        st.success("This total is a multiple of 19 — which may indicate a divine numerical structure.")
                    else:
                        st.warning("This total is not a multiple of 19.")
        elif i == 8:
            with st.expander(titles[i]):
                st.markdown("**The word 'Allah'** appears **2698 times** (which is **19 × 142**).")
        elif i == 9:
            with st.expander(titles[i]):
                st.markdown("The **sum of the verse numbers** where the word 'Allah' appears is also a **multiple of 19**.")
        elif i == 10:
            with st.expander(titles[i]):
                st.markdown("Some surahs start with mysterious Arabic letters like **Alif-Lam-Meem**. If we count their frequency and multiply each letter by its alphabetic rank, the total is a **multiple of 19**.")
        elif i == 11:
            with st.expander(titles[i]):
                st.markdown("**Alif (ا)** is the most frequent letter in the Qur’an and is central in many 19-based patterns.")


    st.divider()

    st.markdown("📌 **Note:** These facts are often studied under the topic of _Qur'anic numerical miracles_ or _code 19 theory_, but interpretations may vary among scholars.")

if option == "Surah Ar - Rahman":
    st.header("Surah Ar - Rahman")
    prime_sum_upto_55th = sum(get_prime_nums_upto_nth(55))
    surah_55th = find_surah_no(quran, 55)
    st.markdown(f"""
> Total Number of Verses in Holy Quran (6236) = 
Sum of first 55th prime numbers is : {prime_sum_upto_55th}
 - Chapter number 55 is {surah_55th[1]}
 - Number of Verses 78 in Ar-Rahman
 + number of Repeated verses 31

Now 6338 - 55 - 78 + 31 = {prime_sum_upto_55th - 55 - 78 + 31}
""")