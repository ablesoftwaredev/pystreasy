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
