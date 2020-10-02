def is_vowel(char):
    """
    Returns True if char is vowel, False otherwise.
    >>> is_vowel('a')
    True
    >>> is_vowel('X')
    False
    >>> is_vowel('E')
    True
    """
    return char.lower() in 'aeiouy'


def count_vowels(text):
    """
    Returns the number of vowels in text.

    >>> count_vowels('')
    0
    >>> count_vowels('Hello World.')
    3
    >>> count_vowels('Aaaaargh')
    5
    """
    is_vowel()


def house_passwords(password):
    """
    Returns True if given password is secure, False otherwise.

    Stephan and Sophia forget about security and use simple
    passwords for everything. Help Nikola develop a password
    security check module. The password will be considered
    strong enough if its length is greater than or equal to 10
    symbols, it has at least one digit, as well as containing
    one uppercase letter and one lowercase letter in it. The
    password contains only ASCII latin letters or digits.

    :param password: A password as a string
    :return: True if password is safe or False if not.

    >>> house_password('A1213pokl')
    False
    >>> house_password('bAse730onE')
    True
    >>> house_password('asasasasasasasaas')
    False
    >>> house_password('QWERTYqwerty')
    False
    >>> house_password('123456123456')
    False
    >>> house_password('QwErTy911poqqqq')
    True
    """
