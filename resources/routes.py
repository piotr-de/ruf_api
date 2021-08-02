import requests
import threading
import time
from translate import Translator
from flask import jsonify, request
from yaml import load, Loader


def initialize_routes(app):
    @app.route('/')
    def home():
        try:
            with open('schema.yml', 'r') as schema:
                output = load(schema, Loader=Loader)
                return jsonify(output)
        except:
            return jsonify('Schema load error')


    @app.route('/status')
    def status():
        global facts, error
        if error is True:
            status = 'ERROR'
        elif len(facts) < 1000:
            status = 'LOADING'
        else:
            status = 'COMPLETED'
        fact_ids = refresh_facts()
        response = {
            'status': status,
            'facts': {
                'total': len(facts),
                'unique': len(set(fact_ids))
            }
        }
        return jsonify(response)


    @app.route('/facts')
    def facts():
        fact_ids = refresh_facts()
        if len(fact_ids) == 0:
            return status()
        return jsonify({'facts': fact_ids})


    @app.route('/facts/<fact_id>')
    def fact(fact_id):
        global facts
        fact_ids = refresh_facts()
        if fact_id in fact_ids:
            index = fact_ids.index(fact_id)
            fact = facts[index]
        else:
            response = requests.get(f'https://uselessfacts.jsph.pl/{fact_id}.json')
            if response.status_code == 429:
                delay = int(response.headers['Retry-After'])
                return jsonify({'HTTP Response Code': f'429. Too Many Attempts. Try again in {delay} seconds.'}), 429
            elif response.status_code == 200:
                fact = response.json()
            else:
                return jsonify({'HTTP Response Code': response.status_code}), response.status_code
        to_lang = request.args.get('lang')
        from_lang = fact['language']
        if to_lang is not None and to_lang != from_lang:
            translation = translate(fact['text'], from_lang, to_lang)
            fact_translated = fact.copy()
            fact_translated['language'] = fact['language'] if fact['text'] == translation else to_lang
            fact_translated['text'] = translation
            return fact_translated
        return fact


def start_loader():
    def fetch_fact():
        response = requests.get(
            'https://uselessfacts.jsph.pl/random.json', timeout=5)
        return response

    def load_facts():
        global facts, error
        facts = []
        try:
            error = False
            for _ in range(1000):
                response = fetch_fact()
                if response.status_code == 200:
                    facts.append(response.json())
                if response.status_code == 429:
                    delay = int(response.headers['Retry-After'])
                    print(f'Pausing for {delay} seconds...')
                    time.sleep(delay)
                    facts.append(fetch_fact().json())
            print('Done.')
        except Exception as e:
            error = True
            print(f'Error fetching facts: {e}')
    print('Fetching 1000 random facts...')
    thread = threading.Thread(target=load_facts)
    thread.start()


def refresh_facts():
    global facts
    fact_ids = [fact['id'] for fact in facts]
    return fact_ids


def translate(fact, from_lang, to_lang):
    if len(to_lang) == 2 and len(from_lang) == 2:
        translator = Translator(from_lang=from_lang, to_lang=to_lang)
        translation = translator.translate(fact)
        return translation
    return fact
