from flask import Flask
from flask_restful import Api
from data import db_session
from data import users_resource, cinemas_resource, halls_resource, logs_resource, \
    playbills_resource, prices_resource, sessions_resource
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


def main():
    db_session.global_init('db/cinema.db')
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(halls_resource.HallsListResource, '/api/v2/halls')
    api.add_resource(halls_resource.HallsResource, '/api/v2/halls/<int:hall_id>')
    api.add_resource(cinemas_resource.CinemasListResource, '/api/v2/cinemas')
    api.add_resource(cinemas_resource.CinemasResource, '/api/v2/cinemas/<int:cinema_id>')
    api.add_resource(logs_resource.LogsListResource, '/api/v2/logs')
    api.add_resource(logs_resource.LogsResource, '/api/v2/logs/<int:log_id>')
    api.add_resource(playbills_resource.PlaybillsListResource, '/api/v2/playbills')
    api.add_resource(playbills_resource.PlaybillsResource,
                     '/api/v2/playbills/<int:playbill_id>')
    api.add_resource(prices_resource.PricesListResource, '/api/v2/prices')
    api.add_resource(prices_resource.PricesResource, '/api/v2/prices/<int:price_id>')
    api.add_resource(sessions_resource.SessionsListResource, '/api/v2/sessions')
    api.add_resource(sessions_resource.SessionsResource, '/api/v2/sessions/<int:session_id>')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


@app.route('/')
def index():
    return 'HI'


if __name__ == '__main__':
    main()
