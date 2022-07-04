import socket;

HOST = '127.0.0.1';
PORT = 56903;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, addr = s.accept();
    with conn:
      print(f'Conectado com {addr}');

      nome, nível, salário, dependentes = conn.recv(1024).decode().split(','); 

      if nível == 'A':
        if int(dependentes) == 0:
          salárioFinal = float(salário) * 0.97;
        else:
          salárioFinal = float(salário) * 0.92;
      if nível == 'B':
        if int(dependentes) == 0:
          salárioFinal = float(salário) * 0.95;
        else:
          salárioFinal = float(salário) * 0.90;
      if nível == 'C':
        if int(dependentes) == 0:
          salárioFinal = float(salário) * 0.92;
        else:
          salárioFinal = float(salário) * 0.85;
      if nível == 'D':
        if int(dependentes) == 0:
          salárioFinal = float(salário) * 0.90;
        else:
          salárioFinal = float(salário) * 0.83;

      resposta = f'Funcionário {nome} de nível {nível} --> Salário líquido = R${round(salárioFinal, 2)}';
      conn.sendall(resposta.encode());
      conn.close();