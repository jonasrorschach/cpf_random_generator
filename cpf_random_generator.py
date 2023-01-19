'''
Baseado na explicação do algoritmo de números de CPF do
site: https://www.macoratti.net/alg_cpf.htm
'''

import random


while True:

    quest = input('Deseja criar um novo CPF? [S/n]')


    if quest.upper() == 'S':


        cpf = ''

        for i in range(0, 11):   # nesse for ele vai gerar o cpf aleatório
            num_cpf_raw = random.randint(0,9)
            cpf += str(num_cpf_raw)  # armazena os dígitos



        cpf_9_num_raw = cpf[0:8] # fatia quais números queremos para a conta
        x = 10
        cpf_conta_soma = 0



        cpf_conta_vezes = 0
        for i in range(0, 8):
            cpf_conta_vezes += int(cpf_9_num_raw[i]) * x # vai multiplicar da esquerda para a direita
            x -= 1


        conta_resto_prim_dig_cpf = cpf_conta_vezes % 11 # 


        if conta_resto_prim_dig_cpf < 2: # se for menor que 2 será 0 nosso primeiro dígito verificador
            prim_dig_veri_cpf = 0

        elif conta_resto_prim_dig_cpf >= 2: # se não vai ser 11 menos o resto da conta
            prim_dig_veri_cpf = 11 - conta_resto_prim_dig_cpf












        cpf += str(prim_dig_veri_cpf) # aqui vai entrar o primeiro
                                                # dígito verificador para calcularmos
                                                # o segundo dígito

        cpf_conta_vezes += 0
        cpf_10_num_raw = cpf[0:9]
        y = 10

        for i in range(0, 9):
            cpf_conta_vezes += int(cpf_10_num_raw[i]) * y
            y -= 1

        conta_resto_seg_dig_cpf = cpf_conta_vezes % 11

        if conta_resto_seg_dig_cpf < 2:
            seg_dig_veri_cpf = 0

        elif conta_resto_seg_dig_cpf >= 2:
            seg_dig_veri_cpf = 11 - conta_resto_seg_dig_cpf

        cpf += str(seg_dig_veri_cpf)








        cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
        print(f'novo CPF: {cpf}')
    
    
    
    
    
    elif quest.upper() == 'N':
        print('Terminando programa...')
        break

    else:
        print('Por favor apenas digite "S" para "sim" ou "N" para "não"')