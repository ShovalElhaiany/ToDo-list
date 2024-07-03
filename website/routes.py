from .views import home, delete_task
from .auth import login, logout, sign_up

def set_routes(views, auth):
    # Add routes to views blueprint
    views.add_url_rule('/', methods=['GET', 'POST'], view_func=home, endpoint='home')
    views.add_url_rule('/delete-task', methods=['POST'], view_func=delete_task, endpoint='delete_task')

    # Add routes to auth blueprint
    auth.add_url_rule('/login', methods=['GET', 'POST'], view_func=login, endpoint='login')
    auth.add_url_rule('/logout', view_func=logout, endpoint='logout')
    auth.add_url_rule('/sign-up', methods=['GET', 'POST'], view_func=sign_up, endpoint='sign_up')