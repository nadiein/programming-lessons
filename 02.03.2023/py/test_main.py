import main


# First approach
def test_top_3_words():
    test_cases = (
        ('a a a  b  c c  d d d d  e e e e e', ['e','d','a']),
        ('a a c b b', ['a','b','c']),
        ('e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e', ['e','ddd','aa']),
        ("  //wont won't won't ", ["won't", "wont"]),
        ('  , e   .. ', ['e']),
        ('  ...  ', []),
        ("  '  ", []),
        ('''In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income.''', ['a','of','on'])
    )

    for x, y in test_cases:
        # First approach
        assert main.top_3_words_one(x) == y
        # Second approach
        assert main.top_3_words_two(x) == y
