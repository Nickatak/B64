# Second iteration?

class B64Decoder(object):

    def __init__(self):
        self.char_map = self.__mk_char_map()
        self.byte_array = []


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

    def split(self, iterable, length):
        return [iterable[start_slice: start_slice + length] for start_slice in range(0, len(iterable), length)]

    # Should be a set of 6 bit integers. Woooeee, I don't even know if this is better.
    def __indices_to_bytes(self, chunk):
        buffer = 0
        
        for char in chunk:
            buffer |= self.char_map[char]
            buffer <<= 6

        # "Truncate" it back down.
        buffer >>= 6

        return buffer

    def __buffer_to_ints(self, buffer):
        ints = [None] * 3
        # Read the ints backwards.

        for x in range(3):
            byte = 0
            for y in range(8):
                byte |= (buffer & 1) << y
                buffer >>= 1

            ints[x] = byte

        ints.reverse()
        return ints

    def __read_text(self):
        return ''.join([chr(x) for x in self.byte_array])

    def decode(self, input_str):
        chunks = self.split(input_str, 4)
        self.byte_array = [None] * (3 * len(chunks))
        byte_array_ptr = 0

        for chunk in chunks:
            buffer = self.__indices_to_bytes(chunk)
            ints = self.__buffer_to_ints(buffer)

            for num in ints:
                self.byte_array[byte_array_ptr] = num
                byte_array_ptr += 1
        
        return self.__read_text()


tester = 'TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4='
a = B64Decoder()
print(a.decode(tester))


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        