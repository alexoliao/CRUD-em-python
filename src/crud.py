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
