import socket;

HOST = '127.0.0.1';
PORT = 56902;

idade = input('Insira a idade do nadador: ');



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = idade.encode();
  st.sendall(msg);
  resposta = st.recv(1024).decode();
  print(resposta);