import classes as cl

if __name__ == '__main__':
    # Entrada de dados
    nome = input('Digite o nome do Usuário: ')
    email = input('Digite o e-mail do Usuário: ')
    cpf = input('Digite o CPF do Usuário: ')
    profissao = input('Digite a profissão do Usuário: ')
    endereco = input('Digite o endereço do Usuário: ')
    telefone = input('Digite o telefone do Usuário: ')

    # instancia a classe pessoa física
    usuario = cl.PessoaFisica(nome, cpf, profissao, endereco, email, telefone)

    # entrada de dados
    nome = input('Digite o nome da empresa: ')
    email = input('Digite o email da empresa: ')
    cnpj = input('Digite o CNPJ da empresa: ')
    razao_social = input('Digite a razão social da empresa: ')
    endereco = input('Digite o endereço da empresa: ')
    telefone = input('Digite o telefone da empresa: ')

    # instancia a classe pessoa jurídica
    empresa = cl.PessoaJuridica(nome, razao_social, cnpj, endereco, email, telefone)

    # saida de dados
    usuario.mostrar_cartao_visitas()
    print('-'*70, '\n')
    empresa.mostrar_cartao_visitas()
