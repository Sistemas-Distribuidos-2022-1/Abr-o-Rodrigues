import time;
import zmq;

ctx = zmq.Context();
socket = ctx.socket(zmq.PUB);
addr = "tcp://127.0.0.1:34065";
socket.bind(addr);

while True:
  time.sleep(2);
  socket.send_string("ex1 " + "Sergio,programador,1000");

  time.sleep(2);
  socket.send_string("ex2 " + "Carlos,masculino,25");

  time.sleep(2);
  socket.send_string("ex3 " + "8,5,10");

  time.sleep(2);
  socket.send_string("ex4 " + "feminino,1.76");

  time.sleep(2);
  socket.send_string("ex5 " + "13");

  time.sleep(2);
  socket.send_string("ex6 " + "Marta,A,1453,5");

  time.sleep(2);
  socket.send_string("ex7 " + "45,20");

  time.sleep(2);
  socket.send_string("ex8 " + "400");