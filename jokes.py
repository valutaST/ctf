import secrets
import string
import random
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

flag = os.getenv('FLAG', 'f13{J0k3s_4S1D3_1C4Nt_pu11_4_Gf}').strip()
random_bytes = secrets.token_bytes(32)
pad_character = random.choice(string.ascii_letters)

backend = default_backend()
mode = modes.ECB()
cipher = Cipher(algorithms.AES(random_bytes), mode, backend)

while True:
    try:
        text_input = input('text: ')
        plain_text = text_input + flag
        length = len(plain_text)

        pad_count = (length // 64 + 1) * 64 if length % 64 != 0 else 0

        plain_text = plain_text.ljust(pad_count, pad_character)

        print("ciphered:")
        print((cipher.encryptor().update(plain_text.encode())).hex())

    except KeyboardInterrupt:
        break