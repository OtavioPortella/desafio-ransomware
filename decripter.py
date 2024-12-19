# decripter.py

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave para descriptografia
key = b"testeransomwares"
nonce = file_data[:16]  # Extrai o nonce usado na criptografia (primeiros 16 bytes)
encrypted_data = file_data[16:]  # Dados criptografados restantes

# Configurar o decifrador
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
decipher = cipher.decryptor()
decrypt_data = decipher.update(encrypted_data) + decipher.finalize()

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
with open("teste.txt", "wb") as new_file:
    new_file.write(decrypt_data)
