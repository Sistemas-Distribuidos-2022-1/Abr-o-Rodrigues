import Pyro5.api;

func1 = Pyro5.api.Proxy("PYRONAME:func1");
print(func1.pode_aposentar());