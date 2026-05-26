"""
Programa principal do CRUD de Pessoa - Menu Interativo
"""

from src.crud import CRUDPessoa


def validar_idade(idade_str):
    """Valida se a entrada é uma idade válida."""
    try:
        idade = int(idade_str)
        if idade < 0 or idade > 150:
            return None
        return idade
    except ValueError:
        return None


def validar_cpf(cpf):
    """Valida o formato básico do CPF."""
    # Remove pontos e hífens
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    # Verifica se tem 11 dígitos
    if len(cpf_limpo) == 11 and cpf_limpo.isdigit():
        return True
    return False


def adicionar_pessoa(crud):
    """Menu para adicionar uma nova pessoa."""
    print("\n" + "=" * 50)
    print("ADICIONAR NOVA PESSOA")
    print("=" * 50)
    
    try:
        # Entrada de dados
        nome = input("Nome completo: ").strip()
        if not nome:
            print("❌ Erro: Nome não pode estar vazio!")
            return
        
        cpf = input("CPF (formato: XXX.XXX.XXX-XX ou XXXXXXXXXXX): ").strip()
        if not validar_cpf(cpf):
            print("❌ Erro: CPF inválido! Use o formato correto.")
            return
        
        idade_str = input("Idade: ").strip()
        idade = validar_idade(idade_str)
        if idade is None:
            print("❌ Erro: Idade deve ser um número entre 0 e 150!")
            return
        
        email = input("Email: ").strip()
        if not email or "@" not in email:
            print("❌ Erro: Email inválido!")
            return
        
        telefone = input("Telefone (formato: (XX) XXXXX-XXXX ou qualquer formato): ").strip()
        if not telefone:
            print("❌ Erro: Telefone não pode estar vazio!")
            return
        
        # Adiciona a pessoa
        pessoa = crud.adicionar(nome, cpf, idade, email, telefone)
        print(f"\n✅ Pessoa adicionada com sucesso!")
        print(f"   {pessoa}")
        
    except ValueError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ Erro ao adicionar pessoa: {e}")


def buscar_por_id(crud):
    """Menu para buscar uma pessoa por ID."""
    print("\n" + "=" * 50)
    print("BUSCAR PESSOA POR ID")
    print("=" * 50)
    
    try:
        id_str = input("Digite o ID: ").strip()
        id = int(id_str)
        
        pessoa = crud.buscar_por_id(id)
        
        if pessoa:
            print(f"\n✅ Pessoa encontrada:")
            print(f"   {pessoa}")
        else:
            print(f"❌ Nenhuma pessoa encontrada com ID {id}")
            
    except ValueError:
        print("❌ Erro: ID deve ser um número inteiro!")
    except Exception as e:
        print(f"❌ Erro ao buscar: {e}")


def buscar_por_cpf(crud):
    """Menu para buscar uma pessoa por CPF."""
    print("\n" + "=" * 50)
    print("BUSCAR PESSOA POR CPF")
    print("=" * 50)
    
    try:
        cpf = input("Digite o CPF: ").strip()
        
        if not cpf:
            print("❌ Erro: CPF não pode estar vazio!")
            return
        
        pessoa = crud.buscar_por_cpf(cpf)
        
        if pessoa:
            print(f"\n✅ Pessoa encontrada:")
            print(f"   {pessoa}")
        else:
            print(f"❌ Nenhuma pessoa encontrada com CPF {cpf}")
            
    except Exception as e:
        print(f"❌ Erro ao buscar: {e}")


def buscar_por_nome(crud):
    """Menu para buscar pessoas por nome."""
    print("\n" + "=" * 50)
    print("BUSCAR PESSOA POR NOME")
    print("=" * 50)
    
    try:
        nome = input("Digite o nome (ou parte do nome): ").strip()
        
        if not nome:
            print("❌ Erro: Nome não pode estar vazio!")
            return
        
        pessoas = crud.buscar_por_nome(nome)
        
        if pessoas:
            print(f"\n✅ {len(pessoas)} pessoa(s) encontrada(s):")
            for pessoa in pessoas:
                print(f"   {pessoa}")
        else:
            print(f"❌ Nenhuma pessoa encontrada com nome contendo '{nome}'")
            
    except Exception as e:
        print(f"❌ Erro ao buscar: {e}")


def menu_principal():
    """Menu principal do sistema."""
    crud = CRUDPessoa()
    
    while True:
        print("\n" + "=" * 50)
        print("SISTEMA CRUD DE PESSOA")
        print("=" * 50)
        print("1. Adicionar pessoa")
        print("2. Listar todas as pessoas")
        print("3. Buscar pessoa por ID")
        print("4. Buscar pessoa por CPF")
        print("5. Buscar pessoa por nome")
        print("6. Atualizar pessoa")
        print("7. Deletar pessoa")
        print("8. Sair")
        print("=" * 50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_pessoa(crud)
        elif opcao == "2":
            print("\n" + "=" * 50)
            print("LISTAR TODAS AS PESSOAS")
            print("=" * 50)
            pessoas = crud.listar_todos()
            if not pessoas:
                print("Nenhuma pessoa cadastrada.")
            else:
                for pessoa in pessoas:
                    print(pessoa)
            print(f"Total: {crud.contar()} pessoa(s)")
        elif opcao == "3":
            buscar_por_id(crud)
        elif opcao == "4":
            buscar_por_cpf(crud)
        elif opcao == "5":
            buscar_por_nome(crud)
        elif opcao == "8":
            print("\n👋 Encerrando o sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()
