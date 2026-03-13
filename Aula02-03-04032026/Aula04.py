carro=true
combustivel=true
# qual a condição pra que este carro funcione?

if carro==true and combustivel == true: # <<< ambas condições são verdadeiras: é o que eu quero
    print("Meu fusquinha está redando.")
else:
     print("Não sobrou nada pro fusquinha.")


if not carro and not combustivel: # <<< ambas as condições são verdadeiras: é o que eu quero
    print("Meu fusquinha está rodando.")
else(carro==false or combustivel==false:
print("Não sobrou nada pro fusquinha.")
                print('*'*15)

semana = 3
if semana == 1:
 print("Domingo")
elif semana == 2:
 print("Segunda-feira")
elif semana == 3:
 print("Terça-feira")
elif semana == 4:
 print("Quarta-feira")
elif semana == 5:
 print("Quinta-feira")
elif semana == 6:
 print("Sexta-feira")
elif semana == 7:
 print("Sábado")
else: # O 'else' funciona como o 'default'
 print("Dia inválido")


try:
     mes = int(input("informe o mês:"))
     match mes:
        case 1:
            print("Janeiro")
        case 2:
            print("Fevereiro")
        case 3:
            print("Março")
        case 5:
            print("maio")
        case 6:
            print("junho")
        case 7:
            print("julho")
        case 8:
            print("agosto")
        case 9:
            print("setembro")
        case 10:
            print("outubro")
        case 11:
            print("novenbro")
        case 12:
            print("dezembro")
            case
        except ValuError:
            print("entrada inválida.por favor, digite um número inteiro.")

                            


 math mes
 numero_mes = int(input("Digite um número de 1 a 12: "))
 match numero_mes:
 case 1:
 print("O número 1 corresponde a Janeiro.")
 # Inclua todos os outros meses aqui!
 case 12:
 print("O número 12 corresponde a Dezembro.")
 case _:
 print(f"Número {numero_mes} inválido. Digite entre 1 e 12.")
except ValueError:
 print("Entrada inválida. Por favor, digite um número inteiro.")