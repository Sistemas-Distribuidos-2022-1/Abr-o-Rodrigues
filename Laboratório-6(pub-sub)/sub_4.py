import zmq;

ctx = zmq.Context();
socket = ctx.socket(zmq.SUB);
addr = "tcp://127.0.0.1:34065";
socket.connect(addr);
socket.setsockopt_string(zmq.SUBSCRIBE, "ex4");

altura, sexo = socket.recv().decode().split(' ')[1].split(','); 

if sexo == 'masculino':
  pesoIdeal = 72.7 * float(altura) - 58;
else:
  pesoIdeal = 62.1 * float(altura) - 44.7;

resposta = f'O peso ideal é {round(pesoIdeal, 2)}';

print(resposta);

  