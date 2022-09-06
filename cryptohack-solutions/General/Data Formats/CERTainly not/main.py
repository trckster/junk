import OpenSSL.crypto

data = open('2048b-rsa-cert.der', 'rb').read()
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, data)
public_numbers = x509.get_pubkey().to_cryptography_key().public_numbers()

print(public_numbers.n)
