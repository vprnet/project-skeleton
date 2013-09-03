import sys
from upload_s3 import set_metadata

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True


@app.route('/')
def index():
    return render_template('content.html')


#@app.route("/xml")
def xml():
    link = ''
    title = ''
    subtitle = ''
    teaser = ''
    storyDate = ''
    pubDate = ''
    tags = []
    bylines = []
    image = ''
    return render_template('nprml.xml',
                            link=link,
                            title=title,
                            subtitle=subtitle,
                            teaser=teaser,  # label teaser par with id="teaser" and scrape from page
                            storyDate=storyDate,
                            pubDate=pubDate,
                            tags=tags,
                            bylines=bylines,
                            image=image)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        set_metadata()
    else:
        app.run(debug=True)
