from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator

app = Flask(__name__)

@app.route("/transcript", methods=["POST"])
def get_transcript():
    data = request.get_json()
    video_id = data.get("video_id")

    # 抓字幕
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    text = " ".join([item['text'] for item in transcript])

    # 翻譯
    translator = Translator()
    translation = translator.translate(text, dest='zh-tw')

    return jsonify({"transcript": translation.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
