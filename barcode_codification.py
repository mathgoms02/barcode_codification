from barcode import EAN13
from barcode.writer import ImageWriter
import random

chaves_acesso = []

def inser(name, re):
    caminho_log = "códigos-criados.txt"
    key = str(random.randint(111111111111, 999999999999))
    acess_key = {f"{name}_{re}" : key}
    with open(caminho_log, 'a') as file:
        log = f"{name}_{re} : {key}\n"
        file.write(log)

    chaves_acesso.append(acess_key)

    return acess_key

def crea():
    if chaves_acesso:
        for pessoas in chaves_acesso:
            for nome, chave in pessoas.items():
                codigo_barra = EAN13(chave, writer=ImageWriter())
                codigo_barra.save(f'barcodes/{nome}_key')
