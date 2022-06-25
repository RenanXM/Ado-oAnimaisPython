import time

# Lista/strings úteis na hora de verificar a validade dos nomes
lista_a=['Á','À','Ã','Â']
lista_e=['É','È','Ê']
lista_i=['Í']
lista_o=['Ó','Ò','Õ','Ô']
lista_u=['Ú','Ù','Û']
lista_pontuacoes = ['!','?',',',';']
letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros ='0123456789'



# 1) Início do programa

# 1.1) Caso os 3 arquivos ainda não existam, inicializamos eles.
# Caso já existam, os arquivos apenas são abertos e fechados, sem nenhuma alteração.
def abrir_e_fechar_os_3_arquivos():

    arquivo = open('Animais adotados.txt','a')
    arquivo.close()

    arquivo = open('Animais não adotados.txt','a')
    arquivo.close()

    arquivo = open('Entrevistas.txt','a')
    arquivo.close()



# 1.2) Decicindo o que o programa vai fazer.
def escolha():
    while True:
        print('                  MENU PRINCIPAL')
        time.sleep(0.2)
        print('1 - Criar/inserir informações nos arquivos de animais adotados.')
        time.sleep(0.2)
        print('2 - Criar/inserir informações nos arquivos de animais não adotados.')
        time.sleep(0.2)
        print('3 - Criar/inserir informações nos arquivos das entrevistas.')
        time.sleep(0.2)
        print('4 - Remover informações dos arquivos de animais adotados.')
        time.sleep(0.2)
        print('5 - Remover informações dos arquivos de animais não adotados.')
        time.sleep(0.2)
        print('6 - Remover informações dos arquivos de entrevistas.')
        time.sleep(0.2)
        print('7 - Modificar informações dos arquivos de animais adotados.')
        time.sleep(0.2)
        print('8 - Modificar informações dos arquivos de animais não adotados.')
        time.sleep(0.2)
        print('9 - Modificar informações dos arquivos das entrevistas.')
        time.sleep(0.2)
        print('10 - Ler as informações dos arquivos de animais adotados.')
        time.sleep(0.2)
        print('11 - Ler as informações dos arquivos de animais não adotados.')
        time.sleep(0.2)
        print('12 - Ler as informações dos arquivos de entrevistas.')
        time.sleep(0.2)
        print('13 - Mostrar as fichas dos animais passíveis de adoção por um certo candidato.')
        time.sleep(0.2)
        print('14 - Encerrar o programa.')
        time.sleep(0.2)

        lista = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
        opcao = input('Digite a sua opção: ')
        time.sleep(0.2)

        if opcao in lista:
            return opcao
        
        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, escolha uma opção válida.\n')
            time.sleep(1)



# 2) Funções suporte:

# 2.1) Verificador de "nome"
# Caso "nome" tenha ao menos 1 letra ou 1 número, "nome" é válido.

def verificador_nomes(nome):

    # Criamos uma string para alterar caracteres indesejados que podem ter sido digitados pelo usuário,
    # fazendo uso das "listas úteis".
    nome_alterado = ''
    for caractere in nome:
        if caractere in lista_a:
            nome_alterado += 'A'

        elif caractere in lista_e:
            nome_alterado += 'E'

        elif caractere in lista_i:
            nome_alterado += 'I'

        elif caractere in lista_o:
            nome_alterado += 'O'

        elif caractere in lista_u:
            nome_alterado += 'U'

        elif caractere=='Ç':
            nome_alterado += 'C'

        elif caractere in lista_pontuacoes:
            nome_alterado += ''

        else:
            nome_alterado += caractere


    # Agora verificamos se nome_alterado é um "nome" válido
    contador_letras = 0
    contador_numeros = 0

    for letra in letras:
        contador_letras += nome_alterado.count(letra)

    for numero in numeros:
        contador_numeros += nome_alterado.count(numero)

    # Retornamos uma lista com True e o nome_final caso o parâmetro "nome" seja válido
    if contador_letras + contador_numeros >= 1:
        return [True,nome_alterado]

    else:
        return [False]



# 2.2) Verificador de porte/tamanho máximo do animal que o candidato pode ter em casa
def verificador_porte(porte):
    if porte == 'PEQUENO':
        return [True,'PEQUENO']

    elif porte == 'MEDIO' or porte == 'MÉDIO':
        return [True,'MEDIO']

    elif porte == 'GRANDE':
        return [True,'GRANDE']
    
    else:
        return [False]



# 2.3) Verificador de respostas 'sim' ou 'nao' do candidato
def verificador_sim_nao(resposta):
    if resposta=='sim':
        return [True,'Sim']

    elif resposta=='nao' or resposta=='não':
        return [True,'Nao']

    else:
        return [False]



# 2.4) Função que retorna o número de animais disponíveis até o porte do parâmetro "porte".
def num_animais_disponiveis_porte(porte):

    # Abrimos o arquivo no modo de leitura
    arquivo = open('Animais não adotados.txt','r')
    contador_animais_disponiveis = 0
    
    # Para cada linha do arquivo, verificamos se aquela linha contém "Porte: 'porte'"
    # Se tiver, significa que há um animal disponível até o porte do parâmetro "porte".
    if porte == 'PEQUENO':
        for linha in arquivo:
            if 'Porte: PEQUENO' in linha:
                contador_animais_disponiveis += 1

    elif porte == 'MEDIO':
        for linha in arquivo:
            if 'Porte: PEQUENO' in linha or 'Porte: MEDIO' in linha:
                contador_animais_disponiveis += 1

    elif porte == 'GRANDE':
        for linha in arquivo:
            if 'Porte: PEQUENO' in linha or 'Porte: MEDIO' in linha or 'Porte: GRANDE' in linha:
                contador_animais_disponiveis += 1

    return(contador_animais_disponiveis)



# 2.5) Verificador de "Apto"
# Retorna "apto" e "justificativa" dependendo das respostas 1, 2 e 3.
def verificador_apto(resposta_1,resposta_2,resposta_3):

    # Contamos quantos animais disponíveis há que tenham porte compatíveis com "resposta_3"
    contador_animais_disponiveis = num_animais_disponiveis_porte(resposta_3)

    # Caso haja animais disponíveis
    if contador_animais_disponiveis >= 1:
        if resposta_1=='Sim' and resposta_2=='Sim':
            apto = 'Sim'
            justificativa = ''
        
        elif resposta_1 == 'Nao' and resposta_2 == 'Sim':
            apto = 'Nao'
            justificativa = 'O candidato nao possui condicoes financeiras'

        elif resposta_1 == 'Nao' and resposta_2 == 'Nao':
            apto = 'Nao'
            justificativa = 'O candidato nao possui nem condicoes financeiras e nem tempo livre'

        elif resposta_1 == 'Sim' and resposta_2 == 'Nao':
            apto = 'Nao'
            justificativa = 'O candidato nao possui tempo livre'

    # Caso não haja animais disponíveis
    else:
        if resposta_1 =='Sim' and resposta_2=='Sim':
            apto = 'Nao'
            justificativa = 'Nao ha animais de porte adequado ao candidato'

        elif resposta_1 =='Sim' and resposta_2=='Nao':
            apto = 'Nao'
            justificativa = 'Nao ha animais de porte adequado ao candidato, e o candidato nao possui tempo livre'

        elif resposta_1 =='Nao' and resposta_2=='Sim':
            apto = 'Nao'
            justificativa = 'Nao ha animais de porte adequado ao candidato, e o candidato nao possui condicoes financeiras'

        elif resposta_1 =='Nao' and resposta_2=='Nao':
            apto = 'Nao'
            justificativa = 'Nao ha animais de porte adequado ao candidato, e o candidato nao possui nem condicoes financeiras e nem tempo livre'


    return [apto,justificativa]



# 2.6) Verificador de data
# Retorna [False] ou [True, data_adocao_ajustada]
def verificador_data(data_adocao):
    # Transformamos data_adocao em uma lista
    # Observe que "data_adocao", se for válida, está no formato "dia/mes/ano"

    data = data_adocao.split('/')
    
    # Criamos 2 listas para guardarem o número dos meses com 30 e 31 dias.
    lista_meses_30_dias = [4,6,9,11]
    lista_meses_31_dias = [1,3,5,7,8,10,12]
    
    # Verificamos se o tamanho da lista "data" é 3, isto é, se "data_adocao" está no formato "dia/mes/ano"
    if len(data) == 3:

        # Nesse caso, significa que data = [ dia , mes , ano ]
        # Tentamos pegar a parte inteira de data[0], data[1] e data[2]
        try:
            dia = int(data[0])
            mes = int(data[1])
            ano = int(data[2])

        # Caso não seja possível pegar a parte inteira de ao menos um dos elementos da lista "data",
        # "data_adocao" é inválida
        except ValueError:
            return [False]
    
        # Fazemos um teste de verificação preliminar
        # (Queremos um ano que tenha exatamente 4 dígitos)
        if ano>=1000 and ano <= 9999 and dia>=1 and dia<=31 and mes>=1 and mes<=12:

            # Verificamos se "dia" e "mes" são compatíveis entre si em um ano bissexto
            if (ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0) :

                # Caso sejam compatíveis
                if (mes in lista_meses_30_dias and dia<=30) or (mes in lista_meses_31_dias and dia<=31) or (mes == 2 and dia<=29):

                    # Vemos quantos dígitos têm "dia" e "mes"
                    # Queremos ajustar as datas para todas serem no padrão "dd/mm/aaaa"
                    # Para tanto, precisamos adicionar um 0 à esquerda, tratando o caso em que o usuário digita
                    # uma data do tipo: "9/9/9999", onde o padrão é "d/m/aaaa"
                    if dia <= 9:
                        string_dia = '0' + str(dia)

                    else:
                        string_dia = str(dia)

                    if mes <= 9:
                        string_mes = '0' + str(mes)

                    else:
                        string_mes = str(mes)
                    
                    # Agora, organizamos a data corretamente
                    data_organizada = string_dia + '/' + string_mes + '/' + str(ano)
                    return [True,data_organizada]

                # Caso "dia" e "mes" não sejam compatíveis entre si em um ano bissexto
                else:
                    return [False]


            # Verificamos se o dia e o mês são compatíveis entre si em um ano não bissexto
            else:
                
                # De maneira análoga ao caso acima:
                if (mes in lista_meses_30_dias and dia<=30) or (mes in lista_meses_31_dias and dia<=31) or (mes == 2 and dia<=28):
                    if dia <= 9:
                        string_dia = '0' + str(dia)

                    else:
                        string_dia = str(dia)

                    if mes <= 9:
                        string_mes = '0' + str(mes)

                    else:
                        string_mes = str(mes)
                    
                    data_organizada = string_dia+ '/' + string_mes + '/' + str(ano)
                    return [True,data_organizada]

                else:
                    return [False]
        
        # Caso "dia", "mes" e "ano" não passem no teste preliminar
        else:
            return [False]

    # Caso a lista "data" não tenha exatamente 3 elementos
    else:
        return [False]



