import socket;

HOST = '127.0.0.1';
PORT = 56900;

n1 = input('Insira a nota da prova 1: ');
n2 = input('Insira a nota da prova 2: ');
n3 = input('Insira a nota da prova 3: ');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = f'{n1},{n2},{n3}'.encode();
  st.sendall(msg);
  resultado = st.recv(1024).decode();
  print(resultado);