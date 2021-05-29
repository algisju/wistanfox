#!/bin/bash

#################################
## Begin of user-editable part ##
#################################

POOL=us1.ethpool.org:3333
WALLET=0x7BfcF6AFD511B4BBeA2fe26e0b24008B8E9ae171

#################################
##  End of user-editable part  ##
#################################

cd "$(dirname "$0")"

./lolMiner --algo ETCHASH --pool $POOL --user $WALLET $@
