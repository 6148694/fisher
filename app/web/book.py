from helper import isbn_or_key
from flask import request,jsonify
from yushu_book import YuShuBook
from . import web

@web.route("/book/search")
def  search():
    q = request.args['q']
    page = request.args['page']
    isbn_or_key1 = isbn_or_key(q)
    if isbn_or_key1 =="isbn":
        result = YuShuBook.search_by_isbn(q)
    else:
        result =YuShuBook.search_by_keyword(q)
    return jsonify(result)

1111
