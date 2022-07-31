from banco import Conta

def test_conta():
  conta1=Conta("Yasmin", 1, 100)
  conta2=Conta("Joana", 2, 200)
  conta1.saque(50)
  conta2.deposito(50)
  conta1.saque(10.15)
  conta2.deposito(40)
  conta2.deposito(1000)
  conta1.saque(9)
  conta2.deposito(45.50)
  conta2.saque(250)
  conta2.saque(2500)
  assert conta1.saldo == 30.85
  assert conta2.saldo == 1085.5
