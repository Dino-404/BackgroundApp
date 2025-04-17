from flask import Flask, jsonify, request
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route("/get_audio_url")
def get_audio_url():
    video_id = request.args.get('id')
    if not video_id:
        return jsonify({'error': 'Video ID is required'}), 400

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'extractaudio': True,
        'audioquality': 1,
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
        audio_url = info_dict['formats'][0]['url']
        return jsonify({'audio_url': audio_url})

if __name__ == "__main__":
    app.run(debug=True)
