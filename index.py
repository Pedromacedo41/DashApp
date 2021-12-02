from app import app
from layout import serve_layout

from pages.select_csv import callbacks
from pages.csv_dashboard import callbacks
from pages.csv_review import callbacks
from pages.home import callbacks
from pages.text_extraction import callbacks

import routing
import callbacks

# Running the server
if __name__ == "__main__":
    app.layout = serve_layout
    app.run_server(debug=True, port=8050)
