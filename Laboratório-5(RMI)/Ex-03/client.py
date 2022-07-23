import Pyro5.api;

aluno1 = Pyro5.api.Proxy("PYRONAME:aluno1");
print(aluno1.resultado_final());