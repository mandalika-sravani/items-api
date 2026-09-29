from itertools import count

from flask import Flask, abort, jsonify, request


def create_app():
    app = Flask(__name__)
    items = {}
    ids = count(1)

    @app.get("/health")
    def health():
        return jsonify(status="ok", service="items-api", version="1.0.0")

    @app.get("/items")
    def list_items():
        return jsonify(list(items.values()))

    @app.post("/items")
    def create_item():
        data = request.get_json(silent=True) or {}
        name = data.get("name")
        if not name:
            abort(400, description="'name' is required")
        item = {"id": next(ids), "name": name}
        items[item["id"]] = item
        return jsonify(item), 201

    @app.get("/items/<int:item_id>")
    def get_item(item_id):
        item = items.get(item_id)
        if item is None:
            abort(404)
        return jsonify(item)

    @app.put("/items/<int:item_id>")
    def update_item(item_id):
        if item_id not in items:
            abort(404)
        data = request.get_json(silent=True) or {}
        name = data.get("name")
        if not name:
            abort(400, description="'name' is required")
        items[item_id]["name"] = name
        return jsonify(items[item_id])

    @app.delete("/items/<int:item_id>")
    def delete_item(item_id):
        if items.pop(item_id, None) is None:
            abort(404)
        return "", 204

    return app


if __name__ == "__main__":
    create_app().run(debug=True)