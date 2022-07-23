import Pyro5.api;

@Pyro5.api.expose
class Funcionario:
  def __init__(self, nome, cargo, salário):
    self.nome = nome;
    self.cargo = cargo;
    self.salário = salário;

  def ajusta_salario(self):
    if self.cargo == 'operador':
      salário = float(self.salário) * 1.2;
    elif self.cargo == 'programador':
      salário = float(self.salário) * 1.18;

    return f"Salário do funcionário {self.nome} reajustado para R${salário}";


func1 = Funcionario("Ronaldo", "programador", 1000);

daemon = Pyro5.api.Daemon();
ns = Pyro5.api.locate_ns();
uri = daemon.register(func1);
ns.register('func1', uri);

daemon.requestLoop();
      