class Decoder(object):
    
    def __init__(self):
        self.char_map = self.__mk_char_map()

    def __split(self, enumerable, chunk_size):
        return [enumerable[chunk_start: chunk_start + chunk_size] for chunk_start in range(0, len(enumerable), chunk_size)]

    def __mk_char_map(self):
            char_map = {}
            uppercase_offset = 65
            lower_case_offset = 97

            # Add uppercase.
            for idx in range(0, 26):
                char_map[chr(uppercase_offset + idx)] = idx

            # Add lowercase.
            for idx in range(26, 52):
                char_map[chr(lower_case_offset - 26 + idx)] = idx

            # Add numbers (0-9)
            for idx in range(0, 10):
                char_map[str(idx)] = 52 + idx

            char_map['+'] = 62
            char_map['/'] = 63
            char_map['='] = 0

            return char_map


    def __pad_str_l(self, input_str, length, char):
        while len(input_str) != length:
            input_str = char + input_str

        return input_str

    def __char_to_bin_str(self, char):
        int_value = self.char_map[char]

        bin_str = ''

        while int_value:
            bin_str = str(int_value & 1) + bin_str
            int_value >>= 1

        return self.__pad_str_l(bin_str, 6, '0')
            
    def __chunk_to_bin_strs(self, chunk):
        bin_str = ''
        for char in chunk:
            bin_str += self.__char_to_bin_str(char)

        return self.__split(bin_str, 8)

    def __byte_to_char(self, byte_str):
        int_value = 0

        for idx, bit in enumerate(byte_str):
            if bit == '1':
                int_value += 2 ** (len(byte_str) - 1 - idx)

        return chr(int_value)
        
    def decode(self, input_str):
        chunks = self.__split(input_str, 4)
        output = ''
        
        for chunk in chunks:
            bytes = self.__chunk_to_bin_strs(chunk)
            for byte in bytes:
                output += self.__byte_to_char(byte)

        return output
        

if __name__ == '__main__':
    tester = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="
    
    a = Decoder()
    a.decode(tester)