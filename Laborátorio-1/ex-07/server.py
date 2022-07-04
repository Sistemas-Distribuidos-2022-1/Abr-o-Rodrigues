import socket;

HOST = '127.0.0.1';
PORT = 56904;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, addr = s.accept();
    with conn:
      print(f'Conectado com {addr}');

      idade, tempo = conn.recv(1024).decode().split(','); 

      if idade >= 65 and tempo >= 30:
        resposta = 'Pode se aposentar';
      elif 60 <= idade < 65 and tempo >= 25:
        resposta = 'Pode se aposentar';
      else:
        resposta = 'Não pode se aposentar'

      conn.sendall(resposta.encode());
      conn.close();