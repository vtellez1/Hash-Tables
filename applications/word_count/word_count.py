def word_count(s):
    count = {}
    translation_table = dict.fromkeys(map(ord, '":;,.-+=/\|[]}{()*^&'), None)
    string = s.translate(translation_table)

    lower_case = string.lower()
    words = lower_case.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
