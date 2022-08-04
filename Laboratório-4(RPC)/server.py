import re
from xmlrpc.server import SimpleXMLRPCServer

def calcula_salario(nome, cargo, salário): 
  if cargo == 'operador':
    salário = float(salário) * 1.2;
  elif cargo == 'programador':
    salário = float(salário) * 1.18;

  return f"Salário do funcionário {nome} reajustado para R${salário}";
      
def maioridade(nome, sexo, idade):
  if sexo == 'masculino' :
    if int(idade) >= 18:
      maioridade = nome + ' já atingiu a maioridade';
    else :
      maioridade = nome + ' não atingiu a maioridade';

  if sexo == 'feminino' :
    if int(idade) >= 21:
      maioridade = nome + ' já atingiu a maioridade';
    else :
      maioridade = nome + ' não atingiu a maioridade';

  return maioridade;

def resultado_final(n1, n2, n3):
  media = (n1 + n2) / 2;
  
  if media >= 7:
    resultado = 'Aprovado';
  elif media >=3:
    mediaFinal = (media + n3) / 2;
    if mediaFinal >= 5:
      resultado = 'Aprovado';
    else:
      resultado = 'Reprovado';
  else:
      resultado = 'Reprovado';

  return resultado;

def peso_ideal(altura, sexo):
  if sexo == 'masculino':
    pesoIdeal = 72.7 * float(altura) - 58;
  else:
    pesoIdeal = 62.1 * float(altura) - 44.7;

  resposta = f'O peso ideal é {round(pesoIdeal, 2)}';

  return resposta;

def classifica_nadador(idade):
  if idade >= 18:
    classificação = 'adulto';
    resposta = f'Nadador com classificação {classificação}';
  elif idade >= 14:
    classificação = 'juvenil B';
    resposta = f'Nadador com classificação {classificação}';
  elif idade >= 11:
    classificação = 'juvenil A';
    resposta = f'Nadador com classificação {classificação}';
  elif idade >= 8:
    classificação = 'infantil B';
    resposta = f'Nadador com classificação {classificação}';
  elif idade >= 5:
    classificação = 'infantil A';
    resposta = f'Nadador com classificação {classificação}';
  else:
    resposta = 'Idade muito baixa';

  return resposta;

def salario_final(nome, nível, salário, dependentes):
  if nível == 'A':
    if int(dependentes) == 0:
      salárioFinal = float(salário) * 0.97;
    else:
      salárioFinal = float(salário) * 0.92;
  if nível == 'B':
    if int(dependentes) == 0:
      salárioFinal = float(salário) * 0.95;
    else:
      salárioFinal = float(salário) * 0.90;
  if nível == 'C':
    if int(dependentes) == 0:
      salárioFinal = float(salário) * 0.92;
    else:
      salárioFinal = float(salário) * 0.85;
  if nível == 'D':
    if int(dependentes) == 0:
      salárioFinal = float(salário) * 0.90;
    else:
      salárioFinal = float(salário) * 0.83;

  resposta = f'Funcionário {nome} de nível {nível} --> Salário líquido = R${round(salárioFinal, 2)}';

  return resposta;

def aposentadoria(idade, tempo):
  if idade >= 65 and tempo >= 30:
    resposta = 'Pode se aposentar';
  elif 60 <= idade < 65 and tempo >= 25:
    resposta = 'Pode se aposentar';
  else:
    resposta = 'Não pode se aposentar';

  return resposta;

def calcula_credito(saldoMédio):
  if saldoMédio >= 601:
    resposta = f'Saldo médio de R${saldoMédio} possui um valor de crédito de R${round(0.4 * saldoMédio, 2)}';
  elif saldoMédio >= 401:
    resposta = f'Saldo médio de R${saldoMédio} possui um valor de crédito de R${round(0.3 * saldoMédio, 2)}';
  elif saldoMédio >= 201:
    resposta = f'Saldo médio de R${saldoMédio} possui um valor de crédito de R${round(0.2 * saldoMédio, 2)}';
  else:
    resposta = f'Saldo médio de R${saldoMédio} não possui nenhum crédito';

  return resposta;

HOST = "localhost";
PORT = 32002;

server = SimpleXMLRPCServer((HOST, PORT));
server.register_function(calcula_salario, "calcula_salario");
server.register_function(maioridade, "maioridade");
server.register_function(resultado_final, "resultado_final");
server.register_function(peso_ideal, "peso_ideal");
server.register_function(classifica_nadador, "classifica_nadador");
server.register_function(salario_final, "salario_final");
server.register_function(aposentadoria, "aposentadoria");
server.register_function(calcula_credito, "calcula_credito");
server.serve_forever();