# 2.7) Função que recebe uma data de adoção e retorna um número (que representa o número de dias desde a data 01/01/01)
# Essa função serve para auxiliar a organizar as fichas dos animais adotados em ordem decrescente de data
# de adoção.
def recebe_data_retorna_numero(data):

    # "data" está no formato "dd/mm/aaaa"
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    # As 2 listas abaixo representam o número de dias já passados com base no número do mês
    # mes = 1, passaram 0 dias
    # mes = 2, passaram 31 dias
    # ...
    lista_dias_ano_bissexto = [0,31,60,91,121,152,182,213,244,274,305,335]
    lista_dias_ano_nao_bissexto = [0,31,59,90,120,151,181,212,243,273,304,334]

    # Já se passaram (dia-1) dias
    num_dias = dia-1

    if (ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0):

        # Observe que 1<= mes <= 12
        #             0<= pos <= 11 (posição de qualquer uma das listas_dias)
        # Assim, associamos "mes" e "pos" fazendo pos = mes - 1
        num_dias += lista_dias_ano_bissexto[mes-1]

    else:
        num_dias += lista_dias_ano_nao_bissexto[mes-1]

    # Contamos quantos anos bissextos e não bissextos se passaram do ano 1 até o ano "ano"
    contador_anos_bissextos = (int(ano/4)) - (int(ano/100)) + (int(ano/400))
    contador_anos_nao_bissextos = ano - contador_anos_bissextos

    # Se ano é bissexto
    if (ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0) :
        # O próprio ano não está completo
        contador_anos_bissextos_completos = contador_anos_bissextos - 1
        contador_anos_nao_bissextos_completos = contador_anos_nao_bissextos

    # Se ano não é bissexto
    else:
        contador_anos_bissextos_completos = contador_anos_bissextos

        # O próprio ano não está completo
        contador_anos_nao_bissextos_completos = contador_anos_nao_bissextos - 1

    num_dias += contador_anos_bissextos_completos * 366
    num_dias += contador_anos_nao_bissextos_completos * 365
    return (num_dias)



# 2.8) Função que recebe uma lista de datas e a organiza em forma decrescente
def organiza_datas_em_forma_decrescente(lista_datas):
    lista_numeros = []

    for data in lista_datas:
        # Para cada data da lista_datas, transformamos a data em um número e o guardamos na lista_numeros
        numero = recebe_data_retorna_numero(data)
        lista_numeros += [numero]

    # Organizamos a lista_numeros em ordem decrescente
    lista_numeros.sort(reverse=True)

    lista_datas_ordem_decrescente = []

    # lista_numeros == [num1,num2,num3,...,numN]
    # lista_datas == [data1,data2,data3,...,dataN]
    # Agora precisamos preencher a lista "lista_dados_ordem_decrescente"

    # Criamos uma lista para guardar os indíces das datas já colocadas
    lista_indices_das_datas_ja_colocadas = []

    # Para cada "elemento" da lista_numeros, verificamos qual é a "data" (da lista_datas) cujo
    # recebe_data_retorna_numero("data") seja igual a "elemento".

    # Quando houver igualdade, significa que "elemento" é a forma decodificada de "data". Assim, guardamos
    # "data" na lista_datas_ordem_decrescente.

    # Além disso, se i estiver na lista "lista_indices_das_data_ja_colocadas", significa que a data
    # referentes a esse índice já foi contabilizada e, portanto, não deve ser contabilizada novamente.

    
    for elemento in lista_numeros:
        for i in range (len(lista_datas)):

            data = lista_datas[i]
            numero = recebe_data_retorna_numero(data)

            if numero == elemento and i not in lista_indices_das_datas_ja_colocadas:
                lista_datas_ordem_decrescente += [data]

                lista_indices_das_datas_ja_colocadas += [i]
                
                break

    return lista_datas_ordem_decrescente



# 2.9) Recebendo os dados para o arquivo de animais adotados
def recebendo_entradas_animais_adotados():
    
    # Recebemos o nome do animal.
    while True:
        time.sleep(0.2)
        nome_animal = input('\nDigite o nome do animal adotado: ').upper()

        lista_retorno = verificador_nomes(nome_animal)

        # lista_retorno == [False] ou lista_retorno == [True , nome_final ].
        # A posiçao [0] indica True ou False.
        # Criamos uma variável que tem o objetivo apenas de receber o booleano retornado pela função.

        validade_nome_animal = lista_retorno[0]

        if validade_nome_animal:
            # Nesse caso, lista_retorno == [True, nome_final]
            nome_animal = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite um nome válido.\n')
            time.sleep(1)

    # Recebemos a idade.
    while True:
        try:
            time.sleep(0.2)
            idade = int(input('Digite a idade, em meses, do animal adotado: '))
            if idade >= 0:
                validade_idade = True

            else:
                validade_idade = False

        except ValueError:
            validade_idade = False

        if validade_idade:
            break
        
        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite uma idade válida.\n')
            time.sleep(1)

    # Recebemos o porte.
    while True:
        time.sleep(0.2)
        porte = input('Digite o porte do animal adotado (pequeno, medio ou grande): ').upper()

        lista_retorno = verificador_porte(porte)

        validade_porte = lista_retorno[0]
        if validade_porte:
            porte = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite um porte válido.\n')
            time.sleep(1)

    # Recebemos a raça.
    while True:
        time.sleep(0.2)
        raca = input('Digite a raça do animal adotado (Se você não souber a raça, deixe a entrada vazia): ').upper()

        # Caso raca seja vazio, devemos colocar, por padrão, "SRD".
        if raca == '':
            raca = 'SRD'
            break
        

        else:
            # Repetimos o processo de verificação de validade utilizando a mesma lógica da lista de retorno.
            lista_retorno = verificador_nomes(raca)

            validade_raca = lista_retorno[0]
            if validade_raca:
                raca = lista_retorno[1]
                break

            else:
                print('\n'+ '-=' * 30)
                time.sleep(0.1)
                print(' '*26 + 'ERRO')
                time.sleep(0.2)
                print('-=' * 30)
                time.sleep(0.1)
                print('\nPor favor, digite uma raca válida.\n')
                time.sleep(1)


    # Recebemos o nome do lar temporário.
    while True:
        time.sleep(0.2)
        lar_temporario = input('Digite o lar temporário do animal adotado: ').upper()

        lista_retorno = verificador_nomes(lar_temporario)

        validade_lar_temp = lista_retorno[0]
        if validade_lar_temp:
            lar_temporario = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite um nome de lar temporário válido.\n')
            time.sleep(1)

    # Recebemos o nome do responsável.
    while True:
        time.sleep(0.2)
        nome_do_responsavel = input('Digite o nome do responsável pela adoção: ').upper()

        lista_retorno = verificador_nomes(nome_do_responsavel)

        validade_nome_resp = lista_retorno[0]
        if validade_nome_resp:
            nome_do_responsavel = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite um nome de responsável válido.\n')
            time.sleep(1)

    # Recebemos a data de adoção.
    while True:
        time.sleep(0.2)
        data_adocao = input('Digite a data de adoção (formato dd/mm/aaaa): ')

        lista_retorno = verificador_data(data_adocao)

        validade_data = lista_retorno[0]
        if validade_data:
            data_adocao = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite uma data de adoção válida.\n')
            time.sleep(1)
    
    # Retornamos uma lista com os dados recebidos para preencher o arquivo "Animais adotados.txt"
    return [nome_animal,str(idade),porte,raca,lar_temporario,nome_do_responsavel,data_adocao]



