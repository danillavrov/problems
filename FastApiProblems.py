from fastapi import FastAPI

app = FastAPI(
    title='Trading App'
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]


@app.get('/trades')
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]


fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.post('/users/{users_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users2))[0]
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user}


# задание 1
@app.get('/info')
def info():
    return 'Это трейдинговое приложение'


# задание 2
@app.get('/trades/{trade_id}')
def get_trade(trade_id: int):
    if trade_id in [trade['id'] for trade in fake_trades]:
        return [trade for trade in fake_trades if trade.get('id') == trade_id][0]
    else:
        return 'error'


# задание 3
@app.post('/trades/{trade_id}')
def add_trade(data: dict):
    for trade in fake_trades:
        trade[list(data.keys())[0]] = data[list(data.keys())[0]]
