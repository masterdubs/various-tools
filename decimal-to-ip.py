def decimal_to_ipv4(decimal_ip):
    """
    Convert a decimal number to an IPv4 address.

    Parameters:
    decimal_ip (int): The decimal number representing the IPv4 address.

    Returns:
    str: The IPv4 address in standard dot notation.
    """
    # Convert to a 32-bit binary string
    binary_ip = format(decimal_ip, '032b')

    # Split the binary string into four octets and convert each to decimal
    octet1 = int(binary_ip[0:8], 2)
    octet2 = int(binary_ip[8:16], 2)
    octet3 = int(binary_ip[16:24], 2)
    octet4 = int(binary_ip[24:32], 2)

    # Combine the octets into a standard IPv4 address format
    return f"{octet1}.{octet2}.{octet3}.{octet4}"

# Example usage:
decimal_ip = 921335384
ipv4_address = decimal_to_ipv4(decimal_ip)
print(ipv4_address)
