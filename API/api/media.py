from pathlib import Path
from urllib.parse import urlsplit
from uuid import uuid4

from flask import jsonify, request
from werkzeug.utils import secure_filename

MEDIA_ROOT = Path(__file__).resolve().parent.parent / "media"
ALLOWED_EXTENSIONS = {"gif", "jpeg", "jpg", "png", "webp"}


def normalize_media_path(value):
    value = (value or "").strip()
    if not value:
        return value
    path = urlsplit(value).path
    marker = "/media/"
    if marker in path.lower():
        index = path.lower().index(marker)
        return marker + path[index + len(marker):].lstrip("/")
    return value


def public_media_url(value):
    value = normalize_media_path(value)
    if value.startswith("/media/"):
        return request.host_url.rstrip("/") + value
    return value


class Media:
    @staticmethod
    def upload():
        upload = request.files.get("image")
        category = request.form.get("category", "associates").strip().lower()
        if category not in {"associates", "users"}:
            return jsonify({"Message": "Invalid media category", "Response": 400}), 400
        if not upload or not upload.filename:
            return jsonify({"Message": "Image is required", "Response": 400}), 400

        original = secure_filename(upload.filename)
        extension = Path(original).suffix.lower().lstrip(".")
        if extension not in ALLOWED_EXTENSIONS:
            return jsonify({"Message": "Unsupported image type", "Response": 400}), 400

        destination = MEDIA_ROOT / category
        destination.mkdir(parents=True, exist_ok=True)
        filename = f"{uuid4().hex}-{original}"
        upload.save(destination / filename)
        path = f"/media/{category}/{filename}"
        return jsonify({"Message": "Uploaded Successfully", "Response": 200, "path": path}), 200