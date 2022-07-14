import socket;
from pathlib import Path;

HOST = '127.0.0.1';
PORT = 56903;

root = Path('pessoas');
if not root.exists():
  root.mkdir();
  exemplo_1 = Path(root.joinpath('Carlos.txt'));
  exemplo_1.write_text('1.82,masculino');
  exemplo_2 = Path(root.joinpath('Claudia.txt'));
  exemplo_2.write_text('1.65,feminino');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, adrr = s.accept();
    with conn:
      nome = conn.recv(64).decode();
      
      for pessoa in root.iterdir():
        if pessoa.stem == nome:
          info = pessoa.read_text();
          conn.sendall(info.encode());
          conn.close();
          break;
      else:
        conn.sendall(''.encode());
        conn.close()