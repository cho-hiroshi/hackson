org_path='../../01_init_data/google-readme/'
docs=`ls $org_path`
for doc in $docs
do
	cmark $org_path$doc -o ./$doc.json -aj
done