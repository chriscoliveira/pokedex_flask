
from flask import Flask, render_template
from flask import request
import requests
from models.pokemon import Pokemon
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pokedex_home.html')


@app.route('/buscar', methods=['GET', 'post'])
def buscar():

    try:
        pokemon = Pokemon(request.form['nome'].lower(),
                          '', '', '', '', '', '', '', '', '', '')
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

        txt = ''
        for i in tipos:
            txt += i + ', '
        pokemon.tipo = txt

        # movimentos
        qtd_movimentos = len(res['moves'])
        movimentos = []
        for i in range(qtd_movimentos):
            movimentos.append(res['moves'][i]['move']['name'])

        txt = ''
        for i in movimentos:
            txt += i + ', '
        pokemon.movimentos = txt

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

        txt = ''
        for i in habilidades:
            txt += i + ', '
        pokemon.habilidades = txt

        # local
        pokemon.local = res['location_area_encounters']

        # status
        qtd_status = len(res['stats'])
        status = []
        for i in range(qtd_status):
            status.append(
                f"{res['stats'][i]['stat']['name'] }={res['stats'][i]['base_stat']} ")

        txt = ''
        for i in status:
            txt += i + ', '
        pokemon.status = txt
        return render_template('pokedex.html',
                               nome=pokemon.nome.upper(),
                               foto=pokemon.foto,
                               foto1=pokemon.foto1,
                               tipo=pokemon.tipo.upper(),
                               movimentos=pokemon.movimentos.upper(),
                               id=pokemon.id,
                               peso=pokemon.peso,
                               habilidades=pokemon.habilidades.upper(),
                               local=pokemon.local.upper(),
                               status=pokemon.status.upper(),
                               formas=pokemon.formas.upper())
    except Exception as e:
        return render_template('pokedex_home.html', nome='Pokemon não encontrado', foto='', foto1='', tipo='', movimentos='', id='', peso='', habilidades='', local='', status='', formas='')


if __name__ == '__main__':
    app.run(debug=True)
