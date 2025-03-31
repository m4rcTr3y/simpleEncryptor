# SimpleEncryptor and Cipher

This file contains two encryption classes: `SimpleEncryptor` (basic XOR-based cipher) and `Cipher` (more complex cipher with multiple rounds).

## Overview

### SimpleEncryptor
A lightweight symmetric encryption class that:
- Uses a key to generate a base 4x4 matrix
- Creates unique key matrices per 16-byte block
- Applies XOR operations for encryption/decryption
- Outputs ciphertext in hexadecimal format

### Cipher
A more complex symmetric encryption class that:
- Uses multiple rounds of XOR, blending, and scrambling
- Processes 16-byte blocks with dynamic key matrices
- Includes bit rotation and matrix operations for better diffusion

## Features
- **Block-based encryption**: Both classes process data in 16-byte blocks
- **Dynamic keying**: Unique key matrices generated per block
- **Symmetric**: Same key used for encryption and decryption
- **Hex output**: Ciphertext returned as hexadecimal strings
- **Padding**: Handles variable-length messages with delimiter (255) and zeros
- **Cipher-specific**: Multiple rounds with blending and scrambling for enhanced diffusion

## Usage

### SimpleEncryptor
```python
encryptor = SimpleEncryptor("HELLO")
plaintext = "THIS IS A VERY LONG MESSAGE TO ENCRYPT"
ciphertext = encryptor.encrypt(plaintext)
decrypted = encryptor.decrypt(ciphertext)
```
## Limitations

- **Security**: These are educational ciphers, not suitable for high-security applications
- **SimpleEncryptor**: Lacks diffusion, vulnerable to known-plaintext attacks
- **Cipher**: More complex but still not cryptographically secure by modern standards
- **Key Length**: Keys are padded or truncated to 16 bytes; short keys may repeat
- **Performance**: Not optimized for large data volumes

## Requirements

- Python 3.x
- No external dependencies

## License

- MIT License