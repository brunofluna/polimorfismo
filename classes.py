# superclasse, classe-pai, classe base
class Pessoa:
    # atributos
    def __init__(self, endereco, email, telefone):
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
    
    # método de ação
    def mostrar_cartao_visitas(self):
        print(f'Endereço: {self.endereco}.')
        print(f'E-mail: {self.email}.')
        print(f'Telefone: {self.telefone}.')

# Subclasse, classe-filha, classe derivada Pessoa física
class PessoaFisica(Pessoa):
    # Polimorfismo do construtor
    def __init__(self, nome, cpf, profissao, endereco, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        super().__init__(endereco, email, telefone)

    def mostrar_cartao_visitas(self):
        print(f'Nome do Usuário: {self.nome}.')
        print(f'CPF do Usuário: {self.cpf}.')
        print(f'Profissão do Usuário: {self.profissao}.')
        super().mostrar_cartao_visitas()
        
class PessoaJuridica(Pessoa):
    # Polimorfismo do construtor
    def __init__(self, nome_fantasia, razao_social, cnpj, endereco, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        super().__init__(endereco, email, telefone)

    def mostrar_cartao_visitas(self):
        print(f'Nome da Empresa: {self.nome_fantasia}.')
        print(f'Razão Social: {self.razao_social}.')
        print(f'CNPJ: {self.cnpj}.')
        super().mostrar_cartao_visitas()
