from youtube_transcript_api import YouTubeTranscriptApi

# 影片 ID
video_id = "dQw4w9WgXcQ"

# 取得 transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# 把所有字幕合併成一段文字
result = " ".join([item['text'] for item in transcript])

print(result)
