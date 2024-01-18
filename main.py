import re
import nltk
import ssl
import json
import os
from pprint import pprint
import shlex
import requests
from PyPDF2 import PdfReader


from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.corpus import stopwords
from nltk.tokenize import MWETokenizer




cleaingPatterns = [r"Page \d+ of \d+", r"\d+ of \d+"]
tocPatterns = r"^PART \d+: [A-Za-z &]+$"
lastTableHeaders = []

def mergeCells(row):
    merged_row = []
    cell_to_merge = ""
    for cell in row:
        if cell is not None:
            if cell_to_merge:
                merged_row.append(cell_to_merge)
                cell_to_merge = ""
            merged_row.append(cell)
        else:
            if cell_to_merge:
                # If already in a sequence of Nones, continue appending Nones
                cell_to_merge += " "
            else:
                # Start of a new sequence of Nones
                temp = ''
                if len(merged_row) > 0:
                    temp = merged_row.pop()
                cell_to_merge = temp + " "
    if cell_to_merge:  # If the last cells were Nones, append the merged content
        merged_row.append(cell_to_merge)
    return merged_row


def isTableHeader(row):
    for c in range(len(row)):
        words = shlex.split(row[c])
        if len(words) > 10: return False
    if len(row) < 2: return False
    return True



def label_row_with_headers(row, headers):
    workingHearders = headers
    if len(headers) == 1:
        workingHearders = lastTableHeaders

    if isTableHeader(headers) == False: return row

    if len(row) == len(workingHearders):  # Check if the row matches the header length
        if len(workingHearders) == 1:
            labeled_row = []
            for header, cell in zip(workingHearders, row):
                labeled_cell = f"{cell}"
                labeled_row.append(labeled_cell)
        else:
            labeled_row = []
            for header, cell in zip(workingHearders, row):
                labeled_cell = f"{header}: {cell}"
                labeled_row.append(labeled_cell)
    else:
        # If the row doesn't match, just append the original row
        return row
    return labeled_row

def normalizeTableBoundary(row):
    return cleanPage(' '.join(row))

def create_removal_pattern(phrase1, phrase2):
    # Escape special regex characters in phrases
    escaped_phrase1 = re.escape(phrase1)
    escaped_phrase2 = re.escape(phrase2)
    
    # Create a regex pattern to match any text between the two phrases
    pattern = rf"{escaped_phrase1}.*?{escaped_phrase2}"
    
    return pattern

def tableToText(tab, hasHeaders = True):
    tabText =''
    for r in range(len(tab)):
        if r == 0 and hasHeaders: continue
        for c in range(len(tab[r])):
            tabText += cleanPage(tab[r][c]) + '\n'
    return tabText

def pageToTextProcessing(page):
    text = ''
    tabs = page.find_tables()
    text = cleanPage(page.get_text("text"))
    processedTabs = []
    if tabs.tables:
        for t in tabs:
            processedTab = {
                'content':[],
                'boundaries':[],
                'text':[]
            }
            extractedTable = t.extract()
            textTable = format_table_into_text(extractedTable)
            for r in range(len(extractedTable)):
                processedRow = mergeCells(extractedTable[r])
                if r == 0 or r == len(extractedTable)-1:
                    processedTab['boundaries'].append(normalizeTableBoundary(processedRow))
                # if r != 0:
                    # processedRow = label_row_with_headers(processedRow, processedTab['content'][0])
                # processedTab['content'].append(processedRow)
            processedTab['text'] = textTable # tableToText(processedTab['content'], isTableHeader(processedTab['content'][0]))
            processedTabs.append(processedTab)
            # lastTableHeaders = processedTab['content'][0]

    for tp in range(len(processedTabs)):
        pattern = create_removal_pattern(processedTabs[tp]['boundaries'][0], processedTabs[tp]['boundaries'][1])
        text = re.sub(pattern, processedTabs[tp]['text'], text, flags=re.DOTALL)

    return text

def cleanPage(pageText):
    for p in cleaingPatterns:
        pageText = re.sub(p, "", pageText)

    pageText = pageText.replace('TV052205', ' ')
    pageText = pageText.replace('QSR022206', ' ')
    pageText = pageText.replace('\n', ' ')
    pageText = re.sub(r'\s+', ' ', pageText).strip() 

    pageText = remove_unwanted_spaces(pageText)
    

    return pageText

def remove_unwanted_spaces(text):
    words = text.split()
    new_words = []

    for word in words:
        # If a word appears to be spaced out (i.e., 'M a x i m u m'), remove the spaces
        if all(len(char) == 1 for char in word):
            new_word = ''.join(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    
    return ' '.join(new_words)

def filterSections(toc):
    filtered = [string for string in toc if re.match(tocPatterns, string[1])]
    return filtered


def format_table_into_text(table, min_values_per_row=2):
    tableText = ""
    headers = table[0]
    non_null_headers = sum(1 for value in headers if value)

    index = 1
    hasHeaders = True
    if non_null_headers < min_values_per_row:
        index = 0
        hasHeaders = False

    for row in table[index:]:
        non_null_values = sum(1 for value in row if value)
        
        if non_null_values >= min_values_per_row:
            if hasHeaders:
                for i, value in enumerate(row):
                    title = headers[i] if i < len(headers) else f""
                    if title:
                        tableText += f"{title}: {value}\n"
                    else:
                        tableText += f"{value}\n"
            else:
                for value in  row: 
                    tableText += f"{value}\n"
            tableText += "\n"
        else:
            for value in row: 
                    tableText += f"{value}\n"
    
    return tableText.strip()



# pdf = fitz.open(project_path + "/PolicyWording-hlas.pdf")
def getPdf_data(path):
    import fitz

    fullText = ''
    fullTextTokens = ''
    pdf = fitz.open(path)

    toc = filterSections(pdf.get_toc())



    stop_words = set(stopwords.words('english'))
    lst=[]
    for page_num in range(pdf.page_count):
        page_text = pageToTextProcessing(pdf.load_page(page_num))
        tokens = word_tokenize(page_text)
        # Filter out the stopwords from your tokens
        filtered_tokens = [w for w in tokens if not w.lower() in stop_words]
        # Remove punctuation and make everything lowercase
        tokens = [word.lower() for word in filtered_tokens if word.isalpha()]
        fullTextTokens += ' '.join(tokens)
        fullText += page_text
        lst.append(page_text)

    pdf.close()
    return lst



            

# fullText = ''
# fullTextTokens = ''

# toc = filterSections(pdf.get_toc())

# for t in toc:
#     print(t[1])


# stop_words = set(stopwords.words('english'))

# for page_num in range(pdf.page_count):
#     # if page_num == 5:
#         # print('test')
#     page_text = pageToTextProcessing(pdf.load_page(page_num))
#     tokens = word_tokenize(page_text)
#     # Filter out the stopwords from your tokens
#     filtered_tokens = [w for w in tokens if not w.lower() in stop_words]
#     # Remove punctuation and make everything lowercase
#     tokens = [word.lower() for word in filtered_tokens if word.isalpha()]
#     fullTextTokens += ' '.join(tokens)
#     fullText += ' '.join(page_text)

# pdf.close()

# for t in toc:
#     position = fullText.find(t[1])
#     t[2] = position
#     print(t[1] + " -> " + str(position))

# with open(project_path + '/output-msig-1.txt', 'w') as file:
#    file.write(fullText)