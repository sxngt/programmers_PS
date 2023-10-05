def solution(n, words):
    a = dict()
    for i, word in enumerate(zip(words, words[1:])):
        print(words[:i], word[1])
        if word[0][-1] != word[1][0] or word[1] in words[:i]:
            return [len(words) // words.index(word[1]), len(words) % words.index(word[1])]


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
