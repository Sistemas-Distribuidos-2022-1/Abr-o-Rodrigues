import socket;
from pathlib import Path;

HOST = '127.0.0.1';
PORT = 56905;

root = Path('nadadores');
if not root.exists():
  root.mkdir();
  exemplo_1 = Path(root.joinpath('Carlos.txt'));
  exemplo_1.write_text('10');
  exemplo_2 = Path(root.joinpath('Claudia.txt'));
  exemplo_2.write_text('15');
  exemplo_3 = Path(root.joinpath('Austin.txt'));
  exemplo_3.write_text('22');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, adrr = s.accept();
    with conn:
      nome = conn.recv(64).decode();
      
      for nadador in root.iterdir():
        if nadador.stem == nome:
          info = nadador.read_text();
          conn.sendall(info.encode());
          conn.close();
          break;
      else:
        conn.sendall(''.encode());
        conn.close()