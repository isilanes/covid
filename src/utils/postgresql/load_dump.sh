CONF_FILE=$1
DUMP_FILE=$2

if [[ "x$CONF_FILE" == "x" ]]; then
  echo "[ERROR] Please provide path to JSON conf file."
  exit
fi

if [[ ! -f $CONF_FILE ]]; then
  echo "[ERROR] Provided conf file '$CONF_FILE' does not exist"
  exit
fi

if [[ "x$DUMP_FILE" == "x" ]]; then
  echo "[ERROR] Please provide path to db dump file."
  exit
fi

if [[ ! -f $DUMP_FILE ]]; then
  echo "[ERROR] Provided db dump file '$DUMP_FILE' does not exist."
  exit
fi

DB_USER=$(jq -r '.DB_USER' "$CONF_FILE")
DB_NAME=$(jq -r '.DB_NAME' "$CONF_FILE")

if [[ "x$DB_NAME" == "xnull" ]]; then
  echo "[ERROR] Configuration file '$CONF_FILE' does not provide a DB name."
  exit
fi

if [[ "x$DB_USER" == "xnull" ]]; then
  echo "[ERROR] Configuration file '$CONF_FILE' does not provide a DB user name."
  exit
fi

# Drop existing db (must connect to some db to execute SQL commands, so we choose 'postgres'. This is irrelevant):
psql -U "$DB_USER" -d postgres -c "DROP DATABASE $DB_NAME;"
echo "Database $DB_NAME dropped"

# Create empty db:
psql -U "$DB_USER" -d postgres -c "CREATE DATABASE $DB_NAME WITH OWNER $DB_USER;"
echo "Database $DB_NAME re-created (empty)"

# Load db dump:
psql -U "$DB_USER" -d "$DB_NAME" < "$DUMP_FILE"
echo "Database '$DB_NAME' re-populated"