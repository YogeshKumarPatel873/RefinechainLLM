template_refine_map_json= """
            Role: Underwriter Agent Specializing in Insurance Policy Wording
            ------------
            DOCUMENT:The information is contained within the following text:
            {{context}}
            
            ------------
            You have to examination above content very narrowly and map all the values and details according to json object.
            **Output**:
            json output must be in a tree structure as described here :
              -JSON
                  -Plan (Basic, Premium, Luxe etc)
                    -JSON
                      -Bénéfices (Hospitalization, repatriation etc)
                        -JSON
                          -Information on the benefice : Limits, payablePerUnit, quantityPerUnit and other.
            
            Provide JSON Outputs for each benefice policy based on section describe by the given content in following format: 

                
    -----------------------
    here's a detailed breakdown of each key within the insurance policy wording context:

- **"name": "name of policy"**
  - Description: Represents the identifier or title given to the specific insurance policy or benefit. It combines a code (insurer-based) along with a descriptive name for the policy.

- **"limit"**
  - Description: Denotes the maximum benefit limit associated with the policy. This limit signifies the highest monetary value or coverage that the policy provides for the specified benefit.

- **"groupCode":**
  - Description: This field refers to a code applicable for grouped benefits within the policy structure. It serves as a root code, often linking or categorizing related benefits under one group.

- **"benefit":**
  - **"type": "type given in context"**
    - Description: Describes the specific type of benefit being offered or covered under the policy. It signifies the nature or category of the benefit within the insurance context.
  - **"code":**
    - Description: An internal identifier or code associated with the benefit type. It helps in mapping and properly categorizing the benefit according to supported lists or predefined categories.

- **"groupBenefit":**
  - Description: Pertains to benefits that apply within grouped structures or as child elements within a specific group. It signifies the relationship of the benefit with other related or nested benefits.

- **"payable":**
  - Description: Indicates a fixed payable amount associated with the benefit, applicable under certain conditions specified within the policy.

- **"payablePerUnit":**
  - Description: Specifies a fixed payable amount allocated per each quantityPerUnit affected. It represents a fixed amount provided for each unit or block of affected time (such as hours or days) under the policy.

- **"quantityPerUnit":**
  - Description: Represents the block or unit of time (for instance, hours or days) that affects the payable amount. It outlines the duration or units impacting the benefit payment.

- **"itemLimit":**
  - Description: Relevant for benefits that involve expenses, indicating the limit for each bill or item that should be included. It represents the maximum value or coverage for individual items or bills included under the benefit.

- **"expressionLimit":**
  - Description: Represents a custom expression used to dynamically set the limit based on specific claims conditions. This field provides a way to dynamically define the limit under certain conditions instead of a fixed value.

- **"expressionItemLimit":**
  - Description: Similar to expressionLimit, this field represents a custom expression used to set the limit per each item claimed, if applicable. It serves as a dynamic way to define item-specific limits based on conditions.

- **"messageLimitExpression":**
  - Description: Indicates a custom message intended to be displayed when the limit associated with the benefit is being reached. It serves as a notification or alert regarding the limit status.

- **"wordingSections":**
  - Description: Contains a list of sections where the benefit is referenced within the insurance policy wording. This is often used for various purposes like email templates, referring to the sections where this particular benefit is mentioned or utilized.
    - **"code": "Found section"**
      - Description: Denotes the code or identifier of a specific section within the policy wording where this benefit is referenced or utilized. This helps in tracking and understanding where the benefit's details are employed or referenced within the insurance documentation.

    you have to give all data in json object and if value of any object is not present then replace it with 'Null' instead of writing 'Additional JSON objects for other benefits can be added here following the same structure'.
    
            """





template_refine_concate= """
You currently have an existing analysis up to a specific point:
------------
PREVIOUS CONTEXT:
{{prev_response}}
------------

Now, you have to merge it with next context.


------------
ADDITIONAL CONTEXT:
{{context}}
------------

Return the whole structure of the original analysis without any kind of instuction or specification.
do not add 'Additional JSON objects for other benefits can be added here following the same structure.' at the end.
"""
