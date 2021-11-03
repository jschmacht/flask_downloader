from flask import Flask, Response, stream_with_context, request, abort, jsonify, send_from_directory

from pip._vendor import requests

api = Flask(__name__)

UPLOAD_DIRECTORY = "/project/api_uploaded_files"

@api.route('/')
def hello_world():
    return 'Hello World!'


CHUNK_SIZE = 8192
def read_file_chunks(path):
    with open(path, 'rb') as fd:
        while 1:
            buf = fd.read(CHUNK_SIZE)
            if buf:
                yield buf
            else:
                break

@api.route('/download/<name>')
def serve_generated_database(name):
    fp = '/mnt/vol1/tax2proteome_result/' + name + '.fasta.gz'
    if fp.exists():
        return Response(
            stream_with_context(read_file_chunks(fp)),
            headers={
                'Content-Disposition': f'attachment; filename={name}'
            }
        )
    else:
        raise exc.NotFound()

@api.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8000)