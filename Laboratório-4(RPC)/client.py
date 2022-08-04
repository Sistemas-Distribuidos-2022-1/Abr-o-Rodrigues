from xmlrpc.client import ServerProxy;

HOST = "localhost";
PORT = "32002";

with ServerProxy(f"http://{HOST}:{PORT}") as proxy:
  print(proxy.calcula_salario("Sanders", "programador", "100"));
  print(proxy.maioridade("Sanders", "masculino", "25"));
  print(proxy.resultado_final(7,3,10));
  print(proxy.peso_ideal(1.83, "masculino"));
  print(proxy.classifica_nadador(12));
  print(proxy.salario_final("Sanders", "A", 1000, 3));
  print(proxy.aposentadoria(60, 40));
  print(proxy.calcula_credito(300));