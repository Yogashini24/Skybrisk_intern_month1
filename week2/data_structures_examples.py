def demo_lists():
    nums = [1, 2, 3]
    nums.append(4)
    squares = [x * x for x in nums]
    print('List', nums, 'Squares', squares)


def demo_tuples():
    t = (1, 'a')
    print('Tuple', t)


def demo_dicts():
    d = {'a': 1, 'b': 2}
    d['c'] = 3
    print('Dict keys', list(d.keys()))


def demo_sets():
    s = set([1, 2, 2, 3])
    print('Set', s)


def demo_functions():
    def add(a, b=0):
        return a + b

    print('Add', add(2, 3))
    print('Lambda map', list(map(lambda x: x * 2, [1, 2, 3])))


def demo_recursion(n):
    if n <= 1:
        return 1
    return n * demo_recursion(n - 1)


if __name__ == '__main__':
    demo_lists()
    demo_tuples()
    demo_dicts()
    demo_sets()
    demo_functions()
    print('Recursion 5! =', demo_recursion(5))
