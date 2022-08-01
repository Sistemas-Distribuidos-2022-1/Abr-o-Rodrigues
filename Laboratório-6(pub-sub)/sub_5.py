import zmq;

ctx = zmq.Context();
socket = ctx.socket(zmq.SUB);
addr = "tcp://127.0.0.1:34065";
socket.connect(addr);
socket.setsockopt_string(zmq.SUBSCRIBE, "ex5");

idade = int(socket.recv().decode().split(' ')[1]); 

if idade >= 18:
  classificação = 'adulto';
  resposta = f'Nadador com classificação {classificação}';
elif idade >= 14:
  classificação = 'juvenil B';
  resposta = f'Nadador com classificação {classificação}';
elif idade >= 11:
  classificação = 'juvenil A';
  resposta = f'Nadador com classificação {classificação}';
elif idade >= 8:
  classificação = 'infantil B';
  resposta = f'Nadador com classificação {classificação}';
elif idade >= 5:
  classificação = 'infantil A';
  resposta = f'Nadador com classificação {classificação}';
else:
  resposta = 'Idade muito baixa';

print(resposta);

  