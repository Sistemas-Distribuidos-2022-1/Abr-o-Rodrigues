import socket;
from pathlib import Path;

HOST = '127.0.0.1';
PORT = 56901;

root = Path('alunos');
if not root.exists():
  root.mkdir();
  exemplo_1 = Path(root.joinpath('Sergio.txt'));
  exemplo_1.write_text('9.3,9.4,0');
  exemplo_2 = Path(root.joinpath('Joao.txt'));
  exemplo_2.write_text('7,5,8.6');
  exemplo_3 = Path(root.joinpath('Paula.txt'));
  exemplo_3.write_text('5,4,5');

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT));
  s.listen();
  while True:
    conn, adrr = s.accept();
    with conn:
      nome = conn.recv(64).decode();
      
      for aluno in root.iterdir():
        if aluno.stem == nome:
          info = aluno.read_text();
          conn.sendall(info.encode());
          conn.close();
          break;
      else:
        conn.sendall(''.encode());
        conn.close()