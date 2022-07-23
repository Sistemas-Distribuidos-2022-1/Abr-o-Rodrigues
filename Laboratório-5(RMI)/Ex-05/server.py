import Pyro5.api;

@Pyro5.api.expose
class Nadador:
  def __init__(self, idade):
    self.idade = idade;

  def get_classificação(self):
    if self.idade >= 18:
      classificação = 'adulto';
      resposta = f'Nadador com classificação {classificação}';
    elif self.idade >= 14:
      classificação = 'juvenil B';
      resposta = f'Nadador com classificação {classificação}';
    elif self.idade >= 11:
      classificação = 'juvenil A';
      resposta = f'Nadador com classificação {classificação}';
    elif self.idade >= 8:
      classificação = 'infantil B';
      resposta = f'Nadador com classificação {classificação}';
    elif self.idade >= 5:
      classificação = 'infantil A';
      resposta = f'Nadador com classificação {classificação}';
    else:
      resposta = 'Idade muito baixa';

    return resposta;

nadador1 = Nadador(12);

daemon = Pyro5.api.Daemon();
ns = Pyro5.api.locate_ns();
uri = daemon.register(nadador1);
ns.register('nadador1', uri);

daemon.requestLoop();
      