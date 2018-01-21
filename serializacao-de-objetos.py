import pickle
import json

meus_dados = ['anderson', 3.14, [1, 2, 3]]

with open('arquivo.txt', 'wb') as file:
    pickle.dump(meus_dados, file)

with open('arquivo.txt', 'rb') as file:
    dados_carregados = pickle.load(file)

assert meus_dados == dados_carregados

# Serializando objetos: JSON - Javascript Object Notation


class Contato:
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return ('{} {}'
                .format(self.primero_nome,
                        self.sobrenome))


c = Contato('Anderson', 'Matheus')
print(json.dumps(c.__dict__))
