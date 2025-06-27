from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator

app = Flask(__name__)

# 根路由，讓 Vercel 不會 404
@app.route("/", methods=["GET"])
def index():
    return "✅ Vercel 部署成功！Flask 正在運作中！"

# 抓字幕 + 翻譯 API
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
