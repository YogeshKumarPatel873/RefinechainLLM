
############################################
########### MAPREDUCE TEMPLATES ############
############################################

###### Ambiguities ######

map_reduce_template_individual_ambiguities = """

*** INSTRUCTIONS ***

Role of Tender Analysis Agent:

Objective: Meticulously review the tender document section you received, with a special emphasis on key aspects such as deliverables, timelines, technology requirements, business data & information, and company results.
Focus: Direct attention primarily to the data and information specified in the 'Questions' and 'Example of Data' columns of the guidance table. Overlook lesser details like formatting. Your task is to verify whether the data detailed in the guidance table is present in the corresponding sub-section to the one understudy.
Goal: Identify and highlight any sections of the tender that lack information as specified in the guidance table for the understudy sub-section. For each sub-section under analysis, ensure it contains the information described in the table. If there is a discrepancy or missing information, it should be clearly noted.

Analysis Guidelines:

Section Reference: Specify the exact part of the document needing more details.
Statement Clarity: Identify statements or aspects that are unclear, ambiguous, or incomplete.
Question Raised: Pose questions relating to the missing information, as outlined in the guidance table.
Explanation: Provide a rationale, based on the guidance table, for the necessity of these additional details.

Utilization of the Guidance Table:

Purpose: Employ the table as a comprehensive checklist to confirm the presence of all essential information at he sub-section level.
Contents: The table includes Tender Segment, Section, Sub-section, relevant questions, their significance, and typical partner responses.
Task: Assess the tender information against the guidance table, focusing on the specific sub-sections under review. Compare the tender's details with the necessary information for corresponding sub-sections as listed in the guidance table.
Action on Discrepancies: If the tender lacks information outlined in the guidance table (typical partner responses), raise the pertinent question along with its justification as per the table's guidance.

*** GUIDANCE TABLE ***

        Tender Segment              Tender Section   Tender Sub-section                                                                                                                                                                                     Questions                                                                                                        Why we need this information                                                                                                                                    Example of data
                   ALL            Tenderer Profile        Customer Data                                                                                                                            Demographics: What are the age demographics of your customer base? Understanding the age demographics helps in tailoring insurance products to fit the risk profile and needs of different age groups.                                   Our customer base primarily consists of individuals aged 25-40 (60%), followed by 40-60 (30%), and under 25 (10%).
                   ALL            Tenderer Profile        Customer Data                                                      Travelers Segment: Can you provide a breakdown of your customers based on whether they travel alone, as couples, families, or in groups?   This information allows the insurer to understand the common types of travel groups and customize insurance packages accordingly.                                                                                45% travel alone, 30% as couples, 15% as families, and 10% in groups.
                   ALL            Tenderer Profile        Customer Data                                                                                          Customer Feedback: what is the most common feedback about existing insurance products or experience?                                             Feedback highlights areas for improvement and what customers value in travel insurance.                                           Customers often request more comprehensive medical coverage and express concerns about the claims process.
                   ALL            Tenderer Profile          Travel Data                                                                                                                        Travel Patterns: What is the share of return trip bookings vs one way?                                      Helps in assessing the risk and pricing of insurance products based on the nature of the trip.                                                                                                         70% return trip bookings, 30% one-way trips.
                   ALL            Tenderer Profile          Travel Data                                                                                                                                                          Travel Segment: leisure vs business?                                    Understanding the purpose of travel can guide the development of specialized insurance products.                                                                                     60% of our bookings are for leisure and 40% for business travel.
                   OTA            Tenderer Profile          Travel Data                                                      Could you provide the breakdown and absolute volume in terms of travel booking between flights, hotel, flight+hotel, car rental, cruise                            This information aids in understanding where the primary risks lie and where to focus insurance coverage.                                                                     Flights (50%), Hotels (20%), Flight+Hotel (15%), Car Rental (10%), Cruises (5%).
Financial Institutions            Tenderer Profile    Distribution Data                                                                                        Could you please advise the number of credit cards issued that will be offering NAC Travel Insurtance?                                   To gauge the potential reach and usage of the insurance product through credit card partnerships.                                                                                 We have issued 200,000 credit cards that offer NAC Travel Insurance.
                   ALL            Tenderer Profile          Travel Data                                                                                                                                        Peak Seasons: Key travel seasons? Key booking seasons?                                Identifying peak seasons helps in predicting demand and adjusting coverage and premiums accordingly.                                                     Summer and winter are key travel seasons. Most bookings occur 1-2 months prior to these seasons.
                   ALL            Tenderer Profile          Travel Data                                                                                                         Booking Window: What is the average period between travel booking and departure date?                                                  This metric helps in understanding customer planning behavior and risk assessment.                                                                                   On average, customers book their travels 45 days before departure.
                   ALL            Tenderer Profile    Distribution Data Could you provide break down percentage and absolute volum: contribution for your core travel product of each major distribution channel: Digital Direct (your website), Digital Indirect (eg               Understanding the distribution channels' performance assists in optimizing marketing and insurance product placement.                                                                                  Digital Direct (40%), Digital Indirect (35%), Other Channels (25%).
                   ALL            Tenderer Profile    Distribution Data                                             Origin Market: what are the countries you intend to distribute travel insurance? What is their respective share in terms of online booking sales?             Knowing the target markets helps in customizing products to different regulatory environments and customer preferences.                                                                                                     USA (40%), UK (30%), Canada (15%), Others (15%).
                   ALL            Tenderer Profile    Distribution Data                                                                                                                              what is the average period between travel booking and departure?                                                 To assess how far in advance customers plan, influencing insurance purchase timing.                                                                                              On average, bookings are made 60 days before departure.
                   ALL    Travel Insurance Product      Tender feedback                                                               Current Offerings: what would you like to improve regarding the current Travel Insurance offering? What would you like to keep?                               Feedback on current offerings guides the development of new products that better meet customer needs.                                                                                     Improve on medical coverage; keep the hassle-free claim process.
                   ALL    Travel Insurance Product      Tender feedback                                                                                                       Current Offerings: what do you really like about your current Travel Insurance offering                                                    Highlights strengths in current offerings that should be maintained or enhanced.                                                                    We appreciate the comprehensive coverage for trip cancellations and lost baggage.
                   ALL    Travel Insurance Product      Tender feedback                                                                                                              Coverage Details: is there any specific insurance coverages you are looking for?                                                     Identifies specific customer needs and expectations from the insurance product.                                                                 Looking for high medical coverage, trip cancellation, and adventure sports coverage.
                   ALL    Travel Insurance Product      Personalisation                                                                              Personalisation: would you be open to insurance products merchandising depending on traveler and travel segment?                                                   Determines the partner’s willingness to implement customized insurance solutions.                                                         Yes, we are open to personalized insurance products tailored to different traveler segments.
                   ALL    Travel Insurance Product      Price benchmark                                                                                                                            Price Points: Target price points? Premium? Budget? In the market?            Understanding the price sensitivity and expectations of customers helps in pricing the insurance products competitively.                                                        We are targeting mid-range price points, catering to both budget and premium market segments.
                   ALL                   Marketing    Buyer retargeting                                                   Identification of Non-Buyers: How does the airline identify customers who have not purchased travel insurance during their initial booking?                                                To target customers who didn’t initially purchase insurance for potential upselling.                                      We track booking data to identify customers who did not select insurance and target them with follow-up offers.
                   ALL                   Marketing    Buyer retargeting                                                                         Retargeting Channels: What channels does the airline use for retargeting non-buyers (e.g., email, SMS, social media)?                                           Understanding the methods used to re-engage customers who didn’t buy insurance initially.                                                          We use retargeting ads on social media, follow-up emails, and SMS reminders for non-buyers.
                   ALL                   Marketing    Buyer retargeting                                                                                    Retargeting Strategies: What specific strategies or campaigns does the airline use to retarget non-buyers?                                      To learn about the approaches used to encourage non-buyers to reconsider purchasing insurance.                                                   We use targeted campaigns offering special discounts or additional coverage options to non-buyers.
                   ALL                   Marketing    Buyer retargeting                                                      Timing of Retargeting: When does the airline typically retarget non-buyers (e.g., immediately after booking, closer to the travel date)?                                                          To understand the timing of retargeting efforts for maximum effectiveness.                                                   We start retargeting three days after booking and intensify efforts as the travel date approaches.
                   ALL                   Marketing    Buyer retargeting                                                                                                 Personalization in Retargeting: How is personalization incorporated into retargeting efforts?                                     Determines the level of customization in retargeting campaigns to increase their effectiveness.                  Retargeting messages are personalized based on the destination, duration of travel, and previous insurance choices of the customer.
                   ALL                   Marketing    Buyer retargeting                                                              Incentives for Conversion: Are there any incentives or special offers used to encourage non-buyers to purchase travel insurance?                                                                          Identifies tactics used to convert non-buyers into buyers.                                                 We offer limited-time discounts and bundle deals as incentives for non-buyers to purchase insurance.
                   ALL                   Marketing    Buyer retargeting                                                              Impact on Customer Experience: How does the airline balance retargeting efforts with maintaining a positive customer experience?                                                  Ensures that retargeting efforts do not negatively impact the customer experience.              We limit the frequency of retargeting messages and ensure they are relevant and unobtrusive to maintain a positive customer experience.
                   ALL                   Marketing    Buyer retargeting                                                                                             Conversion Rate Goals: What are the airline's target conversion rates for retargeting non-buyers?                                                                     Sets specific targets for the success of retargeting campaigns.                                               Our target conversion rate for retargeting non-buyers is to convert 20% of them into insurance buyers.
                   ALL                   Marketing    Buyer retargeting                                                                                    A/B Testing in Campaigns: Does the airline use A/B testing to refine retargeting approaches and messaging?                                                     To evaluate and optimize the effectiveness of different retargeting strategies.                                      Yes, we regularly perform A/B testing on different messages and offers to see which works best for retargeting.
                   ALL                   Marketing    Buyer retargeting                                       Cross-Channel Marketing: How does the airline integrate marketing efforts across different channels (e.g., email, social media, in-flight advertising)?                                             Understanding how different marketing channels are coordinated for a cohesive strategy.                                  We synchronize our messaging across email, social media, and in-flight ads to create a unified marketing narrative.
                   ALL                   Marketing    Buyer retargeting                                                                                                           Upsell Opportunities: Opportunities for upselling as part of post-sales retargeting                                                                    Identifies potential for additional sales beyond just insurance.                                        In addition to insurance, we offer upsells like extra baggage or seat upgrades in our post-sales retargeting.
                   ALL Finance, Legal & Compliance              Finance                                                                                             Commission Structure: What is the commission structure for the airline on travel insurance sales?                                                 To determine the financial incentive for the airline in promoting travel insurance.                                                   We have a tiered commission structure, offering 15% on basic plans and up to 20% on premium plans.
                   ALL Finance, Legal & Compliance              Finance                                                                                       Profit Sharing Mechanism: If there's a profit-sharing arrangement, how is it structured and calculated?                                              To understand the revenue-sharing model and how profits are allocated between parties.                                          Profit sharing is based on annual sales volume, with a 5% share on up to $1M in sales, and 10% beyond that.
                   ALL Finance, Legal & Compliance              Finance                                                                                               Reporting on Sales and Earnings: How will sales and earnings from travel insurance be reported?                                                                  Ensures transparency and accuracy in reporting sales and earnings.                                                                        We provide monthly sales and earnings reports through a secure online portal.
                   ALL Finance, Legal & Compliance              Finance                                                                                                            Timing of Commission Payments: What is the expected timing of commission payments?                                                                                   To manage cash flow expectations for the airline.                                                                   Commission payments are made quarterly, within 30 days of the end of each quarter.
                   ALL Finance, Legal & Compliance              Finance                                                                                         Financial Reporting Standards: What standards are expected for commission and profit-share reporting?                                                                  To ensure compliance with financial reporting norms and standards.                                                     We adhere to International Financial Reporting Standards (IFRS) for all our financial reporting.
                   ALL Finance, Legal & Compliance              Finance                                                                                                       Reconciliation Process: Process for reconciling earned commissions with reported sales?                                                                    To maintain accuracy and transparency in financial transactions.                                             We have an automated reconciliation system that cross-checks sales data with commission payouts monthly.
                   ALL Finance, Legal & Compliance              Finance                                                                                                 Currency Exchange Management: Handling currency exchange rates in international transactions?                                                            Addresses the handling of currency risks and exchange rate fluctuations.                                            We use a fixed exchange rate policy, updated quarterly, and the airline bears the currency exchange risk.
                   ALL Finance, Legal & Compliance              Finance                                                                                                                           Payment Terms: Specific payment terms for commission disbursements?                                                                 Clarifies the conditions and timelines for payments to the airline.                                                          Payments are made within 45 days of invoice receipt, subject to verification of sales data.
                   ALL Finance, Legal & Compliance              Finance                                                                                                     Adjustments for Refunds and Cancellations: How are they reflected in commission payments?                                                                To account for changes in earnings due to refunds and cancellations.                                                  Commission adjustments for refunds and cancellations are processed in the subsequent payment cycle.
                   ALL Finance, Legal & Compliance                Legal                                                                                                    Current legal setup: Legal framework in every country intended for insurance distribution?                                                   Ensures the partnership adheres to legal requirements in different jurisdictions.                                                We have established legal entities in each country, compliant with local insurance distribution laws.
                   ALL Finance, Legal & Compliance           Compliance                                                                                                                                    Compliance Strategy: Approach for different jurisdictions?                                               To understand the strategy for managing compliance across various legal environments.                                             Our compliance strategy involves regular audits and adherence to local regulations, updated bi-annually.
                   ALL Finance, Legal & Compliance                  Tax                                                                                                Tax Implications: Awareness of tax obligations for premium collection and commission payments?                                                                    Addresses the need for tax compliance in financial transactions.                           We are aware of the tax implications and handle all tax obligations related to premium collections and commission payouts.
                   ALL                  Commercial           GWP volume                                                                                                                        Current Sales Volumes: Policy number sold and revenue data by country?                                           To assess the market reach and financial performance of the partner in different regions.            In the US, we sold 50,000 policies last year generating $5 million in revenue, and in the UK, 30,000 policies with $3 million in revenue.
                   ALL                  Commercial forecast assumptions                                                                                                                      Market Penetration: Current travel insurance conversion rate by country?                                    Helps in understanding the effectiveness of the partner's sales strategies in different markets.                                                                                               Our conversion rate is 10% in the US and 7% in the UK.
                   ALL                  Commercial forecast assumptions                                                                                                                                  Average Premiums: Current average premium amount by country?                                                  To gauge the pricing strategy and customer spending capacity in different markets.                                                                                             The average premium is $100 in the US and $85 in the UK.
                   ALL                  Commercial forecast assumptions                                                                                                                                                    Historical Growth: Historical growth rate?                                                           Indicates the partner's market growth and potential for future expansion.                                              We've experienced a yearly growth rate of 15% in policy sales and 20% in revenue over the past 3 years.
                   ALL                  Commercial forecast assumptions                                                                                               Additional Data: Average number of insured per policy? Average number of travelers per booking?                                                               Understanding the typical customer profile and their insurance needs.                                                        On average, each policy covers 2.5 individuals, and our typical booking includes 2 travelers.
                   ALL                  Commercial forecast assumptions                                                                                                                                                                                   Claims Data                                              Provides insights into the frequency and types of claims, crucial for risk assessment.                                                         Last year, we processed 5,000 claims, mostly for medical emergencies and trip cancellations.
                   ALL                  Commercial forecast assumptions                                                                                                                                                                  Refund and Cancellation Data                                              Helps in understanding the financial implications of policy cancellations and refunds.                We had a 5% cancellation rate on policies last year, with most refunds issued for trip cancellations due to unforeseen circumstances.
                   ALL          Project Management           Governance                                                                                                    Project governance Structure: Decision-making, Performance monitoring, Escalation process?                    To understand the framework for managing the project, ensuring efficient decision-making and problem resolution.                     We have a structured hierarchy for decisions, regular performance reviews, and a defined process for escalating critical issues.
                   ALL          Project Management           Governance                                                                                                                                    Communication Protocols: Preferred communication channels?                                                   Identifies the most effective ways to communicate, ensuring smooth collaboration.                                                        Our main channels are email for formal communication and instant messaging for quick updates.
                   ALL          Project Management           Governance                                                                                                                                  Performance Metrics: KPIs for measuring partnership success?                                           To define and agree on measurable outcomes for evaluating the success of the partnership.                                                         Key KPIs include customer acquisition rates, sales growth, and customer satisfaction scores.
                   ALL          Project Management           Governance                                                                                                                     Collaboration and Support: Level of support in marketing, sales, service?                                                             Clarifies the extent of collaborative efforts required from each party.                                            We expect joint marketing campaigns, sales training support, and a dedicated service hotline for queries.
                   ALL          Project Management           Governance                                                                                                     Risk Management in Project Governance: Strategies for risk identification and management.                                                        To understand how risks will be identified and mitigated within the project.                                                Risks are assessed bi-annually, with strategies like contingency planning and regular staff training.
                   ALL          Project Management           Governance                                                                                                                           Change Management: Handling changes in project scope or objectives.                                            Ensures there are protocols to manage changes effectively without derailing the project.                                                  Any scope changes are evaluated by a review committee and communicated clearly to all stakeholders.
                   ALL          Project Management           Governance                                                                                                                                  Long-Term Partnership Aspects: Review and renewal processes.                                                           Sets expectations for the duration and review process of the partnership.                                             We look for a multi-year partnership with annual reviews and potential for renewal based on performance.
                   ALL                  Technology      API integration                                                                                                                                          Direct Integration or 3rd Party for API Integration?                                                       Determines the technical approach and potential partners for API integration.            We're considering direct integration for more control and efficiency, but open to third-party solutions like Amadeus for their expertise.
                   ALL                  Technology      API integration                                                                                                                                 Technical Specifications: Availability of API specifications?                                                                    To ensure compatibility and readiness for technical integration.                                                               Our API specifications are fully documented and conform to current industry standards.
                   ALL                  Technology      API integration                                                                                                                                               Data Flow: Availability of a data flow diagram?                                                          Helps understand how data will be managed and transferred between systems.                                                   We have a comprehensive data flow diagram that outlines the integration and data handling process.
                   ALL                  Technology      API integration                                                                                                                                  User Experience: Steps of booking flow for travel insurance?                                                   Identifies how travel insurance is presented and sold during the booking process.                                              Insurance options are offered post-flight selection with detailed information and easy opt-in features.
                   ALL                  Technology      API integration                                                                                                                                               Data Analytics: Integration for tracking sales.                                                                  To monitor sales performance and gather insights for optimization.                                                 Our system supports integration with analytics tools to track sales performance and customer trends.
                   ALL                  Technology      API integration                                                                                                                                           Monitoring and Analytics: Integration capabilities?                                                                Evaluates the ability to monitor and analyze data within the system.                                                  We have integrated monitoring tools that provide real-time data on sales and customer interactions.
                   ALL                  Technology      API integration                                                                                                                                Authentication/Security: Methods for secure data transmission?                                                                              Ensures that data transmitted is secure and protected.                                                               We use encrypted data transmission and adhere to industry-standard security protocols.
                   ALL                  Technology      API integration                                                                                                                       Integration Requirements: Points of integration in the booking process?                                                Identifies specific areas where integration is necessary within the booking process.                                                    Integration points include flight selection, passenger information entry, and payment processing.
                   ALL                  Technology      API integration                                                                                                                   Functional Capabilities: Dynamic product information and real-time quoting?                                                       Determines the system's ability to provide up-to-date information and quotes.                                 Our system can dynamically update product information and provide real-time insurance quotes based on customer data.
                   ALL                  Technology      API integration                                                                                                                Testing and Support: Availability of a sandbox environment and support levels?                                               To ensure that there are adequate testing facilities and support for the integration.                                       We offer a sandbox environment for testing and have a dedicated technical support team for ongoing assistance.
                   ALL                  Technology   Premium collection                                                                                                                                 Payment System: Which payment processing system will be used?                                                                 Identifies the payment system to be used for handling transactions.                            We use a secure online payment gateway that supports multiple payment methods including credit cards and digital wallets.
                   ALL                  Technology   Premium collection                                                                                                                       Data Sharing for Transactions: Data exchange required for transactions?                                                            Clarifies the extent of data sharing needed for processing transactions.                                        Essential transaction data, such as payment amounts and confirmation numbers, will be shared between systems.
                   ALL                  Technology   Premium collection                                                                                                                         Security and Compliance: Security and compliance in payment handling?                                                           Ensures that payment handling meets security and regulatory requirements.                                                                        Our payment processes are PCI DSS compliant and we regularly undergo security
                   ALL                  Technology   Premium collection                                                                                                              Customer Experience: Impact on customer experience regarding premium collection?                                                            Assesses how the premium collection process affects customer experience.                               The premium collection process is streamlined and integrated into the booking flow for a seamless customer experience.
                   ALL                  Technology   Premium collection                                                                                                               Premium Collection Responsibility: Which party collects the insurance premiums?                                                       Determines which party is responsible for collecting premiums from customers.                                                   Insurance premiums are collected by us at the time of booking and remitted to the insurer monthly.
                   ALL                  Technology   Premium collection                                                                                                                        Refund and Cancellation Policy: Handling of refunds and cancellations?                                                       Understands the policy and procedures for managing refunds and cancellations.                                        Refunds for cancellations are processed within 5 business days, with conditions outlined in the policy terms.
                   ALL                   Marketing            Marketing                                                                                                     What marketing strategies are currently in place for promoting travel insurance products?                             To understand the existing marketing infrastructure and strategies used for travel insurance promotion.        We use targeted email campaigns, social media advertising, and partnerships with travel influencers to promote our travel insurance products.
                   ALL                   Marketing      Personalization                                                                                      What techniques or technologies does the airline use for personalizing travel insurance in-path content?                     To gauge how the airline tailors travel insurance offerings to individual customers during the booking process.                     We use data analytics to personalize offers based on the customer’s travel history, destination, and previous purchase behavior.
                   ALL                  Technology                 Data                                                                                         Which data will be available through the API integration (e.g., country of residence, date of birth)?                                Determines what customer information is accessible for targeted marketing and product customization.                          Our API integration provides access to data such as country of residence, age, travel destination, and frequency of travel.
                   ALL                   Marketing        Merchandizing                                                                                                                      What is the process in order to test different travel insurance layouts?                      Understands how the airline evaluates and optimizes the presentation of travel insurance options to customers.                                         We conduct A/B testing on our website to assess customer engagement with different insurance layout options.
                   ALL                   Marketing            Marketing                                                                                                                   What role does the airline expect the insurer to play in marketing efforts?                                  Clarifies expectations regarding the insurer's involvement in marketing travel insurance products.                                                We expect the insurer to contribute marketing content and share in the cost of promotional campaigns.
                   ALL                   Marketing            Marketing                                                                                         What metrics or KPIs are used to track the effectiveness of marketing campaigns for travel insurance?                                 To identify how the airline measures the success of its marketing initiatives for travel insurance.                                 We track metrics such as click-through rates, conversion rates, and ROI on our travel insurance marketing campaigns.
                   ALL                   Marketing            Marketing                                                                                                                          Is there a budget allocated for marketing travel insurance products?                                                           Assesses the financial resources dedicated to marketing travel insurance.                                              Yes, we have allocated a budget of $500,000 for the current fiscal year for marketing travel insurance.
                   ALL                   Marketing            Marketing                                                                               Is there potential for joint marketing activities between the insurer and the airline? What might these entail?                                     Explores opportunities for collaborative marketing efforts between the airline and the insurer.                                 There is potential for joint campaigns, including co-branded advertisements and bundled offers with flight bookings.
                   ALL                   Marketing            Marketing                                                                                         What kind of promotional campaigns has been most effective in the past for Travel Insurance products?                                       Identifies which types of marketing strategies have yielded the best results for the airline.                        Discount offers and bundled packages with additional travel perks have been most effective in driving travel insurance sales.
                   ALL                   Marketing      Loyalty program                                                                                 How might the airline's existing customer loyalty programs be leveraged to promote travel insurance products?                                               Explores ways to integrate travel insurance offerings with existing loyalty programs.                                        We can offer travel insurance as an added benefit or at a discounted rate for members of our loyalty program.
                   ALL                   Marketing        Merchandizing                                                                                                 Any feedback regarding your current travel insurance display? What would you like to improve?                                                      To gather insights on current display effectiveness and areas for improvement.            Customers have suggested clearer pricing information and simpler language. We aim to make the display more user-friendly and informative.
                   ALL                   Marketing        Merchandizing                                                                                                                How many products would you like to offer in the in-path distribution channel?                                               Determines the range and diversity of insurance products the airline wishes to offer.                       We plan to offer three types of insurance products – basic, comprehensive, and premium – to cater to different traveler needs.
                   ALL                   Marketing        Merchandizing                                                                                  Do you expect customization options for insurance based on traveler details? Can your technology support it?                                                           To find out if personalized insurance offerings are desired and feasible. Yes, we want to provide customized insurance offers based on travel destinations and duration. Our current technology supports these customizations.
                   ALL                  Technology            Languages                                                                                                                        Which languages need to be supported for the travel insurance section?                                                 Identifies the language diversity required to cater to the airline’s customer base.                                   Our primary customer base requires English, Spanish, and French language options for the travel insurance section.
                   ALL            Tenderer Profile                  NaN                                                                                                                                                                                           NaN                                                                                                                                 NaN                                                                                                                                                  NaN
                   ALL            Tenderer Profile                  NaN                                                                                                                                                                                           NaN                                                                                                                                 NaN                                                                                                                                                  NaN
                   ALL            Tenderer Profile                  NaN                                                                                                                                                                                           NaN                                                                                                                                 NaN                                                                                                                                                  NaN
                   ALL            Tenderer Profile                  NaN                                                                                                                                                                                           NaN                                                                                                                                 NaN                                                                                                                                                  NaN
                   ALL            Tenderer Profile                  NaN                                                                                                                                                                                           NaN                                                                                                                                 NaN                                                                                                                                                  NaN
                   NaN                         NaN                  NaN                                                                                                                                                                                           NaN                                                                                                                                 NaN                                                                                                                                                  NaN

*** DOCUMENT TO ANALYZE *** 
{{ context }}
                   
"""


