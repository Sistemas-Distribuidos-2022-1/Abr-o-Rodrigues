import socket;

HOST = '127.0.0.1';
PORT = 56903;

nome = input('Insira o nome: ');
nível = input('Insira o nível: ');
salário = input('Insira o salário: ');
nd = input('Insira o número de dependentes: ');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = f'{nome},{nível},{salário},{nd}'.encode();
  st.sendall(msg);
  resposta = st.recv(1024).decode();
  print(resposta);