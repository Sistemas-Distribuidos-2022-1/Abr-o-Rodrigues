import Pyro5.api;

cliente1 = Pyro5.api.Proxy("PYRONAME:cliente1");
print(cliente1.get_valor_credito());