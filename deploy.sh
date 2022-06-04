docker build --tag iplookupv2 .
docker stop iplookupv2
docker rm iplookupv2
nohup docker run --restart unless-stopped --name iplookupv2 -p 5001:5001 iplooku
pv2_image &
