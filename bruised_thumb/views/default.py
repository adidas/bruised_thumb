from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
import re
import copy

from ..models import Post


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    # ToDo: Figure out how to use RE to find "========..." So that I can just pull
    #   the beginning of the post.
    try:
        posts = request.dbsession.query(Post) \
        .order_by(Post.date.desc()).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    truncated_posts = copy.deepcopy(posts)
    header_pattern = re.compile("={5,}")
    for pos, post in enumerate(posts):
        # Find where we want to cut off.
        match = header_pattern.search(post.body)
        trunc_end = post.body[:match.start()-1].rfind('\n')
        truncated_posts[pos].body = post.body[:trunc_end]+'\n'

    return {'posts': truncated_posts}

@view_config(route_name='post', renderer='../templates/post_view.jinja2')
def post(request):
    try:
        post = request.dbsession.query(Post) \
        .filter(Post.date == request.matchdict['date']) \
        .order_by(Post.date.desc()).first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'post': post}


db_err_msg = """\
Pyramid is having a problem with the SQL database.
"""