# 2.10) Recebendo os dados para o arquivo de animais não adotados:
def recebendo_entradas_animais_nao_adotados():
    
    # Recebemos o nome do animal.
    while True:
        time.sleep(0.2)
        nome_animal = input('\nDigite o nome do animal não adotado: ').upper()

        lista_retorno = verificador_nomes(nome_animal)

        validade_nome_animal = lista_retorno[0]
        if validade_nome_animal:
            nome_animal = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite um nome válido.\n')

    # Recebemos a idade.
    while True:
        try:
            time.sleep(0.2)
            idade = int(input('Digite a idade, em meses, do animal não adotado: '))
            if idade >= 0:
                validade_idade = True

            else:
                validade_idade = False

        except ValueError:
            validade_idade = False

        if validade_idade:
            break
        
        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite uma idade válida.\n')

    # Recebemos o porte.
    while True:
        time.sleep(0.2)
        porte = input('Digite o porte do animal não adotado (pequeno, medio ou grande): ').upper()

        lista_retorno = verificador_porte(porte)

        validade_porte = lista_retorno[0]
        if validade_porte:
            porte = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite um porte válido.\n')

    # Recebemos a raça.
    while True:
        time.sleep(0.2)
        raca = input('Digite a raça do animal não adotado (Se você não souber a raça, deixe a entrada vazia): ').upper()

        # Caso raca seja vazio, devemos colocar, por padrão, "SRD".
        if raca == '':
            raca = 'SRD'
            break
        

        else:
            lista_retorno = verificador_nomes(raca)

            validade_raca = lista_retorno[0]
            if validade_raca:
                raca = lista_retorno[1]
                break

            else:
                print('\n'+ '-=' * 30)
                time.sleep(0.1)
                print(' '*26 + 'ERRO')
                time.sleep(0.2)
                print('-=' * 30)
                time.sleep(0.1)
                print('\nPor favor, digite uma raca válida.\n')


    # Recebendo o nome do lar temporário.
    while True:
        time.sleep(0.2)
        lar_temporario = input('Digite o lar temporário do animal não adotado: ').upper()

        lista_retorno = verificador_nomes(lar_temporario)

        validade_lar_temp = lista_retorno[0]
        if validade_lar_temp:
            lar_temporario = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite um nome de lar temporário válido.\n')

    # Como os animais ainda não foram adotados, então os campos "nome do responsavel" e "data de adocao"
    # devem ficar vazios.
    nome_do_responsavel = ''
    data_adocao = ''
    
    # Retornamos uma lista com os dados para preencher o arquivo "Animais não adotados.txt"
    return [nome_animal,str(idade),porte,raca,lar_temporario,nome_do_responsavel,data_adocao]



# 2.11) Recebendo as entradas das entrevistas:
def recebendo_entradas_entrevistas():

    # Recebemos o nome do candidato.
    while True:
        time.sleep(0.2)
        nome_do_candidato = input('\nDigite o nome do candidato: ').upper()

        lista_retorno = verificador_nomes(nome_do_candidato)
        v_nome = lista_retorno[0]
        if v_nome:
            nome_do_candidato = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, digite um nome de candidato válido.\n')

    # Recebemos a resposta da pergunta 1.
    while True:
        time.sleep(0.2)
        resposta_1 = input('Você possui condições financeiras para adotar um novo animal? (Sim/Não): ').lower()

        lista_retorno = verificador_sim_nao(resposta_1)
        v_resposta_1 = lista_retorno[0]

        if v_resposta_1:
            resposta_1 = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, responda "sim" ou "nao".')

    # Recebemos a resposta da pergunta 2.
    while True:
        time.sleep(0.2)
        resposta_2 = input('Avaliando sua rotina, você possui tempo livre para se dedicar ao seu novo pet? (Sim/Não): ').lower()

        lista_retorno = verificador_sim_nao(resposta_2)
        v_resposta_2 = lista_retorno[0]

        if v_resposta_2:
            resposta_2 = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, responda "sim" ou "nao".')

    # Recebemos a resposta da pergunta 3.
    while True:
        time.sleep(0.2)
        print('Pense agora no espaço que você possui em casa: qual o porte máximo que o animal deverá ter para viver confortavelmente com você?')
        time.sleep(0.2)
        resposta_3 = input('(Pequeno/Médio/Grande) ').upper()

        lista_retorno = verificador_porte(resposta_3)
        v_resposta_3 = lista_retorno[0]

        if v_resposta_3:
            resposta_3 = lista_retorno[1]
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nPor favor, responda "Pequeno", "Medio" ou "Grande".')

    # Criamos a string_respostas, que é a concatenação das 3 respostas.
    string_respostas = resposta_1 + '; ' + resposta_2 + '; ' + resposta_3

    # Verificamos se o candidato é apto ou não e a justificativa.
    lista_retorno = verificador_apto(resposta_1,resposta_2,resposta_3)
    apto = lista_retorno[0]
    justificativa = lista_retorno[1]


    # Retornamos uma lista com dados para preencher o arquivo "Entrevistas.txt"
    return [nome_do_candidato,string_respostas,apto,justificativa]



# A partir daqui, utilizamos fortemente as funções auxiliares criadas acima, que foram criadas exclusivamente com o
# intuito de transformar uma "rotina" de verificações em um processo simples e direto, o que facilitou muito o 
# andamento do algoritmo, visto que exploramos muito os retornos com informações valiosas como nomes finais,
# Booleanos importantes, etc. 

# 3) Funções principais:

# Opção 1: Criar/inserir informações nos arquivos de animais adotados.
def inserir_dados_no_arquivo_de_animais_adotados():

    while True:
        print('\n' + '-=' * 30)
        time.sleep(0.1)
        print('      Inserindo dados em "Animais adotados.txt"')
        time.sleep(0.3)
        print('-=' * 30)
        time.sleep(0.1)
        print('\nDigite 1 para inserir dados em "Animais adotados.txt".')
        time.sleep(0.2)
        print('Digite 0 para voltar ao menu principal.')
        time.sleep(0.2)
        continuar = input('Digite 1 ou 0: ')
        time.sleep(0.2)

        if continuar == '1':
            # Abrimos o arquivo "Animais adotados.txt".
            arquivo = open('Animais adotados.txt','a')

            # Recebemos todas as 7 entradas
            lista_retorno = recebendo_entradas_animais_adotados()

            # Preenchemos "Animais adotados.txt" com os elementos da lista_retorno, atentando aos "\n".
            arquivo.write('Nome: ' + lista_retorno[0] + '\n')
            arquivo.write('Idade: ' + lista_retorno[1] + '\n')
            arquivo.write('Porte: ' + lista_retorno[2] + '\n')
            arquivo.write('Raca: ' + lista_retorno[3] + '\n')
            arquivo.write('Lar temporario: ' +lista_retorno[4] + '\n')
            arquivo.write('Nome do responsavel: ' + lista_retorno[5] + '\n')
            arquivo.write('Data de adocao: ' + lista_retorno[6] + '\n')
            arquivo.write('\n')

            # Fechamos para evitar problemas.
            arquivo.close()

        elif continuar == '0':
            print('')
            time.sleep(0.5)
            print('VOLTANDO AO MENU PRINCIPAL...')
            time.sleep(1)
            print('')
            time.sleep(0.2)
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.2)
            print('\nPor favor, digite 1 ou 0.\n')
            time.sleep(1)



# Opção 2:  Criar/inserir informações nos arquivos de animais não adotados.
def inserir_dados_no_arquivo_de_animais_nao_adotados():

    while True:
        print('\n' + '-=' * 30)
        time.sleep(0.1)
        print('      Inserindo dados em "Animais não adotados.txt"')
        time.sleep(0.3)
        print('-=' * 30)
        time.sleep(0.1)
        print('\nDigite 1 para inserir dados em "Animais não adotados.txt".')
        time.sleep(0.2)
        print('Digite 0 para voltar ao menu principal.')
        time.sleep(0.2)
        continuar = input('\nDigite 1 ou 0: ')
        time.sleep(0.2)

        if continuar == '1':
            # Abrimos o arquivo "Animais não adotados.txt".
            arquivo = open('Animais não adotados.txt','a')

            # Recebemos todas as 5 entradas
            # Lista retorno tem 7 elementos : as 5 entradas e 2 elementos vazios.
            # Os 2 elementos vazios são referentes aos campos "Nome do responsável" e "Data de adoção"
            lista_retorno = recebendo_entradas_animais_nao_adotados()

            # Preenchemos "Animais não adotados.txt" com os elementos da lista_retorno 
            arquivo.write('Nome: ' + lista_retorno[0] + '\n')
            arquivo.write('Idade: ' + lista_retorno[1] + '\n')
            arquivo.write('Porte: ' + lista_retorno[2] + '\n')
            arquivo.write('Raca: ' + lista_retorno[3] + '\n')
            arquivo.write('Lar temporario: ' + lista_retorno[4] + '\n')
            arquivo.write('Nome do responsavel: ' + lista_retorno[5] + '\n')
            arquivo.write('Data de adocao: ' + lista_retorno[6] + '\n')
            arquivo.write('\n')

            arquivo.close()

        elif continuar == '0':
            print('')
            time.sleep(0.5)
            print('VOLTANDO AO MENU PRINCIPAL...')
            time.sleep(1)
            print('')
            time.sleep(0.2)
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.2)
            print('\nPor favor, digite 1 ou 0.\n')
            time.sleep(1)



