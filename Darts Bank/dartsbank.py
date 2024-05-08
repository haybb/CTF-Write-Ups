import base64, ast


# Lire la liste de chaînes de données chiffrées à partir du fichier encrypted_data.txt
with open("encrypted_data.txt", "r") as f:
    encrypted_data = f.read().split()


# Lire la liste de clés à partir du fichier key.txt
with open("key.txt", "r") as f:
    key = ast.literal_eval(f.read().strip())

# Décoder et déchiffrer chaque message
all_plaintexts = []
for idx, enc_data in enumerate(encrypted_data):
    # Décoder la chaîne de données chiffrées
    decoded_data = base64.b64decode(enc_data.encode('ascii'))

    decrypted_data = bytearray()

    # Appliquer XOR sur chaque message chiffré décodé
    for i in range(len(decoded_data)):
        decrypted_data.append(decoded_data[i] ^ key[i % len(key)])

    # Décode les données déchiffrées en utilisant UTF-8
    plaintext = decrypted_data.decode('utf-8')
    all_plaintexts.append(plaintext)

# Affiche les données déchiffrées
# for plaintext in all_plaintexts:
#     print(plaintext)

# Enregistrer les clés SSL dans un fichier sslkey.log
with open("sslkey.log", "w") as f:
    for plaintext in all_plaintexts:
        f.write(plaintext + "\n")

print("Done, cf sslkey.log :)")