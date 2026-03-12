import http.server
import json
import os

ENV = {}
env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                ENV[k.strip()] = v.strip()


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/config":
            url = ENV.get("SUPABASE_URL", "")
            key = ENV.get("SUPABASE_SERVICE_KEY", "")
            bucket = ENV.get("SUPABASE_BUCKET", "eye-test-sessions")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()

            if not url or not key:
                body = {"error": "Supabase environment variables not configured"}
            else:
                body = {"url": url, "key": key, "bucket": bucket}

            self.wfile.write(json.dumps(body).encode())
            return

        return super().do_GET()


if __name__ == "__main__":
    port = 8080
    server = http.server.HTTPServer(("", port), Handler)
    print(f"Serving on http://localhost:{port}")
    server.serve_forever()
