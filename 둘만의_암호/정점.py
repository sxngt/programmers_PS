def solution(s, skip, index):
    return ''.join([[chr(i) for i in range(97,123) if chr(i) not in skip][([chr(i) for i in range(97,123) if chr(i) not in skip].index(char) + index) % len([chr(i) for i in range(97,123) if chr(i) not in skip])] for char in s])
