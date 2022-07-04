import socket;

HOST = '127.0.0.1';
PORT = 56901;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, addr = s.accept();
    with conn:
      print(f'Conectado com {addr}');

      altura, sexo = conn.recv(1024).decode().split(','); 

      if sexo == 'masculino':
        pesoIdeal = 72.7 * float(altura) - 58;
      else:
        pesoIdeal = 62.1 * float(altura) - 44.7;

      resposta = f'O peso ideal é {round(pesoIdeal, 2)}';

      conn.sendall(resposta.encode());
      conn.close();