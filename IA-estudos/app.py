from flask import Flask, render_template, request, session
from professor import responder_pergunta


app = Flask(__name__)

app.secret_key = "estuda-ia-chave"


@app.route("/")
def inicio():

    if "historico" not in session:
        session["historico"] = []

    return render_template(
        "index.html",
        historico=session["historico"]
    )


@app.route("/perguntar", methods=["POST"])
def perguntar():

    pergunta = request.form.get(
        "pergunta",
        ""
    ).strip()

    if not pergunta:

        return render_template(
            "index.html",
            historico=session.get(
                "historico",
                []
            )
        )

# Linha extra
    historico = session.get(
        "historico",
        []
    )

    resposta = responder_pergunta(
        pergunta,
        session
    )

    historico.append(
        {
            "pergunta": pergunta,
            "resposta": resposta
        }
    )

    session["historico"] = historico

    return render_template(
        "index.html",
        historico=historico
    )


if __name__ == "__main__":
    app.run(debug=True)
