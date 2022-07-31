from agenda import Agenda

def test_agenda():
  agenda = Agenda()
  agenda.adicionar_contato("Jonas", "3333-3333")
  agenda.adicionar_contato("Thiago", "3334-3334")
  agenda.adicionar_contato("Maria", "1111-1111")
  agenda.exibir()
  agenda.remover_contato("Thiago")
  agenda.exibir()

  assert len(agenda.contatos) == 2
