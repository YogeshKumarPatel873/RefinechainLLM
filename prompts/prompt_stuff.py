########################################
########### STUFF TEMPLATES ############
########################################

template_stuff_comparaison = """
You are a policy wording analyser trying to help customer.\n
Consider the following context composed of two extractions from policy wording, each emphasizing the flexibility of a policy toward clients.\n
Your task is to compare these two extractions and provide insights into the implications of their flexibility for clients.\n
Focus on real arguments like :
- coverage_areas
- covered_events
- coverage_options
- maximum_trip_duration_days
- cancellation_policy
- exclusion_clause
- countries_covered
- deductible_amount
- medical_claim_condition
- benefits_covered
- Others
- And all other relevant analysis

Analyze all the axes and numbers that makes sens for the customer.
------------\n
POLICIES WORDING:\n
{{content}}\n
------------\n\n


Compare the flexibilities highlighted in the context for each policy wording.\n
Ultimately, identify the policy that exhibits the highest level of flexibility towards the client ans justify your choice with numbers.\n
Please provide a single, definitive response with a clear jsutification.\n\n


**** OUTPUT *****
Think step by step analyze numbers and compare them.\n
Conduct an in-depth examination of the contractual flexibility

Ultimately, pinpoint the policy that demonstrates the better flexibility and justify your saying with number and arguments.\n 
Be detailled et precise with your justification. \n
The output must  advise a customer which policy wording :
- Provides more value\n
- Is less restrictive or strict on requirements to claim\n
- Has less exclusions\n

Finally, finish by saying : "As a client, i would go for the policy X. And justify yourself.
"""

template_stuff_gap_policy = """
You are a policy wording analyzer agent.\n
Consider the following context to provide a analyze of differences between the perfect policy and the understudy policy (non perfect) :\n\n
------------\n
PERFEXT STRUCTURE AND UNDERSTUDY POLICIES WORDING STRUCTURE:\n
{{content}}\n
------------\n\n

**** INSTRUCTION *****
Your task is to compare the given understudy structure to the perfect structure, which serves as the reference. 
Focus on the meaning of each section to identify the missing parts in the undertudy structure (non perfect).
The objectives is to higlight the lacks or missing elements in the understudy structure (non perfect).

**** OUTPUT *****
Return your result as a friendly debrief with the list of the gaps or missing part in the understudy structure. 
"""

template_stuff_ambiguities = """
You are a tender analysis agent.\n
Consider the information as follow :
First part : an exaggerated extraction of ambiguities from the document.
Second part : The understudy tender :\n\n
------------\n
EXAGGERATED AMBIGUITIES\n
------------\n
{{content}}\n
------------\n\n
------------\n
UNDERSTUDY TENDER:\n
 ------------\n\n

**** INSTRUCTION *****
Evaluate extracted ambiguities and discard irrelevant ones based on the global information provided in the understudy tender.\n
Incorporate new ambiguities if identified.\n

**** OUTPUT *****
Return your result as a JSON\n
"""

template_stuff_ambiguities_transform = """
Analyze and combine following JSON data containing ambiguities data from a document,
remove any duplicated, similiar, and exagerated ambiguities from the list.
After the list is combined, transform the JSON to follow the structure of JSON schema given below.
Your final answer must be only JSON data in JSON format without narration or any additional formatting or code block syntax,
which can be validated using the given JSON Schema.

JSON data:
{{content}}\n

JSON Schema:
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "documentInfo": {
      "type": "object",
      "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "date": {"type": "string"},
        "filename": {"type": "string"}
      },
      "required": ["title", "author", "date", "source"]
    },
    "ambiguities": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "section": {"type": "string"},
          "statement": {"type": "string"},
          "explanation": {"type": "string"}
        },
        "required": ["section", "statement", "explanation"]
      }
    }    
  },
  "required": ["documentInfo", "ambiguities"]
}

"""

template_stuff_requirements = """
As a tender agent for Ancileo, your task is to analyze a lengthy list of requirements and filter out only those that are directly relevant to technical specifications or closely associated with Ancileo's services. 
The refined list will be crucial for preparing a targeted and precise response to the tender.

Follow these steps to complete the task:

Carefully review each requirement in the provided list.
Identify and retain only those requirements that pertain to technical specifications or are directly linked to Ancileo's services. Remove any irrelevants, duplicates, or non-essential entries.
Compile the final list of refined requirements, ensuring clarity and precision in your selections.
Present the processed list, emphasizing the technical and Ancileo-specific aspects, as this will form the basis of Ancileo's response to the tender.
Your goal is to streamline the requirements, focusing on technical aspects and Ancileo's service-related conditions, providing a concise and effective foundation for the tender response.
------------\n
LIST OF REQUIREMENTS:\n
{{content}}\n
------------\n\n

Return your result as a JSON format :

{
  "requirements": [
    {
      "id": 1,
      "description": "Text of the first requirement.",
      "level": ex : Mandatory
    },
    {
      "id": 2,
      "description": "Text of the second requirement.",
      "mandatory": ex : Not mandatory
    },
    {
      "id": 3,
      "description": "Text of the third requirement.",
      "mandatory": ex : Nice to have
    },
    // ... (continue with other requirements)
  ]
}
"""


template_stuff_summary = """
Analyze following JSON data containing summaries data from a document,
Transform the JSON to follow the structure of JSON schema given below.
Your final answer must be only JSON data in JSON format without narration or any additional formatting or code block syntax,
which can be validated using the given JSON Schema.

JSON data:
{{content}}\n

JSON Schema:
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "documentInfo": {
      "type": "object",
      "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "date": {"type": "string"},
        "filename": {"type": "string"}
      },
      "required": ["title", "author", "date", "filename"]
    },
    "summary": {
      "type": "object",
      "properties": {
        "topics": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": {"type": "string"},
              "description": {"type": "string"},
              "content": {"type": "string"}
            },
            "required": ["title", "description", "content"]
          }
        }   
      },
      "required": ["sections"]
    }
  },
  "required": ["documentInfo", "summary"]
}

Topic list:
{
  "Travel Insurance Products": "Information related with all product related with travel insurance, mentioning requirements like product portfolio, benefits, coverage, pricing, or distribution channels.",
  "Other Travel Services": "Information related with any additional travel-related services",
  "Financial Compensation": "Information related with requirements for financial compensation.",
  "Technical Integration": "Information related with requirements for technical integration.",
  "IT Security": "Informations related with IT security",
  "Post-sales Service and Claims": "Information related with requirements for post-sales service and claims processing.",
  "Medical Assistance Service": "Information related with requirements for medical assistance services.",
  "Legal and Compliance": "Information related with legal and compliance requirements, including geographical presence and tender host setup.",
  "Project Planning and Delivery": "Information related with requirements for project planning and delivery timelines.",
  "Innovation": "Information related with requirements related to innovation.",
}

"""

template_stuff_gap_analysis = """
Envision yourself as an underwriter agent specializing in insurance policy wording. 
You received an a section-wise analysis of gaps or missing part of a insurance policy wording :
------------
ANALYSIS:
{{content}}
------------

Analyze step by step each of the sections to return a JSON as describe below.
Summarise the feedbacks to clearly highlight missing part if there are be sure that each section has a statut. 
If the status i not here, write it according to your comprehension of feedbacks.
Return the result as a JSON :

{
  "feedbackTopics": [
    {
      "topic": "XXXX",
      "summary": "XXXXX",
      "status": "Yes/No/Unclear",
      "description": "XXXXX"
    },
    ]
}

"""