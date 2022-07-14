import socket;

HOST = '127.0.0.1';
PORT = 56898;

nome = input('Insira o nome: ');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = nome.encode();
  st.sendall(msg);
  maioridade = st.recv(1024).decode();
  print(maioridade);