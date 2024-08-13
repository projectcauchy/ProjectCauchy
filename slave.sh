#!/bin/bash
set -e

until mysql -h mysql-master -u root -padmin123 -e "SELECT 1"; do
  echo "Waiting for mysql-master database connection..."
  sleep 4
done

mysql -h mysql-master -u root -padmin123 <<-EOSQL
  SHOW MASTER STATUS\G
EOSQL

echo "Slave configuration started"

MASTER_STATUS=$(mysql -h mysql-master -u root -padmin123 -e "SHOW MASTER STATUS\G")
MASTER_LOG_FILE=$(echo "$MASTER_STATUS" | grep "File:" | awk '{print $2}')
MASTER_LOG_POS=$(echo "$MASTER_STATUS" | grep "Position:" | awk '{print $2}')

mysql -u root -padmin123 <<-EOSQL
  STOP SLAVE;
  CHANGE MASTER TO MASTER_HOST='mysql-master',
  MASTER_USER='replica_user',
  MASTER_PASSWORD='admin123',
  MASTER_LOG_FILE='$MASTER_LOG_FILE',
  MASTER_LOG_POS=$MASTER_LOG_POS;
  START SLAVE;
  SHOW SLAVE STATUS\G
EOSQL

echo "Slave configuration completed"