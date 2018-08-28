mkdir -p hackson
mkdir -p import 
docker run -p 8983:8983 -v hackson:/opt/solr/server/solr/hackson -v import:/opt/solr/import solr /bin/bash
docker ps -a | grep 8983

