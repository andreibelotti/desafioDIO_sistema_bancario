# Sistema Bancário Simples em Python

---

## Visão Geral do Projeto

Este é um projeto simples de sistema bancário desenvolvido em Python. Ele simula operações básicas de uma conta bancária, como **depósito**, **saque** e **exibição de extrato**. O sistema é projetado para ser intuitivo e fácil de usar, operando em um console.

**Este projeto faz parte de um desafio proposto no bootcamp "Backend Python Santander Academy" da Santander / DIO, com o objetivo de aplicar conceitos fundamentais da linguagem Python.**

---

## Funcionalidades

O sistema oferece as seguintes operações:

* **Depositar (`d`):** Permite adicionar fundos à conta. O valor deve ser positivo.
* **Sacar (`s`):** Permite retirar fundos da conta. Possui as seguintes restrições:
    * Não é possível sacar mais do que o saldo disponível.
    * O valor do saque não pode exceder o limite de R$ 500,00 por operação.
    * Há um limite de 3 saques diários.
* **Extrato (`e`):** Exibe todas as movimentações (depósitos e saques) realizadas na conta, além do saldo atual.
* **Sair (`q`):** Encerra a aplicação.

---

## Como Rodar o Projeto

Para executar este sistema bancário em seu ambiente local, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado em sua máquina.
2.  **Clone o Repositório (ou baixe o arquivo):**
    * Se você tem Git:
        ```bash
        git clone [https://github.com/andreibelotti/sistema-bancario-simples-python.git](https://github.com/andreibelotti/sistema-bancario-simples-python.git)
        ```
    * Se preferir, baixe o arquivo `banco.py` diretamente.
3.  **Navegue até a Pasta do Projeto:**
    ```bash
    cd sistema-bancario-simples-python
    ```
    (Ou para a pasta onde você salvou o arquivo.)
4.  **Execute o Script:**
    ```bash
    python banco.py
    ```

---

## Exemplo de Uso

Ao rodar o programa, você verá um menu interativo no console:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>


Você pode digitar a letra correspondente à operação desejada e seguir as instruções.

---

## Contribuição

Este projeto é um exemplo básico e pode ser expandido com diversas funcionalidades, como:

* Gerenciamento de múltiplas contas.
* Transferências entre contas.
* Autenticação de usuário.
* Persistência de dados (salvar em arquivo).

Sinta-se à vontade para explorar e aprimorar!

---

## Autor

* **Andrei Belotti** - [https://github.com/andreibelotti](https://github.com/andreibelotti)

---
