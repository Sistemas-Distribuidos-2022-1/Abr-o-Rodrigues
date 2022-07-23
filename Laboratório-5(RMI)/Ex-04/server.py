import Pyro5.api;

@Pyro5.api.expose
class Pessoa:
  def __init__(self, altura, sexo):
    self.sexo = sexo;
    self.altura = altura;

  def peso_ideal(self):
    if self.sexo == 'masculino':
      pesoIdeal = 72.7 * float(self.altura) - 58;
    else:
      pesoIdeal = 62.1 * float(self.altura) - 44.7;

    resposta = f'O peso ideal é {round(pesoIdeal, 2)}Kgs';

    return resposta;

pessoa1 = Pessoa(1.81, 'feminino');

daemon = Pyro5.api.Daemon();
ns = Pyro5.api.locate_ns();
uri = daemon.register(pessoa1);
ns.register('pessoa1', uri);

daemon.requestLoop();
      