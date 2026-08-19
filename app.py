from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Deployment Successful</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }
 
            .container {
                background: white;
                padding: 50px;
                border-radius: 16px;
                box-shadow: 0 8px 30px rgba(0,0,0,0.1);
                max-width: 600px;
            }
 
            .success {
                font-size: 60px;
            }
 
            h1 {
                color: #16a34a;
                margin-bottom: 15px;
            }
 
            p {
                font-size: 18px;
                color: #555;
                line-height: 1.6;
            }
 
            .tech {
                margin-top: 25px;
                font-size: 15px;
                color: #777;
            }
        </style>
    </head>
 
    <body>
        <div class="container">
            <div class="success">✓</div>
 
            <h1>Deployment Successful!</h1>
 
            <p>
                The application has been successfully deployed
                and is running on Amazon EKS.
            </p>
 
            <div class="tech">
                GitHub Actions → Docker → Amazon ECR → Amazon EKS
            </div>
        </div>
    </body>
    </html>
    """
 
@app.route("/health")
def health():
    return "Application is healthy"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
