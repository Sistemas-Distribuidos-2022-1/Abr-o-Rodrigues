import Pyro5.api;

pessoa1 = Pyro5.api.Proxy("PYRONAME:pessoa1");
print(pessoa1.peso_ideal());