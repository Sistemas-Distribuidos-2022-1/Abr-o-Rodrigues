import Pyro5.api;

@Pyro5.api.expose
class Funcionario:
  def __init__(self, nome, nível, salário, dependentes):
    self.nome = nome;
    self.nível = nível;
    self.salário = salário;
    self.dependentes = dependentes;

  def get_salario_liquido(self):
    if self.nível == 'A':
      if int(self.dependentes) == 0:
        salárioFinal = float(self.salário) * 0.97;
      else:
        salárioFinal = float(self.salário) * 0.92;
    if self.nível == 'B':
      if int(self.dependentes) == 0:
        salárioFinal = float(self.salário) * 0.95;
      else:
        salárioFinal = float(self.salário) * 0.90;
    if self.nível == 'C':
      if int(self.dependentes) == 0:
        salárioFinal = float(self.salário) * 0.92;
      else:
        salárioFinal = float(self.salário) * 0.85;
    if self.nível == 'D':
      if int(self.dependentes) == 0:
        salárioFinal = float(self.salário) * 0.90;
      else:
        salárioFinal = float(self.salário) * 0.83;

    return f'Funcionário {self.nome} de nível {self.nível} --> Salário líquido = R${round(salárioFinal, 2)}';


func1 = Funcionario("Ronaldo", "B", 1000, 4);

daemon = Pyro5.api.Daemon();
ns = Pyro5.api.locate_ns();
uri = daemon.register(func1);
ns.register('func1', uri);

daemon.requestLoop();
      