import glob
import re
import sys

"""
Usage
python3 md_to_tsv.py **.md
"""


def extract_sentences_from_md(markdown: str) -> list:
    """
    extract sentences from markdown format
    """

    # delete URL
    result = re.sub(r"\(*(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)\)*", "" ,markdown)
    # delete "*" and "-"
    result = re.sub("[\*\-]\s.+", "", result)
    # delete number colum marks
    result = re.sub("[0-9]+\.+\s", "", result)
    # delete source codes
    result = re.sub(r"`+(.+\n)+`+", "", result)
    result = re.sub(r"\s{4,}.+", "", result)
    result = re.sub(r"<[^>]+>", "", result)
    result = re.sub(r"^>\s.+", "", result)
    result = re.sub(r"\$\s.+", "", result)
    # delete "[]" and "()"
    result = re.sub(r"!\[.+Status\]", "", result)
    result = re.sub(r"[\[\]\(\)]", " ", result)
    # delete only one word in sentence
    result = re.sub(r"\n\S+\n", "\n", result)
    # delete extra "\n"
    result = re.sub(r"\n+", "\n", result)
    # delete enchance marks
    result = re.sub(r"`", "", result)
    result = re.sub(r"|", "", result)
    result_array = result.split("\n")
    while result_array.count("") > 0:
        result_array.remove("")
    return result_array


def parse_header_sentence_dict(array: list) -> dict:
    """
    make dict
    ex.)
    # About
    This is a NLP application. This application is examples search application.

    ## Using Acai to start services
    The real power of Acai comes when your production server is configured
    with Guice and you create an alternate test module which configures your server
    with heavyweight dependencies like databases replaced with local in-memory
    implementations. You could then start this server once for all tests in the
    suite (to avoid waiting for it to start between each test) and wipe the
    database between tests (to cheaply isolate test-cases from one-another).

    => {About: This is a NLP application. This application is examples search application., Using Acai to start services: The real power of Acai comes ... test-cases from one-another).}
    """

    i = 0
    row_2 = ""
    dic = {}
    while i < len(array):
        if array[i][0] == "#":
            row_2 = re.sub(r"#+\s", "", array[i])
            dic[row_2] = ""
        elif row_2 != "":
            dic[row_2] += array[i]
        i += 1
    return dic


def parse_to_tsv_format(name: str, dic: dict) -> str:
    """
    parse tsv format
    """

    tsv = ""
    for k, v in dic.items():
        sentences = v.split(". ")
        for sentence in sentences:
            if sentence != "":
                tsv += name + "\t" + k + "\t" + sentence + "\n"
    return tsv


def markdown_to_tsv(filename: str):
    with open(filename, "r") as f:
        markdown = f.read()
    array = extract_sentences_from_md(markdown)
    dic = parse_header_sentence_dict(array)
    name = filename[filename.find("/") + 1:] if "/" in filename else filename
    name = name.replace(".md", "")
    print(parse_to_tsv_format(name, dic))


if __name__ == "__main__":
    args = sys.argv
    markdown_to_tsv(args[1])
