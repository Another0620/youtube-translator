from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator

video_id = "dQw4w9WgXcQ"

# 抓取 transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
text = " ".join([item['text'] for item in transcript])

# 翻譯
translator = Translator()
translation = translator.translate(text, dest='zh-tw')

# 印出翻譯結果
print(translation.text)
