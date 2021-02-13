CONF_FILE=$1
DUMP_NAME=$2
COMPRESS="NO"

if [[ "x$CONF_FILE" == "x" ]]; then
    echo "[ERROR] Please provide a valid configuration file."
    exit
fi

if [[ ! -f $CONF_FILE ]]; then
    echo "[ERROR] Provided conf file '$CONF_FILE' does not exist"
    exit
fi

DB_NAME=$(jq -r '.DB_NAME' "$CONF_FILE")
DB_USER=$(jq -r '.DB_USER' "$CONF_FILE")

if [[ "x$DB_NAME" == "xnull" ]]; then
    echo "[ERROR] Conf file '$CONF_FILE' does not provide a DB name."
    exit
fi

if [[ "x$DB_USER" == "xnull" ]]; then
    echo "[ERROR] Conf file '$CONF_FILE' does not provide a DB user name."
    exit
fi

if [[ "x$DUMP_NAME" == "x" ]]; then
    DUMP_NAME=$DB_NAME
fi

if [[ "x$3" == "xgz" ]]; then
    COMPRESS="GZ"
elif [[ "x$3" == "xxz" ]]; then
    COMPRESS="XZ"
fi

DUMP_FILE=${DUMP_NAME}_$(date +%Y%m%d_%H%M%S).dump
if [[ "x$COMPRESS" == "xGZ" ]]; then
    DUMP_FILE=$DUMP_FILE.gz
elif [[ "x$COMPRESS" == "xXZ" ]]; then
    DUMP_FILE=$DUMP_FILE.xz
fi

if [[ -f $DUMP_FILE ]]; then
    echo "[ERROR] Provided db dump file '$DUMP_FILE' exists! Refusing to overwrite"
    exit
fi

#  Execute dump:
if [[ "x$COMPRESS" == "xGZ" ]]; then
    pg_dump -U $DB_USER "$DB_NAME" | gzip > $DUMP_FILE
elif [[ "x$COMPRESS" == "xXZ" ]]; then
    pg_dump -U $DB_USER "$DB_NAME" | xz > $DUMP_FILE
else
    pg_dump -U $DB_USER "$DB_NAME" > $DUMP_FILE
fi
