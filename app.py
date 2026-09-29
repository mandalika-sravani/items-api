from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok", version="1.0.0")    

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
