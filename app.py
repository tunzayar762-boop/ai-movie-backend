from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Frontend ကနေ လှမ်းချိတ်လို့ရအောင်

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.json
    video_link = data.get('videoLink')
    voice_type = data.get('voiceType')
    ai_gender = data.get('aiGender')
    bgm = data.get('bgm')
    platform = data.get('platform')

    print(f"Received Link: {video_link}")
    print(f"Voice: {voice_type}, Gender: {ai_gender}, BGM: {bgm}, Platform: {platform}")

    # TODO: ဒီနေရာမှာ MoviePy နဲ့ AI အသံတွေကို ပေါင်းစပ်ပြီး 30 Sec Video ထုတ်မယ့် Logic ရေးရပါမယ်။
    
    # ယာယီအနေနဲ့ အလုပ်လုပ်ကြောင်း Response ပြန်ပေးခြင်း
    return jsonify({
        "status": "success",
        "message": "ဗီဒီယို အောင်မြင်စွာ ထုတ်လုပ်ပြီးပါပြီ!",
        "video_url": "#"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