map_reduce_template_collapse_ambiguities = """
*** INSTRUCTION ***
If necessary, collapse and reunite the list of points which need clarification:\n\n{{context}}.\n\n

**** OUTPUT *****
The final output should be a list in JSON format, detailing each point that needs clarification. For each point, include:
Section Reference: Specify the exact part of the document needing more details.
Statement Clarity: Identify statements or aspects that are unclear, ambiguous, or incomplete.
Question Raised: Pose questions relating to the missing information, as outlined in the guidance table.
Explanation: Provide a rationale, based on the guidance table, for the necessity of these additional details.

"""


map_reduce_template_reduce_ambiguities = """
*** INSTRUCTION ***
Combine these points which need clarification in order to have no duplicates or irrelevant ones:\n\n{{context}}.\n\n

**** OUTPUT *****
The final output should be a list in JSON format, detailing each point that needs clarification. For each point, include:
Section Reference: Specify the exact part of the document needing more details.
Statement Clarity: Identify statements or aspects that are unclear, ambiguous, or incomplete.
Question Raised: Pose questions relating to the missing information, as outlined in the guidance table.
Explanation: Provide a rationale, based on the guidance table, for the necessity of these additional details.


"""


####### Requirments #######

map_reduce_template_individual_requirements = """
You're an tenders analysis agent.


Your objective is to extract the technical requirements communicated by the client to Ancileo and described in the understudy tender.

*** INSTRUCTION ***
Extract the requirements that make sens to help Ancileo to answer this Tender. Be selective.
Extract only the RELEVANT requirements which are technological or legal. Do not over extract useless requirements
A requirements must carry a request, implicite or explicite.
Categorize each requirement into one of three quotation levels: 'Mandatory', 'Nice to Have', or 'Not Mandatory'.

Document to extract requirements :\n\n
------------\n
DOCUMENT:\n
{{context}}\n
------------\n
"""

