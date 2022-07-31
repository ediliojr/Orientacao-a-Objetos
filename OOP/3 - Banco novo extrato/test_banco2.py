from banco2 import Conta

def test_conta(capfd):
  conta=Conta("Yasmin", 1, 100)
  conta.saque(50)
  conta.deposito(40)
  conta.saque(9)
  assert conta.saldo == 81
  expected_response = "Operação: Saque    | Valor: R$ 50\nOperação: Depósito | Valor: R$ 40\nOperação: Saque    | Valor: R$ 9\nSaldo Final: R$ 81\n"
  conta.extrato()
  out, err = capfd.readouterr()
  assert out == expected_response
