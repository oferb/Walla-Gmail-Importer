import csv
import chardet
import codecs
from pprint import pprint
import os

def walla_to_gmail_import(input_filename, print_debug=False):
    # get encoding
    with open(input_filename) as f:
        content = f.readlines()
    chardet_res = chardet.detect(content[0])
      
    # read file contents into lines
    try:
        data = codecs.open(input_filename, 'r', chardet_res['encoding']).read()
    except:
        data = codecs.open(input_filename, 'r', 'UTF-16LE').read()
        
    if data.startswith(u'\ufeff'):
        data = data[1:] # remove BOM - byte order mark
    lines = filter(None, data.split('\n'))
    filter(None, lines)

    names_first_line = []
    emails_first_line = []
    
    # process first line
    first_line = lines[0]
    first_line_emails = first_line.split(',')
    first_line_emails = [x.strip() for x in first_line_emails]
    for email in first_line_emails:
        name = email.split('@')[0] + " " + email.split('@')[1].split('.')[0]
        names_first_line.append(name)
        emails_first_line.append(email)

    names_rest = []
    emails_rest = []    

    del lines[0]
    lines = [x for x in lines if len(x) > 1]
    for line in lines:
        
        line_space_spit = line.split()
        email = [x for x in line_space_spit if '@' in x][0]
        line_space_spit.remove(email)
        name = " ".join([x for x in line_space_spit])
        name.replace(',','')
        names_rest.append(name)
        emails_rest.append(email)
    
    names_rest = [x.replace(',',' ') for x in names_rest]
    
    if print_debug:
        for name, email,line in zip(names_rest, emails_rest, lines):
            print 'ORIGINAL=%s' % (line)
            print 'PROCESSED=(name=%s,email=%s)' % (name, email)
            print
        
    names = names_first_line + names_rest
    emails = emails_first_line + emails_rest

    print 'Name,Email Address'
    for name, email in zip(names, emails):
        print '%s,%s' % (name, email) 
    
    return names, emails

if __name__ == "__main__":
    walla_to_gmail_import(os.path.join(os.path.dirname(__file__), 'walla_contacts.txt'))
    
       