"""
출처: https://www.hackerrank.com/challenges/apple-and-orange/problem
"""


def countApplesAndOranges(s, t, a, b, apples, oranges):
    def houseFruit(p):
        result = 0
        for point in p:
            if s <= point <= t:  # 집 사이에 과일이 떨어졌는가?
                result += 1
        return result

    apple_point = [a + apple for apple in apples]  # 사과가 떨어진 지점
    orange_point = [b + orange for orange in oranges]  # 오렌지가 떨어진 지점

    print(houseFruit(apple_point))
    print(houseFruit(orange_point))


def improvement(s, t, a, b, apples, oranges):
    def houseFruit(tree, fruits):
        count = 0
        for f in fruits:
            if s <= f + tree <= t:
                count += 1
        return count

    print(houseFruit(a, apples))
    print(houseFruit(b, oranges))


# countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
improvement(7, 11, 5, 15, [-2, 2, 1], [5, -6])
