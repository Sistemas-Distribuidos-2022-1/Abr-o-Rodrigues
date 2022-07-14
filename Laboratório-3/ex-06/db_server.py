import socket;
from pathlib import Path;

HOST = '127.0.0.1';
PORT = 56907;

root = Path('funcionários');
if not root.exists():
  root.mkdir();
  exemplo_1 = Path(root.joinpath('Carlos.txt'));
  exemplo_1.write_text('A,667,10');
  exemplo_2 = Path(root.joinpath('Claudia.txt'));
  exemplo_2.write_text('B,1200,0');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, adrr = s.accept();
    with conn:
      nome = conn.recv(64).decode();
      
      for funcionario in root.iterdir():
        if funcionario.stem == nome:
          info = funcionario.read_text();
          conn.sendall(info.encode());
          conn.close();
          break;
      else:
        conn.sendall(''.encode());
        conn.close()