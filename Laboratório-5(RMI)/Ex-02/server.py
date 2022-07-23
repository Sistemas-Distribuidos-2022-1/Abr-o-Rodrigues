import Pyro5.api;

@Pyro5.api.expose
class Pessoa:
  def __init__(self, nome, sexo, idade):
    self.nome = nome;
    self.sexo = sexo;
    self.idade = idade;

  def maioridade(self):
    if self.sexo == 'masculino' :
      if int(self.idade) >= 18:
        maioridade = 'já atingiu a maioridade';
      else :
        maioridade = 'não atingiu a maioridade';

    if self.sexo == 'feminino' :
      if int(self.idade) >= 21:
        maioridade = 'já atingiu a maioridade';
      else :
        maioridade = 'não atingiu a maioridade';

    return f"{self.nome} {maioridade}";


pessoa1 = Pessoa("Ronaldo", "masculino", 22);

daemon = Pyro5.api.Daemon();
ns = Pyro5.api.locate_ns();
uri = daemon.register(pessoa1);
ns.register('pessoa1', uri);

daemon.requestLoop();
      