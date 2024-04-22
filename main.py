from flask import Flask, jsonify
app = Flask(__name__)

def converter_tempo(segundos):
    minutos = segundos // 60
    segundos_restantes = segundos % 60

    horas = minutos // 60
    minutos_restantes = minutos % 60

    dias = horas // 24
    horas_restantes = horas % 24

    meses = dias // 30  # Aproximação de 30 dias por mês
    dias_restantes = dias % 30

    anos = meses // 12  # Aproximação de 12 meses por ano
    meses_restantes = meses % 12

    return anos, meses_restantes, dias_restantes, horas_restantes, minutos_restantes, segundos_restantes

@app.route('/converter/<int:segundos>')
def converter(segundos):
    anos, meses, dias, horas, minutos, segundos_restantes = converter_tempo(segundos)
    return jsonify({
        "anos": anos,
        "meses": meses,
        "dias": dias,
        "horas": horas,
        "minutos": minutos,
        "segundos": segundos_restantes
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