# Opção 3: Criar/inserir informações nos arquivos de entrevistas
def inserir_dados_no_arquivo_de_entrevistas():


    while True:
        print('\n' + '-=' * 30)
        time.sleep(0.1)
        print('          Inserindo dados em "Entrevistas.txt"')
        time.sleep(0.3)
        print('-=' * 30)
        time.sleep(0.1)
        print('\nDigite 1 para inserir dados em "Entrevistas.txt".')
        time.sleep(0.2)
        print('Digite 0 para voltar ao menu principal.')
        time.sleep(0.2)
        continuar = input('\nDigite 1 ou 0: ')
        time.sleep(0.2)

        if continuar == '1':
            # Abrimos o arquivo "Entrevistas.txt"
            arquivo = open('Entrevistas.txt','a')

            # Recebemos as 4 entradas
            # Lista_retorno tem 4 elementos : "nome do candidato", "resposta_1; resposta_2; resposta_3",
            # "apto" e "justificativa"
            lista_retorno = recebendo_entradas_entrevistas()

            # Preenchemos o arquivo "Entrevistas.txt" com os elementos da lista_retorno
            arquivo.write('Nome: ' + lista_retorno[0] + '\n')
            arquivo.write(lista_retorno[1] + '\n')
            arquivo.write('Apto: ' + lista_retorno[2] + '\n')
            arquivo.write('Justificativa: ' + lista_retorno[3] + '\n')
            arquivo.write('\n')

            arquivo.close()

        elif continuar == '0':
            print('')
            time.sleep(0.5)
            print('VOLTANDO AO MENU PRINCIPAL...')
            time.sleep(1)
            print('')
            time.sleep(0.2)
            break

        else:
            print('\n'+ '-=' * 30)
            time.sleep(0.1)
            print(' '*26 + 'ERRO')
            time.sleep(0.2)
            print('-=' * 30)
            time.sleep(0.2)
            print('\nPor favor, digite 1 ou 0.\n')
            time.sleep(1)



# Função que organiza o arquivo "Animais adotados" de acordo com a data de adoção
def funcao_organizadora_arquivo_animais_adotados():

    # Abrimos o arquivo no modo de leitura
    arquivo = open('Animais adotados.txt','r')

    # Pegamos uma lista que contém todas as linhas do arquivo
    lista_arquivo = arquivo.readlines()
    arquivo.close()
    t = len(lista_arquivo)

    # Criamos uma lista para guardar todas as datas contidas em "Animais adotados.txt"
    lista_datas = []

    # Observe o padrão das posições das datas no arquivo "Animais adotados.txt"
    # Começa na posição 6 e pula 8 posições para chegar na próxima data
    for i in range(6,t-1,8):

        # Tiramos "\n" do fim de lista_arquivo[i]
        lista_arquivo[i] = lista_arquivo[i].rstrip()

        # lista_arquivo[i] == "Data de adoção: data"
        # Guardamos "Data de adoção" e "data" na lista_auxiliar
        lista_auxiliar = lista_arquivo[i].split(': ')

        # Pegamos o valor de "data" da lista_auxiliar e o guardamos na lista_datas
        lista_datas += [lista_auxiliar[1]]

    # Com a lista_datas completa, usamos organiza_datas_em_forma_decrescente(lista_datas) para retornar
    # uma lista de datas onde as datas estão organizadas em ordem decrescente.
    lista_retorno = organiza_datas_em_forma_decrescente(lista_datas)

    # Abrimos o arquivo novamente
    arquivo = open('Animais adotados.txt','w')

    # Criamos uma lista para guardar os índices dos dados já usados
    lista_indices_dos_dados_ja_colocados = []

    # Agora, para cada data_ordem_decrescente, verificamos qual é a primeira data da lista_arquivo que é igual
    # a data_ordem_decrescente. Quando houver igualdade, adicionamos conteúdo a "Animais adotados.txt".
    for data_ordem_decrescente in lista_retorno:

        for i in range(6,t-1,8):
            # Como retiramos o "\n" no processo anterior, não há mais "\n" no fim de lista_arquivo[i]
            # lista_arquivo[i] == "Data de adoção: data"
            # Guardamos "Data de adoção" e "data" na lista_auxiliar
            lista_auxiliar = lista_arquivo[i].split(': ')

            # Pegamos o valor de "data" da lista_auxiliar
            data_ordem_original = lista_auxiliar[1]

            # Comparamos data_ordem_original e data_ordem_decrescente
            # Quando houver igualdade, preechemos "Animais adotados.txt" com as informações referentes
            # à data_ordem_original

            # Além disso, se i estiver na lista "lista_indices_dos_dados_ja_colocados", significa que os dados
            # referentes a esse índice já foram colocados e, portanto, não devem ser repetidos.
            if data_ordem_original == data_ordem_decrescente and i not in lista_indices_dos_dados_ja_colocados:
                # Nome
                arquivo.write(lista_arquivo[i-6])

                # Idade
                arquivo.write(lista_arquivo[i-5])

                # Porte
                arquivo.write(lista_arquivo[i-4])

                # Raça
                arquivo.write(lista_arquivo[i-3])

                # Lar temporário
                arquivo.write(lista_arquivo[i-2])

                # Nome do responsável
                arquivo.write(lista_arquivo[i-1])

                # Data de adoção
                # Como retiramos o "\n" ao preencher lista_datas, precisamos colocar "\n" na parte da data.
                arquivo.write(lista_arquivo[i] + '\n')

                # Espaço em branco
                arquivo.write(lista_arquivo[i+1])

                lista_indices_dos_dados_ja_colocados += [i]
                break

    # No fim, fechamos o arquivo para evitar problemas.
    arquivo.close()
    


# Função que organiza o arquivo "Animais não adotados.txt" de acordo com a idade
def funcao_organizadora_arquivo_animais_nao_adotados():

    # Abrimos o arquivo no modo de leitura
    arquivo = open('Animais não adotados.txt','r')

    # Pegamos uma lista que contém todas as linhas do arquivo
    lista_arquivo = arquivo.readlines()
    arquivo.close()
    t = len(lista_arquivo)

    # Criamos uma lista para guardar todas as idades contidas em "Animais não adotados.txt"
    lista_idade = []
    

    # Observe o padrão das posições das idades no arquivo "Animais não adotados.txt".
    # Começa na posição 1 e pula 8 posições para chegar na próxima idade.
    for i in range(1,t-6,8):

        # Tiramos "\n" do fim de lista_arquivo[i]
        lista_arquivo[i] = lista_arquivo[i].rstrip()

        # lista_arquivo[i] == "Idade: num"
        # Guardamos "Idade" e "num" na lista_auxiliar
        lista_auxiliar = lista_arquivo[i].split(': ')

        # Pegamos o valor de "num" da lista_auxiliar e o guardamos na lista_idade
        lista_idade += [int(lista_auxiliar[1])]

    # Colocamos as datas em ordem decrescente
    lista_idade.sort(reverse=True)
    
    # Abrimos o arquivo novamente
    arquivo = open('Animais não adotados.txt','w')

    # Criamos uma lista para guardar os índices dos dados já usados
    lista_indices_dos_dados_ja_colocados = []
    # Agora, para cada idade_ordem_decrescente, verificamos qual é a primeira idade da lista_arquivo que é igual
    # a idade_ordem_decrescente. Quando houver igualdade, adicionamos conteúdo a "Animais não adotados.txt".
    for idade_ordem_decrescente in lista_idade:

        for i in range(1,t-6,8):

            # Como retiramos o "\n" no processo anterior, não há mais "\n" no fim de lista_arquivo[i]
            # lista_arquivo[i] == "Idade: num"
            # Guardamos "Idade" e "num" na lista_auxiliar
            lista_auxiliar = lista_arquivo[i].split(': ')

            # Pegamos a parte inteira de "num" da lista_auxiliar
            idade_ordem_original = int(lista_auxiliar[1])

            # Comparamos idade_ordem_original e idade_ordem_decrescente
            # Quando houver igualdade, preechemos "Animais não adotados.txt" com as informações referentes
            # à idade_ordem_original

            # Além disso, se i estiver na lista "lista_indices_dos_dados_ja_colocados", significa que os dados
            # referentes a esse índice já foram colocados e, portanto, não devem ser repetidos. 
            if idade_ordem_original == idade_ordem_decrescente and i not in lista_indices_dos_dados_ja_colocados:

                # Nome
                arquivo.write(lista_arquivo[i-1])

                # Idade
                # Como retiramos o "\n" ao preencher lista_idade, precisamos colocar "\n" na parte de idade.
                arquivo.write(lista_arquivo[i] + '\n')

                # Porte
                arquivo.write(lista_arquivo[i+1])

                # Raça
                arquivo.write(lista_arquivo[i+2])

                # Lar temporário
                arquivo.write(lista_arquivo[i+3])
                
                # Nome do responsável
                arquivo.write(lista_arquivo[i+4])

                # Data de adoção
                arquivo.write(lista_arquivo[i+5])

                # Espaço em branco
                arquivo.write(lista_arquivo[i+6])

                lista_indices_dos_dados_ja_colocados += [i]
                break

    # No fim, fechamos o arquivo para evitar problemas.
    arquivo.close()



