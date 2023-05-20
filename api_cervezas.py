from flask import Flask, jsonify

app = Flask(__name__)

cervezas = [
    {
        "Nombre": "DAMM INEDIT",
        "Descripción": "Creada por los cerveceros de Damm junto a Ferrán Adriá y los sumilleres de El Bulli, se elabora con una mezcla de malta de cebada y trigo aromatizada con cilantro, piel de naranja y regaliz.",
        "Graduación": "4,8º",
        "Envase": "Botella de 75cl",
        "Precio": "3,90€"
    },
    # Resto de las cervezas...
]

@app.route('/api/cervezas', methods=['GET'])
def obtener_cervezas():
    return jsonify(cervezas)

if __name__ == '__main__':
    app.run()
