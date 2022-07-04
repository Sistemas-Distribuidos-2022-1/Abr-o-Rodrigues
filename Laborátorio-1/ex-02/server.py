import socket;

HOST = '127.0.0.1';
PORT = 56898;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, addr = s.accept();
    with conn:
      print(f'Conectado com {addr}');

      nome, sexo, idade = conn.recv(1024).decode().split(','); 

      if sexo == 'masculino' :
        if int(idade) >= 18:
          maioridade = 'Já atingiu a maioridade';
        else :
          maioridade = 'Não atingiu a maioridade';

      if sexo == 'feminino' :
        if int(idade) >= 21:
          maioridade = 'Já atingiu a maioridade';
        else :
          maioridade = 'Não atingiu a maioridade';

      conn.sendall(maioridade.encode());
      conn.close();