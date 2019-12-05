from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    for q in quotes:
        if qid == q["id"]:
            return q


def _quote_exists(existing_quote):
    """Recommended helper"""
    for q in quotes:
        if existing_quote == q["quote"]:
            return True
    return False


def _get_highest_quote_id():
    result = 0
    for q in quotes:
        if q["id"] > result:
            result = q["id"]
    return result


def _get_index(qid):
    for i, e in enumerate(quotes):
        if e["id"] == qid:
            return i


def _is_valid_cu_quote(r):
    j = r.get_json()
    if not j:
        return False

    try:
        quote = j["quote"]
        movie = j["movie"]
    except KeyError:
        return False

    if _quote_exists(quote):
        return False

    return True


def _is_valid_cu_quote2(r):
    j = r.get_json()
    if not j:
        return False

    try:
        quote = j["quote"]
        movie = j["movie"]
    except KeyError:
        return False

    return True


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes=quotes)


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    q = _get_quote(qid)
    if q:
        return jsonify(quotes=[q])
    else:
        abort(404)


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    if _is_valid_cu_quote(request):
        j = request.get_json()
        q = {
            "quote": j["quote"],
            "movie": j["movie"],
            "id": _get_highest_quote_id() + 1
        }
        quotes.append(q)
        return jsonify(quote=q), 201
    else:
        abort(400)


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    idx = _get_index(qid)
    if not idx:
        abort(404)

    if _is_valid_cu_quote2(request):
        j = request.get_json()
        q = {
            "quote": j["quote"],
            "movie": j["movie"],
            "id": qid
        }
        quotes[idx] = q
        return jsonify(quote=q), 200
    else:
        abort(400)


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    idx = _get_index(qid)
    if not idx:
        abort(404)

    del quotes[idx]
    return get_quotes(), 204