# Função que atualiza os dados do arquivo de entrevistas
def funcao_atualizar_dados_do_arquivo_de_entrevistas():

    # Abrimos o arquivo de entrevistas no modo de leitura
    arquivo = open('Entrevistas.txt','r')

    # Pegamos os dados do arquivo de entrevistas no formato de lista
    lista_dados_originais_da_entrevista = arquivo.readlines()

    t_arquivo_original = len(lista_dados_originais_da_entrevista)

    # Fechamos o arquivo
    arquivo.close()

    # Abrimos o arquivo no modo 'w'. Assim, apagamos o conteúdo que tinha em 'Entrevistas.tx'
    arquivo = open('Entrevistas.txt','w')

    # Observe que a linha das respostas começa na posição 1 e pula de 5 em 5 na lista_dados_originais_da_entrevistas.
    # Além disso, a última linha das respostas se encontra exatamente 3 posições antes da última posição
    # da lista_dados_originais_da_entrevistas.
    for i in range(1,t_arquivo_original-3,5):

        # Tiramos o '\n' da lista_dados_originais_da_entrevista[i]
        string_respostas = lista_dados_originais_da_entrevista[i].rstrip()

        # Observe que  'respostas' está no formato "resposta_1; resposta_2; resposta_3".
        # Transformamos 'respostas' em uma lista
        lista_respostas = string_respostas.split('; ')

        # lista_respostas == [ resposta_1 , resposta_2 , resposta_3 ]

        resposta_1 = lista_respostas[0]
        resposta_2 = lista_respostas[1]
        resposta_3 = lista_respostas[2]
        
        # Aqui é onde atualizamos os dados do arquivo de entrevistas.
        # Nesse ponto, verificamos se o candidato está apto para adotar algum animal após atualizarmos
        # o arquivo "Animais não adotados.txt"
        # Observe que, na função 'verificador_apto', usamos a função 'num_animais_disponiveis_porte' para
        # verificar se a atualização de 'Animais não adotados.txt' aumentou o número de animais disponíveis
        # de algum porte que estava sem animais.
        lista_retorno_apto = verificador_apto(resposta_1,resposta_2,resposta_3)

        # lista_retorno_apto = [ apto , justificativa ]
        apto = lista_retorno_apto[0]
        justificativa = lista_retorno_apto[1]

        # Agora preenchemos o arquivo 'Entrevistas.txt' usando os dados originais e usando os dados
        # atualizados de "Apto/Justificativa"
        arquivo.write(lista_dados_originais_da_entrevista[i-1])
        arquivo.write(lista_dados_originais_da_entrevista[i])
        arquivo.write('Apto: ' + apto + '\n')
        arquivo.write('Justificativa: ' + justificativa + '\n')
        arquivo.write('\n')

    # Fechamos o arquivo
    arquivo.close()



# Opção 4: Remover_dados_do_arquivo_de_animais_adotados
def remover_dados_do_arquivo_de_animais_adotados():

    # Fazemos um loop
    while True:

        # Abrimos o arquivo "Animais adotados.txt"
        arquivo = open('Animais adotados.txt','r')

        # Guardamos os dados do arquivo em "lista_dados_animais_adotados"
        lista_dados_animais_adotados = arquivo.readlines()

        t_arquivo = len(lista_dados_animais_adotados)

        arquivo.close()

        # Caso t_arquivo seja menor do que 7, então "Animais adotados.txt" está vazio
        if t_arquivo < 7:
            print('')
            time.sleep(0.2)
            print('O arquivo "Animais adotados" está vazio.')
            time.sleep(1)
            print('Você será redirecionado ao menu principal.')
            time.sleep(1)
            print('')
            break
        
        # Caso contrário, prosseguimos
        else:
            print('\n' + '-=' * 30)
            time.sleep(0.1)
            print('        Removendo dados de "Animais adotados.txt"')
            time.sleep(0.3)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nDigite 1 para remover dados de "Animais adotados.txt".')
            time.sleep(0.2)
            print('Digite 0 para voltar ao menu principal.')
            time.sleep(0.2)
            continuar = input('Digite 1 ou 0: ')
            time.sleep(0.2)

            if continuar == '1':

                # Recebemos o nome do animal a ser removido
                while True:
                    print('')
                    time.sleep(0.2)
                    nome_animal = input('Digite o nome do animal adotado: ').upper()

                    lista_retorno = verificador_nomes(nome_animal)
                    v_nome_animal = lista_retorno[0]

                    if v_nome_animal:
                        nome_animal = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite um nome válido.\n')

                # Recebemos a raça do animal a ser removido
                while True:
                    print('')
                    time.sleep(0.2)
                    raca = input('Digite a raça do animal adotado: ').upper()

                    lista_retorno = verificador_nomes(raca)

                    validade_raca = lista_retorno[0]
                    if validade_raca:
                        raca = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite uma raça válida.\n')

                # Criamos string_nome e string_raca
                string_nome = 'Nome: ' + nome_animal + '\n'
                string_raca = 'Raca: ' + raca + '\n'

                # Se string_nome e string_raca estão na lista_dados_animais_adotados, então podemos remover o animal
                # do arquivo "Animais adotados.txt"
                if string_nome in lista_dados_animais_adotados and string_raca in lista_dados_animais_adotados:
                    
                    # Para removermos o animal, iremos apagar todos dados de "Animais adotados.txt" e preencher 
                    # o arquivo "Animais adotados.txt" usando os dados da lista_dados_animais adotados, com exceção
                    # dos dados referentes ao animal que desejamos remover.
                    arquivo = open('Animais adotados.txt','w')

                    # Observe que "Nome: nome\n" aparece, primeiramente, na posição 0 e, posterioremente, nas posições
                    # múltiplas de 8. 
                    # Além disso, "Raca: raca\n" sempre aparece 3 posições após "Nome: nome\n".
                    # O limite do range é devido à última ocorrência de "Nome: nome\n" acontecer exatamente 7 posições antes
                    # do fim da lista "lista_dados_animais_adotados".                  
                    for i in range(0,t_arquivo-7,8):
                        if string_nome != lista_dados_animais_adotados[i] or string_raca != lista_dados_animais_adotados[i+3]:
                            # Nome
                            arquivo.write(lista_dados_animais_adotados[i])

                            # Idade
                            arquivo.write(lista_dados_animais_adotados[i+1])

                            # Porte
                            arquivo.write(lista_dados_animais_adotados[i+2])

                            # Raça
                            arquivo.write(lista_dados_animais_adotados[i+3])

                            # Lar temporário
                            arquivo.write(lista_dados_animais_adotados[i+4])

                            # Nome do responsável
                            arquivo.write(lista_dados_animais_adotados[i+5])

                            # Data de adoção
                            arquivo.write(lista_dados_animais_adotados[i+6])

                            # Espaço em branco
                            arquivo.write(lista_dados_animais_adotados[i+7])

                    arquivo.close()

                # Caso string_nome e string_raca não estejam na lista
                else:
                    print('')
                    time.sleep(0.2)
                    print('Não há nenhum animal com nome ' + nome_animal + ' e raça ' + raca + '.')
                    time.sleep(1)

            # Caso o usuário queira retornar ao menu principal
            elif continuar == '0':
                print('')
                time.sleep(0.5)
                print('VOLTANDO AO MENU PRINCIPAL...')
                time.sleep(1)
                print('')
                time.sleep(0.2)
                break

            else:
                print('\n'+ '-=' * 30)
                time.sleep(0.1)
                print(' '*26 + 'ERRO')
                time.sleep(0.2)
                print('-=' * 30)
                time.sleep(0.2)
                print('\nPor favor, digite 1 ou 0.\n')
                time.sleep(1)



# Opção 5: Remover dados do arquivo de animais não adotados
def remover_dados_do_arquivo_de_animais_nao_adotados():

    # Situação análoga à "Opção 4: Remover_dados_do_arquivo_de_animais_adotados".
    while True:
        arquivo = open('Animais não adotados.txt','r')

        lista_dados_animais_nao_adotados = arquivo.readlines()

        t_arquivo = len(lista_dados_animais_nao_adotados)

        arquivo.close()

        if t_arquivo < 7:
            print('')
            time.sleep(0.2)
            print('O arquivo "Animais não adotados" está vazio.')
            time.sleep(1)
            print('Você será redirecionado ao menu principal.')
            time.sleep(1)
            print('')
            break

        else:
            print('\n' + '-=' * 30)
            time.sleep(0.1)
            print('       Removendo dados de "Animais não adotados.txt"')
            time.sleep(0.3)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nDigite 1 para remover dados de "Animais não adotados.txt".')
            time.sleep(0.2)
            print('Digite 0 para voltar ao menu principal.')
            time.sleep(0.2)
            continuar = input('Digite 1 ou 0: ')
            time.sleep(0.2)

            if continuar == '1':
                while True:
                    print('')
                    time.sleep(0.2)
                    nome_animal = input('Digite o nome do animal não adotado: ').upper()

                    lista_retorno = verificador_nomes(nome_animal)
                    v_nome_animal = lista_retorno[0]

                    if v_nome_animal:
                        nome_animal = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite um nome válido.\n')

                while True:
                    print('')
                    time.sleep(0.2)
                    raca = input('Digite a raça do animal não adotado: ').upper()

                    lista_retorno = verificador_nomes(raca)

                    validade_raca = lista_retorno[0]
                    if validade_raca:
                        raca = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite uma raça válida.\n')


                string_nome = 'Nome: ' + nome_animal + '\n'
                string_raca = 'Raca: ' + raca + '\n'

                if string_nome in lista_dados_animais_nao_adotados and string_raca in lista_dados_animais_nao_adotados:

                    arquivo = open('Animais não adotados.txt','w')

                    for i in range(0,t_arquivo-7,8):
                        if string_nome != lista_dados_animais_nao_adotados[i] or string_raca != lista_dados_animais_nao_adotados[i+3]:
                            arquivo.write(lista_dados_animais_nao_adotados[i])
                            arquivo.write(lista_dados_animais_nao_adotados[i+1])
                            arquivo.write(lista_dados_animais_nao_adotados[i+2])
                            arquivo.write(lista_dados_animais_nao_adotados[i+3])
                            arquivo.write(lista_dados_animais_nao_adotados[i+4])
                            arquivo.write(lista_dados_animais_nao_adotados[i+5])
                            arquivo.write(lista_dados_animais_nao_adotados[i+6])
                            arquivo.write(lista_dados_animais_nao_adotados[i+7])

                    arquivo.close()

                else:
                    print('')
                    time.sleep(0.2)
                    print('Não há nenhum animal com nome ' + nome_animal + ' e raça ' + raca + '.')
                    time.sleep(1)

            elif continuar == '0':
                print('')
                time.sleep(0.5)
                print('VOLTANDO AO MENU PRINCIPAL...')
                time.sleep(1)
                print('')
                time.sleep(0.2)
                break

            else:
                print('\n'+ '-=' * 30)
                time.sleep(0.1)
                print(' '*26 + 'ERRO')
                time.sleep(0.2)
                print('-=' * 30)
                time.sleep(0.2)
                print('\nPor favor, digite 1 ou 0.\n')
                time.sleep(1)



