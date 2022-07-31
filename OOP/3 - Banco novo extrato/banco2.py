# Você deve copiar o seu código do Exercício anterior e realizar algumas modificações.
# Agora no método extrato deverá retornar as operações:
# Exemplo:
#
# conta=Conta("Yasmin", 1, 100)
# conta.saque(50)
# conta.deposito(40)
# conta.saque(9)
# conta.extrato()
# O método extrato() deverá retornar uma extrato bancário (Você deve retornar frases exatamentes como essas, até com os mesmos espaços):
# Operação: Saque    | Valor: R$ 50
# Operação: Depósito | Valor: R$ 40
# Operação: Saque    | Valor: R$ 9
# Saldo Final: R$ 81

# Faça as modificações necessárias nos outros métodos para contemplar o novo extrato.

class conta():
  contas={}
  def __init__(self, nome_cliente, numero_conta, saldo):
    self.nome_cliente=nome_cliente
    self.numero_conta=numero_conta
    self.saldo=saldo


  def extrato(self):
    i=self.contas[self.numero_conta]
    if i <0:
      print("operação: Saque  |  Valor:",i)
      return  "operação: Saque  |  Valor:",self.contas.keys()
    elif i >0:
      print("operação: Deposito  |  Valor:",i)
      return  "operação: Deposito  |  Valor:",self.contas.keys()
  def saque(self,numero_conta,valor):

    self.lista= - valor
    self.saldo=self.saldo - valor
    self.contas[numero_conta]=(-valor)

    print(self.contas)
  def deposito(self,numero_conta,valor):

    self.lista=valor
    self.saldo=self.saldo + valor
    self.contas[numero_conta]=valor



conta1=conta("Yasmin", 1, 100)
conta2=conta("Joana", 2, 200)
conta1.saque(1, 100)
print(conta1.saldo)
conta2.deposito(2, 150)
print(conta2.saldo)
conta1.deposito(1, 150)
conta1.extrato()
conta2.extrato()
print(conta.contas)

