from flask_restx import Namespace, Resource, reqparse

# 학생조회
student_get_parser = reqparse.RequestParser()
student_get_parser.add_argument('student', type=str)
student_get_parser.add_argument('name', type=str)
student_get_parser.add_argument('phone', type=str)
student_get_parser.add_argument('email', type=str)

# 학생갱신
student_put_parser = reqparse.RequestParser()
student_put_parser.add_argument('name', type=str)
student_put_parser.add_argument('major_id', type=str)
student_put_parser.add_argument('year', type=int)
student_put_parser.add_argument('semester', type=int)
student_put_parser.add_argument('phone', type=str)
student_put_parser.add_argument('email', type=str)
student_put_parser.add_argument('process_id', type=str)

# 과목조회
class_put_parser = reqparse.RequestParser()
class_put_parser.add_argument('class_id', type=str)
class_put_parser.add_argument('year', type=int)
class_put_parser.add_argument('quarter', type=int)
class_put_parser.add_argument('name', type=str)
class_put_parser.add_argument('class_professor', type=str)

# 게시판 작성
post_post_parser = reqparse.RequestParser()
post_post_parser.add_argument('title', type=str, required=True)
post_post_parser.add_argument('content', type=str, required=True)
post_post_parser.add_argument('is_notice', type=bool, required=True)
post_post_parser.add_argument('class_id', type=bool, required=True)

# 게시판 조회
post_get_parser = reqparse.RequestParser()
post_get_parser.add_argument('title', type=str)
post_get_parser.add_argument('content', type=str)
post_get_parser.add_argument('is_notice', type=bool)
post_get_parser.add_argument('class_id', type=str)
post_get_parser.add_argument('year', type=int)
post_get_parser.add_argument('quarter', type=int)

# 게시판 갱신
post_put_parser = reqparse.RequestParser()
post_put_parser.add_argument('post_id', type=str, required=True)
post_put_parser.add_argument('title', type=str)
post_put_parser.add_argument('content', type=str)

# 게시판 삭제
post_delete_parser = reqparse.RequestParser()
post_delete_parser.add_argument('post_id', type=str, required=True)

# 게시판 내 댓글 작성
comment_post_parser = reqparse.RequestParser()
comment_post_parser.add_argument('post', type=str, required=True)
comment_post_parser.add_argument('content', type=str, required=True)

# 게시판 내 댓글조회
comment_get_parser = reqparse.RequestParser()
comment_get_parser.add_argument('post', type=str, required=True)

# 게시판 내 댓글 갱신
comment_put_parser = reqparse.RequestParser()
comment_put_parser.add_argument('comment_id', type=str, required=True)
comment_put_parser.add_argument('content', type=str)

# 게시판 내 댓글 삭제
comment_delete_parser = reqparse.RequestParser()
comment_delete_parser.add_argument('comment_id', type=str, required=True)

# 게시판 좋아요
post_like_put_parser = reqparse.RequestParser()
post_like_put_parser.add_argument('post_id', type=str, required=True)

# 게시판 싫어요
post_hate_put_parser = reqparse.RequestParser()
post_hate_put_parser.add_argument('post_id', type=str, required=True)

# 게시판 내 댓글 좋아요
comment_like_put_parser = reqparse.RequestParser()
comment_like_put_parser.add_argument('comment_id', type=str, required=True)

# 게시판 내 댓글 싫어요
comment_hate_put_parser = reqparse.RequestParser()
comment_hate_put_parser.add_argument('comment_id', type=str, required=True)

# 성적 조회
grade_get_parser = reqparse.RequestParser()
grade_get_parser.add_argument('year', type=str)
grade_get_parser.add_argument('quarter', type=str)
grade_get_parser.add_argument('retake', type=str)
grade_get_parser.add_argument('grade', type=str)

# 선후수과목 조회
prereq_get_parser = reqparse.RequestParser()

# 선후수과목 조회
timetable_get_parser = reqparse.RequestParser()

# 선후수과목 조회
enroll_post_parser = reqparse.RequestParser()
grade_get_parser.add_argument('class_id', type=str)

# 선후수과목 조회
scholarship_get_parser = reqparse.RequestParser()
grade_get_parser.add_argument('start_year', type=str)

# 마법 조회
wizard_get_parser = reqparse.RequestParser()
grade_get_parser.add_argument('TODO', type=str)

# 로그인
login_post_parser = reqparse.RequestParser()

# 선후수과목 조회
logout_post_parser = reqparse.RequestParser()