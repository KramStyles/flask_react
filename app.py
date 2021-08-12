from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    pg = {
        'title' : 'Homepage',
        'langs': ['java', 'python', 'javascript', 'perl', 'c-sharp']
    }
    return render_template('index.html', pg=pg)


@app.route('/about')
def about():
    pg = {
        'title' : 'about'
    }
    return render_template('about.html', pg=pg)


@app.route('/contact')
def contact():
    pg = {
        'title' : 'contact us'
    }
    return render_template('contact.html', pg=pg)


@app.route('/terms')
def terms():
    pg = {
        'title' : 'terms and conditions'
    }
    return render_template('terms.html', pg=pg)


@app.route('/privacy')
def privacy():
    pg = {
        'title' : 'privacy policy'
    }
    return render_template('privacy.html', pg=pg)


if __name__ == '__main__':
    app.run()