# Opção 6: Remover dados do arquivo de entrevistas
def remover_dados_do_arquivo_de_entrevistas():

    # Situação análoga à "Opção 4: Remover_dados_do_arquivo_de_animais_adotados", mas com 3 pequenas diferenças.
    while True:

        arquivo = open('Entrevistas.txt','r')

        lista_dados_entrevistas = arquivo.readlines()

        t_arquivo = len(lista_dados_entrevistas)

        arquivo.close()

        # Primeira diferença:
        # Ao invés de 7, t_arquivo tem que ser maior ou igual a 4
        if t_arquivo < 4:
            print('')
            time.sleep(0.2)
            print('O arquivo "Entrevistas" está vazio.')
            time.sleep(1)
            print('Você será redirecionado ao menu principal.')
            time.sleep(1)
            print('')
            break

        else:
            print('\n' + '-=' * 30)
            time.sleep(0.1)
            print('           Removendo dados de "Entrevistas.txt"')
            time.sleep(0.3)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nDigite 1 para remover dados de "Entrevistas.txt".')
            time.sleep(0.2)
            print('Digite 0 para voltar ao menu principal.')
            time.sleep(0.2)
            continuar = input('Digite 1 ou 0: ')
            time.sleep(0.2)

            if continuar == '1':
                while True:
                    print('')
                    time.sleep(0.2)
                    nome_candidato = input('Digite o nome do candidato: ').upper()

                    lista_retorno = verificador_nomes(nome_candidato)
                    v_nome_candidato = lista_retorno[0]

                    if v_nome_candidato:
                        nome_candidato = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite um nome válido.\n')


                string_nome = 'Nome: ' + nome_candidato + '\n'

                if string_nome in lista_dados_entrevistas:

                    arquivo = open('Entrevistas.txt','w')


                    # Segunda e Terceira diferenças: limite do range e padrão do arquivo "Entrevistas.txt".

                    # O padrão do arquivo "Entrevistas" é:
                    # "Nome: nome\n"
                    # "resposta_1; resposta_2; resposta_3\n"
                    # "Apto: apto\n"
                    # "Justificativa: justificativa\n"
                    # "\n"
                    # "Nome: nome\n"
                    # ... (e assim sucessivamente)
                    for i in range(0,t_arquivo-4,5):
                        if string_nome != lista_dados_entrevistas[i]:
                            arquivo.write(lista_dados_entrevistas[i])
                            arquivo.write(lista_dados_entrevistas[i+1])
                            arquivo.write(lista_dados_entrevistas[i+2])
                            arquivo.write(lista_dados_entrevistas[i+3])
                            arquivo.write(lista_dados_entrevistas[i+4])

                    arquivo.close()

                else:
                    print('')
                    time.sleep(0.2)
                    print('Não há nenhum candidato chamado ' + nome_candidato +'.')
                    time.sleep(1)

            elif continuar == '0':
                print('')
                time.sleep(0.5)
                print('VOLTANDO AO MENU PRINCIPAL...')
                time.sleep(1)
                print('')
                time.sleep(0.2)
                break

            else:
                print('\n'+ '-=' * 30)
                time.sleep(0.1)
                print(' '*26 + 'ERRO')
                time.sleep(0.2)
                print('-=' * 30)
                time.sleep(0.1)
                print('\nPor favor, digite 1 ou 0.\n')
                time.sleep(1)



# Opção 7: Modificar dados do arquivo animais adotados
def modificar_dados_do_arquivo_de_animais_adotados():

    # Fazemos um loop
    while True:

        # Abrimos o arquivo "Animais adotados.txt".
        arquivo = open('Animais adotados.txt','r')

        # Guardamos os dados do arquivo em "lista_dados_animais_adotados".
        lista_dados_animais_adotados = arquivo.readlines()

        t_arquivo = len(lista_dados_animais_adotados)

        arquivo.close()

        # Caso t_arquivo seja menor do que 7, então "Animais adotados.txt" está vazio.
        if t_arquivo < 7:
            print('')
            time.sleep(0.2)
            print('O arquivo "Animais adotados" está vazio.')
            time.sleep(1)
            print('Você será redirecionado ao menu principal.')
            time.sleep(1)
            print('')
            break

        # Caso contrário, prosseguimos
        else:
            print('\n' + '-=' * 30)
            time.sleep(0.1)
            print('        Modificando dados de "Animais adotados.txt"')
            time.sleep(0.3)
            print('-=' * 30)
            time.sleep(0.1)
            print('\nDigite 1 para modificar dados de "Animais adotados.txt".')
            time.sleep(0.2)
            print('Digite 0 para voltar ao menu principal.')
            time.sleep(0.2)
            continuar = input('Digite 1 ou 0: ')
            time.sleep(0.2)

            if continuar == '1':

                # Recebemos o nome do animal a ter os dados modificados
                while True:
                    print('')
                    time.sleep(0.2)
                    nome_animal = input('\nDigite o nome do animal adotado que você quer modificar os dados: ').upper()

                    lista_retorno = verificador_nomes(nome_animal)
                    v_nome_animal = lista_retorno[0]

                    if v_nome_animal:
                        nome_animal = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite um nome válido.\n')

                # Recebemos a raça do animal a ter os dados modificados
                while True:
                    print('')
                    time.sleep(0.2)
                    raca = input('Digite a raça do animal adotado que você quer modificar os dados: ').upper()

                    lista_retorno = verificador_nomes(raca)

                    validade_raca = lista_retorno[0]
                    if validade_raca:
                        raca = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite uma raça válida.\n')


                # Criamos string_nome e string_raca
                string_nome = 'Nome: ' + nome_animal + '\n'
                string_raca = 'Raca: ' + raca + '\n'

                # Se string_nome e string_raca estão na lista_dados_animais_adotados, então podemos modificar os dados do animal
                # no arquivo "Animais adotados.txt"
                if string_nome in lista_dados_animais_adotados and string_raca in lista_dados_animais_adotados:

                    # Para modificarmos os dados do animal, iremos apagar todos dados de "Animais adotados.txt" e preencher 
                    # o arquivo "Animais adotados.txt" usando os dados da lista_dados_animais adotados, com exceção
                    # dos dados referentes ao animal que desejamos modificar. 
                    # Quanto aos dados do animal que desejamos modificar, iremos pedir os novos dados ao usuário.
                    # Escrevemos os novos dados no arquivo "Animais adotados.txt".
                    arquivo = open('Animais adotados.txt','w')


                    # Observe que "Nome: nome\n" aparece, primeiramente, na posição 0 e, posterioremente, nas posições
                    # múltiplas de 8.
                    # Além disso, "Raca: raca\n" sempre aparece 3 posições após "Nome: nome\n"
                    # O limite do range é devido à última ocorrência de "Nome: nome\n" acontecer exatamente 7 posições antes
                    # do fim da lista "lista_dados_animais_adotados".  
                    for i in range(0,t_arquivo-7,8):

                        # Quando encontrarmos string_nome e string_raca na lista_dados_animais_adotados,
                        # devemos pedir os novos dados do animal
                        if string_nome == lista_dados_animais_adotados[i] and string_raca == lista_dados_animais_adotados[i+3]:

                            # De posse dos novos dados, preenchemos o arquivo com eles.
                            lista_retorno = recebendo_entradas_animais_adotados()
                            arquivo.write('Nome: ' + lista_retorno[0] + '\n')
                            arquivo.write('Idade: ' + lista_retorno[1] + '\n')
                            arquivo.write('Porte: ' + lista_retorno[2] + '\n')
                            arquivo.write('Raca: ' + lista_retorno[3] + '\n')
                            arquivo.write('Lar temporario: ' +lista_retorno[4] + '\n')
                            arquivo.write('Nome do responsavel: ' + lista_retorno[5] + '\n')
                            arquivo.write('Data de adocao: ' + lista_retorno[6] + '\n')
                            arquivo.write('\n')

                        # Em todas as outras linhas que não contém os dados que queremos modificar, apenas escrevemos
                        # os dados antigos.
                        else:
                            arquivo.write(lista_dados_animais_adotados[i])
                            arquivo.write(lista_dados_animais_adotados[i+1])
                            arquivo.write(lista_dados_animais_adotados[i+2])
                            arquivo.write(lista_dados_animais_adotados[i+3])
                            arquivo.write(lista_dados_animais_adotados[i+4])
                            arquivo.write(lista_dados_animais_adotados[i+5])
                            arquivo.write(lista_dados_animais_adotados[i+6])
                            arquivo.write(lista_dados_animais_adotados[i+7])

                    arquivo.close()

                # Caso o animal que queremos modificar os dados não estejam na lista
                else:
                    print('')
                    time.sleep(0.2)
                    print('Não há nenhum animal com nome ' + nome_animal + ' e raça ' + raca + '.')
                    time.sleep(1)

            elif continuar == '0':
                print('')
                time.sleep(0.5)
                print('VOLTANDO AO MENU PRINCIPAL...')
                time.sleep(1)
                print('')
                time.sleep(0.2)
                break

            else:
                print('\n'+ '-=' * 30)
                time.sleep(0.1)
                print(' '*26 + 'ERRO')
                time.sleep(0.2)
                print('-=' * 30)
                time.sleep(0.1)
                print('\nPor favor, digite 1 ou 0.\n')



