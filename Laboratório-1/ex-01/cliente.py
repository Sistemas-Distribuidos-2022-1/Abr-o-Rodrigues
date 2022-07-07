import socket;

HOST = '127.0.0.1';
PORT = 56895;

nome = input("Insira o nome do funcionário: ");
cargo = input("Insira o cargo do funcionário: ");
salário = input("Insira o salário do funcionário: ");

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as st:
  st.connect((HOST, PORT));
  msg = f'{nome},{cargo},{salário}'.encode();
  st.sendall(msg);
  nomeRetornado, salárioNovo = st.recv(1024).decode().split(',');
  print(f"Salário do funcionário {nomeRetornado} reajustado para R${salárioNovo}");