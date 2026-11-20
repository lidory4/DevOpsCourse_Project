from flask import Flask
import Score
import Utils

app = Flask(__name__)

@app.route("/")
def score_server():
    score = Score.read_score() 
    if score == Utils.BAD_RETURN_CODE:
        return """<html>
        <head>
        <title>Scores Game</title>
        <style>
              body {
                margin: 0;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, #1e1b4b, #0f766e);
                font-family: Segoe UI, Arial, sans-serif;
              }
              .card {
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 20px;
                padding: 40px 60px;
                text-align: center;
                color: white;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
              }
              .label {
                font-size: 40px;
                letter-spacing: 3px;
                text-transform: uppercase;
                opacity: 0.7;
              }
              #score {
                display: block;
                font-size: 28px;
                font-weight: bold;
                color: #ef4444;
              }
            </style>
          </head>
          <body>
            <div class="card">
              <div class="label">score</div>
              <span id="score">Score is unvalible</span>
            </div>
          </body>
        </html>""", 500
    return """<html>
  <head>
    <title>Scores Game</title>
    <style>
      body {
        margin: 0;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #1e1b4b, #0f766e);
        font-family: Segoe UI, Arial, sans-serif;
      }
      .card {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 40px 60px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
      }
      .label {
        font-size: 40px;
        letter-spacing: 3px;
        text-transform: uppercase;
        opacity: 0.7;
      }
      #score {
        display: block;
        font-size: 28px;
        font-weight: bold;
        color: #fbbf24;
      }
    </style>
  </head>
  <body>
    <div class="card">
      <div class="label">score</div>
      <span id="score">""" + str(score) + """</span>
    </div>
  </body>
</html>"""

app.run(port=5000)