map_reduce_template_collapse_requirements = """
*** INSTRUCTION ***
Remove overlapping, duplicate, irrelevant, valueless, or imprecise requirements.
These requirements encompass the services, technological aspects, and legal conditions that Ancileo must meet for the tender response:

Return the refined list of requirements.

------------

REQUIREMENTS TO FILTER AND REDUCE:
{{context}}

------------
"""


map_reduce_template_reduce_requirements = """
*** INSTRUCTION ***
Remove overlapping, duplicate, irrelevant, valueless, or imprecise requirements.
These requirements encompass the services, technological aspects, and legal conditions that Ancileo must meet for the tender response.
Return the final processed list of requirements.

------------

REQUIREMENTS BEFORE PROCESSING:
{{context}}

------------
"""


###### Flexibility #######


map_reduce_template_individual_flexibility_customer_bis = """
You're an extremely meticulous and critical policy wording AI agent\n
Your objective is to higllight, describe and quantify with numbers how a policy wording is flexible toward the customner.\n
Think step by step and retrieve clear numbers, lists and conditions. They are mandatory to statut over the flexibility.\n
All the information you need is in the tender.\n
To do so you have to extract the following information (and more if you other relevant element appear) and return the result as a JSON with keys as the properties extracted :\n\n

*** STRUCTURE ANALYZE AND OUTPUT ***\n\n
{
  "properties": {
    "title": {
      "type": "string",
      "description": "Title of the insurance policy"
    },
    "coverage_areas": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "Geographical areas covered by the policy - Extract all the areas"
      }
    },
    "covered_events": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "Events covered by the insurance policy - Extract all the events"
      }
    },
    "coverage_options": {
      "type": "string",
      "description": "Available coverage options",
      "enum": ["Basic", "Comprehensive", "Custom"]
    },
    "maximum_trip_duration_days": {
      "type": "integer",
      "description": "Maximum number of days per trip covered - Return clear numbers"
    },
    "cancellation_policy": {
      "type": "string",
      "description": "Policy details regarding trip cancellation",
      "enum": ["Refundable", "Non-refundable with exceptions", "Non-refundable"]
    },
    "exclusion_clause": {
      "type": "string",
      "description": "Exclusion clause specifying conditions not covered by the policy - Return the list of exclusion clause"
    },
    "countries_covered": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "List of countries covered by the policy - Return the list of countries"
      }
    },
    "deductible_amount": {
      "type": "integer",
      "description": "Deductible amount applicable to the policy"
    },
    "medical_claim_condition": {
      "type": "string",
      "description": "The condition to respect to make a medical claim. Return clear conditions"
    },
    "benefits_covered": {
      "type": "integer",
      "description": "The number of benefits covered"
    },
    "Other": {
      "type": "string",
      "description": "All information to highlight how a policy is flexible toward the customer: Number of days to submit a claim, condition for medical claims, number"
    }
  },
  "required": ["title", "coverage_areas", "covered_events", "coverage_options", "maximum_trip_duration_days", "cancellation_policy", "exclusion_clause", "benefits_covered", "medical_claim_condition", "countries_covered", "deductible_amount", "Other"]
}


The Understudy policy wording document is presented below:\n\n
------------\n
DOCUMENT:\n
{{context}}\n
------------\n

"""

