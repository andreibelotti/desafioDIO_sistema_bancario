# Sistema Bancário em POO com Python

Este projeto é uma implementação de um sistema bancário simples, desenvolvido em Python, com foco nos conceitos de Programação Orientada a Objetos (POO), herança e polimorfismo. O sistema permite a criação de clientes (pessoas físicas), contas correntes, e a realização de operações bancárias como depósitos, saques e visualização de extrato, tudo gerenciado por objetos e suas interações.

---

## Funcionalidades

O sistema bancário oferece as seguintes funcionalidades principais:

* **Criação de Usuários (Clientes Pessoa Física):**
    * Cadastro de novos clientes com nome, data de nascimento, CPF e endereço.
    * Validação para evitar CPFs duplicados.
* **Criação de Contas Correntes:**
    * Vinculação de contas correntes a clientes existentes.
    * Geração de número de conta sequencial e agência fixa (`0001`).
    * Permite que um mesmo cliente tenha múltiplas contas.
* **Depósito:**
    * Realiza depósitos em contas específicas.
    * Valida se o valor é positivo.
* **Saque:**
    * Permite saques com limites diários (padrão de R$ 500,00) e limite de quantidade de saques (padrão de 3 saques por dia por conta).
    * Valida saldo, limite por operação e limite diário de saques.
* **Extrato:**
    * Exibe todas as movimentações (depósitos e saques) de uma conta específica, com data/hora e o saldo atual.
* **Listagem de Contas:**
    * Exibe detalhes de todas as contas cadastradas no sistema.

---

## 💡 Conceitos de POO Aplicados

Este projeto foi estruturado utilizando os seguintes princípios da Programação Orientada a Objetos:

* **Classes e Objetos:** `Cliente`, `PessoaFisica`, `Conta`, `ContaCorrente`, `Historico`, `Transacao`, `Deposito`, `Saque`.
* **Herança:**
    * `PessoaFisica` herda de `Cliente`.
    * `ContaCorrente` herda de `Conta`.
    * `Deposito` e `Saque` herdam da interface `Transacao`.
* **Encapsulamento:** Utilização de atributos privados (prefixo `_`) acessados por meio de propriedades (`@property`).
* **Abstração (Interfaces):** A classe `Transacao` é uma classe abstrata (`ABC`) que define um contrato para as operações de depósito e saque, garantindo que implementem o método `registrar`.
* **Polimorfismo:** Os métodos `sacar` e `registrar` (da `Transacao`) se comportam de maneira diferente dependendo da classe que os implementa ou herda.

---

## 🛠️ Como Executar o Projeto

Para rodar o sistema bancário em seu ambiente local, siga os passos abaixo:

1.  **Pré-requisitos:**
    * Python 3.x instalado em sua máquina.
    * Git (opcional, para clonar o repositório).

2.  **Clonar o Repositório (se ainda não fez):**
    ```bash
    git clone [https://github.com/andreibelotti/sistema_bancario_poo_python.git](https://github.com/andreibelotti/sistema_bancario_poo_python.git)
    # Ou o nome do seu novo repositório, se você mudou.
    ```
    ```bash
    cd sistema_bancario_poo_python
    ```

3.  **Executar o Script:**
    ```bash
    python seu_arquivo_principal.py
    # Substitua 'seu_arquivo_principal.py' pelo nome do seu arquivo, ex: Sistema_bancario_desafio.py
    ```

4.  **Interagindo com o Sistema:**
    Após executar o script, um menu será exibido no terminal. Você pode digitar as opções para interagir:
    * `[d]` Depositar
    * `[s]` Sacar
    * `[e]` Extrato
    * `[nc]` Nova conta
    * `[lc]` Listar contas
    * `[nu]` Novo usuário
    * `[q]` Sair

---

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum bug, sinta-se à vontade para:

1.  Abrir uma [Issue](link-para-suas-issues-no-github).
2.  Criar um [Pull Request](link-para-seus-pull-requests-no-github).

---


## ✨ Agradecimentos

Um agradecimento especial à [DIO](https://www.dio.me/) e ao Santander Academy pelo desafio de aprendizado e por fornecer a base conceitual para a construção deste sistema.
