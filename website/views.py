from flask import Blueprint

# blue print of the applications (root/urls)
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"
