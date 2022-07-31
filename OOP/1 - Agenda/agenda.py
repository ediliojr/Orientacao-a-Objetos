# Nesse exercícios vamos recriar a nossa agenda.
# Intruções:
# 1 - Crie uma classe Agenda, que receba um nome na inicialização Você deverá ter um atributo chamado contatos do tipo dicionário (Hash) para armazenar os contatos.
# 2 - Crie um método chamado adicionar_contato que receba dois parâmetros nome e telefone
# 3 - Crie outro método chamado remover_contato que receba como parâmetro o nome de um contato a ser removido



# TODO: Escreva seu código aqui

class Agenda():

  def __init__ (self):
    self.contatos = {}
   #definicao de tamanho, formato que o objeto terá

  def adicionar_contato(self,nome,numero):
    self.contatos[nome]=numero
  #comandar o que procurar no input
  def remover_contato(self,nome,numero):
    self.contatos.pop(nome)
  def exibir_contatos(self):
    for i,j in self.contatos.items():
      print(i ," ", j)
# Para testar:
agenda = Agenda()
print(agenda)

agenda.adicionar_contato("Tulio", "3333")
agenda.adicionar_contato("Ana", "1111")
agenda.adicionar_contato("Carol", "3334")

print(agenda.contatos)
print(agenda.exibir_contatos())
# agenda.exibir()
# agenda.remover_contato("Carol")
# agenda.exibir()
#Agenda.adicionar_contato("Carol", "3334")
#Agenda.adicionar_contato("Tulio", "3333")
#print(Agenda.dictionary)

