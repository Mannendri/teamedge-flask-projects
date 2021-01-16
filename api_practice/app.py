from flask import Flask, json, jsonify, request, render_template
import os


app = Flask(__name__)
albums_path = os.path.join(app.static_folder,'data','albums.json')

@app.route('/api/v1/albums/all')
def api_albums_all():
    with open (albums_path,'r') as json_data:
        albums = json.load(json_data)
        return render_template("index.html",albums=albums)

@app.route('/api/v1/albums/search', methods=['GET'])
def api_albums_search():
    with open (albums_path,'r') as json_data:
        albums = json.load(json_data)

    results=[] 

    if 'artist' in request.args:
        artist = request.args['artist']
        for album in albums:
            if artist in album['artist']:
                results.append(album)

    if 'year' in request.args:
        year = request.args['year']
        for album in albums:           
            if (year == str(album['year'])):
                print("Match found!")
                results.append(album)

    if 'song' in request.args:
        song = request.args['song'].lower()
        for album in albums:
            for s in album["songs"]:
                if song in s.lower():
                    print("Match found!")
                    results.append(album)    
    
    if (len(results) < 1):
        return "Sorry, your query did not find any matches."
    else:
        return render_template("index.html",albums=results)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

