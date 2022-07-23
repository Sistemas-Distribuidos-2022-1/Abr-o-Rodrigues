from xmlrpc.server import SimpleXMLRPCServer

def calcula_salario(nome, cargo, salário): 
  if cargo == 'operador':
    salário = float(salário) * 1.2;
  elif cargo == 'programador':
    salário = float(salário) * 1.18;

  return f"Salário do funcionário {nome} reajustado para R${salário}";
      

HOST = "localhost";
PORT = 32002;

server = SimpleXMLRPCServer((HOST, PORT));
server.register_function(calcula_salario, "calcula_salario");
server.serve_forever();