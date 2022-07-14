import socket;

HOST = '127.0.0.1';
PORT = 56908;

nome = input('Insira o nome do funcionário: ');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = nome.encode();
  st.sendall(msg);
  resposta = st.recv(1024).decode();
  print(resposta);