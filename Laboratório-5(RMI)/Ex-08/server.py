import Pyro5.api;

@Pyro5.api.expose
class Cliente:
  def __init__(self, saldo_medio):
    self.saldo_medio = saldo_medio;

  def get_valor_credito(self):
    if self.saldo_medio >= 601:
      resposta = f'Saldo médio de R${self.saldo_medio} possui um valor de crédito de R${round(0.4 * self.saldo_medio, 2)}';
    elif self.saldo_medio >= 401:
      resposta = f'Saldo médio de R${self.saldo_medio} possui um valor de crédito de R${round(0.3 * self.saldo_medio, 2)}';
    elif self.saldo_medio >= 201:
      resposta = f'Saldo médio de R${self.saldo_medio} possui um valor de crédito de R${round(0.2 * self.saldo_medio, 2)}';
    else:
      resposta = f'Saldo médio de R${self.saldo_medio} não possui nenhum crédito';
    
    return resposta;

cliente1 = Cliente(267);

daemon = Pyro5.api.Daemon();
ns = Pyro5.api.locate_ns();
uri = daemon.register(cliente1);
ns.register('cliente1', uri);

daemon.requestLoop();
      