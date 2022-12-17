from cmath import nan


def is_ip_address_valid(ip_address: str) -> bool:
    """Check if the IP address is valid. (IPv4)
    Args:
        ip_address (str): The IP address to check.

    Returns:
        bool: True if the IP address is valid, False otherwise
    """

    try:
        # check for number input
        if type(ip_address) is not str:
            return (
                "invalid input. You need to provide a valid IP address in string format"
            )

        ip_list = ip_address.split(".")
        octets_count = len(ip_list)

        # check for -ve octets
        for octet in ip_list:
            if abs(int(octet)) != int(octet):
                return f"invalid ip: {ip_address}"

        # check for 4 octets
        if octets_count != 4:
            return f"need 4 octets. given {octets_count}"
        else:
            valid_octets = 0
            for octet in ip_list:
                if int(octet) >= 0 and int(octet) <= 255:
                    valid_octets += 1

            return True if valid_octets == 4 else False

    except:
        return f"invalid input:{ip_address}"


def is_palindrome(string: str) -> bool:
    """Check if the string is a palindrome.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False
    """
    # did user enter a string?
    if type(string) is not str:
        return "invalid input: You need to enter a string"

    # empty string
    if len(string) == 0:
        return "invalid input: empty string"
    try:
        result = True if string[::-1] == string else False
        return result
    except:
        return False


def is_prime(number: int) -> bool:
    """Check if specified number is a prime number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a prime number else returns False
    """
    # did user enter a number?
    if type(number) is not int:
        return "invalid input: You need to enter a number"

    # check for -ve numbers
    if number < 0:
        return "invalid input: You need to enter a positive number"

    # check for 0 and 1
    if number == 0 or number == 1:
        return False

    # check for 2
    if number == 2:
        return True

    # check for even numbers
    if number % 2 == 0:
        return False

    # check for odd numbers
    for i in range(3, number):
        if number % i == 0:
            return False

    return True
