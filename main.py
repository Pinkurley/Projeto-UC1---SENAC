import os
from time import sleep

alunos = []
tamanho = 30
professores = [{'usuario': 'Joao', 'senha': 1234}, {'usuario': 'Carla', 'senha': 2024}]

def main():
    def menu(funcao_menu):
        os.system('cls')
        print('='*tamanho)
        if funcao_menu == 'ALTERAR/RETIRAR NOTA':
            print(f'   |{"-" * 2}{funcao_menu}{"-" * 2}|')
        else:
            print(f'   |  {"-" * 2}{funcao_menu}{"-" * 2}  |')
        print('='*tamanho)

    def menu_aluno(informacao_pessoa):
        print(f'   {alunos[informacao_pessoa]["nome"]}  |  Turma: {alunos[informacao_pessoa]["turma"]}')
        print('-' * tamanho)

    def verificacao_geral(acao, informacao_aluno):
        if acao == 'adicionar nome' or acao == 'adicionar turma' or acao == 'remover aluno':
            verificacao_temporaria = input(f'A informação está certa: {informacao_aluno} [S/N]\n')
        elif acao == 'pagina aluno':
            verificacao_temporaria = input(f'Você deseja ver informações de {informacao_aluno} [S/N]\n')
        else:
            verificacao_temporaria = input(f'Você deseja {acao} de {informacao_aluno} [S/N]\n')
        verificacao_info = verificacao_temporaria.upper().strip()
        return verificacao_info

    def ler_string(informacao_input, funcao_retorno, informacao_funcao):
        if informacao_input == '':
            print('Digite algo...')
            sleep(3)
            if funcao_retorno == editar_nome or funcao_retorno == alterar_retirar_nota:
                funcao_retorno(informacao_funcao)
            else:
                funcao_retorno()
        else:
            try:
                verific_string = int(informacao_input)
                if funcao_retorno == cadastrar_aluno or funcao_retorno == login:
                    invalidez(funcao_retorno, None, None, None)
                else:
                    invalidez(funcao_retorno, informacao_funcao, None, None)
            except ValueError:
                return True

    def ler_inteiro(informacao_input_2, funcao_retorno_2, informacao_funcao_2):
        try:
            verific_inteiro = int(informacao_input_2)
            return True
        except ValueError:
            if funcao_retorno_2 == pagina_aluno or funcao_retorno_2 == remover_aluno or funcao_retorno_2 == login:
                invalidez(funcao_retorno_2, None, None, None)
            elif funcao_retorno_2 == cadastrar_aluno:
                print('A turma é um número!\n')
                sleep(3)
            else:
                invalidez(funcao_retorno_2, informacao_funcao_2, None, None)

    def ler_float(informacao_input_3, funcao_retorno_3, informacao_funcao_3):
        try:
            verific_inteiro = float(informacao_input_3)
            return True
        except ValueError:
            if funcao_retorno_3 == alterar_retirar_nota:
                invalidez(funcao_retorno_3, informacao_funcao_3, None, None)
            else:
                print('A nota só pode ser um número...')
                sleep(3)
            
    def ler_lista(informacao_input_4, funcao_retorno_4, informacao_funcao_4):
        if funcao_retorno_4 == alterar_retirar_nota:
            if len(alunos[informacao_funcao_4]["notas"])-1 < informacao_input_4 or informacao_input_4 < 0:
                invalidez(funcao_retorno_4, informacao_funcao_4, None, None)
            else:
                return True
        else:
            if informacao_input_4 < 0 or informacao_input_4 > len(alunos)-1:
                invalidez(funcao_retorno_4, None, None, None)
            else:
                return True

    def invalidez(prox_funcao, parametro_prox_funcao, funcao_inv, opcao_retorno):
        if prox_funcao == login:
            print('Usuário ou senha inválido')
            sleep(3)
            prox_funcao()
        else:
            print('Opção inválida')
            sleep(3)
            if prox_funcao == pagina_aluno or prox_funcao == cadastrar_aluno or prox_funcao == remover_aluno:
                prox_funcao()
            elif opcao_retorno == 'retorno_1':
                os.system('cls')
                prox_funcao(parametro_prox_funcao, None, opcao_retorno)
            elif opcao_retorno == 'retorno_2':
                os.system('cls')
                prox_funcao(funcao_inv, parametro_prox_funcao, opcao_retorno)
            elif prox_funcao == opcao:
                prox_funcao(parametro_prox_funcao, funcao_inv)
            else:
                prox_funcao(parametro_prox_funcao)

    def verificar_qntd(parametro_qntd, funcao_str):
        if alunos == []:
            print('Não há alunos para serem listados\n')
            sleep(3)
            opcao(None, 'primeira_opcao')
        elif funcao_str == 'Alterar/retirar Nota' or funcao_str == 'Retirar Falta' or funcao_str == 'mostrar_media' or funcao_str == 'mostrar_notas':
            if alunos[parametro_qntd]["faltas"] == 0 and funcao_str == 'Retirar Falta':
                print('O aluno não tem faltas')
                sleep(3)
                retorno(funcao_str, parametro_qntd, 'retorno_2')
            elif alunos[parametro_qntd]["notas"] == [] and funcao_str != 'Retirar Falta': 
                print('O aluno não possui notas')
                sleep(3)
                retorno(funcao_str, parametro_qntd, 'retorno_2')
            else:
                return True
        else:
            return True
    
    def mostrar_qntd_alunos():
        for indice, aluno in enumerate(alunos):  
            print(f'{indice + 1} | {aluno["nome"]} | turma: {aluno["turma"]}')
        
    def login():
        menu('LOGIN')
        professor = input('\nUsuário: ').strip().lower().capitalize()
        if ler_string(professor, login, None) == True:
            senha = input('\nSenha: ')
            if ler_inteiro(senha, login, None) == True:
                qntd_professor = 0
                for posicao in range(len(professores)):
                    if professores[posicao]["usuario"] == professor and professores[posicao]["senha"] == int(senha):
                        opcao(None, 'primeira_opcao')
                    else:
                        qntd_professor += 1
                if qntd_professor == len(professores):
                    invalidez(login, None, None, None)
    
    def opcao(parametro_aluno, qual_opcao):
        if qual_opcao == 'segunda_pergunta':
            menu('PÁGINA ALUNO')
            menu_aluno(parametro_aluno)
            segunda_pergunta = input('(1): Editar Nome \n(2): Editar Turma \n(3): Adicionar Nota \n(4): Adicionar Falta \n(5): Mostrar Média \n(6): Mostrar Notas \n(7): Mostrar Faltas \n(8): Retirar Falta \n(9): Alterar/retirar nota \n(0): Voltar \n')
                
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
                case '8':
                    retirar_falta(parametro_aluno)
                case '9':
                    alterar_retirar_nota(parametro_aluno)
                case '0': 
                    voltar()
                case default:
                    invalidez(opcao, parametro_aluno, qual_opcao, None)
        else:
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
                    invalidez(opcao, None, qual_opcao, None)

    def pagina_aluno():
        menu('PÁGINA DO ALUNO')
        if verificar_qntd(None, None):
            mostrar_qntd_alunos()
            print('-'*tamanho)
            posicao_aluno_temporaria = input('\nQual aluno deseja ver as informações?\n')
            if ler_inteiro(posicao_aluno_temporaria, pagina_aluno, None) == True:
                posicao_aluno = int(posicao_aluno_temporaria) - 1
                if ler_lista(posicao_aluno, pagina_aluno, None):
                    menu('PÁGINA DO ALUNO')
                    match verificacao_geral('pagina aluno', alunos[posicao_aluno]["nome"]):
                        case 'S':
                            opcao(posicao_aluno, 'segunda_pergunta')
                        case 'N':
                            retorno('Página Aluno', None, 'retorno_1')
                        case default:
                            invalidez(pagina_aluno, None, None, None)

    def cadastrar_aluno():
        menu('CADASTRAR ALUNO')
        nome_aluno = input('Qual o nome do aluno? \n').strip().lower().capitalize()
        if ler_string(nome_aluno, cadastrar_aluno, None) == True:
            match verificacao_geral('adicionar nome', nome_aluno):
                case 'S':
                    while True:
                        menu('CADASTRAR ALUNO')
                        turma_aluno_temporaria = input('Qual a turma do aluno? \n')
                        if ler_inteiro(turma_aluno_temporaria, cadastrar_aluno, None) == True:
                            turma_aluno = int(turma_aluno_temporaria)
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
                                        retorno('Cadastrar Aluno', None, 'retorno_1')
                                        break
                                    case 'N':
                                        continue
                                    case default:
                                        print('Opção inválida\n')
                                        sleep(3)
                case 'N':
                    cadastrar_aluno()
                case default:
                    invalidez(cadastrar_aluno, None, None, None)

    def mostrar_alunos():
        menu('MOSTRAR ALUNOS')
        if verificar_qntd(None, None):
            mostrar_qntd_alunos()
            sleep(3)
            retorno('Mostrar Alunos', None, 'retorno_1')

    def remover_aluno():
        menu('REMOVER ALUNO')
        if verificar_qntd(None, None):
            mostrar_qntd_alunos()
            posicao_aluno_remover_temporaria = input('\nEscolha a posição de qual aluno deseja excluir do sistema: \n')
            if ler_inteiro(posicao_aluno_remover_temporaria, remover_aluno, None) == True:
                posicao_aluno_remover = int(posicao_aluno_remover_temporaria) - 1
                if ler_lista(posicao_aluno_remover, remover_aluno, None):
                    menu('REMOVER ALUNO')
                    match verificacao_geral('remover aluno', alunos[posicao_aluno_remover]["nome"]):
                        case 'S':
                            alunos.pop(posicao_aluno_remover)
                            print('Remoção concluída.\n')
                            sleep(3)
                            retorno('Remover Aluno', None, 'retorno_1')
                        case 'N':
                            retorno('Remover Aluno', None, 'retorno_1')
                        case default:
                            invalidez(remover_aluno, None, None, None)

    def sair():
        os.system('cls')
        return print('Finalizando o programa...')
    
    def editar_nome(parametro_nome):
        menu('EDITAR NOME')
        menu_aluno(parametro_nome)
        match verificacao_geral('editar nome', alunos[parametro_nome]["nome"]):
            case 'S':
                menu('EDITAR NOME')
                menu_aluno(parametro_nome)  
                novo_nome = input('Qual o novo nome do aluno: \n').strip().lower().capitalize()
                if ler_string(novo_nome, editar_nome, parametro_nome) == True:
                    menu('EDITAR NOME')
                    menu_aluno(parametro_nome) 
                    alunos[parametro_nome]["nome"] = novo_nome
                    print('O nome foi alterado!')
                    sleep(3)
                    retorno('Editar Nome', parametro_nome, 'retorno_2')
            case 'N':
                retorno('Editar Nome', parametro_nome, 'retorno_2')
            case default:
                invalidez(editar_nome, parametro_nome, None, None)

    def editar_turma(parametro_turma):
        menu('EDITAR TURMA')
        menu_aluno(parametro_turma)
        match verificacao_geral('editar turma', alunos[parametro_turma]["nome"]):
            case 'S':
                menu('EDITAR TURMA')
                menu_aluno(parametro_turma)
                nova_turma = input('Qual a nova turma do aluno: \n')
                if ler_inteiro(nova_turma, editar_turma, parametro_turma):
                    alunos[parametro_turma]["turma"] = int(nova_turma)
                    print('A turma foi alterada!')
                    sleep(3)
                    retorno('Editar Turma', parametro_turma, 'retorno_2')
            case 'N':
                retorno('Editar Turma', parametro_turma, 'retorno_2')
            case default:
                invalidez(editar_turma, parametro_turma, None, None)

    def adicionar_nota(parametro_nota):
        menu('ADICIONAR NOTAS')
        menu_aluno(parametro_nota)
        match verificacao_geral('adicionar nota', alunos[parametro_nota]["nome"]):
            case 'S':
                menu('ADICIONAR NOTAS')
                menu_aluno(parametro_nota)
                qntd_notas_temporaria = input('Quantas notas deseja adicionar: \n')
                if ler_inteiro(qntd_notas_temporaria, adicionar_nota, parametro_nota) == True:
                    qntd_notas = int(qntd_notas_temporaria)
                    if qntd_notas <= 0:
                        invalidez(adicionar_nota, parametro_nota, None, None)
                    else:
                        while qntd_notas > 0:
                            menu('ADICIONAR NOTAS')
                            menu_aluno(parametro_nota)
                            nota_temporaria = input(f'Qual a {qntd_notas}º nota: ').replace(',', '.')
                            if ler_float(nota_temporaria, adicionar_nota, parametro_nota) == True:
                                nota = float(nota_temporaria)
                                if nota < 0 or nota > 10:
                                    print('A nota não pode ser menor que 0 ou maior que 10')
                                    sleep(3)
                                    continue
                                else:
                                    alunos[parametro_nota]["notas"].append(nota)
                                    qntd_notas -= 1
                        print('Nota(s) adicionada(s)!')
                        sleep(3)
                        retorno('Adicionar Nota', parametro_nota, 'retorno_2')
            case 'N':
                retorno('Adicionar Nota', parametro_nota, 'retorno_2')
            case default:
                invalidez(adicionar_nota, parametro_nota, None, None)

    def adicionar_falta(parametro_falta):
        menu('ADICIONAR FALTAS')
        menu_aluno(parametro_falta)
        match verificacao_geral('adicionar falta', alunos[parametro_falta]["nome"]):
            case 'S':
                menu('ADICIONAR FALTAS')
                menu_aluno(parametro_falta)  
                qntd_faltas_temporaria = input('Qual a quantidade de faltas do aluno que deseja adicionar: \n')
                if ler_inteiro(qntd_faltas_temporaria, adicionar_falta, parametro_falta) == True:
                    qntd_faltas = int(qntd_faltas_temporaria)
                    if qntd_faltas <= 0:
                        invalidez(adicionar_falta, parametro_falta, None, None)
                    else:
                        alunos[parametro_falta]["faltas"] += qntd_faltas
                        print('A quantidade de faltas foi alterada!')
                        sleep(3)
                        retorno('Adicionar Falta', parametro_falta, 'retorno_2')
            case 'N':
                retorno('Adicionar Falta', parametro_falta, 'retorno_2')
            case default:
                invalidez(adicionar_falta, parametro_falta, None, None)

    def retirar_falta(parametro_retirar_falta):
        menu('RETIRAR FALTAS')
        menu_aluno(parametro_retirar_falta)
        if verificar_qntd(parametro_retirar_falta, 'Retirar Falta'):
            match verificacao_geral('retirar falta', alunos[parametro_retirar_falta]["nome"]):
                case 'S':
                    menu('RETIRAR FALTAS')
                    menu_aluno(parametro_retirar_falta)
                    retirar_qntd_temporario = input('Qual a quantidade de faltas do aluno que deseja retirar: \n')
                    if ler_inteiro(retirar_qntd_temporario, retirar_falta, parametro_retirar_falta) == True:
                        retirar_qntd = int(retirar_qntd_temporario)
                        if retirar_qntd <= 0 or retirar_qntd > alunos[parametro_retirar_falta]["faltas"]:
                            invalidez(retirar_falta, parametro_retirar_falta, None, None)
                        else:
                            alunos[parametro_retirar_falta]["faltas"] -= retirar_qntd
                            print('A quantidade de faltas foi alterada!')
                            sleep(3)
                            retorno('Retirar Falta', parametro_retirar_falta, 'retorno_2')
                case 'N':
                    retorno('Retirar Falta', parametro_retirar_falta, 'retorno_2')
                case default:
                    invalidez(retirar_falta, parametro_retirar_falta, None, None)
    
    def alterar_retirar_nota(parametro_alterar_retirar_nota):
        menu('ALTERAR/RETIRAR NOTA')
        menu_aluno(parametro_alterar_retirar_nota)
        if verificar_qntd(parametro_alterar_retirar_nota, 'Alterar/retirar Nota'):
            match verificacao_geral('alterar/retirar nota', alunos[parametro_alterar_retirar_nota]["nome"]):
                case 'S':
                    menu('ALTERAR/RETIRAR NOTA')
                    menu_aluno(parametro_alterar_retirar_nota)
                    for indice, nota in enumerate(alunos[parametro_alterar_retirar_nota]["notas"]):
                        print(f'{indice+1}º nota: {nota:0.1f}')
                    nota_posicao_temporaria = input('\nQual nota deseja alterar/retirar: \n')
                    if ler_inteiro(nota_posicao_temporaria, alterar_retirar_nota, parametro_alterar_retirar_nota) == True:
                        nota_posicao = int(nota_posicao_temporaria) - 1
                        if ler_lista(nota_posicao, alterar_retirar_nota, parametro_alterar_retirar_nota) == True:
                            menu('ALTERAR/RETIRAR NOTA')
                            menu_aluno(parametro_alterar_retirar_nota)
                            alterar_retirar = input(f'Você deseja alterar [A] ou retirar [R] a nota {alunos[parametro_alterar_retirar_nota]["notas"][nota_posicao]} (Voltar [V]) : \n').strip().lower().capitalize()
                            if ler_string(alterar_retirar, alterar_retirar_nota, parametro_alterar_retirar_nota) == True:
                                match alterar_retirar:
                                    case 'A':
                                        menu('ALTERAR NOTA')
                                        menu_aluno(parametro_alterar_retirar_nota)
                                        nova_nota = input('Qual a nova nota: \n').replace(',', '.')
                                        if float(nova_nota) > 10 or float(nova_nota) < 0:
                                            invalidez(alterar_retirar_nota, parametro_alterar_retirar_nota, None, None)
                                        else:
                                            if ler_float(nova_nota, alterar_retirar_nota, parametro_alterar_retirar_nota) == True:
                                                alunos[parametro_alterar_retirar_nota]["notas"][nota_posicao] = float(nova_nota)
                                                print('\nA nota foi alterada!')
                                                sleep(3)
                                                retorno('Alterar/retirar Nota', parametro_alterar_retirar_nota, 'retorno_2')
                                    case 'R':
                                        menu('RETIRAR NOTA')
                                        menu_aluno(parametro_alterar_retirar_nota)
                                        alunos[parametro_alterar_retirar_nota]["notas"].pop(nota_posicao)
                                        print('A nota foi retirada!')
                                        sleep(3)
                                        retorno('Alterar/retirar Nota', parametro_alterar_retirar_nota, 'retorno_2')
                                    case 'V':
                                        retorno('Alterar/retirar Nota', parametro_alterar_retirar_nota, 'retorno_2')
                                    case default:
                                        invalidez(alterar_retirar_nota, parametro_alterar_retirar_nota, None, None)
                case 'N':
                    retorno('Alterar/retirar Nota', parametro_alterar_retirar_nota, 'retorno_2')
                case default:
                    invalidez(alterar_retirar_nota, parametro_alterar_retirar_nota, None, None)
        
    def mostrar_media(parametro_mostrar_media):
        menu('MOSTRAR MÉDIA')
        menu_aluno(parametro_mostrar_media)
        if verificar_qntd(parametro_mostrar_media, 'mostrar_media'):
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
                    retorno('mostrar_media', parametro_mostrar_media, 'retorno_2')
                case 'N':
                    retorno('mostrar_media', parametro_mostrar_media, 'retorno_2')
                case default:
                    invalidez(mostrar_media, parametro_mostrar_media, None, None)

    def mostrar_notas(parametro_mostrar_notas):
        menu('MOSTRAR NOTAS')
        menu_aluno(parametro_mostrar_notas)
        if verificar_qntd(parametro_mostrar_notas, 'mostrar_notas'):
            match verificacao_geral('mostrar notas', alunos[parametro_mostrar_notas]["nome"]):
                case 'S':
                    menu('MOSTRAR NOTAS')
                    menu_aluno(parametro_mostrar_notas)
                    for indice, nota in enumerate(alunos[parametro_mostrar_notas]["notas"]):
                        print(f'{indice+1}º nota: {nota:0.1f}')
                    sleep(2)
                    retorno('mostrar_notas', parametro_mostrar_notas, 'retorno_2')
                case 'N':
                    retorno('mostrar_notas', parametro_mostrar_notas, 'retorno_2')
                case default:
                    invalidez(mostrar_notas, parametro_mostrar_notas, None, None)

    def mostrar_faltas(parametro_mostrar_faltas):
        menu('MOSTRAR FALTAS')
        menu_aluno(parametro_mostrar_faltas)
        match verificacao_geral('mostrar faltas', alunos[parametro_mostrar_faltas]["nome"]):
            case 'S':
                menu('MOSTRAR FALTAS')
                menu_aluno(parametro_mostrar_faltas)
                print(f'As faltas de {alunos[parametro_mostrar_faltas]["nome"]} são {alunos[parametro_mostrar_faltas]["faltas"]}')
                sleep(2)
                retorno('mostrar_faltas', parametro_mostrar_faltas, 'retorno_2')
            case 'N':
                retorno('mostrar_faltas', parametro_mostrar_faltas, 'retorno_2')
            case default:
                invalidez(mostrar_faltas, parametro_mostrar_faltas, None, None)

    def voltar():
        os.system('cls')
        print('Voltando ao Menu Inicial...')
        sleep(3)
        opcao(None, 'primeira_opcao')

    def retorno(funcao, parametro_retorno, qual_opcao_2):
        if qual_opcao_2 == 'retorno_2':
            if funcao == 'mostrar_media' or funcao == 'mostrar_notas' or funcao == 'mostrar_faltas':
                opcao2 = input(f'\nVocê deseja...\n(0): Finalizar o programa\n(1): Voltar ao Menu Inicial\n(2): Voltar a Página do Aluno\n')
            else: 
                os.system('cls')
                opcao2 = input(f'Você deseja...\n(0): Finalizar programa\n(1): Voltar ao Menu Inicial\n(2): Voltar a Página do Aluno\n(3): {funcao} novamente\n')
            match opcao2:
                case '0':
                    sair()
                case '1':
                    voltar()
                case '2':
                    opcao(parametro_retorno, 'segunda_pergunta')
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
                        case 'Retirar Falta':
                            retirar_falta(parametro_retorno)
                        case 'Alterar/retirar Nota':
                            alterar_retirar_nota(parametro_retorno)
                        case default:
                            invalidez(retorno, parametro_retorno, funcao, 'retorno_2')    
                case default:
                    invalidez(retorno, parametro_retorno, funcao, 'retorno_2')
        else:
            if funcao == 'Mostrar Alunos':
                opcao1 = input(f'\nVocê deseja...\n(0): Finalizar programa\n(1): Voltar ao menu inicial\n')
            else:
                os.system('cls')
                opcao1 = input(f'Você deseja...\n(0): Finalizar programa\n(1): Voltar ao menu inicial\n(2): {funcao} novamente\n')
            match opcao1:
                case '0':
                    sair()
                case '1':
                    opcao(None, 'primeira_opcao')
                case '2':
                    match funcao:
                        case 'Cadastrar Aluno':
                            cadastrar_aluno()
                        case 'Página Aluno':
                            pagina_aluno()
                        case 'Remover Aluno':
                            remover_aluno()
                        case default:
                            invalidez(retorno, funcao, None, 'retorno_1')   
                case default:
                    invalidez(retorno, funcao, None, 'retorno_1')
    
    login()

main()