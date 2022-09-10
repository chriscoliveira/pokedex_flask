
from flask import Flask, render_template
from flask import request
import requests
from models.pokemon import Pokemon
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buscar', methods=['GET', 'post'])
def buscar():
    pokemon = Pokemon(request.form['nome'].lower(),
                      '', '', '', '', '', '', '', '', '', '')
    try:
        res = json.loads(requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pokemon.nome}').text)

        # foto
        resultado = res['sprites']['front_default']
        pokemon.foto = resultado
        resultado = res['sprites']['other']['dream_world']['front_default']
        pokemon.foto1 = resultado

        # tipo
        qtd_tipos = len(res['types'])
        tipos = []
        for i in range(qtd_tipos):
            tipos.append(res['types'][i]['type']['name'])
        pokemon.tipo = tipos

        # movimentos
        qtd_movimentos = len(res['moves'])
        movimentos = []
        for i in range(qtd_movimentos):
            movimentos.append(res['moves'][i]['move']['name'])
        pokemon.movimentos = movimentos

        # peso
        pokemon.peso = res['weight']

        # id
        pokemon.id = res['id']

        # formas
        pokemon.formas = res['forms'][0]['name']

        # habilidades
        qtd_habilidades = len(res['abilities'])
        habilidades = []
        for i in range(qtd_habilidades):
            habilidades.append(res['abilities'][i]['ability']['name'])
        pokemon.habilidades = habilidades

        # local
        pokemon.local = res['location_area_encounters']

        # status
        qtd_status = len(res['stats'])
        status = []
        for i in range(qtd_status):
            status.append(
                f"{res['stats'][i]['stat']['name'] } -> {res['stats'][i]['base_stat']}")
        pokemon.status = status

    except Exception as e:
        return 'Pokemon não encontrado '+str(e)
    return render_template('index.html',
                           nome=pokemon.nome,
                           foto=pokemon.foto,
                           foto1=pokemon.foto1,
                           tipo=pokemon.tipo,
                           movimentos=pokemon.movimentos,
                           id=pokemon.id,
                           peso=pokemon.peso,
                           habilidades=pokemon.habilidades,
                           local=pokemon.local,
                           status=pokemon.status,
                           formas=pokemon.formas)


if __name__ == '__main__':
    app.run(debug=True)
