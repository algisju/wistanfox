while read subdomain; do
if host "$subdomain" > /dev/null; then
# If host is live, print it into
# a file called "live.txt".
echo "$subdomain" >> live.txt
fi
done < validsub.txt
