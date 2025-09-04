import re

SEQUENCES = ["12345","abcdef","qwerty"]
COMMON_WORDS = ["password","welcome","admin"]

def has_sequence(pw):
    return any(seq in pw.lower() for seq in SEQUENCES)

def has_common_word(pw):
    return any(word in pw.lower() for word in COMMON_WORDS)
