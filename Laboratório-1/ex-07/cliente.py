import socket;

HOST = '127.0.0.1';
PORT = 56904;

idade = input('Insira a idade: ');
tempo = input('Insira o tempo de serviço: ');


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = f'{idade},{tempo}'.encode();
  st.sendall(msg);
  resposta = st.recv(1024).decode();
  print(resposta);