def is_ip_address_valid(ip_address: str) -> bool:
    """Check if the IP address is valid. (IPv4)
    Args:
        ip_address (str): The IP address to check.

    Returns:
        bool: True if the IP address is valid, False otherwise
    """

    try:
        ip_list = ip_address.split(".")
        octets_count = len(ip_list)

        if octets_count < 4 or octets_count > 4:
            return f"need 4 octets. given {octets_count}"
        else:
            valid_octets = 0

            for octet in ip_list:
                if int(octet) >= 0 and int(octet) <= 255:
                    valid_octets += 1

            return True if valid_octets == 4 else False

    except:
        return f"invalid input:{ip_address}"