# Opção 8: Modificando informações do arquivo de animais não adotados
def modificar_dados_do_arquivo_de_animais_nao_adotados():

    # Situação análoga à "Opção 7: Modificar dados do arquivo animais adotados".
    while True:
        arquivo = open('Animais não adotados.txt','r')

        lista_dados_animais_nao_adotados = arquivo.readlines()

        t_arquivo = len(lista_dados_animais_nao_adotados)

        arquivo.close()

        if t_arquivo < 7:
            print('')
            time.sleep(0.2)
            print('O arquivo "Animais não adotados" está vazio.')
            time.sleep(1)
            print('Você será redirecionado ao menu principal.')
            time.sleep(1)
            print('')
            break

        else:
            print('\n' + '-=' * 30)
            time.sleep(0.1)
            print('       Modificando dados de "Animais não adotados.txt"')
            time.sleep(0.3)
            print('-=' * 30)
            time.sleep(0.1)
            print('Digite 1 para modificar dados de "Animais não adotados.txt".')
            time.sleep(0.2)
            print('Digite 0 para voltar ao menu principal.')
            time.sleep(0.2)
            continuar = input('Digite 1 ou 0: ')
            time.sleep(0.2)

            if continuar == '1':

                while True:
                    print('')
                    time.sleep(0.2)
                    nome_animal = input('\nDigite o nome do animal não adotado que você quer modificar os dados: ').upper()

                    lista_retorno = verificador_nomes(nome_animal)
                    v_nome_animal = lista_retorno[0]

                    if v_nome_animal:
                        nome_animal = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite um nome válido.\n')

                while True:
                    print('')
                    time.sleep(0.2)
                    raca = input('Digite a raça do animal não adotado que você quer modificar os dados: ').upper()

                    lista_retorno = verificador_nomes(raca)

                    validade_raca = lista_retorno[0]
                    if validade_raca:
                        raca = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite uma raça válida.\n')

                string_nome = 'Nome: ' + nome_animal + '\n'
                string_raca = 'Raca: ' + raca + '\n'

                if string_nome in lista_dados_animais_nao_adotados and string_raca in lista_dados_animais_nao_adotados:

                    arquivo = open('Animais não adotados.txt','w')

                    for i in range(0,t_arquivo-7,8):
                        if string_nome == lista_dados_animais_nao_adotados[i] and string_raca == lista_dados_animais_nao_adotados[i+3]:
                            lista_retorno = recebendo_entradas_animais_nao_adotados()
                            arquivo.write('Nome: ' + lista_retorno[0] + '\n')
                            arquivo.write('Idade: ' + lista_retorno[1] + '\n')
                            arquivo.write('Porte: ' + lista_retorno[2] + '\n')
                            arquivo.write('Raca: ' + lista_retorno[3] + '\n')
                            arquivo.write('Lar temporario: ' +lista_retorno[4] + '\n')
                            arquivo.write('Nome do responsavel: ' + lista_retorno[5] + '\n')
                            arquivo.write('Data de adocao: ' + lista_retorno[6] + '\n')
                            arquivo.write('\n')


                        else:
                            arquivo.write(lista_dados_animais_nao_adotados[i])
                            arquivo.write(lista_dados_animais_nao_adotados[i+1])
                            arquivo.write(lista_dados_animais_nao_adotados[i+2])
                            arquivo.write(lista_dados_animais_nao_adotados[i+3])
                            arquivo.write(lista_dados_animais_nao_adotados[i+4])
                            arquivo.write(lista_dados_animais_nao_adotados[i+5])
                            arquivo.write(lista_dados_animais_nao_adotados[i+6])
                            arquivo.write(lista_dados_animais_nao_adotados[i+7])

                    arquivo.close()

                else:
                    print('')
                    time.sleep(0.2)
                    print('Não há nenhum animal com nome ' + nome_animal + ' e raça ' + raca + '.')
                    time.sleep(1)

            elif continuar == '0':
                print('')
                time.sleep(0.5)
                print('VOLTANDO AO MENU PRINCIPAL...')
                time.sleep(1)
                print('')
                time.sleep(0.2)
                break

            else:
                print('\n'+ '-=' * 30)
                time.sleep(0.1)
                print(' '*26 + 'ERRO')
                time.sleep(0.2)
                print('-=' * 30)
                time.sleep(0.1)
                print('\nPor favor, digite 1 ou 0.\n')



# Opção 9: Modificando dados do arquivo de entrevistas
def modificar_dados_do_arquivo_de_entrevistas():

    # Situação análoga à "Opção 7: Modificar dados do arquivo animais adotados",
    # mas com 3 pequenas diferenças.
    while True:

        arquivo = open('Entrevistas.txt','r')

        lista_dados_entrevistas = arquivo.readlines()

        t_arquivo = len(lista_dados_entrevistas)

        arquivo.close()

        # Primeira diferença:
        # Ao invés de 7, t_arquivo tem que ser maior ou igual a 4
        if t_arquivo < 4:
            print('')
            time.sleep(0.2)
            print('O arquivo "Entrevistas" está vazio.')
            time.sleep(1)
            print('Você será redirecionado ao menu principal.')
            time.sleep(1)
            print('')
            break

        else:
            print('\n' + '-=' * 30)
            time.sleep(0.1)
            print('          Modificando dados de "Entrevistas.txt"')
            time.sleep(0.3)
            print('-=' * 30)
            time.sleep(0.1)
            print('Digite 1 para modificar dados de "Entrevistas.txt".')
            time.sleep(0.2)
            print('Digite 0 para voltar ao menu principal.')
            time.sleep(0.2)
            continuar = input('Digite 1 ou 0: ')
            time.sleep(0.2)

            if continuar == '1':

                while True:
                    print('')
                    time.sleep(0.2)
                    nome_candidato = input('\nDigite o nome do candidato que você quer modificar os dados: ').upper()

                    lista_retorno = verificador_nomes(nome_candidato)
                    v_nome_candidato = lista_retorno[0]

                    if v_nome_candidato:
                        nome_candidato = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite um nome válido.\n')


                string_nome = 'Nome: ' + nome_candidato + '\n'

                if string_nome in lista_dados_entrevistas:

                    arquivo = open('Entrevistas.txt','w')
                    
                    # Segunda e Terceira diferenças: limite do range e padrão do arquivo "Entrevistas.txt".

                    # O padrão do arquivo "Entrevistas" é:
                    # "Nome: nome\n"
                    # "resposta_1; resposta_2; resposta_3\n"
                    # "Apto: apto\n"
                    # "Justificativa: justificativa\n"
                    # "\n"
                    # "Nome: nome\n"
                    # ... (e assim sucessivamente)
                    for i in range(0,t_arquivo-4,5):
                        if string_nome == lista_dados_entrevistas[i]:
                            lista_retorno = recebendo_entradas_entrevistas()
                            arquivo.write('Nome: ' + lista_retorno[0] + '\n')
                            arquivo.write(lista_retorno[1] + '\n')
                            arquivo.write('Apto: ' + lista_retorno[2] + '\n')
                            arquivo.write('Justificativa: ' + lista_retorno[3] + '\n')
                            arquivo.write('\n')

                        else:
                            arquivo.write(lista_dados_entrevistas[i])
                            arquivo.write(lista_dados_entrevistas[i+1])
                            arquivo.write(lista_dados_entrevistas[i+2])
                            arquivo.write(lista_dados_entrevistas[i+3])
                            arquivo.write(lista_dados_entrevistas[i+4])

                    arquivo.close()

                else:
                    print('')
                    time.sleep(0.2)
                    print('Não há nenhum candidato chamado ' + nome_candidato +'.')
                    time.sleep(1)

            elif continuar == '0':
                print('')
                time.sleep(0.5)
                print('VOLTANDO AO MENU PRINCIPAL...')
                time.sleep(1)
                print('')
                time.sleep(0.2)
                break

            else:
                print('\n'+ '-=' * 30)
                time.sleep(0.1)
                print(' '*26 + 'ERRO')
                time.sleep(0.2)
                print('-=' * 30)
                time.sleep(0.1)
                print('\nPor favor, digite 1 ou 0.\n')
                time.sleep(1)



# Opção 10: Ler dados do arquivo de animais adotados
def ler_dados_do_arquivo_de_animais_adotados():

    # Abrimos o arquivo "Animais adotados.txt"
    arquivo = open('Animais adotados.txt','r')

    # Pegamos os dados do arquivo em formato de lista
    lista_arquivo = arquivo.readlines()

    t_arquivo = len(lista_arquivo)

    arquivo.close()

    # Caso t_arquivo seja menor do que 7, então "Animais adotados.txt" está vazio.
    if t_arquivo < 7:
        print('')
        time.sleep(0.2)
        print('O arquivo "Animais adotados" está vazio.')
        time.sleep(1)
        print('Você será redirecionado ao menu principal.')
        time.sleep(1)
        print('')

    # Caso contrários, iremos printar todas as linhas de lista_arquivo.
    else:
        print('\n' + '-=' * 30)
        time.sleep(0.1)
        print('          Lendo os dados de "Animais adotados.txt"')
        time.sleep(0.3)
        print('-=' * 30)
        time.sleep(0.1)
        print('')
        for linha in lista_arquivo:
            
            # Removemos o "\n" de todas as linhas de lista_arquivo
            linha = linha.rstrip()
            print(linha)
            time.sleep(0.3)

        voltar = input('Digite qualquer coisa para voltar ao menu principal ')
        time.sleep(0.2)
        print('')
        time.sleep(0.2)
        


