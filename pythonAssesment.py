import re
def count_specific_word(text: str, word: str) -> int:
    if not text or not word:
        return 0

    text_lower = text.lower()
    word_lower = word.lower()

    words = re.findall(r'\w+', text_lower)
    count = words.count(word_lower)
    return count

    def identify_most_common_word(text: str) ->str:
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
