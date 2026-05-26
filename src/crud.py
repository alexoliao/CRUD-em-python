"""
Módulo CRUD para gerenciar pessoas usando vetores (listas)
"""

from src.pessoa import Pessoa


class CRUDPessoa:
    """
    Classe que gerencia operações CRUD (Create, Read, Update, Delete) 
    de pessoas usando vetores (listas Python).
    """
    
    def __init__(self):
        """Inicializa o CRUD com um vetor vazio de pessoas."""
        self.pessoas = []  # Vetor de pessoas
        self.proximo_id = 1  # Contador para gerar IDs únicos
    
    def adicionar(self, nome, cpf, idade, email, telefone):
        """
        Adiciona uma nova pessoa ao sistema.
        
        Args:
            nome (str): Nome da pessoa
            cpf (str): CPF da pessoa
            idade (int): Idade da pessoa
            email (str): Email da pessoa
            telefone (str): Telefone da pessoa
            
        Returns:
            Pessoa: A pessoa adicionada
        """
        # Verifica se o CPF já existe
        if self._cpf_existe(cpf):
            raise ValueError(f"Erro: CPF '{cpf}' já cadastrado no sistema.")
        
        # Cria nova pessoa com ID automático
        pessoa = Pessoa(self.proximo_id, nome, cpf, idade, email, telefone)
        self.pessoas.append(pessoa)
        self.proximo_id += 1
        
        return pessoa
    
    def listar_todos(self):
        """
        Lista todas as pessoas cadastradas.
        
        Returns:
            list: Vetor de todas as pessoas
        """
        return self.pessoas.copy()
    
    def listar_com_limite(self, limite):
        """
        Lista um número limitado de pessoas.
        
        Args:
            limite (int): Quantidade de pessoas a listar
            
        Returns:
            list: Vetor com até 'limite' pessoas
        """
        if limite <= 0:
            return []
        return self.pessoas[:limite]
    
    def buscar_por_id(self, id):
        """
        Busca uma pessoa pelo ID.
        
        Args:
            id (int): ID da pessoa
            
        Returns:
            Pessoa: A pessoa encontrada ou None
        """
        for pessoa in self.pessoas:
            if pessoa.id == id:
                return pessoa
        return None
    
    def buscar_por_cpf(self, cpf):
        """
        Busca uma pessoa pelo CPF.
        
        Args:
            cpf (str): CPF da pessoa
            
        Returns:
            Pessoa: A pessoa encontrada ou None
        """
        for pessoa in self.pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None
    
    def buscar_por_nome(self, nome):
        """
        Busca pessoas pelo nome (busca parcial/contém).
        
        Args:
            nome (str): Nome ou parte do nome
            
        Returns:
            list: Vetor de pessoas encontradas
        """
        resultado = []
        for pessoa in self.pessoas:
            if nome.lower() in pessoa.nome.lower():
                resultado.append(pessoa)
        return resultado
    
    def atualizar(self, id, nome=None, cpf=None, idade=None, email=None, telefone=None):
        """
        Atualiza os dados de uma pessoa.
        
        Args:
            id (int): ID da pessoa a atualizar
            nome (str, opcional): Novo nome
            cpf (str, opcional): Novo CPF
            idade (int, opcional): Nova idade
            email (str, opcional): Novo email
            telefone (str, opcional): Novo telefone
            
        Returns:
            bool: True se atualizado, False se não encontrado
        """
        pessoa = self.buscar_por_id(id)
        
        if pessoa is None:
            return False
        
        # Verifica se o novo CPF já existe (em outra pessoa)
        if cpf is not None and cpf != pessoa.cpf and self._cpf_existe(cpf):
            raise ValueError(f"Erro: CPF '{cpf}' já cadastrado no sistema.")
        
        pessoa.atualizar(nome, cpf, idade, email, telefone)
        return True
    
    def deletar(self, id):
        """
        Deleta uma pessoa do sistema.
        
        Args:
            id (int): ID da pessoa a deletar
            
        Returns:
            bool: True se deletado, False se não encontrado
        """
        for i, pessoa in enumerate(self.pessoas):
            if pessoa.id == id:
                self.pessoas.pop(i)
                return True
        return False
    
    def contar(self):
        """
        Retorna a quantidade de pessoas cadastradas.
        
        Returns:
            int: Quantidade de pessoas
        """
        return len(self.pessoas)
    
    def _cpf_existe(self, cpf):
        """
        Verifica se um CPF já existe no sistema.
        
        Args:
            cpf (str): CPF a verificar
            
        Returns:
            bool: True se existe, False caso contrário
        """
        for pessoa in self.pessoas:
            if pessoa.cpf == cpf:
                return True
        return False
