import json
from functools import partial
from operator import itemgetter
from langchain.callbacks.manager import trace_as_chain_group
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.prompts import format_document
from functools import partial
from langchain.schema import Document
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from PIL import Image
from io import BytesIO
from langchain.chains.combine_documents import split_list_of_docs
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.prompts import format_document
from langchain.cache import InMemoryCache
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_llm_cache

from prompts.prompt_missing_2 import (
                    template_refine_map_json,
                    template_refine_concate,
                    )

from main import getPdf_data            





class Chain :
    _chat: ChatOpenAI = None

    def __init__(self):
        """Constructor"""
        set_llm_cache(InMemoryCache())

    @property
    def chat(self) -> ChatOpenAI:
        """ChatOpenAI lazy read-only property."""
        if self._chat is None:
            self._chat = ChatOpenAI(
                api_key='',
                cache=True,
                max_retries=10,
                model="gpt-4-1106-preview",
                temperature=0,
            )
        return self._chat

    @property
    def chat4(self) -> ChatOpenAI:
        """ChatOpenAI lazy read-only property."""
        if self._chat is None:
            self._chat = ChatOpenAI(
                api_key='',
                cache=True,
                max_retries=10,
                model="gpt-4-1106-preview",
                temperature=0,
            )
        return self._chat


class Refine(Chain):
    def __init__(self, refine_prompt_summarize, refine_prompt_refine, file):
        """Constructor"""
        self.refine_prompt_summarize = refine_prompt_summarize
        self.refine_prompt_refine = refine_prompt_refine
        self.file = file
        # self.structure_json = structure_json
        set_llm_cache(InMemoryCache())


    def refine(self):
        # Chain for generating initial summary based on the first document

        first_prompt = PromptTemplate.from_template(template = self.refine_prompt_summarize, 
                                                    template_format = 'jinja2')
        document_prompt = PromptTemplate.from_template("{page_content}")
        partial_format_doc = partial(format_document, prompt=document_prompt)
        summary_chain = {"context": partial_format_doc} | first_prompt | self.chat | StrOutputParser()

        # Chain for refining an existing summary based on
        # an additional document

        refine_prompt = PromptTemplate.from_template(template = self.refine_prompt_refine,
                                                      input_variable=['prev_response', 'context'], 
                                                      template_format = 'jinja2')
        refine_chain = (
            {
                "prev_response": itemgetter("prev_response"),
                "context": lambda x: partial_format_doc(x["doc"]),
            }
            | refine_prompt
            | self.chat4
            | StrOutputParser()
        )

        # The final refine loop, which generates an initial summary
        # then iteratively refines it based on each of the rest of the documents


        def refine_loop(docs):
            with trace_as_chain_group("refine loop", inputs={"input": docs}) as manager:
                print("====FIRST====")
                lst=[]
                summary = summary_chain.invoke(
                    docs[0], config={"callbacks": manager, "run_name": "initial summary"}
                )
                for i, doc in enumerate(docs[1:]):
                    # if (i == 5): break
                    print(f"===={i}/{len(docs)}====")
                    summary = refine_chain.invoke(
                        {"prev_response": summary, "doc": doc},
                        config={"callbacks": manager, "run_name": f"refine {i}"},
                    )
                    lst.append(summary)
                manager.on_chain_end({"output": summary})
            return summary

        def format_docs(docs):
            return "\n\n".join(partial_format_doc(doc) for doc in docs)

        def get_num_tokens(docs):
            return self.chat.get_num_tokens(format_docs(docs))

        token_max = 16000
        split_docs = split_list_of_docs(self.file, get_num_tokens, token_max)
        split_docs = split_docs[0]
        result = refine_loop(split_docs)
        return result

    def refine_alternative(self):
        # Chain for generating initial summary based on the first document

        first_prompt = PromptTemplate.from_template(template = self.refine_prompt_summarize,
                                                    template_format = 'jinja2')
        document_prompt = PromptTemplate.from_template("{page_content}")
        partial_format_doc = partial(format_document, prompt=document_prompt)
        summary_chain = {"context": partial_format_doc} | first_prompt | self.chat | StrOutputParser()

        # Chain for refining an existing summary based on
        # an additional document

        #Overriding chat
        _chat = ChatOpenAI(
            api_key='',
            cache=True,
            max_retries=10,
            model="gpt-4-1106-preview",
            temperature=0,
        )


        refine_prompt = PromptTemplate.from_template(template = self.refine_prompt_refine, 
                                                     input_variable=['prev_response', 'context'], 
                                                     template_format = 'jinja2')
        refine_chain = (
            {
                "prev_response": itemgetter("prev_response"),
                "context": lambda x: partial_format_doc(x["doc"]),
            }
            | refine_prompt
            | _chat
            | StrOutputParser()
        )

        # The final refine loop, which generates an initial summary
        # then iteratively refines it based on each of the rest of the documents


        def refine_loop(docs):
            outputs = ""
            with trace_as_chain_group("refine loop", inputs={"input": docs}) as manager:
                print("====INITIAL SUMMARY====")
                initial_summary = summary_chain.invoke(
                    docs[0], config={"callbacks": manager, "run_name": "initial summary"}
                )
                outputs += initial_summary
                print(initial_summary)

                for i, doc in enumerate(docs[1:], start=1):
                    print(f"====REFINING DOC {i} / {len(docs)}====")
                    refined_summary = refine_chain.invoke(
                        {"prev_response": outputs, "doc": doc},
                        config={"callbacks": manager, "run_name": f"refine {i}"},
                    )
                    outputs += refined_summary

                print("========PRINTING OUTPUTS========")
                

                manager.on_chain_end({"output": outputs})

            return json.dumps(outputs)


        def format_docs(docs):
            return "\n\n".join(partial_format_doc(doc) for doc in docs)

        def get_num_tokens(docs):
            return self.chat.get_num_tokens(format_docs(docs))

        token_max = 16000
        split_docs = split_list_of_docs(self.file, get_num_tokens, token_max)
        split_docs = split_docs[0]
        result = refine_loop(split_docs)
        return result

