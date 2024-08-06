def url_similarity(word1, word2, threshold=0.85):
    length = max(len(word1), len(word2))
    chars1 = set(word1)
    chars2 = set(word2)
    chars = chars1.union(chars2)
    unmatched_chars = 0

    for c in chars:
        unmatched_chars += abs(word1.count(c) - word2.count(c))

    similarity = "{:.2}".format(1 - unmatched_chars / length)
    if float(similarity) >= threshold:
        return True
    return False


def title_similarity(word1, word2, threshold=0.85):
    keywords1 = word1.split(" ")
    keywords2 = word2.split(" ")
    length = max(len(set(keywords1)), len(set(keywords2)))
    common = set(keywords1).intersection(set(keywords2))

    similarity = "{:.2}".format(len(common) / length)
    if float(similarity) >= threshold:
        return True
    return False


url_similarity("h", "h")
title_similarity("j j p", "j j j p")
