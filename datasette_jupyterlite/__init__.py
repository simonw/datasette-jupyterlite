from datasette import hookimpl
from datasette.utils.asgi import Response, NotFound
import mimetypes
from importlib import resources
import tarfile


tarpath = list(resources.files("jupyterlite").glob("*.tgz"))[0]
tf = tarfile.open(tarpath)


async def serve_juptyerlite(request):
    path = request.url_vars["path"]
    if not path:
        path = "index.html"
    path = "package/" + path
    try:
        member = tf.getmember(path)
    except KeyError:
        raise NotFound("Path not found: {}".format(path))
    # Set content-type based on extension
    content_type = mimetypes.guess_type(path)[0]
    if content_type is None:
        content_type = "application/octet-stream"
    return Response(tf.extractfile(member).read(), content_type=content_type)


@hookimpl
def register_routes():
    return [(r"^/jupyterlite/(?P<path>.*)$", serve_juptyerlite)]


@hookimpl
def menu_links(datasette):
    return [
        {"href": datasette.urls.path("/jupyterlite/"), "label": "JupyterLite"},
    ]
