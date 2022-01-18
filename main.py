
# sistema de cadastro
l1 = '1'
l2 = '2'
while True:
    aswr1 = input('registrar um novo cadastro [1] efetuar login [2] ')
    print()

    if aswr1 == l1:
        cad_usr = input('digite o usuário >(')
        print()
        while True:
            cad_psw = input('digite a senha >(')
            print()
            cad_pswck = input('confirme a senha >(')
            if cad_psw == cad_pswck:
                print('usuario cadastrado')
                print()
                break
                
            else:
                print('as senhas não coincidem')
                continue
    if aswr1 == l2:
        while True:
            lgn_usr = input('digite o usuário >(')

            if lgn_usr == cad_usr:
                while True:
                    lgn_psw = input('digite a senha >(')
                    if lgn_psw == cad_psw:
                        print('login efetuado com sucesso')
                        break
            else:
                print('usuário não cadastrado')
                continue
            break
    break
cadst_dtb = {cad_usr:cad_psw}
