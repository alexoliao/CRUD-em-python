"""
Módulo que define a classe Pessoa para o sistema CRUD
"""


class Pessoa:
    """
    Classe que representa uma pessoa com atributos básicos.
    
    Atributos:
        id (int): Identificador único da pessoa
        nome (str): Nome completo da pessoa
        cpf (str): CPF da pessoa
        idade (int): Idade da pessoa
        email (str): Email da pessoa
        telefone (str): Telefone da pessoa
    """
    
    def __init__(self, id, nome, cpf, idade, email, telefone):
        """
        Inicializa uma nova instância de Pessoa.
        
        Args:
            id (int): Identificador único
            nome (str): Nome completo
            cpf (str): CPF (formato: XXX.XXX.XXX-XX)
            idade (int): Idade da pessoa
            email (str): Email da pessoa
            telefone (str): Telefone (formato: (XX) XXXXX-XXXX)
        """
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        self.telefone = telefone
    
    def __str__(self):
        """Retorna uma representação em string da pessoa."""
        return (f"ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf} | "
                f"Idade: {self.idade} | Email: {self.email} | Telefone: {self.telefone}")
    
    def __repr__(self):
        """Retorna uma representação técnica da pessoa."""
        return (f"Pessoa(id={self.id}, nome='{self.nome}', cpf='{self.cpf}', "
                f"idade={self.idade}, email='{self.email}', telefone='{self.telefone}')")
    
    def atualizar(self, nome=None, cpf=None, idade=None, email=None, telefone=None):
        """
        Atualiza os atributos da pessoa.
        
        Args:
            nome (str, opcional): Novo nome
            cpf (str, opcional): Novo CPF
            idade (int, opcional): Nova idade
            email (str, opcional): Novo email
            telefone (str, opcional): Novo telefone
        """
        if nome is not None:
            self.nome = nome
        if cpf is not None:
            self.cpf = cpf
        if idade is not None:
            self.idade = idade
        if email is not None:
            self.email = email
        if telefone is not None:
            self.telefone = telefone
    
    def para_dicionario(self):
        """
        Converte a pessoa em um dicionário.
        
        Returns:
            dict: Dicionário com os atributos da pessoa
        """
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'idade': self.idade,
            'email': self.email,
            'telefone': self.telefone
        }
    
    @classmethod
    def de_dicionario(cls, dados):
        """
        Cria uma instância de Pessoa a partir de um dicionário.
        
        Args:
            dados (dict): Dicionário com os dados da pessoa
            
        Returns:
            Pessoa: Nova instância de Pessoa
        """
        return cls(
            id=dados['id'],
            nome=dados['nome'],
            cpf=dados['cpf'],
            idade=dados['idade'],
            email=dados['email'],
            telefone=dados['telefone']
        )
