#Identificar a variável#
'''
5. Média do Aluno com Optativa:
Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
recuperação, de acordo com as informações abaixo:
'''

# nota1=float(input('Primeira Nota:'))
# nota2=float(input('segunda nota:'))
# optativa=float(input('tem notaoptativa)?'))

# if optativa == -1:
#     media=(nota1+nota2)/2
# else: 
#     if optativa > nota1:
#         media=(optativa+nota2)/2
#     else:
#         media=(optativa+nota1)/2 
# if media >= 6.0:
#     resultado='APROVADO'
# elif media >= 3.0:
#     resultado='RECUPERAÇÃO'
# else:
#     resultado='REPROVADO'

# print(f'Média final:{media}; resultado: {resultado}')


'''
5. Média do Aluno com Optativa:
Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
recuperação, de acordo com as informações abaixo:
'''
POTENCIA = 3
lampadas = 0
largura = float(input('largura:'))
comprimento=float(input('comprimento:'))

area=largura*comprimento

lampadas=area/POTENCIA

print(f'são necessárias {round(lampadas)} lâmpadas para iluminar um cômodo de {area}m2.')


