from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Deployment Successful ❤️</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                text-align: center;
            }
 
            .box {
                max-width: 650px;
                padding: 40px;
                border-radius: 20px;
                background: #1e293b;
                box-shadow: 0 0 30px rgba(255, 255, 255, 0.1);
            }
 
            .status {
                color: #22c55e;
                font-size: 18px;
                margin-bottom: 20px;
            }
 
            h1 {
                font-size: 42px;
                margin: 10px;
            }
 
            .heart {
                font-size: 70px;
                animation: beat 1s infinite;
            }
 
            p {
                font-size: 20px;
                line-height: 1.6;
                color: #cbd5e1;
            }
 
            button {
                margin-top: 20px;
                padding: 14px 25px;
                border: none;
                border-radius: 10px;
                background: #ec4899;
                color: white;
                font-size: 18px;
                cursor: pointer;
            }
 
            #message {
                display: none;
                margin-top: 25px;
                font-size: 24px;
                color: #f9a8d4;
            }
 
            @keyframes beat {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.2); }
            }
        </style>
    </head>
 
    <body>
        <div class="box">
 
            <div class="status">
                🟢 Deployment Successful
            </div>
 
            <h1>Version 3 ❤️</h1>
 
            <div class="heart">❤️</div>
 
            <p>
                GitHub pushed the code.<br>
                Docker built the image.<br>
                ECR stored it.<br>
                EKS deployed it.
            </p>
 
            <p>
                But honestly...
                <br>
                <strong>You are still my favourite deployment.</strong> 😂❤️
            </p>
 
            <button onclick="showMessage()">
                Click for a surprise 🥺
            </button>
 
            <div id="message">
                I may know AWS, Docker & Kubernetes...<br>
                but you are the only thing I can't live without. ❤️🥺
            </div>
 
        </div>
 
        <script>
            function showMessage() {
                document.getElementById("message").style.display = "block";
            }
        </script>
 
    </body>
    </html>
    """
 
@app.route("/health")
def health():
    return "Healthy ❤️"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
