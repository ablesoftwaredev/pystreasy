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
