"""A small in-memory catalog for songs and playlists."""

import json
import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE songs (id INTEGER PRIMARY KEY, title TEXT, "
    "artist TEXT, plays INTEGER)"
)


def add_song(title, artist, plays=0, playlist=None):
    """Add a song to the catalog and its playlist, then return the playlist."""
    if playlist is None:
        playlist = []
    conn.execute(
        "INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)",
        (title, artist, plays),
    )
    playlist.append(title)
    return playlist


def shuffle_pick():
    """Return a randomly selected song ID, or None for an empty catalog."""
    ids = [row[0] for row in conn.execute("SELECT id FROM songs")]
    if not ids:
        return None
    return secrets.choice(ids)


def popularity(title):
    """Return the popularity category for a song title."""
    row = conn.execute(
        "SELECT plays FROM songs WHERE title = ?", (title,)
    ).fetchone()
    if row is None:
        return "unknown"
    return "popular" if row[0] > 100 else "niche"


def save_playlist(playlist):
    """Serialize a playlist as a JSON string."""
    return json.dumps(playlist)


def load_playlist(blob):
    """Deserialize a playlist from a JSON string."""
    return json.loads(blob)


def total_plays():
    """Return the total play count across all songs."""
    return conn.execute(
        "SELECT COALESCE(SUM(plays), 0) FROM songs"
    ).fetchone()[0]


def main():
    """Run the catalog demonstration."""
    playlist = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, playlist)
    blob = save_playlist(playlist)
    loaded_playlist = load_playlist(blob)
    if len(loaded_playlist) > 1:
        print("multi-song playlist")
    print(
        popularity("Aurora"),
        popularity("Monsoon"),
        shuffle_pick(),
        total_plays(),
    )


if __name__ == "__main__":
    main()
