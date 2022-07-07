import socket;

HOST = '127.0.0.1';
PORT = 56905;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, addr = s.accept();
    with conn:
      print(f'Conectado com {addr}');

      saldoMédio = float(conn.recv(1024).decode()); 

      if saldoMédio >= 601:
        resposta = f'Saldo médio de R${saldoMédio} possui um valor de crédito de R${round(0.4 * saldoMédio, 2)}';
      elif saldoMédio >= 401:
        resposta = f'Saldo médio de R${saldoMédio} possui um valor de crédito de R${round(0.3 * saldoMédio, 2)}';
      elif saldoMédio >= 201:
        resposta = f'Saldo médio de R${saldoMédio} possui um valor de crédito de R${round(0.2 * saldoMédio, 2)}';
      else:
        resposta = f'Saldo médio de R${saldoMédio} não possui nenhum crédito';

      conn.sendall(resposta.encode());
      conn.close();