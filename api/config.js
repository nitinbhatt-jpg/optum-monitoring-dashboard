export default function handler(req, res) {
  res.setHeader("Content-Type", "application/json");
  res.setHeader("Cache-Control", "no-store");

  const url = process.env.SUPABASE_URL || "";
  const key = process.env.SUPABASE_SERVICE_KEY || "";
  const bucket = process.env.SUPABASE_BUCKET || "eye-test-sessions";

  if (!url || !key) {
    return res.status(500).json({ error: "Supabase environment variables not configured" });
  }

  return res.status(200).json({ url, key, bucket });
}
