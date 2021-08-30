
#!/usr/bin/bash

methods=("TRACE" "GET" "PUT" "HEAD" "DELETE" "CONNECT" "OPTIONS" "invalid")

figlet "CHK-METHODS"
echo -e "$( tput bold )\nHTTP Methods Testing$( tput sgr0 )"

for m in "${methods[@]}";do
	if [[ $( echo "$m" | grep "HEAD" ) ]]; then echo "${m} Request" && curl --insecure --head "$1"
	else echo "${m} Request" && curl --insecure -X "${m}" "$1" ; fi
done
exit 0
