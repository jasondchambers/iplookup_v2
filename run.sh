docker stop iplookup
nohup docker run --name iplookup -p 5001:5001 iplookup &
