# -*- coding: utf-8 -*-
"""
    Simblin Admin Views
    ~~~~~~~~~~~~~~~~~~~

    The different views of the blogging application that are meant for the
    admin.

    :copyright: (c) 2010 by Eugen Kiss.
    :license: BSD, see LICENSE for more details.
"""
import datetime

from flask import Module, render_template, session, request, \
                  flash, redirect, url_for, jsonify, abort
from human.helpers import login_required
from human import datalayer

admin = Module(__name__)


@admin.route('/does-not-exist')
def disqus():
    """Specifically needed for disqus"""
    abort(404)


@admin.route('/compose', methods=['GET', 'POST'], defaults={'slug':None})
@admin.route('/update/<slug>', methods=['GET', 'POST'])
@login_required
def create_post(slug):
    """Create a new or edit an existing blog post"""
    pass

@admin.route('/_delete/<slug>', methods=['GET', 'POST'])
@login_required
def delete_post(slug):
    """Delete a post if existent. Ought to be used with an ajax request"""
    pass


@admin.route('/_add_category', methods=['POST'])
@login_required
def add_category():
    """Add category to database and return its id"""
    pass


@admin.route('/_delete_category', methods=['POST'])
@login_required
def delete_category():
    """Delete category specified by id from database"""
    pass

@admin.route('/_preview', methods=['POST'])
@login_required
def preview():
    """Returns a preview of a blog post. Use with an Ajax request"""
    pass


@admin.route('/login', methods=['GET', 'POST'])
def login():
    """Log the admin in"""
    #: For automatic redirection after login to the last visited page
    error = None
    if request.method == 'POST':
        user = datalayer.get_user(request.form['username'])
        if user is None:
            error = 'Invalid username'
        elif not datalayer.check_user(user.password, request.form['password']):
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You have been successfully logged in')
            return redirect(url_for('main.show_posts'))
    if error: flash(error, 'error')
    return render_template('admin/login.html')


@admin.route('/logout')
def logout():
    """Log the admin out"""
    session.pop('logged_in', None)
    flash('You have been successfully logged out')
    #: For automatic redirection to the last visited page before login
    next = request.values.get('next', '')
    return redirect(next or url_for('main.show_posts'))


@admin.route('/register', methods=['GET', 'POST'])
def register():
    """Register the first visitor of the page as the admin. The admin can
    'reregister' to change his/her password, email etc."""
    pass
