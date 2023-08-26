def principal():
    lista_compras = []

    while True:
        print("\n--- Lista de Compras ---")
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Editar Item")
        print("4. Listar itens")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            item = input("Digite o nome do item a ser adicionado: ")
            lista_compras.append(item)
            print(f"{item} foi adicionado à lista.")

        elif escolha == '2':
            print("Itens na lista: ")
            for index, item in enumerate(lista_compras):
                print(f"{index + 1}. {item}")
            try:
                item_index = int(input("Digite o número do item a ser removido: ")) - 1
                if 0 <= item_index < len(lista_compras):
                    remover_item = lista_compras.pop(item_index)
                    print(f'{remover_item} foi removido da lista.')
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Entrada incorreta, digite um número válido.")

        elif escolha == '3':
            print("Itens na lista")
            for index, item in enumerate(lista_compras):
                print(f"{index + 1}. {item}")
            try:
                item_index = int(input("Digite o número do item a ser editado: ")) - 1
                if 0 <= item_index < len(lista_compras):
                    editar_item = input("Digite o novo nome do item: ")
                    lista_compras[item_index] = editar_item
                    print(f"Item editado para: {editar_item}")
                else:
                    print("Índice Inválido.")
            except ValueError:
                print("Entrada incorreta, digite um número válido.")

        elif escolha == '4':
            if lista_compras:
                print("\nItens na lista: ")
                for index, item in enumerate(lista_compras):
                    print(f"{index + 1}. {item}")
            else:
                print("A lista de compras está vazia, adicione um item para começar.")

        elif escolha == '5':
            print("Saindo.")
            break
        else:
            print("Opção inválida, digite uma opção válida.")

if __name__ == "__main__":
    principal()
