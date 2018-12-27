# def search4vowels(words: str) -> set:
#     '''Display any vowels in an asked-for word. '''
#     vowels = set('aeiou')
#     return vowels.intersection(set(words))


def search4letters(phrase: str, letter: str = 'aeiou') -> set:
    """Return a set of 'letters' found in 'phrase'."""
    return set(letter).intersection(set(phrase))
