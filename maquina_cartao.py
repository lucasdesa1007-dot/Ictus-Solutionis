import datetime

print("=" * 50)
print(" Ictus Solutionis - MAQUININHA DE CARTÃO")
print("=" * 50)

while True:
    try:
        print("\n--- NOVA VENDA ---")
        valor = float(input("Valor da venda: R$ "))

        print("\nTipo de pagamento:")
        print("[1] Débito")
        print("[2] Crédito")
        tipo_opcao = input("Escolha 1 ou 2: ")

        print("\nBandeira do cartão:")
        print("[0] visa, [1] mastercard, [2] elo, [3] amex, [4] hipercard")
        tipo_opcao2 = input("Escolha 0 ate 4: ")

        if tipo_opcao2 == "0":
            tipo_ban = "visa"
        elif tipo_opcao2 == "1":
            tipo_ban = "mastercard"
        elif tipo_opcao2 == "2":
            tipo_ban = "elo"
        elif tipo_opcao2 == "3":
            tipo_ban = "amex"
        elif tipo_opcao2 == "4":
            tipo_ban = "hipercard"
        print(f"bandeira do cartao escolhida: {tipo_ban}")
        parcelas = 1
        tipo_pagamento = ""

        if tipo_opcao == "1":
            tipo_pagamento = "debito"
        elif tipo_opcao == "2":
            tipo_pagamento = "credito"
            parcelas_input = input("Quantas parcelas? (1 a 12) [padrão 1]: ").strip()
            if parcelas_input == "":
                parcelas = 1
            else:
                parcelas = int(parcelas_input)
        else:
            print("Opção inválida! Use 1 ou 2.")
            continue

        # Calculo SEM JUROS
        valor_parcela = valor / parcelas

        # --- RECIBO ---
        print("\n" + "=" * 50)
        print(" COMPROVANTE DE PAGAMENTO")
        print("=" * 50)
        data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Data/Hora: {data}")
        print(f"Bandeira: {tipo_ban}")

        if tipo_pagamento == "debito":
            print(f"Tipo: Débito à vista")
            print(f"Valor gasto pela pessoa: R$ {valor:.2f}")
            print(f"Parcelas: À vista")
        else:
            if parcelas == 1:
                print(f"Tipo: Crédito à vista")
                print(f"Valor gasto pela pessoa: R$ {valor:.2f}")
                print(f"Parcelas: 1x de R$ {valor:.2f}")
            else:
                print(f"Tipo: Crédito parcelado")
                print(f"Valor gasto pela pessoa: R$ {valor:.2f}")
                print(f"Parcelas: {parcelas}x de R$ {valor_parcela:.2f}")

        print(f"Status: APROVADO")
        print("=" * 50)

        continuar = input("\nFazer nova venda? (s/n): ").lower()
        if continuar != 's':
            print("\nMaquininha desligada. Até mais!")
            break

    except ValueError as erro:
        print("\nERRO: ", erro)
        break
