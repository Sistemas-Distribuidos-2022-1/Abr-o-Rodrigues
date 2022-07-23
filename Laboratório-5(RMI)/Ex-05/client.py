import Pyro5.api;

nadador1 = Pyro5.api.Proxy("PYRONAME:nadador1");
print(nadador1.get_classificação());