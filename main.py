from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def reset_input(*widgets):
    for widget in widgets:
        widget.delete("1.0", "end-1c")


def deactivate_input(*widgets):
    for widget in widgets:
        widget.config(state="disabled")


def active_input(*widgets):
    for widget in widgets:
        widget.config(state="normal")


def key_creator():

    # Aqui gera a chave privada
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    # Converte para um arquivo para que possa ser salvo
    global private_pem
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    # Converte para um arquivo para que possa ser salvo
    public_key = private_key.public_key()

    global public_pem
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    # AQUI salva as chaves
    with open("private_key.pem", "wb") as f:
        f.write(private_pem)
    with open("public_key.pem", "wb") as f:
        f.write(public_pem)


def encript(input_step_one, input_step_two, input_step_three, input_public_key, input_private_key):
    key_creator()
    input_step_one.config(state="normal")
    input_step_one_bytes = input_step_one.get("1.0", "end-1c").encode("utf-8")

    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    global ciphertext
    ciphertext = public_key.encrypt(
        input_step_one_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None

        )
    )

    active_input(input_step_two, input_step_three,
                 input_public_key, input_private_key)
    reset_input(input_step_one, input_step_two, input_step_three,
                input_public_key, input_private_key)
    input_step_one.insert("1.0", "Está mensagem está criptografada!")
    input_step_two.insert("1.0", ciphertext)
    input_step_three.insert(
        "1.0", 'Clique no botão para descriptografar a mensagem!')
    input_public_key.insert("1.0", public_pem)
    input_private_key.insert("1.0", private_pem)
    deactivate_input(input_step_one, input_step_two, input_step_three,
                     input_public_key, input_private_key)


def descript(input_step_one, input_step_three):

    with open("private_key.pem", "rb") as f:
        private_key_pem = f.read()
        private_key = serialization.load_pem_private_key(
            private_key_pem,
            password=None
        )
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    active_input(input_step_one, input_step_three)
    reset_input(input_step_three)
    input_step_three.insert(
        "1.0", decrypted_message.decode())
    deactivate_input(input_step_three)
