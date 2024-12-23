from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>صفحة أيمن محمود</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');

            body {
                font-family: 'Cairo', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #2f2f2f;
                color: #ffffff;
                overflow: hidden;
                text-align: center;
            }

            canvas {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
            }

            h1 {
                font-size: 3rem;
                color: #ffffff;
                margin-top: 100px;
                text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.5);
            }

            p {
                font-size: 1.5rem;
                margin-bottom: 30px;
                color: #ffffff;
            }

            a {
                display: inline-block;
                padding: 15px 40px;
                font-size: 1.2rem;
                font-weight: 600;
                color: #ffffff;
                background: linear-gradient(135deg, #00c6ff, #0072ff);
                text-decoration: none;
                border-radius: 30px;
                box-shadow: 0 5px 15px rgba(0, 123, 255, 0.4);
                transition: all 0.3s ease;
            }

            a:hover {
                background: linear-gradient(135deg, #0072ff, #00c6ff);
                transform: translateY(-3px);
                box-shadow: 0 10px 30px rgba(0, 123, 255, 0.6);
            }
        </style>
    </head>
    <body>
        <canvas id="background"></canvas>
        <h1>مرحباً بك في صفحة أيمن محمود!</h1>
        <p>إذا كنت تود الذهاب إلى الموقع الإلكتروني الخاص بشركة أيمن محمود، اضغط على الزر أدناه.</p>
        <a href="https://ayman-mood.my.canva.site/services" target="_blank">الدخول</a>
        <script>
            const canvas = document.getElementById("background");
            const ctx = canvas.getContext("2d");

            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const particles = [];
            const mouse = {
                x: null,
                y: null
            };

            class Particle {
                constructor(x, y, size, speedX, speedY, color) {
                    this.x = x;
                    this.y = y;
                    this.size = size;
                    this.speedX = speedX;
                    this.speedY = speedY;
                    this.color = color;
                }

                draw() {
                    ctx.fillStyle = this.color;
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.closePath();
                    ctx.fill();
                    ctx.shadowColor = this.color;
                    ctx.shadowBlur = 15;
                }

                update() {
                    this.x += this.speedX;
                    this.y += this.speedY;

                    // Bounce particles off walls
                    if (this.x > canvas.width || this.x < 0) this.speedX *= -1;
                    if (this.y > canvas.height || this.y < 0) this.speedY *= -1;

                    // Move particles towards the mouse/touch
                    const dx = mouse.x - this.x;
                    const dy = mouse.y - this.y;
                    const distance = Math.sqrt(dx * dx + dy * dy);

                    if (distance < 100) {
                        this.x -= dx / 20;
                        this.y -= dy / 20;
                    }
                }
            }

            function initParticles() {
                for (let i = 0; i < 50; i++) {
                    const size = Math.random() * 8 + 3;
                    const x = Math.random() * canvas.width;
                    const y = Math.random() * canvas.height;
                    const speedX = Math.random() * 2 - 1;
                    const speedY = Math.random() * 2 - 1;
                    const color = Math.random() > 0.5 ? "rgba(0, 183, 255, 0.8)" : "rgba(150, 150, 150, 0.8)";

                    particles.push(new Particle(x, y, size, speedX, speedY, color));
                }
            }

            function animate() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                particles.forEach((particle) => {
                    particle.draw();
                    particle.update();
                });

                requestAnimationFrame(animate);
            }

            initParticles();
            animate();

            window.addEventListener("resize", () => {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                particles.length = 0;
                initParticles();
            });

            window.addEventListener("mousemove", (event) => {
                mouse.x = event.x;
                mouse.y = event.y;
            });

            window.addEventListener("touchmove", (event) => {
                mouse.x = event.touches[0].clientX;
                mouse.y = event.touches[0].clientY;
            });

            window.addEventListener("mouseleave", () => {
                mouse.x = null;
                mouse.y = null;
            });
        </script>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)