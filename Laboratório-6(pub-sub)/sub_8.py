import zmq;

ctx = zmq.Context();
socket = ctx.socket(zmq.SUB);
addr = "tcp://127.0.0.1:34065";
socket.connect(addr);
socket.setsockopt_string(zmq.SUBSCRIBE, "ex8");

saldoMédio = float(socket.recv().decode().split(' ')[1]); 

if saldoMédio >= 601:
  resposta = f'Saldo médio de R${saldoMédio} possui um valor de crédito de R${round(0.4 * saldoMédio, 2)}';
elif saldoMédio >= 401:
  resposta = f'Saldo médio de R${saldoMédio} possui um valor de crédito de R${round(0.3 * saldoMédio, 2)}';
elif saldoMédio >= 201:
  resposta = f'Saldo médio de R${saldoMédio} possui um valor de crédito de R${round(0.2 * saldoMédio, 2)}';
else:
  resposta = f'Saldo médio de R${saldoMédio} não possui nenhum crédito';

print(resposta);

  