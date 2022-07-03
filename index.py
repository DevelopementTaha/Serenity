from asyncio.windows_events import NULL
from flask import Flask, render_template, request
from urllib.parse import unquote_plus

app = Flask(__name__)
from wixRequests import getSessions, getSession, getPositip, getArticle, getCollection, getkeyword , getAllCollections

@app.route('/')
def home():
    collections, sortedCollectionList, sortedSessionList = getAllCollections()
    anyCollections = any(col.showCollection == True for col in sortedCollectionList) #boolean variable
    keyword = getkeyword()
    return render_template('layoutMain1.html', collections = sortedCollectionList, sortedSessionListFromCollection = sortedSessionList, keys = keyword, anyCollections = anyCollections)

@app.route('/card')
def card():
    clickedKey = request.args.get('keyword', '')
    sessions = getSessions()
    keys = getkeyword()
    return render_template('card.html', sessions = sessions, keys = keys, clickedKey = clickedKey)

@app.route('/showSession')
def showSession():
    sessionId = request.args.get('sessionId', None)
    session = getSession(sessionId)
    return render_template('SessionPage.html', session = session)

@app.route('/showPositips')
def showPositip():
    positipId = request.args.get('positipId', None)
    session = getPositip(positipId)
    return render_template('Positips.html', session = session)

@app.route('/showArticles')
def showArticle():
    articleId = request.args.get('articleId', None)
    session = getArticle(articleId)
    return render_template('Articles.html', session = session)

@app.route('/showSessionAudio')
def showSessionAudio():
    sessionId = request.args.get('sessionId', None)
    session = getSession(sessionId)
    return render_template('SessionAudio.html', session = session)

@app.route('/showCollections')
def showCollections():
    collectionId = request.args.get('collectionId', None)
    collection = getCollection(collectionId)
    return render_template('collection.html', collection = collection)

@app.route('/openLink')
def openLink():
    videoLink = unquote_plus(request.args.get('videoLink'))
    return render_template('/try.html', videoLink = videoLink)

@app.route('/None')
def none():
    return render_template('/notFound.html')

@app.route('/loginPage.html')
def login():    
    return render_template('Loginpage.html')

@app.route('/offline.html')
def offline():
    return app.send_static_file('offline.html')

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4444)
