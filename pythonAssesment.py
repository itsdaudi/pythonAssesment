import re
def count_specific_word(text: str, word: str) -> int:
    if not text or not word:
        return 0

    text_lower = text.lower()
    word_lower = word.lower()

    words = re.findall(r'\w+', text_lower)
    count = words.count(word_lower)
    return count