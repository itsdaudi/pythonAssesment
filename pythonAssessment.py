import re

def count_specific_word(text: str, word: str) -> int:
    if not text or not word:
        return 0
    text_lower = text.lower()
    word_lower = word.lower()
    words = re.findall(r'\w+', text_lower)
    return words.count(word_lower)

def identify_most_common_word(text: str) -> str | None:
    if not text or text.strip() == "":
        return None
    words = re.findall(r'\w+', text.lower())
    if not words:
        return None
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    most_common_word = words[0]
    max_count = frequency[most_common_word]
    for word in words:
        if frequency[word] > max_count:
            most_common_word = word
            max_count = frequency[word]
    return most_common_word
                "calculates average length of words" 
def calculate_average_word_length(text: str) -> float:
    if not text or text.strip() == "":
        return 0.0
    words = re.findall(r'\w+', text)
    if not words:
        return 0.0
    total_length = 0
    for word in words:
        total_length += len(word)
    return total_length / len(words)

    "counts paragraphs"   
def count_paragraphs(text: str) -> int:
    if not text or text.strip() == "":
        return 1
    paragraphs = re.split(r'\n\s*\n', text.strip())
    count = 0
    i = 0
    while i < len(paragraphs):
        if paragraphs[i].strip():
            count += 1
        i += 1
    if count == 0:
        return 1
    return count


    "count sentences"
def count_sentences(text: str) -> int:
    if not text or text.strip() == "":
        return 1

    sentences = re.split(r'[.!?]+(?:\s|$)', text.strip())
    count = 0
    for sentence in sentences:
        if sentence.strip():
            count += 1

    if count == 0:
        return 1
    return count           
