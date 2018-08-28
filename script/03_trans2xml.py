# line: title \t session \t sentence
file_list = './filelist.txt'
tsv_file_path = './readme.tsv'
xml_file_path = './index.xml'

def get_files(file_list):
	file_paths = []
	with open(file_list, 'r+') as f:
		for line in f:
			filename = line.strip()
			file_paths.append(filename)
	return file_paths

def get_contents(filename):
	contents = []
	with open(filename, 'r')as f:
		for line in f:
			splitlines = line.split('\t')
			content = [x.strip() for x in splitlines]
			contents.append(content)
	return contents

def tran2xmlcontents(contents):
	lines = []
	doc_start = '<doc>'
	doc_end = '</doc>\n'
	field_end = '</field>'
	id_start = '<field name="id">'
	title_start = '<field name="title">'
	session_start = '<field name="session">'
	sentence_start = '<field name="sentence">'
	start_id = ID
	## gen xml file 
	for content in contents:
		line = doc_start + id_start + str(start_id) \
				+field_end + title_start + str(content[0]).strip() + field_end \
				+ session_start + str(content[1]).strip() + field_end \
				+ sentence_start + str(content[2]).strip() + field_end + doc_end
		lines.append(line)
		start_id =  start_id + 1
	last_id = start_id
	return lines, last_id
	
def write_xml(xmlcontents, filename):
	with open(filename, 'a') as f:
		for content in xmlcontents:
			f.write(str(content))

if __name__ == '__main__':
	ID = 1
	all_files = get_files(file_list)
	with open(xml_file_path, 'w') as f:
		f.write('<add>\n')
	for tsv_file in all_files:
		init_contents = get_contents(tsv_file)
		xml_contents, last_id = tran2xmlcontents(init_contents)
		ID = last_id
		write_xml(xml_contents, xml_file_path)
	with open(xml_file_path, 'a') as f:
		f.write('</add>\n')