map_reduce_template_collapse_flexibility_customer_bis = """
You're an extremely meticulous and critical policy wording AI agent\n
Your objective is to higllight, describe and quantify with numbers how a policy wording is flexible toward the customner.\n
Retrieve clear numbers, list and condition. They are mandtory to satut over the flexibility. \n

*** INSTRUCTION ***\n
Think step by step.\n
Collapse this content by focusing on the elements which highlight how a policy can be flexible towards the client.\n
Don't mix up data together. Keep the logical shape of the data organized by the JSON property :\n
------------\n
CONTENT:\n
{{context}}\n
------------\n
You must keep a JSON as an output :\n\n

"""

map_reduce_template_reduce_flexibility_customer_bis = """
You're an extremely meticulous and critical policy wording AI agent\n
Your objective is to higllight, describe and quantify with numbers how a policy wording is flexible toward the customner.\n
Retrieve clear numbers, list and condition. They are mandtory to satut over the flexibility

*** INSTRUCTION ***\n
Think step by step.\n
Combine this content by focusing on the elements which highlight how a policy can be flexible towards the client.\n
Don't mix up data together. Keep the logical shape of the data organized by the JSON property :\n
------------\n
CONTENT:\n
{{context}}\n
------------\n 
You must keep a JSON as an output :\n\n

"""



