import socket;

HOST = '127.0.0.1';
PORT = 56895;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, addr = s.accept();
    with conn:
      print(f'Conectado com {addr}');

      nome, cargo, salário = conn.recv(1024).decode().split(','); 

      if cargo == 'operador':
        salário = float(salário) * 1.2;
      elif cargo == 'programador':
        salário = float(salário) * 1.18;

      conn.sendall(f'{nome},{salário}'.encode());
      conn.close();