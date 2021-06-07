"""
출처: https://www.hackerrank.com/challenges/the-time-in-words/problem
"""
dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    21: 'twenty one',
    22: 'twenty two',
    23: 'twenty three',
    24: 'twenty four',
    25: 'twenty five',
    26: 'twenty six',
    27: 'twenty seven',
    28: 'twenty eight',
    29: 'twenty nine',
    30: 'half'
}

def timeInWords(h, m):
    answer = ""
    if m <= 30:
        if m == 00:
            answer += dict[h] + " o' clock"
        elif m == 1:
            answer += dict[m] + " minute past " + dict[h]
        elif m == 15:
            answer += dict[m] + " past " + dict[h]
        elif m == 30:
            answer += dict[m] + " past " + dict[h]
        else:
            answer += dict[m] + " minutes past " + dict[h]
    else:
        if m == 45:
            answer += dict[m - 30] + " to " + dict[h + 1]
        else:
            answer += dict[60 - m] + " minutes to " + dict[h + 1]

    return answer

print(timeInWords(1, 1))