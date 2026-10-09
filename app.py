from math import isfinite

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    try:
        salario = float(request.form["salario"].replace(",", "."))
        dependentes = int(request.form["dependentes"])
    except (KeyError, TypeError, ValueError):
        return render_template(
            "form.html",
            erro="Erro: insira um salário e um número de dependentes válidos.",
        ), 400

    if not isfinite(salario):
        return render_template(
            "form.html",
            erro="Erro: o salário deve ser um número válido.",
        ), 400

    if salario < 0:
        return render_template(
            "form.html",
            erro="Erro: o salário bruto não pode ser negativo.",
        ), 400

    if dependentes < 0:
        return render_template(
            "form.html",
            erro="Erro: o número de dependentes não pode ser negativo.",
        ), 400

    inss = salario * 0.08
    imposto_renda = salario * 0.15 if salario > 2500 else 0
    desconto_dependentes = dependentes * 200
    salario_liquido = salario - inss - imposto_renda + desconto_dependentes

    return render_template(
        "form.html",
        salario=salario,
        dependentes=dependentes,
        inss=inss,
        imposto_renda=imposto_renda,
        desconto_dependentes=desconto_dependentes,
        salario_liquido=salario_liquido,
    )


if __name__ == "__main__":
    app.run(debug=True)
