from xmlrpc.client import ServerProxy;

HOST = "localhost";
PORT = "32002";

with ServerProxy(f"http://{HOST}:{PORT}") as proxy:
  print(proxy.calcula_salario("Sanders", "programador", "100"));