from barcode import EAN13
from barcode.writer import ImageWriter
import random

chaves_acesso = []

print("PARA SAIR, DIGITE 'sair'\n")

def inser(name, re):
    acess_key = {f"{name}_{re}" : str(random.randint(111111111111, 999999999999))}
    print(acess_key,"\n")
    return acess_key

name = ""

while name != "sair":
    name = input("Nome: ")
    if name == "sair":
        break
    re = input("RE: ")
    if re == "sair":
        break
    chaves_acesso.append(inser(name, re))

if chaves_acesso:
    for pessoas in chaves_acesso:
        for nome, chave in pessoas.items():
            codigo_barra = EAN13(chave, writer=ImageWriter())
            codigo_barra.save(f'barcodes/{nome}_key')