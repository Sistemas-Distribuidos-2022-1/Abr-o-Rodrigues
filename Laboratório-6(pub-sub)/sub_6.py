import zmq;

ctx = zmq.Context();
socket = ctx.socket(zmq.SUB);
addr = "tcp://127.0.0.1:34065";
socket.connect(addr);
socket.setsockopt_string(zmq.SUBSCRIBE, "ex6");

nome, nível, salário, dependentes = socket.recv().decode().split(' ')[1].split(','); 

if nível == 'A':
  if int(dependentes) == 0:
    salárioFinal = float(salário) * 0.97;
  else:
    salárioFinal = float(salário) * 0.92;
if nível == 'B':
  if int(dependentes) == 0:
    salárioFinal = float(salário) * 0.95;
  else:
    salárioFinal = float(salário) * 0.90;
if nível == 'C':
  if int(dependentes) == 0:
    salárioFinal = float(salário) * 0.92;
  else:
    salárioFinal = float(salário) * 0.85;
if nível == 'D':
  if int(dependentes) == 0:
    salárioFinal = float(salário) * 0.90;
  else:
    salárioFinal = float(salário) * 0.83;

resposta = f'Funcionário {nome} de nível {nível} --> Salário líquido = R${round(salárioFinal, 2)}';

print(resposta);

  