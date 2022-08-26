class ZeroWidthEncoder:
    bin_list = [" ", "0", "1"]  # mapping of binary string for Zero-Width Characters
    char_list = ["\u2060", "\u200B", "\u200C"]  # default Zero-Width Characters to do encoding

    def encode(self, text: str) -> str:
        def __encode__(secret_text):
            encoded_text = ''
            bin_text = ' '.join(format(ord(x), 'b') for x in secret_text)
            for b in bin_text:
                encoded_text += self.char_list[self.bin_list.index(b)]
            return encoded_text

        return __encode__(text)

    def decode(self, text: str) -> str:
        def __decode__(open_text):
            bin_text = ""
            for w in open_text:
                if w in self.char_list:
                    bin_text += self.bin_list[self.char_list.index(w)]
            bin_val = bin_text.split()
            secret_text = ""
            for b in bin_val:
                secret_text += chr(int(b, 2))
            return secret_text

        return __decode__(text)