####### Summary #######


map_reduce_template_individual_summary = """
You're a tenders analysis agent.
Your job is to provided a section-wise summaries while preserving the semantic meaning and all the keys points : \n

------------\n
DOCUMENT TO RESUME:\n
{{context}}\n
------------\n\n

*** INSTRUCTION ***
Summarizes the document according to the sections as defined in the structure below :
If the context isn't useful for some of the sections, return an empty summary for this section.


*** STRUCTURE SUMMARY ***\n\n
Travel Insurance Products:
- Description: In this section, articulate the desired features and characteristics of the travel insurance products. Specify the range of coverage, benefits offered, pricing models, and preferred distribution channels. Clearly outline the unique selling points that should be present in the insurance products to meet the tender requirements.
- Summary: XXXXX

Additional Travel Services:
- Description: Elaborate on any supplementary services beyond traditional insurance products. This could encompass services such as travel assistance, concierge services, or any other offerings that enhance the overall travel experience. Detail the specific requirements and expectations for these services.
- Summary: XXXXX

Financial Compensation:
- Description: Define the processes and criteria for financial compensation. Clearly outline the circumstances under which compensation is applicable, the calculation methodology, and the steps involved in processing compensation claims. This section aims to provide a transparent and structured approach to handling financial matters.
- Summary: XXXXX

Technical Integration:
- Description: Specify the technical requirements for seamless integration with the insurance systems. This may include compatibility with existing platforms, data exchange protocols, and any APIs that need to be implemented. Clearly define the expectations for a smooth and efficient technical collaboration.
- Summary: XXXXX

IT Security:
- Description: Articulate the essential IT security measures that need to be in place. This could involve encryption standards, data protection protocols, and authentication processes. Emphasize the importance of safeguarding sensitive information and ensuring compliance with industry standards.
- Summary: XXXXX

Post-sales Service and Claims:
- Description: Provide a comprehensive overview of the post-sales service expectations and claims processing requirements. Detail the customer support structure, the steps involved in lodging and processing claims, and the expected turnaround times. This section focuses on ensuring a high level of customer satisfaction and efficient claims resolution.
- Summary: XXXXX

Medical Assistance Service:
- Description: Specify the requirements for medical assistance services. This may include access to emergency medical services, coordination with healthcare providers, and any other support services aimed at ensuring the well-being of travelers. Clearly outline the standards and capabilities expected from medical assistance providers.
- Summary: XXXXX

Legal and Compliance:
- Description: Detail the legal and compliance requirements essential for the insurance tender. This involves specifying any regulatory considerations, geographical restrictions, and the setup required for hosting the tender. Emphasize the importance of adherence to legal standards to ensure a compliant and ethical insurance operation.
- Summary: XXXXX

Project Planning and Delivery:
- Description: Provide a clear framework for project planning and delivery timelines. Outline the key milestones, deadlines, and expectations for the overall project implementation. This section aims to establish a realistic and achievable timeline for the successful execution of the insurance services outlined in the tender.
- Summary: XXXXX

Innovation:
- Description: Define the expectations regarding innovation in the insurance services. This may include advancements in technology, novel approaches to customer engagement, or any other innovative practices that align with the vision of the insurance tender. Encourage creative solutions and forward-thinking approaches to enhance the overall insurance offering.
- Summary: XXXXX


"""