class Stuff(Chain):
    def __init__(self, template_stuff, file):
        """Constructor"""
        self.template_stuff = template_stuff
        self.file = file
        set_llm_cache(InMemoryCache())

    def stuff(self):

        doc_prompt = PromptTemplate.from_template("{page_content}")

        chain = (
            {
                "content": lambda docs: "\n\n".join(
                    format_document(doc, doc_prompt) for doc in docs
                )
            }
            | PromptTemplate.from_template(template = self.template_stuff, input_variable = ['content'],
                                            template_format = 'jinja2')
            | self.chat
            | StrOutputParser()
        )

        result = chain.invoke(self.file)
        return result

    def stuff_alternative(self):

        doc_prompt = PromptTemplate.from_template("{page_content}")

        _chat = ChatOpenAI(
            api_key='',
            cache=True,
            max_retries=10,
            model="gpt-4-1106-preview",
            temperature=0,
        )

        chain = (
            {
                "content": lambda docs: "\n\n".join(
                    format_document(doc, doc_prompt) for doc in docs
                )
            }
            | PromptTemplate.from_template(template = self.template_stuff, input_variable = ['content'],
                                            template_format = 'jinja2')
            | _chat
            | StrOutputParser()
        )

        result = chain.invoke(self.file)
        return result

    
def _merge_documents_Urlcontent(docs,content ,n):

    # Calculate the number of documents per group
    num_docs_per_group = len(docs) // n

    # Split the documents into three groups
    groups = [docs[i:i + num_docs_per_group] for i in range(0, len(docs), num_docs_per_group)]

    # Adjust the last group to include any remaining documents
    if len(groups) > n:
        groups[n-1].extend(groups.pop(n))
    elif len(groups) < n:  # In case there are fewer than 3 documents
        while len(groups) < n:
            groups.append([])

    # Function to concatenate document contents
    def concatenate_docs(doc_group):
        
        return "".join(doc for doc in doc_group)

    # Create new Document instances for each group
    merged_docs = [
        Document(
            page_content=concatenate_docs(group),
            metadata={
                'source': 'Merged from multiple documents',
                'original_docs': [doc for doc in group]
            }
        ) if index < (n-1) else Document(
            
            page_content=concatenate_docs(group) + str(content),
            metadata={
                'source': 'Merged from multiple documents',
                'original_docs': [doc for doc in group]
            }
        ) for index, group in enumerate(groups)
        ]
    
    return merged_docs

