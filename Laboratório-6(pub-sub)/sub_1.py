import zmq;

ctx = zmq.Context();
socket = ctx.socket(zmq.SUB);
addr = "tcp://127.0.0.1:34065";
socket.connect(addr);
socket.setsockopt_string(zmq.SUBSCRIBE, "ex1");

nome, cargo, salário = socket.recv().decode().split(' ')[1].split(','); 

if cargo == 'operador':
  salário = float(salário) * 1.2;
elif cargo == 'programador':
  salário = float(salário) * 1.18;

print(f'{nome},{salário}');
  