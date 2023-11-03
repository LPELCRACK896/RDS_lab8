from PIL import Image
import numpy as np
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad

# Cargar la imagen
img_path = 'tux.bmp'
img = Image.open(img_path)

# Convertir la imagen a un arreglo de numpy con las dimensiones dadas (405, 480, 4)
img_data = np.array(img)
reshaped_img_data = img_data.reshape((405, 480, 4))

# Aplanar la imagen y convertirla a bytes
flat_img_bytes = reshaped_img_data.tobytes()

# Generar una clave y un IV aleatorios para el cifrado AES
key = Random.get_random_bytes(16)  # AES-128
iv = Random.get_random_bytes(16)   # IV debe ser de 16 bytes para AES-128

# Cifrar los datos de la imagen utilizando el modo CBC
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
ciphertext_cbc = cipher_cbc.encrypt(pad(flat_img_bytes, AES.block_size))

# Guardar la imagen cifrada en modo CBC
encrypted_img_path_cbc = 'tux_encrypted_CBC.png'
encrypted_img_cbc = Image.fromarray(ciphertext_cbc[:405 * 480 * 4].reshape((405, 480, 4)), 'RGBA')
encrypted_img_cbc.save(encrypted_img_path_cbc)

# Cifrar los datos de la imagen utilizando el modo ECB
cipher_ecb = AES.new(key, AES.MODE_ECB)
ciphertext_ecb = cipher_ecb.encrypt(pad(flat_img_bytes, AES.block_size))

# Guardar la imagen cifrada en modo ECB
encrypted_img_path_ecb = 'tux_encrypted_ECB.png'
encrypted_img_ecb = Image.fromarray(ciphertext_ecb[:405 * 480 * 4].reshape((405, 480, 4)), 'RGBA')
encrypted_img_ecb.save(encrypted_img_path_ecb)
