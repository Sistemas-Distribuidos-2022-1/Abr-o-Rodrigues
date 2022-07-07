import socket;

HOST = '127.0.0.1';
PORT = 56901;

altura = input('Insira a altura: ');
sexo = input('Insira o sexo: ');


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = f'{altura},{sexo}'.encode();
  st.sendall(msg);
  resposta = st.recv(1024).decode();
  print(resposta);