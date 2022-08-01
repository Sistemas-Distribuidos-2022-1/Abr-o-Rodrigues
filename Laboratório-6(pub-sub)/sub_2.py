import zmq;

ctx = zmq.Context();
socket = ctx.socket(zmq.SUB);
addr = "tcp://127.0.0.1:34065";
socket.connect(addr);
socket.setsockopt_string(zmq.SUBSCRIBE, "ex2");

nome, sexo, idade = socket.recv().decode().split(' ')[1].split(','); 

if sexo == 'masculino' :
  if int(idade) >= 18:
    maioridade = 'Já atingiu a maioridade';
  else :
    maioridade = 'Não atingiu a maioridade';

if sexo == 'feminino' :
  if int(idade) >= 21:
    maioridade = 'Já atingiu a maioridade';
  else :
    maioridade = 'Não atingiu a maioridade';

print(maioridade);

  