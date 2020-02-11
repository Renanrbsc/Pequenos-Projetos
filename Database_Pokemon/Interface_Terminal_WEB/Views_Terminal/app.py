from Controller_Terminal.pokemon_controller import PokemonController
from Controller_Terminal.treinador_controller import TreinadorController
from Model_Terminal.pokemon_model import PokemonModel
from Model_Terminal.treinador_model import TreinadorModel


class Views:
    def __init__(self):
        self.Poke_controller = PokemonController()
        self.Trainer_controller = TreinadorController()
        self.modelController = None
        self.op_menu = None
        self.op = None
        self.id = None
        self.table = ''

    def menu(self):
        print('-=' * 20, '\n1- MENU POKEMON')
        print('2- MENU TREINADOR\n', '-=' * 20)
        self.op_menu = int(input("Digite a opcao: "))
        self.table = f"{'Pokemon' if self.op_menu == 1 else 'Treinador'}"
        self.modelController = self.Poke_controller if self.op_menu == 1 else self.Trainer_controller
        print('-=' * 20)
        print(f'1 - Listar {self.table}')
        print(f'2 - Buscar {self.table} ID')
        print(f'3 - Inserir {self.table}')
        print(f'4 - Alterar {self.table}')
        print(f'5 - Deletar {self.table}')
        print('-=' * 20)
        self.op = int(input("Digite a opcao: "))
        print('-=' * 20)

    def parameters(self):
        if self.op == 2 or self.op == 4 or self.op == 5:
            self.id = int(input(f"Digite a id do {self.table}:"))
        if self.op == 3 or self.op == 4:
            model = PokemonModel() if self.op_menu == 1 else TreinadorModel()
            return model

    def conditions(self):
        if self.op == 1:
            model_all = self.modelController.get_all()
            for model in model_all:
                print(model)

        if self.op == 2:
            print(f'----Buscar ID {self.table}----')
            self.parameters()
            print(self.modelController.get_by_id(self.id))

        if self.op == 3:
            print(f'----Adicionar {self.table}----')
            Pokemon = self.parameters()
            print(self.modelController.post(Pokemon))

        if self.op == 4:
            print(f'----Alterar {self.table}----')
            Pokemon = self.parameters()
            print(self.modelController.put(self.id, Pokemon))

        if self.op == 5:
            print(f'----Remover {self.table}----')
            self.parameters()
            print(self.modelController.delete(self.id))


views = Views()

while True:
    views.menu()
    views.conditions()
