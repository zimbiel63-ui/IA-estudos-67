# Professor de Matemática - 9º Ano
# Estuda IA


import re



conteudos = {

    "numeros_operacoes": [
        "soma",
        "adição",
        "subtração",
        "multiplicação",
        "divisão",
        "conta"
    ],


    "fracoes": [
        "fração",
        "frações",
        "numerador",
        "denominador"
    ],


    "porcentagem": [
        "porcentagem",
        "%"
    ],


    "razao_proporcao": [
        "razão",
        "proporção"
    ],


    "regra_tres": [
        "regra de três",
        "regra de tres"
    ],


    "potenciacao": [
        "potência",
        "potencia",
        "expoente"
    ],


    "radiciacao": [
        "raiz",
        "raiz quadrada"
    ],


    "expressoes_algebricas": [
        "expressão algébrica",
        "expressao algebrica"
    ],


    "equacao_1_grau": [
        "equação do primeiro grau",
        "equação 1 grau",
        "x +"
    ],


    "equacao_2_grau": [
        "equação do segundo grau",
        "bhaskara"
    ],


    "sistemas": [
        "sistema",
        "sistemas de equações"
    ],


    "produtos_notaveis": [
        "produto notável",
        "quadrado da soma"
    ],


    "fatoracao": [
        "fatoração",
        "fatorar"
    ],


    "pitagoras": [
        "pitágoras",
        "hipotenusa"
    ],


    "area_volume": [
        "área",
        "volume",
        "perímetro"
    ],


    "estatistica": [
        "média",
        "mediana",
        "moda",
        "gráfico"
    ],


    "probabilidade": [
        "probabilidade",
        "chance"
    ]

}



def identificar_assunto(pergunta):

    pergunta = pergunta.lower()


    for assunto, palavras in conteudos.items():

        for palavra in palavras:

            if palavra in pergunta:

                return assunto


    return None



def extrair_numeros(texto):

    numeros = re.findall(
        r"\d+",
        texto
    )

    return numeros



def responder_matematica(pergunta):


    assunto = identificar_assunto(
        pergunta
    )


    if assunto is None:

        return None



    respostas = {

        "numeros_operacoes":
        "Vamos trabalhar com números e operações. Vou te ajudar passo a passo.",


        "fracoes":
        "Vamos aprender frações. Primeiro precisamos entender numerador e denominador.",


        "porcentagem":
        "Vamos estudar porcentagem. Ela representa uma parte de 100.",


        "razao_proporcao":
        "Vamos analisar a relação entre grandezas usando razão e proporção.",


        "regra_tres":
        "Vamos montar a regra de três identificando as grandezas.",


        "potenciacao":
        "Vamos entender base e expoente para resolver a potência.",


        "radiciacao":
        "Vamos descobrir qual número elevado gera essa raiz.",


        "expressoes_algebricas":
        "Vamos organizar os termos e resolver a expressão algébrica.",


        "equacao_1_grau":
        "Vamos deixar a incógnita sozinha passo a passo.",


        "equacao_2_grau":
        "Vamos resolver usando os métodos da equação do segundo grau.",


        "sistemas":
        "Vamos resolver as equações juntas encontrando os valores das incógnitas.",


        "produtos_notaveis":
        "Vamos identificar o padrão do produto notável.",


        "fatoracao":
        "Vamos transformar a expressão em fatores menores.",


        "pitagoras":
        "Vamos usar a relação entre os lados do triângulo retângulo.",


        "area_volume":
        "Vamos identificar a fórmula correta para calcular a medida.",


        "estatistica":
        "Vamos analisar os dados usando média, moda ou mediana.",


        "probabilidade":
        "Vamos calcular as chances de um evento acontecer."

    }


    return (
        "📚 Professor de Matemática 9º ano\n\n"
        + respostas[assunto]
        + "\n\nVamos resolver juntos."
    )