#!/bin/bash

#################################
## Begin of user-editable part ##
#################################

POOL=ergo.herominers.com:10250
WALLET=9i9m9AxmqgBUBD6GfYJQHZiHQ5d6AP7Ak3QVFfKiNtopQnMZkmG.lolMinerWorker

#################################
##  End of user-editable part  ##
#################################

cd "$(dirname "$0")"

./lolMiner --algo ETHASH --pool $POOL --user $WALLET $@
while [ $? -eq 42 ]; do
    sleep 10s
    ./lolMiner --algo ETHASH --pool $POOL --user $WALLET $@
done
