import socket;

HOST = '127.0.0.1';
PORT = 56900;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, addr = s.accept();
    with conn:
      print(f'Conectado com {addr}');

      n1, n2, n3 = list(map(float, conn.recv(1024).decode().split(','))); 

      media = (n1 + n2) / 2;
      if media >= 7:
        resultado = 'Aprovado';
      elif media >=3:
        mediaFinal = (media + n3) / 2;
        if mediaFinal >= 5:
          resultado = 'Aprovado';
        else:
          resultado = 'Reprovado';
      else:
          resultado = 'Reprovado';

      conn.sendall(resultado.encode());
      conn.close();