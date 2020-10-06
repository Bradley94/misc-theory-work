"""
Take the following IPv4 address: 128.32.10.1 This address has 4 octets where each 
octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the 32 bit number: 2149583361.

Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and 
returns a 32 bit number.
EXAMPLE
  ip_to_int32("128.32.10.1") => 2149583361
"""
# In future I might try to redo this code without using any inbuilt Python functions

def ip_to_int32(ip):
    split_ip = ip.rsplit('.')  # Separate out our numbers 
    stringed_result = ''  # This will store the binary values connected as a string
    
    for value in split_ip:
        value = int(value)
        x = "{0:b}".format(value)  # Remove leading 0b
        x = str(x).zfill(8)  # Ensure we have 8 'digits' 
        stringed_result += x  
        
    return int(stringed_result, 2)  # Cast back to int and obtain our result
 
"""
Test.describe("Basic Tests")
Test.expect(ip_to_int32("128.114.17.104") == 2154959208, "wrong integer for ip: 128.114.17.104")
Test.expect(ip_to_int32("0.0.0.0") == 0, "wrong integer for ip: 0.0.0.0")
Test.expect(ip_to_int32("128.32.10.1") == 2149583361, "wrong integer for ip: 128.32.10.1")
"""
