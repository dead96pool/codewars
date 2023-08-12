
def int32_to_ip(int32):
    
    if int32 == 0:
        return "0.0.0.0"
    
    # converting the int to binary and padding to get 32 bits 
    bin32 = str(bin(int32)[2:]).zfill(32)

    # taking 8 bits at a time and convert into int and store as string in a list
    ip_bin = [str(int(bin32[i:i+8], 2)) for i in range(0, len(bin32), 8)]
    ip = ".".join(ip_bin)

    return ip


def assert_equals(output, expected):
    print(output == expected)

if __name__ == "__main__":
    #assert_equals(int32_to_ip(2154959208), "128.114.17.104") 
    #assert_equals(int32_to_ip(0), "0.0.0.0")
    #assert_equals(int32_to_ip(2149583361), "128.32.10.1")
    #assert_equals(int32_to_ip(4294967168), "255.255.255.128")
    
    assert_equals(int32_to_ip(213019947), "54.155.211.176")
    