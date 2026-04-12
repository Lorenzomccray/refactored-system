import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://pwttyjytvzanpaotrcrw.supabase.co")
SUPABASE_KEY = os.getenv(
    "SUPABASE_KEY",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB3dHR5anl0dnphbnBhb3RyY3J3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTcwOTY5NjMsImV4cCI6MjA3MjY3Mjk2M30.vvFS5Wk6YRt2jmFRgsiU8IHCTWC1joHHc7rd-agPqmI",
)

_client: Client = None


def get_db() -> Client:
    global _client
    if _client is None:
        _client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return _client
