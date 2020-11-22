from resources import from_postgreSQL as db, kakao_with_flaskrestx as fr

api = fr.Namespace('post', description='Post related operations')

@api.route('/')
class Post(fr.Resource):
    @api.expect(fr.post_get_parser)
    def get(self):
        params = fr.post_get_parser.parse_args()

        predicates = []
        if params['title']: predicates += [f"title LIKE '%{params['title']}%'"]
        if params['content']: predicates += [f"content LIKE '%{params['content']}%'"]
        if params['is_notice']: predicates += [f"is_notice = {params['is_notice']}"]
        if params['class_id']: predicates += [f"class_id = '{params['class_id']}'"]
        if params['year']: predicates += [f"year = {params['year']}"]
        if params['quarter']: predicates += [f"quarter = {params['quarter']}"]

        res = db.fetch(f'''
            SELECT id
            FROM post
            WHERE {db.join_params_for_where(predicates)}
        ''')

        return res
