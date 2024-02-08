from barcode import EAN13
from barcode.writer import ImageWriter
import random

chaves_acesso = {
    "Matheus Gomes_54701": str(random.randint(111111111111, 999999999999)),
    "Felipe Moreira_3001": str(random.randint(111111111111, 999999999999)),
    "Ricardo_Barbosa_6549": str(random.randint(111111111111, 999999999999))
}

for pessoas in chaves_acesso:
    codigo_barra = EAN13(chaves_acesso[pessoas], writer=ImageWriter())
    codigo_barra.save(f'{pessoas}_key')