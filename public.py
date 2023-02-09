from flask import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def index():
    return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():
    return render_template('login.html')


@public.route('/register',methods=['get','post'])
def register():
    return render_template('register.html')
@public.route('/doc',methods=['get','post'])
def doc():
    return render_template('parentreg.html')


