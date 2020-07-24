$env:FLASK_APP = "main.py"
$env:FLASK_DEBUG = "1"
$env:FLASK_ENV = "development"
$env:FLASK_RUN_EXTRA_FILES = "/statics/css/theme.css"

flask run