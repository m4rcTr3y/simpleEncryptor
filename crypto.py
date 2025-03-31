class SimpleEncryptor:

    def __init__(self, key):
        self.key = key
        self.key_bytes = self.text_to_bytes(key)
        self.base_key_matrix = self.make_base_key_matrix(self.key_bytes)

    @staticmethod
    def text_to_bytes(text):
        """Convert text to a list of bytes using ASCII encoding."""
        return [ord(char) for char in text]

    @staticmethod
    def bytes_to_text(byte_list):
        """Convert a list of bytes back to text, stopping at delimiter 255."""
        result = ""
        for b in byte_list:
            if b == 255:  # Delimiter: stop here
                break
            result += chr(b)
        return result

    @staticmethod
    def pad_to_16(text_bytes):
        """Pad or repeat text bytes to exactly 16 bytes."""
        if len(text_bytes) >= 16:
            return text_bytes[:16]  # Truncate to 16 if too long
        repeated = text_bytes * ((16 // len(text_bytes)) + 1)
        return repeated[:16]

    def make_base_key_matrix(self, key_bytes):
        """Create a base 4x4 key matrix using multiplication (row × column, mod 256)."""
        key_bytes = self.pad_to_16(key_bytes)
        matrix = [
            key_bytes[0:4],
            key_bytes[4:8],
            key_bytes[8:12],
            key_bytes[12:16]
        ]
        key_matrix = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                key_matrix[i][j] = (matrix[i][j] * matrix[j][i]) % 256
        return key_matrix

    def make_block_key_matrix(self, block_index):
        """Generate a unique key matrix for each block by XORing with block index."""
        block_matrix = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                # XOR base value with block_index (mod 256 to stay in byte range)
                block_matrix[i][j] = (self.base_key_matrix[i][j] ^ block_index) % 256
        return block_matrix

    @staticmethod
    def split_into_blocks(text_bytes):
        """Split text into 16-byte blocks, pad last block with 255 + zeros."""
        blocks = []
        for i in range(0, len(text_bytes), 16):
            block = text_bytes[i:i + 16]
            if len(block) < 16:  # Last block
                block.append(255)  # Delimiter
                block.extend([0] * (16 - len(block)))  # Pad with zeros
            blocks.append(block)
        return blocks

    @staticmethod
    def matrix_to_bytes(matrix):
        """Flatten a 4x4 matrix into a 16-byte list."""
        return [matrix[i][j] for i in range(4) for j in range(4)]

    @staticmethod
    def bytes_to_matrix(byte_list):
        """Convert a 16-byte list into a 4x4 matrix."""
        return [
            byte_list[0:4],
            byte_list[4:8],
            byte_list[8:12],
            byte_list[12:16]
        ]

    @staticmethod
    def xor_matrices(matrix1, matrix2):
        """XOR two 4x4 matrices element-wise."""
        result = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result[i][j] = matrix1[i][j] ^ matrix2[i][j]
        return result

    def encrypt(self, plaintext):
        """Encrypt plaintext with a dynamic key matrix per block, return hex string."""
        text_bytes = self.text_to_bytes(plaintext)
        
        # Split text into blocks
        blocks = self.split_into_blocks(text_bytes)
        
        # Encrypt each block with a unique key matrix
        ciphertext_bytes = []
        for block_index, block in enumerate(blocks):
            # Generate key matrix for this block
            key_matrix = self.make_block_key_matrix(block_index)
            block_matrix = self.bytes_to_matrix(block)
            encrypted_matrix = self.xor_matrices(block_matrix, key_matrix)
            ciphertext_bytes.extend(self.matrix_to_bytes(encrypted_matrix))
        
        # Convert to hex
        ciphertext_hex = ''.join(format(b, '02x') for b in ciphertext_bytes)
        return ciphertext_hex

    def decrypt(self, ciphertext_hex):
        """Decrypt hex-encoded ciphertext with dynamic key matrices."""
        ciphertext_bytes = [int(ciphertext_hex[i:i+2], 16) for i in range(0, len(ciphertext_hex), 2)]
        
        # Split ciphertext into 16-byte blocks
        cipher_blocks = [ciphertext_bytes[i:i + 16] for i in range(0, len(ciphertext_bytes), 16)]
        
        # Decrypt each block
        plaintext_bytes = []
        for block_index, block in enumerate(cipher_blocks):
            key_matrix = self.make_block_key_matrix(block_index)
            block_matrix = self.bytes_to_matrix(block)
            decrypted_matrix = self.xor_matrices(block_matrix, key_matrix)
            plaintext_bytes.extend(self.matrix_to_bytes(decrypted_matrix))
        
        return self.bytes_to_text(plaintext_bytes)

