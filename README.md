# Gerador de Códigos de Barras para Chaves de Acesso

Este é um programa em Python que gera códigos de barras EAN-13 para chaves de acesso, utilizando a biblioteca `barcode`. O programa solicita o nome e o registro do usuário e gera um código de barras único para cada chave de acesso.

## Funcionalidades

- **Geração de Códigos de Barras**: O programa gera códigos de barras EAN-13 para cada chave de acesso inserida pelo usuário.

- **Personalização do Código de Barras**: Os códigos de barras são personalizados com o nome e o registro do usuário.

## Pré-requisitos

- Instalação da biblioteca `barcode`. Você pode instalar a biblioteca executando o comando `pip install python-barcode`.

## Como usar

1. Clone este repositório:

   ```
   git clone https://github.com/mathgoms02/barcode_codification.git
   ```

2. Navegue até o diretório do projeto:

   ```
   cd barcode_codification
   ```

3. Execute o programa:

   ```
   python barcode_codification.py
   ```

4. Siga as instruções no terminal para inserir o nome e o registro do usuário. Digite 'sair' para encerrar o programa.

5. Os códigos de barras gerados serão salvos como imagens na pasta do projeto.

## Exemplo de Uso

```
PARA GERAR CÓDIGO, DIGITE 'sair'

Nome: Matheus
RE: 54701
{'Matheus_54701': '235213304384'}
Nome: Felipe
RE: 3001
{'Felipe_3001': '425798435950'}
Nome: sair
```

## Contribuição

Contribuições são bem-vindas! Se você quiser contribuir com melhorias para o Gerador de Códigos de Barras para Chaves de Acesso, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---
