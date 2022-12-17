from pystreasy import utils


def test_is_ip_address_valid():
    """
    tests if a given IPv4 ip address is valid or not
    """
    # number
    assert (
        utils.is_ip_address_valid(10)
        == "invalid input. You need to provide a valid IP address in string format"
    )

    # Valid IP
    assert utils.is_ip_address_valid("1.2.3.4") is True
    assert utils.is_ip_address_valid("192.168.10.1") is True

    # # abcd
    assert utils.is_ip_address_valid("abcd") == "invalid input:abcd"

    # # 10.0.0
    assert utils.is_ip_address_valid("10.0.0") == "need 4 octets. given 3"

    # -10.0.0.1
    assert utils.is_ip_address_valid("-10.0.0.1") == "invalid ip: -10.0.0.1"

    # -a.b.c.d
    assert utils.is_ip_address_valid("-a.b.c.d") == "invalid input:-a.b.c.d"


def test_is_palindrome():
    """
    tests if a given string is a palindrome or not
    """
    # palindrome
    assert utils.is_palindrome("madam") is True
    assert utils.is_palindrome("able was i ere i saw elba") is True
    assert utils.is_palindrome("...") is True
    assert utils.is_palindrome("123321") is True
    assert utils.is_palindrome("!@##@!") is True
    assert utils.is_palindrome("_O_") is True
    # number
    assert utils.is_palindrome(10) == "invalid input: You need to enter a string"
    assert utils.is_palindrome(-10) == "invalid input: You need to enter a string"
    assert utils.is_palindrome(10.5) == "invalid input: You need to enter a string"
    # empty string
    assert utils.is_palindrome("") == "invalid input: empty string"
    # number in string
    assert utils.is_palindrome("10.5") is False
    # special characters
    assert utils.is_palindrome("'.'..''") is False
    assert utils.is_palindrome("@#$#^&*") is False
    # only whitespace characters
    assert utils.is_palindrome("  ") is True


def test_is_prime():
    """
    tests if a given number is a prime number or not
    """
    assert utils.is_prime(10) is False
    assert utils.is_prime(11) is True
    assert utils.is_prime(13) is True
    assert utils.is_prime(15) is False
    assert utils.is_prime(17) is True
    assert utils.is_prime(19) is True
    assert utils.is_prime(21) is False
    assert utils.is_prime(23) is True
    assert utils.is_prime(25) is False
    assert utils.is_prime(27) is False
    assert utils.is_prime(29) is True
    assert utils.is_prime(31) is True
    assert utils.is_prime(33) is False
    assert utils.is_prime(35) is False
    assert utils.is_prime(37) is True
    assert utils.is_prime(39) is False
    assert utils.is_prime(41) is True
    assert utils.is_prime(43) is True
    assert utils.is_prime(45) is False
    assert utils.is_prime(47) is True
    assert utils.is_prime(49) is False
    assert utils.is_prime(51) is False
    assert utils.is_prime(53) is True
    assert utils.is_prime(55) is False
    assert utils.is_prime(57) is False
    assert utils.is_prime(59) is True
    assert utils.is_prime(61) is True
    assert utils.is_prime(63) is False
    assert utils.is_prime(65) is False
    assert utils.is_prime(67) is True
    assert utils.is_prime(69) is False
    assert utils.is_prime(71) is True
    assert utils.is_prime(73) is True
    assert utils.is_prime(75) is False
    assert utils.is_prime(77) is False
    assert utils.is_prime(79) is True
    assert utils.is_prime(81) is False
    assert utils.is_prime(83) is True
    assert utils.is_prime(85) is False
    assert utils.is_prime(87) is False
    assert utils.is_prime(89) is True
    assert utils.is_prime(91) is False
    assert utils.is_prime(93) is False
    assert utils.is_prime(95) is False
    assert utils.is_prime(17) is True
