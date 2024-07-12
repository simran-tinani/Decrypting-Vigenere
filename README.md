# Decrypting-Vigenere
A simple Python code to decrypt a Vigenere ciphertext

The code first looks at instances of repeated words in the ciphertext, and uses these to determine the key length as the gcd of the distances at which repetitions are found.

Then, the individual Caeser ciphers are extracted using the key length. The most frequent letter in these is found, and is guessed to be one of "a", "e", "i", "o" and "t". 

Based on all these guesses from the frequency analysis, the set of possible keys is constructed. 

Each of these keys is then used to decrypt the ciphertext. The code stops when a meaningful English text is obtained. This is measured as at least 70% of the words being detected as English dictionary words.

The correct key and plaintext are output.
