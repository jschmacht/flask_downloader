from pathlib import Path
from flask import Flask, Response, send_from_directory
# from flask import stream_with_context, request, abort, jsonify

app = Flask(__name__)

DOWNLOAD_FOLDER = '/mnt/vol1/tax2proteome_results/'

@app.route('/')
def return_Error():
    return 'Use the UID of your database'

@app.route('/<name>')
def serve_generated_database(name):
    file_name = name + '.tar'
    zipped_file = Path(DOWNLOAD_FOLDER) / file_name

    if zipped_file.is_file():
        return send_from_directory(directory=DOWNLOAD_FOLDER, filename=file_name, as_attachment=True)
    else:
        return "The given database ID '%s' does not exists. Generated databases are deleted after 7 days."% name


if __name__ == '__main__':
    app.run()
