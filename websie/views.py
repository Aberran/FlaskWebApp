from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category='error')
            return redirect(url_for('views.home'))
        else: 
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            return redirect(url_for('views.home'))
            
    return render_template('home.html', user=current_user, user_name=current_user.first_name)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})

# search function
@views.route('/searched', methods=['POST', 'GET'])
@login_required
def search():
    
    searched_results = None
    
    if request.method == 'POST': 
        searched = request.form.get('searched')
        if searched != '':
            searched_results = Note.query.filter(Note.data.like(f'%{searched}%'),Note.user_id == current_user.id).all()
            print(searched_results)
            
    return render_template('searched.html', user=current_user, user_name=current_user.first_name, searched_results=searched_results)
