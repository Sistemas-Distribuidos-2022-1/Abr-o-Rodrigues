import socket;

HOST = '127.0.0.1';
PORT = 56902;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, addr = s.accept();
    with conn:
      print(f'Conectado com {addr}');

      idade = int(conn.recv(1024).decode()); 

      if idade >= 18:
        classificação = 'adulto';
        resposta = f'Nadador com classificação {classificação}';
      elif idade >= 14:
        classificação = 'juvenil B';
        resposta = f'Nadador com classificação {classificação}';
      elif idade >= 11:
        classificação = 'juvenil A';
        resposta = f'Nadador com classificação {classificação}';
      elif idade >= 8:
        classificação = 'infantil B';
        resposta = f'Nadador com classificação {classificação}';
      elif idade >= 5:
        classificação = 'infantil A';
        resposta = f'Nadador com classificação {classificação}';
      else:
        resposta = 'Idade muito baixa';
      

      conn.sendall(resposta.encode());
      conn.close();