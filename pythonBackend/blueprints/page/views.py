from flask import Blueprint, Flask, render_template, request, send_from_directory
page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')

@page.route('/nameDemo/')
def nameDemo():
    return render_template('page/nameDemo.html')

@page.route('/textGender/')
def textGender():
    return render_template('page/textGender.html')

# @page.route('/<string:page_name>/')
# def render_static(page_name):
#     # print(page_name)
#     return render_template('page/%s.html' % page_name)


# @page.route('/terms')
# def terms():
#     return render_template('page/terms.html')
#
#
# @page.route('/privacy')
# def privacy():
#     return render_template('page/privacy.html')
