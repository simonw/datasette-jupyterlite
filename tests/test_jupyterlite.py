from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_serve_jupyterlite():
    datasette = Datasette([])
    response = await datasette.client.get("/jupyterlite/")
    assert response.status_code == 200
    assert "# jupyter-lite-root" in response.text


@pytest.mark.asyncio
async def test_menu_link():
    datasette = Datasette([])
    response = await datasette.client.get("/")
    assert response.status_code == 200
    assert '<li><a href="/jupyterlite/">JupyterLite</a></li>' in response.text