# Opção 11: Ler dados do arquivo de animais não adotados
def ler_dados_do_arquivo_de_animais_nao_adotados():

    # Situação análoga à "Opção 10: Ler dados do arquivo de animais adotados".
    arquivo = open('Animais não adotados.txt','r')
    lista_arquivo = arquivo.readlines()

    t_arquivo = len(lista_arquivo)

    arquivo.close()

    if t_arquivo < 7:
        print('')
        time.sleep(0.2)
        print('O arquivo "Animais não adotados" está vazio.')
        time.sleep(1)
        print('Você será redirecionado ao menu principal.')
        time.sleep(1)
        print('')

    else:
        print('\n' + '-=' * 30)
        time.sleep(0.1)
        print('         Lendo os dados de "Animais não adotados.txt"')
        time.sleep(0.3)
        print('-=' * 30)
        time.sleep(0.1)
        print('')
        for linha in lista_arquivo:
            linha = linha.rstrip()
            print(linha)
            time.sleep(0.3)

        voltar = input('Digite qualquer coisa para voltar ao menu principal ')
        time.sleep(0.2)
        print('')
        time.sleep(0.2)



# Opção 12: Ler dados do arquivo de entrevistas
def ler_dados_do_arquivo_de_entrevistas():

    # Situação análoga à "Opção 10: Ler dados do arquivo de animais adotados".
    arquivo = open('Entrevistas.txt','r')
    lista_arquivo = arquivo.readlines()

    t_arquivo = len(lista_arquivo)

    arquivo.close()

    if t_arquivo < 4:
        print('')
        time.sleep(0.2)
        print('O arquivo "Entrevistas" está vazio.')
        time.sleep(1)
        print('Você será redirecionado ao menu principal.')
        time.sleep(1)
        print('')

    else:
        print('\n' + '-=' * 30)
        time.sleep(0.1)
        print('             Lendo os dados de "Entrevistas.txt"')
        time.sleep(0.3)
        print('-=' * 30)
        time.sleep(0.1)
        print('')
        for linha in lista_arquivo:
            linha = linha.rstrip()
            print(linha)
            time.sleep(0.3)

        voltar = input('Digite qualquer coisa para voltar ao menu principal ')
        time.sleep(0.2)
        print('')
        time.sleep(0.2)



# Opção 13: Mostrar as fichas de animais disponíveis para um candidato
def mostrar_as_fichas_de_animais_disponiveis_para_um_candidato():

    while True:

        arquivo = open('Entrevistas.txt','r')

        lista_dados_entrevistas = arquivo.readlines()

        t_arquivo_entrevistas = len(lista_dados_entrevistas)

        arquivo.close()

        # Verificamos se o arquivo está vazio ou não
        if t_arquivo_entrevistas < 4:
            print('')
            time.sleep(0.2)
            print('O arquivo "Entrevistas" está vazio.')
            time.sleep(1)
            print('Você será redirecionado ao menu principal.')
            time.sleep(1)
            print('')
            break

        else:
            print('\n' + '-=' * 30)
            time.sleep(0.1)
            print('          Verificando a situação de um candidato')
            time.sleep(0.3)
            print('-=' * 30)
            time.sleep(0.1)
            print('Digite 1 para ver a situação de um certo candidato.')
            time.sleep(0.2)
            print('Digite 0 para voltar ao menu principal.')
            time.sleep(0.2)
            continuar = input('Digite 1 ou 0: ')

            if continuar == '1':

                # Recebemos o nome do candidato
                while True:
                    print('')
                    time.sleep(0.2)
                    nome_candidato = input('\nDigite o nome do candidato de interesse: ').upper()

                    lista_retorno = verificador_nomes(nome_candidato)
                    v_nome_candidato = lista_retorno[0]

                    if v_nome_candidato:
                        nome_candidato = lista_retorno[1]
                        break

                    else:
                        print('\n'+ '-=' * 30)
                        time.sleep(0.1)
                        print(' '*26 + 'ERRO')
                        time.sleep(0.2)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('\nPor favor, digite um nome válido.\n') 
                        time.sleep(1)

                string_nome = 'Nome: ' + nome_candidato + '\n'

                # Verificamos se o candidato está na lista_dados_entrevistas
                if string_nome in lista_dados_entrevistas:
                    
                    # Procuramos os campos de "resposta_1; resposta_2; resposta_3" e da justificativa
                    # desse candidato

                    # Lembrando que o  padrão do arquivo "Entrevistas" é:
                    # "Nome: nome\n"
                    # "resposta_1; resposta_2; resposta_3\n"
                    # "Apto: apto\n"
                    # "Justificativa: justificativa\n"
                    # "\n"
                    # "Nome: nome\n"
                    # ... (e assim sucessivamente)
                    for i in range(0,t_arquivo_entrevistas-4,5):
                        if lista_dados_entrevistas[i]==string_nome:
                            string_respostas = lista_dados_entrevistas[i+1]
                            justificativa = lista_dados_entrevistas[i+3]
                            break
                    
                    # string_respostas = 'resposta_1; resposta_2; resposta_3\n'
                    lista_respostas = string_respostas.split('; ')

                    # lista_respostas = [resposta_1, resposta_2, resposta_3\n]

                    porte = lista_respostas[2].rstrip()
                    
                    # Agora abrimos o arquivo "Animais não adotados.txt"
                    arquivo = open('Animais não adotados.txt','r')

                    # Pegamos os dados do arquivo no formato de lista
                    lista_dados_animais_nao_adotados = arquivo.readlines()
                    t_arquivo = len(lista_dados_animais_nao_adotados)
                    arquivo.close()

                    # Retiramos o "\n" no fim de todas os elementos de lista_dados_animais_nao_adotados
                    for i in range(len(lista_dados_animais_nao_adotados)):
                        lista_dados_animais_nao_adotados[i] = lista_dados_animais_nao_adotados[i].rstrip()

                    # Caso justificativa seja vazia, isto é, o candidato está apto, mostraremos as fichas dos 
                    # animais disponíveis
                    if justificativa == 'Justificativa: \n':
                        print('\n' + '-=' * 30)
                        time.sleep(0.1)
                        print('       Lendo os dados dos animais passíveis de adoção')
                        time.sleep(0.3)
                        print('-=' * 30)
                        time.sleep(0.1)
                        print('')

                        # Caso o porte máximo do animal que esse candidato pode adotar seja "Grande",
                        # mostramos todos os animais do arquivo "Animais não adotados.txt"
                        if porte == 'GRANDE':

                            # Lembrando que o padrão do arquivo "Animais não adotados" é (desconsiderando o "\n"):
                            # "Nome: nome"
                            # "Idade: idade"
                            # "Porte: porte"
                            # "Raca: raca"
                            # "Lar temporario: lar temporario"
                            # "Nome do responsavel: "
                            # "Data de adocao: "
                            # ""
                            # "Nome: nome"
                            # ... (E assim sucessivamente)
                            for i in range(2,t_arquivo-5,8):


                                    print(lista_dados_animais_nao_adotados[i-2])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i-1])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i+1])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i+2])
                                    time.sleep(0.3)

                                    # Não mostraremos os campos "Nome do responsável" e "Data de adocao" por
                                    # serem irrelevantes para o candidato.
                                    print(lista_dados_animais_nao_adotados[i+5])
                                    time.sleep(0.3)


                        elif porte =='PEQUENO':

                            # Situação análoga ao "if porte=='Grande'", mas, dessa vez, só mostraremos as 
                            # fichas dos animais pequenos
                            for i in range(2,t_arquivo-5,8):
                                if lista_dados_animais_nao_adotados[i] == 'Porte: PEQUENO':

                                    print(lista_dados_animais_nao_adotados[i-2])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i-1])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i+1])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i+2])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i+5])
                                    time.sleep(0.3)

                        elif porte == 'MEDIO':

                            # Situação análoga ao "if porte=='Grande'", mas, dessa vez, só mostraremos as 
                            # fichas dos animais pequenos e médios.
                            for i in range(2,t_arquivo-5,8):
                                if lista_dados_animais_nao_adotados[i] == 'Porte: MEDIO' or lista_dados_animais_nao_adotados[i] == 'Porte: PEQUENO':

                                    print(lista_dados_animais_nao_adotados[i-2])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i-1])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i+1])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i+2])
                                    time.sleep(0.3)
                                    print(lista_dados_animais_nao_adotados[i+5])
                                    time.sleep(0.3)

                        voltar = input('Digite qualquer coisa para voltar ao menu "Verificando a situação de um candidato" ')
                        time.sleep(0.2)
                        print('')
                        time.sleep(0.2)
                    # Caso haja justificativa, o candidato não está apto a adotar nenhum animal. 
                    else:
                        print('O candidato não pode adotar nenhum animal.')
                        time.sleep(1)

                        justificativa = justificativa.rstrip()

                        print(justificativa)
                        time.sleep(1)

                # Caso o nome do candidato não esteja na lista
                else:
                    print('')
                    time.sleep(0.2)
                    print('Não há nenhum candidato chamado ' + nome_candidato +'.')
                    time.sleep(1)

            elif continuar == '0':
                print('')
                time.sleep(0.5)
                print('VOLTANDO AO MENU PRINCIPAL...')
                time.sleep(1)
                print('')
                time.sleep(0.2)
                break

            else:
                print('\n'+ '-=' * 30)
                time.sleep(0.1)
                print(' '*26 + 'ERRO')
                time.sleep(0.2)
                print('-=' * 30)
                time.sleep(0.1)
                print('\nPor favor, digite 1 ou 0.\n')
                time.sleep(1)