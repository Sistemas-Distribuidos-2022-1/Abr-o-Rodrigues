import zmq;

ctx = zmq.Context();
socket = ctx.socket(zmq.SUB);
addr = "tcp://127.0.0.1:34065";
socket.connect(addr);
socket.setsockopt_string(zmq.SUBSCRIBE, "ex3");

n1, n2, n3 = list(map(float, socket.recv().decode().split(' ')[1].split(','))); 

media = (n1 + n2) / 2;
if media >= 7:
  resultado = 'Aprovado';
elif media >=3:
  mediaFinal = (media + n3) / 2;
  if mediaFinal >= 5:
    resultado = 'Aprovado';
  else:
    resultado = 'Reprovado';
else:
    resultado = 'Reprovado';

print(resultado);

  