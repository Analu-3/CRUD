# ============================================================
# SISTEMA DE ADOÇÃO DE GATOS RESGATADOS (versão resumida)
# Utiliza variáveis, if/elif/else, while e for.
# Não utiliza isdigit(), upper(), range() ou funções próprias.
# Capacidade: 5 gatos (posição 1 a 5). Vaga livre = nome vazio.
# Gato disponível = adotante vazio.
# ============================================================

nomes = ["", "", "", "", ""]
idades = ["", "", "", "", ""]
sexos = ["", "", "", "", ""]
cores = ["", "", "", "", ""]
locais = ["", "", "", "", ""]
adotantes = ["", "", "", "", ""]

print("=== SISTEMA DE ADOÇÃO DE GATOS ===")

while True:
    print()
    print("------------- MENU -------------")
    print("1. Cadastrar gato")
    print("2. Listar gatos cadastrados")
    print("3. Atualizar cadastro")
    print("4. Excluir cadastro")
    print("5. Registrar adoção")
    print("6. Sair do sistema")
    opcao = input("Escolha uma opção: ")

    if opcao == "6":
        print("Encerrando o sistema. Obrigado por ajudar os gatinhos!")
        break

    elif opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5":
        escolhido = ""
        feito = False
        if opcao == "3" or opcao == "4" or opcao == "5":
            escolhido = input("Digite o número do cadastro (1 a 5): ")

        # Percorre os cinco cadastros (o número é tratado como texto)
        for numero in "12345":
            i = int(numero) - 1

            # ---------- 2. LISTAR ----------
            if opcao == "2" and nomes[i] != "":
                feito = True
                print()
                print("Cadastro nº " + numero)
                print("  Nome: " + nomes[i])
                print("  Idade: " + idades[i] + " ano(s)")
                print("  Sexo: " + sexos[i])
                print("  Cor: " + cores[i])
                print("  Encontrado em: " + locais[i])
                if adotantes[i] == "":
                    print("  Situação: DISPONÍVEL para adoção")
                else:
                    print("  Situação: JÁ ADOTADO por " + adotantes[i])

            # ---------- 1. CADASTRAR / 3. ATUALIZAR (mesmo bloco) ----------
            elif (opcao == "1" and nomes[i] == "" and feito == False) or (opcao == "3" and escolhido == numero and nomes[i] != ""):
                feito = True
                criando = nomes[i] == ""
                if criando:
                    print("--- Novo cadastro (número " + numero + ") ---")
                else:
                    print("Deixe em branco (Enter) para manter o valor atual.")

                novo = input("Nome [" + nomes[i] + "]: ")
                while novo == "" and criando:
                    print("Erro: o nome não pode ficar vazio.")
                    novo = input("Nome: ")
                if novo != "":
                    nomes[i] = novo

                ok = False
                while ok == False:
                    novo = input("Idade [" + idades[i] + "]: ")
                    ok = novo != "" or criando == False
                    for letra in novo:
                        if letra < "0" or letra > "9":
                            ok = False
                    if ok == False:
                        print("Erro: digite apenas números.")
                if novo != "":
                    idades[i] = novo

                ok = False
                while ok == False:
                    novo = input("Sexo M/F [" + sexos[i] + "]: ")
                    if novo == "m":
                        novo = "M"
                    elif novo == "f":
                        novo = "F"
                    ok = novo == "M" or novo == "F" or (novo == "" and criando == False)
                    if ok == False:
                        print("Erro: digite M ou F.")
                if novo != "":
                    sexos[i] = novo

                novo = input("Cor [" + cores[i] + "]: ")
                if novo != "":
                    cores[i] = novo

                novo = input("Local [" + locais[i] + "]: ")
                if novo != "":
                    locais[i] = novo

                ok = False
                while ok == False:
                    novo = input("Situação 1-Disponível, 2-Adotado: ")
                    ok = novo == "1" or novo == "2" or (novo == "" and criando == False)
                    if ok == False:
                        print("Erro: digite 1 ou 2.")
                if novo == "1":
                    adotantes[i] = ""
                elif novo == "2":
                    while adotantes[i] == "":
                        adotantes[i] = input("Nome do adotante: ")
                        if adotantes[i] == "":
                            print("Erro: informe o nome do adotante.")

                if criando:
                    print("Gato cadastrado com sucesso! Número: " + numero)
                else:
                    print("Cadastro atualizado com sucesso!")

            # ---------- 4. EXCLUIR / 5. REGISTRAR ADOÇÃO ----------
            elif (opcao == "4" or opcao == "5") and escolhido == numero and nomes[i] != "":
                feito = True

                if opcao == "4":
                    confirma = input("Excluir o gato " + nomes[i] + "? (S/N): ")
                    if confirma == "S" or confirma == "s":
                        nomes[i] = ""
                        idades[i] = ""
                        sexos[i] = ""
                        cores[i] = ""
                        locais[i] = ""
                        adotantes[i] = ""
                        print("Cadastro excluído com sucesso!")
                    else:
                        print("Exclusão cancelada.")

                elif adotantes[i] != "":
                    print("Erro: " + nomes[i] + " já foi adotado por " + adotantes[i] + ".")
                else:
                    while adotantes[i] == "":
                        adotantes[i] = input("Nome do adotante: ")
                        if adotantes[i] == "":
                            print("Erro: informe o nome do adotante.")
                    print("Adoção registrada! " + nomes[i] + " agora tem um lar.")

        # ---------- MENSAGENS FINAIS ----------
        if feito == False:
            if opcao == "1":
                print("Erro: limite de 5 gatos atingido. Exclua um cadastro para abrir vaga.")
            elif opcao == "2":
                print("Nenhum gato cadastrado.")
            else:
                print("Erro: não existe cadastro com o número informado.")

    else:
        print("Erro: opção inválida! Escolha um número de 1 a 6.")
