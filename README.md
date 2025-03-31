# SimpleEncryptor

This file contains a single encryption class: `SimpleEncryptor` (basic XOR-based cipher).

## Overview

### SimpleEncryptor
A lightweight symmetric encryption class that:
- Uses a key to generate a base 4x4 matrix
- Creates unique key matrices per 16-byte block
- Applies XOR operations for encryption/decryption
- Outputs ciphertext in hexadecimal format


## Features
- **Block-based encryption**: Both classes process data in 16-byte blocks
- **Dynamic keying**: Unique key matrices generated per block
- **Symmetric**: Same key used for encryption and decryption
- **Hex output**: Ciphertext returned as hexadecimal strings
- **Padding**: Handles variable-length messages with delimiter (255) and zeros
- **Cipher-specific**: Multiple rounds with blending and scrambling for enhanced diffusion

## Usage

### SimpleEncryptor
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
- **SimpleEncryptor**: Lacks diffusion, vulnerable to known-plaintext attacks
- No external dependencies

## License

- MIT License