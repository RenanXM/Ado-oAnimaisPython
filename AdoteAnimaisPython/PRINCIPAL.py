import Funcoes

# 1) Caso os 3 arquivos ainda não existam, inicializamos eles.
# Caso já existam, os arquivos apenas são abertos e fechados, sem nenhuma alteração.
Funcoes.abrir_e_fechar_os_3_arquivos()

while True:
    opcao = Funcoes.escolha()

    if opcao=='1':
        # Criar/inserir informações nos arquivos de animais adotados.
        Funcoes.inserir_dados_no_arquivo_de_animais_adotados()
        Funcoes.funcao_organizadora_arquivo_animais_adotados()

    elif opcao=='2':
        # Criar/inserir informações nos arquivos de animais não adotados.
        Funcoes.inserir_dados_no_arquivo_de_animais_nao_adotados()
        Funcoes.funcao_organizadora_arquivo_animais_nao_adotados()
        Funcoes.funcao_atualizar_dados_do_arquivo_de_entrevistas()

    elif opcao=='3':
        # Criar/inserir informações nos arquivos das entrevistas.
        Funcoes.inserir_dados_no_arquivo_de_entrevistas()

    elif opcao=='4':
        # Remover informações dos arquivos de animais adotados.
        Funcoes.remover_dados_do_arquivo_de_animais_adotados()


    elif opcao=='5':
        # Remover informações dos arquivos de animais não adotados.
        Funcoes.remover_dados_do_arquivo_de_animais_nao_adotados()
        Funcoes.funcao_atualizar_dados_do_arquivo_de_entrevistas()

    elif opcao=='6':
        # Remover informações dos arquivos de entrevistas.
        Funcoes.remover_dados_do_arquivo_de_entrevistas()
        
    elif opcao=='7':
        # Modificar as informações dos arquivos de animais adotados.
        Funcoes.modificar_dados_do_arquivo_de_animais_adotados()
        Funcoes.funcao_organizadora_arquivo_animais_adotados()

    elif opcao=='8':
        # Modificar as informações dos arquivos de animais não adotados.
        Funcoes.modificar_dados_do_arquivo_de_animais_nao_adotados()
        Funcoes.funcao_organizadora_arquivo_animais_nao_adotados()
        Funcoes.funcao_atualizar_dados_do_arquivo_de_entrevistas()

    elif opcao=='9':
        # Modificar as informações dos arquivos das entrevistas
        Funcoes.modificar_dados_do_arquivo_de_entrevistas()

    elif opcao=='10':
        # Ler as informações dos arquivos de animais adotados.
        Funcoes.ler_dados_do_arquivo_de_animais_adotados()

    elif opcao=='11':
        # Ler as informações dos arquivos de animais não adotados.
        Funcoes.ler_dados_do_arquivo_de_animais_nao_adotados()

    elif opcao=='12':
        # Ler as informações dos arquivos de entrevistas
        Funcoes.ler_dados_do_arquivo_de_entrevistas()

    elif opcao=='13':
        # Ler as fichas dos animais disponíveis para um certo candidato.
        Funcoes.mostrar_as_fichas_de_animais_disponiveis_para_um_candidato()

    elif opcao=='14':
        # Encerrar o programa.
        break