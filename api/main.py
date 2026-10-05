import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler

APP_NAME = "Fixable"
APP_VERSION = "3.0.0"


def json_response(handler: BaseHTTPRequestHandler, status: int, payload: dict) -> None:
    body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Cache-Control", "no-store")
    handler.send_header("X-Content-Type-Options", "nosniff")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class handler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        # Do not add application-level request logging.
        return

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]

        if path == "/api/health":
            json_response(
                self,
                200,
                {
                    "status": "ok",
                    "service": APP_NAME,
                    "version": APP_VERSION,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                },
            )
            return

        json_response(self, 404, {"status": "error", "error": "not_found"})
