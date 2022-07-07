import socket;

HOST = '127.0.0.1';
PORT = 56898;

nome = input('Insira o nome: ');
sexo = input('Insira o sexo: ');
idade = input('Insira o idade: ');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = f'{nome},{sexo},{idade}'.encode();
  st.sendall(msg);
  maioridade = st.recv(1024).decode();
  print(maioridade);