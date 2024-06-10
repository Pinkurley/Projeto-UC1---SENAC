import os
from time import sleep

alunos = []
tamanho = 30
verdadeiro = True

def main(chamada):
    def menu(funcao):
        os.system('cls')
        print('='*tamanho)
        print(f'   |  {"-" * 2}{funcao}{"-" * 2}  |')
        print('='*tamanho)

    def menu_aluno(aluno):
        print(f'   {alunos[aluno].get("nome")}  |  Turma: {alunos[aluno].get("turma")}')
        print('-' * tamanho)

    def verificacao_geral(acao, informacao_aluno):
        if acao == 'adicionar nome' or acao == 'adicionar turma' or acao == 'remover aluno':
            verificacao_temporaria = input(f'A informação está certa: {informacao_aluno} [S/N]\n')
            verificacao = verificacao_temporaria.upper().strip()
            return verificacao
        elif acao == 'pagina_aluno':
            verificacao_temporaria = input(f'Você deseja ver informações de {informacao_aluno} [S/N]\n')
            verificacao = verificacao_temporaria.upper().strip()  
            return verificacao
        else:
            verificacao_temporaria = input(f'Você deseja {acao} de {informacao_aluno} [S/N]\n')
            verificacao = verificacao_temporaria.upper().strip()  
            return verificacao

    def verificar_alunos():
        print('Não há alunos para serem listados\n')
        sleep(3)
        primeira_opcao()
    
    def mostrar_qntd_alunos():
        for indice, aluno in enumerate(alunos):  
            print(f'{indice + 1} | {aluno["nome"]} | turma: {aluno["turma"]}')
        
    def pagina_aluno():
        menu('PÁGINA DO ALUNO')
        if alunos == []:
            verificar_alunos()
        else:
            mostrar_qntd_alunos()
            print('-'*37)
            try:
                posicao_aluno = int(input('\nQual aluno deseja ver as informações?\n'))-1
                try:
                    alunos[posicao_aluno] in alunos
                    if posicao_aluno < 0:
                        print('A posição não pode ser menor que 0')
                        sleep(3)
                        pagina_aluno()   
                    else:
                        menu('PÁGINA DO ALUNO')
                        match verificacao_geral('pagina_aluno', alunos[posicao_aluno]["nome"]):
                            case 'S':
                                segunda_opcao(posicao_aluno)
                            case 'N':
                                retorno('Página Aluno')
                            case default:
                                print('Opção inválida\n')
                                sleep(3)
                                pagina_aluno()
                except IndexError as Error:
                    print('Essa não é uma posição válida')
                    sleep(3)
                    pagina_aluno()
            except ValueError as Error:
                print('A posição é um número!\n')
                sleep(3)
                pagina_aluno()

    def cadastrar_aluno():
        menu('CADASTRAR ALUNO')
        nome_aluno_temporario = input('Qual o nome do aluno? \n')
        nome_aluno = nome_aluno_temporario.strip().lower().capitalize()
        if nome_aluno == '':
            print('Escolha um nome...')
            sleep(3)
            cadastrar_aluno()
        else:
            try:
                verificacao_string = int(nome_aluno)
                print('O nome só pode ser usado letras\n')
                sleep(3)
                cadastrar_aluno()
            except ValueError as Error:
                match verificacao_geral('adicionar nome', nome_aluno):
                    case 'S':
                        while True:
                            menu('CADASTRAR ALUNO')
                            try:
                                turma_aluno = int(input('Qual a turma do aluno? \n'))
                                if turma_aluno < 0:
                                    print('A turma não pode ser um número negativo')
                                    sleep(3)
                                    continue
                                else:
                                    match verificacao_geral('adicionar turma', turma_aluno):
                                        case 'S':
                                            menu('CADASTRAR ALUNO')
                                            print(f'O aluno(a) {nome_aluno} da turma {turma_aluno} foi registrado!')
                                            alunos.append({'nome': nome_aluno, 'turma': turma_aluno, 'notas': [], 'faltas': 0})
                                            sleep(3)
                                            retorno('Cadastrar Aluno')
                                            break
                                        case 'N':
                                            continue
                                        case default:
                                            print('Opção inválida\n')
                                            sleep(3)
                            except ValueError as Error:
                                print('A turma é um número!\n')
                                sleep(3)
                    case 'N':
                        cadastrar_aluno()
                    case default:
                        print('Opção inválida\n')
                        sleep(3)
                        cadastrar_aluno()

    def mostrar_alunos():
        menu('MOSTRAR ALUNOS')
        if alunos == []:
            verificar_alunos()
        else:
            mostrar_qntd_alunos()
            sleep(3)
            retorno('Mostrar Alunos')

    def remover_aluno():
        menu('REMOVER ALUNO')
        if alunos == []:
            verificar_alunos()
        else:
            mostrar_qntd_alunos()
            try:
                posicao_aluno = int(input('\nEscolha a posição de qual aluno deseja excluir do sistema: \n')) - 1
                try:
                    alunos[posicao_aluno] in alunos
                    if posicao_aluno < 0:
                        print('A posição não pode ser menor que 0')
                        sleep(3)
                        remover_aluno() 
                    else:
                        menu('REMOVER ALUNO')
                        match verificacao_geral('remover aluno', alunos[posicao_aluno]["nome"]):
                            case 'S':
                                alunos.pop(posicao_aluno)
                                print('Remoção concluída.\n')
                                sleep(3)
                                retorno('Remover Aluno')
                            case 'N':
                                retorno('Remover Aluno')
                            case default:
                                print('Opção inválida\n')
                                sleep(3)
                                remover_aluno()
                except IndexError as Error:
                    print('Essa não é uma posição válida')
                    sleep(3)
                    remover_aluno()
            except ValueError as Error:
                print('Escolha uma posição')
                sleep(3)
                remover_aluno()

    def sair():
        os.system('cls')
        print('Finalizando o programa...')
        return
    
    def primeira_opcao():
        menu('MENU INICIAL')
        primeira_pergunta = input('(1): Página do Aluno \n(2): Mostrar Alunos \n(3): Cadastrar Aluno \n(4): Remover Aluno \n(0): Sair \n')
        match primeira_pergunta:
            case '1':
                pagina_aluno()
            case '2':
                mostrar_alunos()
            case '3':
                cadastrar_aluno()
            case '4':
                remover_aluno()
            case '0':
                sair()
            case default:
                print('Opção inválida\n')
                sleep(3)
                primeira_opcao()

    def retorno(funcao):
        if funcao == 'Mostrar Alunos':
            opcao = input(f'\nVocê deseja...\n(0): Finalizar programa\n(1): Voltar ao menu inicial\n')
        else:
            os.system('cls')
            opcao = input(f'Você deseja...\n(0): Finalizar programa\n(1): Voltar ao menu inicial\n(2): {funcao} novamente\n')
        match opcao:
            case '0':
                sair()
            case '1':
                primeira_opcao()
            case '2':
                match funcao:
                    case 'Cadastrar Aluno':
                        cadastrar_aluno()
                    case 'Página Aluno':
                        pagina_aluno()
                    case 'Remover Aluno':
                        remover_aluno()
                    case default:
                        print('Opção inválida')
                        sleep(3)
                        os.system('cls')
                        retorno(funcao)   
            case default:
                print('Opção inválida\n')
                sleep(3)
                retorno(funcao)
    
    def editar_nome(parametro_nome):
        menu('EDITAR NOME')
        menu_aluno(parametro_nome)
        match verificacao_geral('editar nome', alunos[parametro_nome]["nome"]):
            case 'S':
                menu('EDITAR NOME')
                menu_aluno(parametro_nome)  
                novo_nome_temporario = input('Qual o novo nome do aluno: \n')
                novo_nome = novo_nome_temporario.strip().lower().capitalize()
                if novo_nome == '':
                    print('Escolha um nome...')
                    sleep(3)
                    editar_nome(parametro_nome)
                else:
                    try:
                        verificacao_string = int(novo_nome)
                        print('O nome só pode ser usado letras\n')
                        sleep(3)
                        editar_nome(parametro_nome)
                    except ValueError as Error:
                        menu('EDITAR NOME')
                        menu_aluno(parametro_nome) 
                        alunos[parametro_nome]["nome"] = novo_nome
                        print('O nome foi alterado!')
                        sleep(3)
                        retorno_2('Editar Nome', parametro_nome)
            case 'N':
                retorno_2('Editar Nome', parametro_nome)
            case default:
                print('Opção inválida\n')
                sleep(3)
                editar_nome(parametro_nome)

    def editar_turma(parametro_turma):
        menu('EDITAR TURMA')
        menu_aluno(parametro_turma)
        match verificacao_geral('editar turma', alunos[parametro_turma]["nome"]):
            case 'S':
                menu('EDITAR TURMA')
                menu_aluno(parametro_turma)
                try:
                    nova_turma = int(input('Qual a nova turma do aluno: \n'))
                    alunos[parametro_turma]["turma"] = nova_turma
                    print('A turma foi alterada!')
                    sleep(3)
                    retorno_2('Editar Turma', parametro_turma)
                except ValueError as Error:
                    print('A turma só pode ser um número\n')
                    sleep(3)
                    editar_turma(parametro_turma)
            case 'N':
                retorno_2('Editar Turma', parametro_turma)
            case default:
                print('Opção inválida\n')
                sleep(3)
                editar_turma(parametro_turma)

    def adicionar_nota(parametro_notas):
        menu('ADICIONAR NOTAS')
        menu_aluno(parametro_notas)
        match verificacao_geral('adicionar nota', alunos[parametro_notas]["nome"]):
            case 'S':
                menu('ADICIONAR NOTAS')
                menu_aluno(parametro_notas)
                try:
                    qntd_notas = int(input('Quantas notas deseja adicionar: \n'))
                    if qntd_notas <= 0:
                        print('A quantidade tem que ser maior que 0')
                        sleep(3)
                        adicionar_nota(parametro_notas)
                    else:
                        while qntd_notas > 0:
                            try:
                                menu('ADICIONAR NOTAS')
                                menu_aluno(parametro_notas)
                                nota = input(f'Qual a {qntd_notas}º nota: ')
                                nota = float(nota.replace(',', '.'))
                                if nota < 0 or nota > 10:
                                    print('A nota não pode ser menor que 0 ou maior que 10')
                                    sleep(3)
                                    continue
                                else:
                                    alunos[parametro_notas]["notas"].append(nota)
                                    qntd_notas -= 1
                            except ValueError as Error:
                                print('A nota só pode ser um número...')
                                sleep(3)
                            print('Nota(s) adicionada(s)!')
                        sleep(3)
                        retorno_2('Adicionar Nota', parametro_notas)
                except ValueError as Error:
                    print('A quantidade só pode ser um número\n')
                    sleep(3)
                    adicionar_nota(parametro_notas)
            case 'N':
                retorno_2('Adicionar Nota', parametro_notas)
            case default:
                print('Opção inválida\n')
                sleep(3)
                adicionar_nota(parametro_notas)

    def adicionar_falta(parametro_falta):
        menu('ADICIONAR FALTAS')
        menu_aluno(parametro_falta)
        match verificacao_geral('adicionar falta', alunos[parametro_falta]["nome"]):
            case 'S':
                menu('ADICIONAR FALTAS')
                menu_aluno(parametro_falta)  
                try:
                    menu('ADICIONAR FALTAS')
                    menu_aluno(parametro_falta)  
                    qntd_faltas = int(input('Qual a quantidade de faltas do aluno que deseja adicionar: \n'))
                    if qntd_faltas <= 0:
                        print('A quantidade tem que ser maior que 0')
                        sleep(3)
                        adicionar_falta(parametro_falta)
                    else:
                        alunos[parametro_falta]["faltas"] += qntd_faltas
                        print('A quantidade de faltas foi alterada!')
                        sleep(3)
                        retorno_2('Adicionar Falta', parametro_falta)
                except ValueError as Error:
                    print('A quantidade de faltas só pode ser um número\n')
                    sleep(3)
                    adicionar_falta(parametro_falta)
            case 'N':
                retorno_2('Adicionar Falta', parametro_falta)
            case default:
                print('Opção inválida\n')
                sleep(3)
                adicionar_falta(parametro_falta)

    def mostrar_media(parametro_mostrar_media):
        menu('MOSTRAR MÉDIA')
        menu_aluno(parametro_mostrar_media)
        if alunos[parametro_mostrar_media]["notas"] == []:
            print('O aluno não possui notas')
            sleep(3)
            retorno_2('mostrar_media', parametro_mostrar_media)
        else:
            match verificacao_geral('mostrar média', alunos[parametro_mostrar_media]["nome"]):
                case 'S':
                    menu('MOSTRAR MÉDIA')
                    menu_aluno(parametro_mostrar_media)
                    soma = 0
                    for nota in alunos[parametro_mostrar_media]["notas"]:
                        soma += nota
                    media = soma / len(alunos[parametro_mostrar_media]["notas"])
                    classificacao = 'aprovado(a)' if media >= 7 else 'reprovado(a)'
                    print(f'A média de {alunos[parametro_mostrar_media]["nome"]} é: {media:0.2f} e ele(a) está atualmente {classificacao}')
                    sleep(2)
                    retorno_2('mostrar_media', parametro_mostrar_media)
                case 'N':
                    retorno_2('mostrar_media', parametro_mostrar_media)
                case default:
                    print('Opção inválida\n')
                    sleep(3)
                    mostrar_media(parametro_mostrar_media)

    def mostrar_notas(parametro_mostrar_notas):
        menu('MOSTRAR NOTAS')
        menu_aluno(parametro_mostrar_notas)
        if alunos[parametro_mostrar_notas]["notas"] == []:
            print('O aluno não possui notas')
            sleep(3)
            retorno_2('mostrar_notas', parametro_mostrar_notas)
        else:
            match verificacao_geral('mostrar notas', alunos[parametro_mostrar_notas]["nome"]):
                case 'S':
                    menu('MOSTRAR NOTAS')
                    menu_aluno(parametro_mostrar_notas)
                    for indice in range(len(alunos[parametro_mostrar_notas]["notas"])):
                        print(f'{indice+1}º nota: {(alunos[parametro_mostrar_notas]["notas"])[indice]}')
                    sleep(2)
                    retorno_2('mostrar_notas', parametro_mostrar_notas)
                case 'N':
                    retorno_2('mostrar_notas', parametro_mostrar_notas)
                case default:
                    print('Opção inválida\n')
                    sleep(3)
                    mostrar_notas(parametro_mostrar_notas)

    def mostrar_faltas(parametro_mostrar_faltas):
        menu('MOSTRAR FALTAS')
        menu_aluno(parametro_mostrar_faltas)
        match verificacao_geral('mostrar faltas', alunos[parametro_mostrar_faltas]["nome"]):
            case 'S':
                menu('MOSTRAR FALTAS')
                menu_aluno(parametro_mostrar_faltas)
                print(f'As faltas de {alunos[parametro_mostrar_faltas]["nome"]} são {alunos[parametro_mostrar_faltas]["faltas"]}')
                sleep(2)
                retorno_2('mostrar_faltas', parametro_mostrar_faltas)
            case 'N':
                retorno_2('mostrar_faltas', parametro_mostrar_faltas)
            case default:
                print('Opção inválida\n')
                sleep(3)
                mostrar_faltas(parametro_mostrar_faltas)

    def voltar():
        os.system('cls')
        print('Voltando ao Menu Inicial...')
        sleep(3)
        primeira_opcao()

    def segunda_opcao(parametro_aluno):
        menu('PÁGINA ALUNO')
        menu_aluno(parametro_aluno)
        segunda_pergunta = input('(1): Editar Nome \n(2): Editar Turma \n(3): Adicionar Nota \n(4): Adicionar Falta \n(5): Mostrar Média \n(6): Mostrar Notas \n(7): Mostrar Faltas \n(0): Voltar \n')
            
        match segunda_pergunta:
            case '1':
                editar_nome(parametro_aluno)
            case '2':
                editar_turma(parametro_aluno)
            case '3':
                adicionar_nota(parametro_aluno)
            case '4':
                adicionar_falta(parametro_aluno)
            case '5':
                mostrar_media(parametro_aluno)
            case '6':
                mostrar_notas(parametro_aluno)
            case '7':
                mostrar_faltas(parametro_aluno)
            case '0': 
                voltar()
            case default:
                print('Essa escolha não é válida\n')
                sleep(3)
                segunda_opcao(parametro_aluno)

    def retorno_2(funcao, parametro_retorno):
        if funcao == 'mostrar_media' or funcao == 'mostrar_notas' or funcao == 'mostrar_faltas':
            opcao = input(f'\nVocê deseja...\n(0): Finalizar o programa\n(1): Voltar ao Menu Inicial\n(2): Voltar a Página do Aluno\n')
        else: 
            os.system('cls')
            opcao = input(f'Você deseja...\n(0): Finalizar programa\n(1): Voltar ao Menu Inicial\n(2): Voltar a Página do Aluno\n(3): {funcao} novamente\n')
        match opcao:
            case '0':
                sair()
            case '1':
                voltar()
            case '2':
                segunda_opcao(parametro_retorno)
            case '3':
                match funcao:
                    case 'Editar Nome':
                        editar_nome(parametro_retorno)
                    case 'Editar Turma':
                        editar_turma(parametro_retorno)
                    case 'Adicionar Nota':
                        adicionar_nota(parametro_retorno)
                    case 'Adicionar Falta':
                        adicionar_falta(parametro_retorno)
                    case default:
                        print('Opção inválida')
                        sleep(3)
                        os.system('cls')
                        retorno_2(funcao, parametro_retorno)    
            case default:
                os.system('cls')
                print('Opção inválida\n')
                sleep(3)
                retorno_2(funcao, parametro_retorno)
    
    if chamada == 'primeira_opcao':
        primeira_opcao()

main('primeira_opcao')