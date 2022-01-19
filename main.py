
# sistema de cadastro
l1 = '1'
l2 = '2'
cadst_dtb = {}
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
                cadst_dtb[cad_usr] = cad_psw
                break

            else:
                print('as senhas não coincidem')
                continue
    if aswr1 == l2:
        while True:
            lgn_usr = input('digite o usuário >(')

            if lgn_usr in cadst_dtb:
                while True:
                    lgn_psw = input('digite a senha >(')
                    if lgn_psw == cadst_dtb[lgn_usr]:
                        print('login efetuado com sucesso')
                        break
                    print('senha errada')
            else:
                print('usuário não cadastrado')
                continue
            break

