init_files = './00_readme_url_init.md'
urls_file = '02_repository_urls.txt'
urls = []

with open(init_files, 'r') as f:
	for line in f:
		try:
			urls.append(line.strip().split('](')[1].split(')')[0])
		except:
			pass

with open(urls_file, 'w+') as of:
	for line in urls:
		of.write(line.strip()+'\n')

