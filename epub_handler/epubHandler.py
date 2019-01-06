import epub
from bs4 import BeautifulSoup

#global
epub_page_no = -1

def parse_text(htmlfile):
    soup = BeautifulSoup(htmlfile, 'html.parser')
    soup.prettify('UTF-8')
    text = soup.get_text()
    return text

def load_files(filename):
    item_list = []
    details = {}
    with  epub.open_epub ( filename )  as  book :
        
        #fillup up epub details
        details['Title'] = book.opf.metadata.titles
        details['Creators'] = book.opf.metadata.creators
        details['Subjects'] = book.opf.metadata.subjects
        details['Description'] = parse_text(book.opf.metadata.description)
        details['Publisher'] = book.opf.metadata.publisher
        details['Contributors'] = book.opf.metadata.contributors
        details['Dates'] = book.opf.metadata.dates
        details['Dc_type'] = book.opf.metadata.dc_type
        details['Format'] = book.opf.metadata.format
        details['Identifiers'] = book.opf.metadata.identifiers
        details['Source'] = book.opf.metadata.source
        details['Languages'] = book.opf.metadata.languages
        details['Relation'] = book.opf.metadata.relation
        details['Coverage'] = book.opf.metadata.coverage
        details['Rights'] = book.opf.metadata.right
        details['Metas'] = book.opf.metadata.metas
        
        
        #read the pages
        for  item_id ,  linear  in  book.opf.spine.itemrefs :
            item  =  book . get_item ( item_id )
            # read the content 
            data  =  book . read_item( item )
            item_list.append(data)
            
    return item_list,details,len(item_list)

def get_page_by_number_txt(fileList,num):
    global epub_page_no
    epub_page_no= num
    if(epub_page_no>=len(fileList)):
        epub_page_no=len(fileList)-1
    if(epub_page_no<0):
        epub_page_no=0
    text = parse_text(fileList[epub_page_no])
    return text, epub_page_no+1

def get_next_page(fileList):
    num = epub_page_no +1
    text,num = get_page_by_number_txt(fileList,num)
    return text, num
  
def get_prev_page(fileList):
    num = epub_page_no -1
    text,num = get_page_by_number_txt(fileList,num)
    return text, num
    
def get_page_by_number(fileList,num):
    text, num = get_page_by_number_txt(fileList,num-1)
    return text, num


#l,d,e = load_files('test.epub')
#t,p=get_page_by_number_txt(l,8)