def _merge_documents(docs, n):

    # Calculate the number of documents per group
    num_docs_per_group = len(docs) // n

    # Split the documents into three groups
    groups = [docs[i:i + num_docs_per_group] for i in range(0, len(docs), num_docs_per_group)]

    # Adjust the last group to include any remaining documents
    if len(groups) > 3:
        groups[2].extend(groups.pop(3))
    elif len(groups) < 3:  # In case there are fewer than 3 documents
        while len(groups) < 3:
            groups.append([])

    # Function to concatenate document contents
    def concatenate_docs(doc_group):
        return "\n".join(doc.page_content for doc in doc_group)

    # Create new Document instances for each group
    merged_docs = [
        Document(
            page_content=concatenate_docs(group),
            metadata={
                'source': 'Merged from multiple documents',
                'original_docs': [doc.metadata.get('source') for doc in group]
            }
        ) for group in groups
        ]
    return merged_docs

def _fetch_excel_content(path):
    import pandas as pd
    data=pd.read_excel(path)
    clean_data = data.dropna(how='all')
    clean_data = data.dropna(axis=1,how='all')
    return clean_data

def scrape_webpage(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text
        texts = [p.get_text() for p in soup.find_all('p')]
        # Extract images
        images = [img['src'] for img in soup.find_all('img')]
        # Find all code blocks
        code_blocks = soup.find_all('pre', class_='highlight')
        # Extract tables
        tables = []
        for table in soup.find_all('table'):
            rows = table.find_all('tr')
            table_data = []
            for row in rows:
                cells = row.find_all(['td', 'th'])
                cell_data = [cell.get_text().strip() for cell in cells]
                table_data.append(cell_data)
            tables.append(table_data)
        # Extract and clean code from each block
        codes = []
        for block in code_blocks:
            # Get the text within each <code> tag
            code = block.find('code')
            if code:
                # Remove HTML tags and leading/trailing whitespace
                raw_code = code.get_text().strip()
                codes.append(raw_code)
        # Save and display images
        for i, img_url in enumerate(images):
            try:
                absolute_img_url = urljoin(url, img_url)
                img_response = requests.get(absolute_img_url)
                Image.open(BytesIO(img_response.content))
            except Exception as e:
                pass
        content = {
            'texts': texts,
            'images': images,
            'tables': tables,
            'codes': codes
        }
        return content
    except Exception as e:
        return str(e)



def extract_ambiguities_tender_refine(pdf_path,url=None,excel_path=None): 
        pdf_docs=getPdf_data(pdf_path) 
        if url is not None and excel_path is not None:
            content=scrape_webpage(url)
            content += _fetch_excel_content(excel_path)
            docs = _merge_documents_Urlcontent(pdf_docs,content,7)
        elif excel_path is not None:
            content=_fetch_excel_content(excel_path)
            docs = _merge_documents_Urlcontent(pdf_docs,content,7)
        elif url is not None:
            content=scrape_webpage(url)
            docs = _merge_documents_Urlcontent(pdf_docs,content,7)
        else:
            docs=_merge_documents(pdf_docs,7)


        refine = Refine(
                    template_refine_map_json, 
                    template_refine_concate,
                    docs)
        return refine.refine()
        # return {'list of clarification' : refine.refine()} 


def missing_objects():
    pdf_path="PolicyWording.pdf"
    url='https://www.msig.com.sg/personal-insurance/traveleasy'
    excel_path='Attachment.xlsx'

    output=extract_ambiguities_tender_refine(pdf_path,url)
    print(output)
    return None


missing_objects()
