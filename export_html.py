import sqlite3

DB_PATH = "data/news.db"
OUTPUT_PATH = "output/index.html"


def export_html():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT source, title, url
        FROM articles
        ORDER BY id DESC
        LIMIT 50
    """)

    rows = cursor.fetchall()
    conn.close()

    html = """
<html>
<head>
    <meta charset="UTF-8">
    <title>Tech Digest</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            background: #f7f7f7;
        }

        h1 {
            color: #222;
        }

        li {
            list-style: none;
            background: white;
            padding: 15px;
            margin-bottom: 12px;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        }

        a {
            text-decoration: none;
            color: #0066cc;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
"""
    for source, title, url in rows:
        html += f"""
        <li>
            <b>{source}</b><br>
            <a href="{url}" target="_blank">{title}</a>
        </li>
        <br>
        """

    html += """
        </ul>
    </body>
    </html>
    """

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    print("HTML出力完了:", OUTPUT_PATH)