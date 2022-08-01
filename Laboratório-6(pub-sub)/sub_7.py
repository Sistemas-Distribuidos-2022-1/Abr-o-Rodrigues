import zmq;

ctx = zmq.Context();
socket = ctx.socket(zmq.SUB);
addr = "tcp://127.0.0.1:34065";
socket.connect(addr);
socket.setsockopt_string(zmq.SUBSCRIBE, "ex7");

idade, tempo = socket.recv().decode().split(' ')[1].split(','); 

if idade >= 65 and tempo >= 30:
  resposta = 'Pode se aposentar';
elif 60 <= idade < 65 and tempo >= 25:
  resposta = 'Pode se aposentar';
else:
  resposta = 'Não pode se aposentar'

print(resposta);

  