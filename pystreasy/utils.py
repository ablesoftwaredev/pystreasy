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
