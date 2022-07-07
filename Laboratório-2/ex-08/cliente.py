import socket;

HOST = '127.0.0.1';
PORT = 56905;

saldoMedio = input('Insira o saldo médio: ');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = saldoMedio.encode();
  st.sendall(msg);
  resposta = st.recv(1024).decode();
  print(resposta);