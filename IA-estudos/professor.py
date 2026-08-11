from busca import buscar_conteudo
import re



def detectar_conta(pergunta):

    pergunta = pergunta.lower()

    operacoes = {
        "+": ["+", "mais"],
        "-": ["-", "menos"],
        "*": ["*", "vezes"],
        "/": ["/", "dividido"]
    }


    numeros = re.findall(r"\d+", pergunta)


    if len(numeros) >= 2:

        for simbolo, palavras in operacoes.items():

            for palavra in palavras:

                if palavra in pergunta:

                    return (
                        int(numeros[0]),
                        simbolo,
                        int(numeros[1])
                    )


    return None



def iniciar_conta(pergunta, session):

    conta = detectar_conta(pergunta)


    if conta:

        n1, operacao, n2 = conta


        session["conta"] = {
            "numero1": n1,
            "operacao": operacao,
            "numero2": n2,
            "etapa": 1
        }


        if operacao == "+":

            unidade1 = n1 % 10
            unidade2 = n2 % 10


            session["resposta_etapa"] = unidade1 + unidade2


            return (
                "📚 Vamos aprender juntos!\n\n"
                f"Vamos resolver {n1} + {n2}.\n\n"
                "Primeiro vamos olhar as unidades:\n\n"
                f"{unidade1} + {unidade2} = ?\n\n"
                "Qual é o resultado?"
            )


        return (
            "📚 Vamos aprender juntos!\n\n"
            "Vamos resolver passo a passo.\n"
            "Vou te ajudar durante a conta."
        )


    return None



def continuar_conta(pergunta, session):

    if "conta" not in session:
        return None


    try:

        resposta = int(pergunta)

    except:

        return None



    conta = session["conta"]

    etapa = conta["etapa"]


    n1 = conta["numero1"]
    n2 = conta["numero2"]



    # primeira etapa: unidades

    if etapa == 1:


        if resposta == session["resposta_etapa"]:


            session["conta"]["etapa"] = 2


            session["resposta_etapa"] = (
                (n1 // 10) + (n2 // 10)
            )


            return (
                "✅ Muito bem!\n\n"
                "Agora vamos para as dezenas.\n\n"
                f"{n1 // 10} + {n2 // 10} = ?"
            )


        return (
            "❌ Ainda não.\n\n"
            "Tente novamente olhando somente as unidades."
        )



    # segunda etapa: dezenas

    elif etapa == 2:


        if resposta == session["resposta_etapa"]:


            resultado = n1 + n2


            session["conta"]["etapa"] = 3
            session["resposta_final"] = resultado


            return (
                "✅ Excelente!\n\n"
                "Agora juntamos as partes da conta.\n\n"
                f"Qual é a resposta final de {n1} + {n2}?"
            )


        return (
            "❌ Quase!\n\n"
            "Revise as dezenas."
        )



    # resposta final

    elif etapa == 3:


        if resposta == session["resposta_final"]:


            session.pop("conta")
            session.pop("resposta_final")


            return (
                "🎉 Parabéns!\n\n"
                "Você resolveu a conta sozinho!"
            )


        return (
            "❌ Ainda não.\n\n"
            "Tente juntar novamente as partes da conta."
        )



def limpar_texto(texto):

    texto = texto.replace("\n\n", "\n")
    texto = texto.strip()

    return texto



def explicar(texto):

    texto = limpar_texto(texto)

    return (
        "📚 Vamos aprender juntos!\n\n"
        "💡 Explicação:\n"
        + texto
    )



def responder_pergunta(pergunta, session):


    resposta_conta = continuar_conta(
        pergunta,
        session
    )


    if resposta_conta:

        return resposta_conta



    nova_conta = iniciar_conta(
        pergunta,
        session
    )


    if nova_conta:

        return nova_conta



    conteudo = buscar_conteudo(pergunta)


    return explicar(conteudo)