import socket;
from pathlib import Path;

HOST = '127.0.0.1';
PORT = 56899;

root = Path('users');
if not root.exists():
  root.mkdir();
  exemplo_1 = Path(root.joinpath('Aladin.txt'));
  exemplo_1.write_text('masculino,22');
  exemplo_2 = Path(root.joinpath('Kod.txt'));
  exemplo_2.write_text('masculino,10');
  exemplo_3 = Path(root.joinpath('Helena.txt'));
  exemplo_3.write_text('feminino,18');
  exemplo_4 = Path(root.joinpath('Jessica.txt'));
  exemplo_4.write_text('feminino,22');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, adrr = s.accept();
    with conn:
      nome = conn.recv(64).decode();
      
      for user in root.iterdir():
        if user.stem == nome:
          info = user.read_text();
          conn.sendall(info.encode());
          conn.close();
          break;
      else:
        conn.sendall(''.encode());
        conn.close()