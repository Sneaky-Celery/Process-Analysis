# Author: Sneaky Celery
# I just wanted to see if hashes matched without reading anything.
# Replace these randomly generated hashes with your own.

known_hash = "6f15ed999d9c660991b669644c3b6fb7d57d5a09dcd82681048a53c92a2e3ea7"

generated_hash = "e880f7d85c7c4aa7f2e6369a4008368c2202930241d03854996084d1a0f4a7b7"

if known_hash.lower() == generated_hash.lower():
    print()
    print("Matched")
else: 
    print()
    print("Failed")
