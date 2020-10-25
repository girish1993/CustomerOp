DB_FILE=app.db
APP_PORT=5000

if [ -f "$DB_FILE" ]; then
   echo "Database exists. Starting the server"
   gunicorn -w 4 -b 127.0.0.1:$APP_PORT main:app
else
  echo "Database doesn't exist. Creating the database.."
  python3 DBSetup.py
  echo "Starting the server.."
  gunicorn -w 4 -b 127.0.0.1:$APP_PORT main:app
fi