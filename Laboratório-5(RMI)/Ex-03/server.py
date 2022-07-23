import Pyro5.api;

@Pyro5.api.expose
class Aluno:
  def __init__(self, n1, n2, n3):
    self.n1 = n1;
    self.n2 = n2;
    self.n3 = n3;

  def resultado_final(self):
    media = (self.n1 + self.n2) / 2;
    if media >= 7:
      resultado = 'Aprovado';
    elif media >=3:
      mediaFinal = (media + self.n3) / 2;
      if mediaFinal >= 5:
        resultado = 'Aprovado';
      else:
        resultado = 'Reprovado';
    else:
        resultado = 'Reprovado';

    return resultado;

aluno1 = Aluno(6, 7, 8);

daemon = Pyro5.api.Daemon();
ns = Pyro5.api.locate_ns();
uri = daemon.register(aluno1);
ns.register('aluno1', uri);

daemon.requestLoop();
      