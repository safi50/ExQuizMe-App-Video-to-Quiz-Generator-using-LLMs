from app import app

if __name__ == "__main__":
    # Specifies the host and port on which the app will run. 
    # For development purposes, we use localhost (127.0.0.1) and port 5000.
    # The `debug=True` option enables auto-reload on code changes, facilitating development.
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