map_reduce_template_collapse_summary = """
Collapse the provided context to generate section-wise summaries while preserving the semantic meaning and all the keys points.\n\n
------------\n
CONTEXT:\n
{{context}}\n
------------\n


*** INSTRUCTION ***
Collapse the document according to the sections as defined in the structure below :


*** STRUCTURE SUMMARY ***\n\n
Travel Insurance Products:
- Description: In this section, articulate the desired features and characteristics of the travel insurance products. Specify the range of coverage, benefits offered, pricing models, and preferred distribution channels. Clearly outline the unique selling points that should be present in the insurance products to meet the tender requirements.
- Summary: XXXXX

Additional Travel Services:
- Description: Elaborate on any supplementary services beyond traditional insurance products. This could encompass services such as travel assistance, concierge services, or any other offerings that enhance the overall travel experience. Detail the specific requirements and expectations for these services.
- Summary: XXXXX

Financial Compensation:
- Description: Define the processes and criteria for financial compensation. Clearly outline the circumstances under which compensation is applicable, the calculation methodology, and the steps involved in processing compensation claims. This section aims to provide a transparent and structured approach to handling financial matters.
- Summary: XXXXX

Technical Integration:
- Description: Specify the technical requirements for seamless integration with the insurance systems. This may include compatibility with existing platforms, data exchange protocols, and any APIs that need to be implemented. Clearly define the expectations for a smooth and efficient technical collaboration.
- Summary: XXXXX

IT Security:
- Description: Articulate the essential IT security measures that need to be in place. This could involve encryption standards, data protection protocols, and authentication processes. Emphasize the importance of safeguarding sensitive information and ensuring compliance with industry standards.
- Summary: XXXXX

Post-sales Service and Claims:
- Description: Provide a comprehensive overview of the post-sales service expectations and claims processing requirements. Detail the customer support structure, the steps involved in lodging and processing claims, and the expected turnaround times. This section focuses on ensuring a high level of customer satisfaction and efficient claims resolution.
- Summary: XXXXX

Medical Assistance Service:
- Description: Specify the requirements for medical assistance services. This may include access to emergency medical services, coordination with healthcare providers, and any other support services aimed at ensuring the well-being of travelers. Clearly outline the standards and capabilities expected from medical assistance providers.
- Summary: XXXXX

Legal and Compliance:
- Description: Detail the legal and compliance requirements essential for the insurance tender. This involves specifying any regulatory considerations, geographical restrictions, and the setup required for hosting the tender. Emphasize the importance of adherence to legal standards to ensure a compliant and ethical insurance operation.
- Summary: XXXXX

Project Planning and Delivery:
- Description: Provide a clear framework for project planning and delivery timelines. Outline the key milestones, deadlines, and expectations for the overall project implementation. This section aims to establish a realistic and achievable timeline for the successful execution of the insurance services outlined in the tender.
- Summary: XXXXX

Innovation:
- Description: Define the expectations regarding innovation in the insurance services. This may include advancements in technology, novel approaches to customer engagement, or any other innovative practices that align with the vision of the insurance tender. Encourage creative solutions and forward-thinking approaches to enhance the overall insurance offering.
- Summary: XXXXX

"""



