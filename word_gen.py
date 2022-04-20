from random_word import RandomWords


def guess_word():
    r = RandomWords()
    random = r.get_random_words(hasDictionaryDef="true",
                                includePartOfSpeech="noun,verb", minLength=5,
                                maxLength=5, sortBy="alpha", sortOrder="asc", limit=10)
    return random


word = guess_word()
print(word)
