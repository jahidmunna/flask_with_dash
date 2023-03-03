import flask
import dash
from dash import html
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

flask_server = flask.Flask(__name__)


@flask_server.route("/")
@flask_server.route("/home")
def home():
    return "Home from  Flask!"

@flask_server.route("/about")
def about():
    return "About from Flask!"

app1 = dash.Dash(requests_pathname_prefix="/app1/")
app1.layout = html.Div("Hello, Dash app 1!")

app2 = dash.Dash(requests_pathname_prefix="/app2/")
app2.layout = html.Div("Hello, Dash app 2!")

app = DispatcherMiddleware(
    flask_server,
    {
        "/app1": app1.server, 
        "/app2": app2.server
    },
)

if __name__ == "__main__":
    run_simple("localhost", 1111, app)