import Pyro5.api;

@Pyro5.api.expose
class Funcionario:
  def __init__(self, idade, tempo_servico):
    self.idade = idade;
    self.tempo_servico = tempo_servico;

  def pode_aposentar(self):
    if self.idade >= 65 and self.tempo_servico >= 30:
      resposta = 'Pode se aposentar';
    elif 60 <= self.idade < 65 and self.tempo_servico >= 25:
      resposta = 'Pode se aposentar';
    else:
      resposta = 'Não pode se aposentar';

    return resposta;

func1 = Funcionario(65, 41);

daemon = Pyro5.api.Daemon();
ns = Pyro5.api.locate_ns();
uri = daemon.register(func1);
ns.register('func1', uri);

daemon.requestLoop();
      