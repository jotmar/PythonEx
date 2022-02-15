def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return(f'Com {idade} anos: NÃO VOTA.')
    elif idade >= 18 and idade < 65:
        return(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade >= 65 or idade < 18 and idade >= 16:
        return(f'Com {idade} anos: VOTO OPCIONAL.')


nascimento = int(input('Que ano você nasceu? '))
print(voto(nascimento))