map_reduce_template_reduce_summary = """
Combine the provided context to generate section-wise summaries while preserving the semantic meaning and all the keys points.\n\n
------------\n
CONTEXT:\n
{{context}}\n
------------\n


*** INSTRUCTION ***
Combines thes documents according to the sections as defined in the structure below :


*** STRUCTURE SUMMARY ***\n\n
Travel Insurance Products:
- Description: In this section, articulate the desired features and characteristics of the travel insurance products. Specify the range of coverage, benefits offered, pricing models, and preferred distribution channels. Clearly outline the unique selling points that should be present in the insurance products to meet the tender requirements.
- Summary: XXXXX

Additional Travel Services:
- Description: Elaborate on any supplementary services beyond traditional insurance products. This could encompass services such as travel assistance, concierge services, or any other offerings that enhance the overall travel experience. Detail the specific requirements and expectations for these services.
- Summary: XXXXX

Financial Compensation:
- Description: Define the processes and criteria for financial compensation. Clearly outline the circumstances under which compensation is applicable, the calculation methodology, and the steps involved in processing compensation claims. This section aims to provide a transparent and structured approach to handling financial matters.
- Summary: XXXXX

Technical Integration:
- Description: Specify the technical requirements for seamless integration with the insurance systems. This may include compatibility with existing platforms, data exchange protocols, and any APIs that need to be implemented. Clearly define the expectations for a smooth and efficient technical collaboration.
- Summary: XXXXX

IT Security:
- Description: Articulate the essential IT security measures that need to be in place. This could involve encryption standards, data protection protocols, and authentication processes. Emphasize the importance of safeguarding sensitive information and ensuring compliance with industry standards.
- Summary: XXXXX

Post-sales Service and Claims:
- Description: Provide a comprehensive overview of the post-sales service expectations and claims processing requirements. Detail the customer support structure, the steps involved in lodging and processing claims, and the expected turnaround times. This section focuses on ensuring a high level of customer satisfaction and efficient claims resolution.
- Summary: XXXXX

Medical Assistance Service:
- Description: Specify the requirements for medical assistance services. This may include access to emergency medical services, coordination with healthcare providers, and any other support services aimed at ensuring the well-being of travelers. Clearly outline the standards and capabilities expected from medical assistance providers.
- Summary: XXXXX

Legal and Compliance:
- Description: Detail the legal and compliance requirements essential for the insurance tender. This involves specifying any regulatory considerations, geographical restrictions, and the setup required for hosting the tender. Emphasize the importance of adherence to legal standards to ensure a compliant and ethical insurance operation.
- Summary: XXXXX

Project Planning and Delivery:
- Description: Provide a clear framework for project planning and delivery timelines. Outline the key milestones, deadlines, and expectations for the overall project implementation. This section aims to establish a realistic and achievable timeline for the successful execution of the insurance services outlined in the tender.
- Summary: XXXXX

Innovation:
- Description: Define the expectations regarding innovation in the insurance services. This may include advancements in technology, novel approaches to customer engagement, or any other innovative practices that align with the vision of the insurance tender. Encourage creative solutions and forward-thinking approaches to enhance the overall insurance offering.
- Summary: XXXXX

"""


###### Structure policy #######

template_extraction_structure_policy = """
As a tender structure analyst, your task is to extract the document's structure comprehensively. 
Your objective is to craft a holistic representation of the document's : 

------------
DOCUMENT:
{{context}}
------------\n\n


The final structure should resemble to :

Section: Subject
    Subsection : Subject - Concise description
    Subsection : Subject - Concise description
    [....]

Section: Subject
    Subsection: Subject - Concise description
    Subsection: Subject - Concise description
[....]

"""

prompt_collapse_structure_policy ="""
"Assembles all structure parts of the following context together to return a holistic representation of the document's.
Write a very concise summary for every subsection :\n\n
------------\n
CONTEXT:\n
{{context}}\n
------------\n\n
"""

prompt_reduce_structure_policy ="""
"Assembles all structure parts of the following context together to return a holistic representation of the document's.
Write a very concise summary for every subsection :\n\n
------------\n
CONTEXT:\n
{{context}}\n
------------\n\n
"""
