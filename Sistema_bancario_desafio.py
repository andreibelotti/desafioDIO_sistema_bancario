import textwrap
import datetime # Para a data de nascimento
from abc import ABC, abstractmethod # Para classes abstratas

# --- CLASSE CLIENTE ---
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = [] # Uma lista para armazenar as contas do cliente

    def realizar_transacao(self, conta, transacao):
        # O método registrar da transação tenta executar a operação na conta.
        # Ele retorna True/False indicando sucesso.
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# --- CLASSE PESSOA FÍSICA (HERDA DE CLIENTE) ---
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco) # Chama o construtor da classe pai (Cliente)
        self._cpf = cpf # Atributo privado
        self._nome = nome
        self._data_nascimento = data_nascimento # Formato 'dd-mm-aaaa' ou objeto date

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento


# --- CLASSE HISTORICO ---
class Historico:
    def __init__(self):
        self._transacoes = [] # Lista privada para armazenar as transações

    def adicionar_transacao(self, transacao):
        # Adiciona os detalhes da transação ao histórico
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__, # Nome da classe (Deposito, Saque)
                "valor": transacao.valor,
                "data": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
    
    @property
    def transacoes(self):
        return self._transacoes

# --- CLASSE CONTA ---
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001" # Agência fixa
        self._cliente = cliente # Objeto Cliente
        self._historico = Historico() # Uma Conta tem um Histórico

    # Propriedades (getters) para acessar atributos privados
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    # Método de classe para criar uma nova conta (conforme UML)
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente) # Retorna uma instância da própria classe (Conta ou ContaCorrente)

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        else:
            self._saldo -= valor
            return True # Indica que o saque foi bem-sucedido
        return False # Indica que o saque falhou

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True # Indica que o depósito foi bem-sucedido
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False # Indica que o depósito falhou

# --- CLASSE CONTA CORRENTE (HERDA DE CONTA) ---
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente) # Chama o construtor da classe pai (Conta)
        self._limite = limite
        self._limite_saques = limite_saques
        self._numero_saques = 0 # Contador de saques para o limite diário

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques
    
    @property
    def numero_saques_realizados(self): # Adicionado para exibir quantos saques já foram feitos
        return self._numero_saques

    def sacar(self, valor):
        numero_saques = self._numero_saques
        limite = self._limite
        limite_saques = self._limite_saques

        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_limite:
            print(f"\n@@@ Operação falhou! O valor do saque excede o limite (R${limite:.2f}). @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques diários excedido. @@@")
        elif super().sacar(valor): # Chama o método sacar da classe pai (Conta)
            self._numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===") # Mensagem aqui após sucesso do super
            return True
        return False # Se o sacar da classe pai falhou, este também falha


# --- INTERFACE TRANSAÇÃO E CLASSES CONCRETAS ---

class Transacao(ABC): # ABC = Abstract Base Class
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            print("\n=== Depósito realizado com sucesso! ===") # Mensagem aqui após sucesso


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # O método sacar da ContaCorrente já printa as mensagens de erro/sucesso.
        # Apenas chamamos e adicionamos ao histórico se for bem-sucedido.
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


# --- FUNÇÕES AUXILIARES E MAIN (ADAPTADAS PARA POO) ---

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes): # Renomeado de filtrar_usuario para refletir a classe Cliente
    for cliente in clientes:
        # Verifica se o cliente é uma instância de PessoaFisica e se o CPF corresponde
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            return cliente
    return None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    
    # Permite ao usuário escolher a conta se houver múltiplas
    if len(cliente.contas) > 1:
        print("\nContas do Cliente:")
        for i, conta in enumerate(cliente.contas):
            print(f"{i+1}. Agência: {conta.agencia} - Conta: {conta.numero}")
        
        while True:
            try:
                escolha = int(input("Selecione o número da conta para operar: ")) - 1
                if 0 <= escolha < len(cliente.contas):
                    return cliente.contas[escolha]
                else:
                    print("@@@ Escolha inválida. Tente novamente. @@@")
            except ValueError:
                print("@@@ Entrada inválida. Digite um número. @@@")
    else:
        # Se tiver apenas uma conta, retorna-a diretamente
        return cliente.contas[0]


def main():
    clientes = []
    contas = [] # Esta lista vai guardar objetos ContaCorrente

    numero_conta_global = 1 # Para atribuir números de conta sequenciais

    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)

            if not cliente:
                print("\n@@@ Cliente não encontrado! @@@")
                continue

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                continue # O erro já foi impresso em recuperar_conta_cliente

            valor = input("Informe o valor do depósito: ")
            try:
                valor = float(valor)
                transacao = Deposito(valor) # Criar uma transação de Depósito
                cliente.realizar_transacao(conta, transacao) # O cliente realiza a transação
            except ValueError:
                print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)

            if not cliente:
                print("\n@@@ Cliente não encontrado! @@@")
                continue

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                continue # O erro já foi impresso em recuperar_conta_cliente

            valor = input("Informe o valor do saque: ")
            try:
                valor = float(valor)
                transacao = Saque(valor) # Criar uma transação de Saque
                cliente.realizar_transacao(conta, transacao) # O cliente realiza a transação
            except ValueError:
                print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
        elif opcao == "e":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)

            if not cliente:
                print("\n@@@ Cliente não encontrado! @@@")
                continue

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                continue # O erro já foi impresso em recuperar_conta_cliente
            
            # Exibir extrato da conta (agora é acessado pelo objeto conta.historico)
            print("\n================ EXTRATO ================")
            if not conta.historico.transacoes: # Acessa a lista de transações do histórico
                print("Não foram realizadas movimentações.")
            else:
                for transacao_info in conta.historico.transacoes: # Itera sobre os dicionários no histórico
                    print(f"{transacao_info['data']} - {transacao_info['tipo']}: R$ {transacao_info['valor']:.2f}")
            print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}") # Acessa o saldo via property
            print("==========================================")

        elif opcao == "nu":
            cpf = input("Informe o CPF (somente número): ")
            if filtrar_cliente(cpf, clientes): # Usa a função auxiliar para checar existência
                print("\n@@@ Já existe usuário com esse CPF! @@@")
                continue
            
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

            # Cria um objeto PessoaFisica
            cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
            clientes.append(cliente) # Adiciona o objeto cliente à lista
            print("\n=== Usuário criado com sucesso! ===")

        elif opcao == "nc":
            cpf = input("Informe o CPF do cliente para vincular a conta: ")
            cliente = filtrar_cliente(cpf, clientes) # Encontra o objeto cliente

            if not cliente:
                print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
                continue
            
            # Cria uma nova conta corrente como objeto
            nova_conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta_global)
            
            contas.append(nova_conta) # Adiciona o objeto conta à lista global de contas
            cliente.adicionar_conta(nova_conta) # Adiciona a conta à lista de contas do cliente
            numero_conta_global += 1
            print(f"\n=== Conta {nova_conta.agencia}-{nova_conta.numero} criada com sucesso! ===")

        elif opcao == "lc":
            if not contas: # Verifica se a lista de objetos contas está vazia
                print("\nNão há contas cadastradas.")
                continue
            
            print("\n================ LISTA DE CONTAS ================")
            for conta in contas: # Itera sobre os objetos ContaCorrente
                linha = f"""\
                    Agência:\t{conta.agencia}
                    C/C:\t\t{conta.numero}
                    Titular:\t{conta.cliente.nome}
                """
                print(textwrap.dedent(linha))
                print("-" * 50) # Linha divisória para melhor visualização
            print("===================================================")

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

# Garante que a função main() seja executada quando o script for rodado
if __name__ == "__main__":
    main()