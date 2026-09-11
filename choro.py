import os
import hashlib

# 1. Isso vai disparar o Semgrep (Vulnerabilidade Crítica de Command Injection)
def ping_server(ip_address):
    os.system("ping -c 1 " + ip_address)

# 2. Isso vai disparar o Semgrep (Uso de Hash Fraco/Obsoleto)
def encrypt_password(password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

# 3. Isso vai disparar o Gitleaks (Token realístico do GitHub - Falso, mas com o padrão exato)
API_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890"

# 4. Isso vai disparar o Gitleaks (Chave AWS genérica sem a palavra example)
AWS_KEY = "AKIAIMW6AUJZXBWV6U3Q"