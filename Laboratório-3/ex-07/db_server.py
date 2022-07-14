import socket;
from pathlib import Path;

HOST = '127.0.0.1';
PORT = 56909;

root = Path('funcionários');
if not root.exists():
  root.mkdir();
  exemplo_1 = Path(root.joinpath('Carlos.txt'));
  exemplo_1.write_text('50,20');
  exemplo_2 = Path(root.joinpath('Claudia.txt'));
  exemplo_2.write_text('67,34');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, adrr = s.accept();
    with conn:
      nome = conn.recv(64).decode();
      
      for funcionário in root.iterdir():
        if funcionário.stem == nome:
          info = funcionário.read_text();
          conn.sendall(info.encode());
          conn.close();
          break;
      else:
        conn.sendall(''.encode());
        conn.close()