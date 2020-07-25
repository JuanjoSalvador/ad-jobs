import pytest
from flask import url_for

@pytest.mark.options(debug=False)
def test_app(app):
  assert not app.debug, 'Ensure the app not in debug mode'

"""
    Tests para comprobar las rutas públicas de la aplicación
"""

def test_index(client):
    assert client.get(url_for('public.index')).status_code == 200

def test_send(client):
    assert client.get(url_for('public.send')).status_code == 200

def test_contact(client):
    assert client.get(url_for('public.contact')).status_code == 200

"""
    Tests para comprobar las rutas de administración de la aplicación
"""

def test_admin_login(client):
    assert client.get(url_for('admin.login')).status_code == 200