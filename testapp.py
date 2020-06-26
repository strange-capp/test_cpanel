from project import app, images, db
from flask import render_template, flash, request
from project.models import Recipe

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/save', methods=['GET', 'POST'])
def save():
    filename = images.save(request.files['image'])
    url = images.url(filename)
    new_recipe = Recipe(filename, url)
    db.session.add(new_recipe)
    db.session.commit()
    print(url, filename)
    flash('New recipe, {}, added!'.format(new_recipe.id), 'success')

    return "done"


@app.route('/show/<int:id>')
def show(id):
    recipe = Recipe.query.filter_by(id=id).first()
    url = recipe.image_url
    return render_template('show.html', url=url)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Recipe=Recipe)