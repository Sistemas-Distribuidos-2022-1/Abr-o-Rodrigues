import socket;
from pathlib import Path;

HOST = '127.0.0.1';
PORT = 56911;

root = Path('clientes');
if not root.exists():
  root.mkdir();
  exemplo_1 = Path(root.joinpath('Carlos.txt'));
  exemplo_1.write_text('150');
  exemplo_2 = Path(root.joinpath('Claudia.txt'));
  exemplo_2.write_text('250');
  exemplo_3 = Path(root.joinpath('Joao.txt'));
  exemplo_3.write_text('350');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, adrr = s.accept();
    with conn:
      nome = conn.recv(64).decode();
      
      for cliente in root.iterdir():
        if cliente.stem == nome:
          info = cliente.read_text();
          conn.sendall(info.encode());
          conn.close();
          break;
      else:
        conn.sendall(''.encode());
        conn.close()