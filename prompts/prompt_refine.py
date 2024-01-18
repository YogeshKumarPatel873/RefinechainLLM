
#########################################
########### REFINE TEMPLATES ############
#########################################

refine_template_summarize = """
Summarize this content:\n\n{{context}}
"""

########### Summarize by section ############

refine_summarize_template_by_section = """
Your primary goal, as a tenders analysis agent, revolves around crafting section-specific summaries while preserving the tender's semantic meaning and essential elements. Your task involves extracting pertinent details from the tender and addressing the client's specific requests.

Your output should be a meticulous compilation of factual information sourced directly from the tender. These summaries must encompass comprehensive details without incorporating any recommendations.

Maintaining precision and completeness throughout these summaries is crucial. The objective is to provide a thorough yet concise overview of the tender's contents, ensuring that all crucial points are encapsulated within each section-specific summary.\n\n

------------\n
DOCUMENT:\n
{{context}}\n
------------\n\n


*** INSTRUCTIONS ***\n
Your task involves thoroughly extracting information from individual sections within the tender document. Your aim is to meticulously craft comprehensive summaries for each section, emphasizing crucial tender details and specific client requests.

It's essential that the output you generate comprises solely factual information and concise summaries. Avoid including any recommendations in your summaries.

Ensure that your summaries adhere strictly to the given structure:\n\n


*** STRUCTURE SUMMARY ***\n
Travel Insurance Products:
- Summary: XXXXX

Additional Travel Services:
- Summary: XXXXX

Financial Compensation:
- Summary: XXXXX

Technical Integration:
- Summary: XXXXX

IT Security:
- Summary: XXXXX

Post-sales Service and Claims:
- Summary: XXXXX

Medical Assistance Service:
- Summary: XXXXX

Legal and Compliance:
- Summary: XXXXX

Project Planning and Delivery:
- Summary: XXXXX

Innovation:
- Summary: XXXXX

"""

refine_prompt_summarize_by_section = """
Your primary responsibility entails crafting comprehensive summaries for each section, ensuring that you maintain the semantic essence and capture all critical elements.
You'll build upon an existing summary, extending it further from a specific point. Your task involves not only expanding on the content but also retaining the significance
and essence of the information presented.:
------------\n
PREVIOUS CONTEXT:\n
{{prev_response}}\n
------------\n\n

We have an opportunity to improve our current summaries by incorporating additional context derived from the tender
under review and the specific requests made by our clients.
The goal is to enrich the existing summaries with factual information extracted from these sources.This additional 
information should provide a comprehensive understanding of each section without including any recommendations.
To achieve this, we aim to expand upon the current section-wise summaries by incorporating precise and exhaustive 
details. The focus is on factual information, ensuring that each section's summary becomes more comprehensive without 
including any advice or suggestions.

------------\n
ADDITIONAL CONTEXT:\n
{{context}}\n
------------\n\n

Given the new context, enhance the original summaries by respectibg the structure below : \n\n

*** STRUCTURE SUMMARY ***\n
Travel Insurance Products:
- Summary: XXXXX

Additional Travel Services:
- Summary: XXXXX

Financial Compensation:
- Summary: XXXXX

Technical Integration:
- Summary: XXXXX

IT Security:
- Summary: XXXXX

Post-sales Service and Claims:
- Summary: XXXXX

Medical Assistance Service:
- Summary: XXXXX

Legal and Compliance:
- Summary: XXXXX

Project Planning and Delivery:
- Summary: XXXXX

Innovation:
- Summary: XXXXX
"""

########### Gap Analysis ############

template_refine_gap_analysis = """
Envision yourself as an underwriter agent specializing in insurance policy wording. Your task is to meticulously analyze a document to identify gaps or missing components.

This schema acts as your guide, outlining the various types of information you are expected to scrutinize.
For each part return a comprehensive feedback, status about the missing parts or gaps (Yes/No and justification) and the writing style analysis:

*** ANALYSIS SCHEMA ***
Policy Introduction:
- In-depth overview, insurer details, and policy objectives.
- Feedback: Confirm that the introduction provides a comprehensive understanding of the insurer, policy aim, and key benefits. 
- status: Is any critical information missing? (Yes/No)
- Writing style analysis

Eligibility and Coverage Period:
- Scrutiny of age limits, residency requirements, and policy duration.
- Feedback: Ensure that eligibility criteria are inclusive and residency requirements are clearly defined. Verify that the coverage period aligns with policy expectations. 
- status: Are there any gaps or missing details in eligibility or coverage period? (Yes/No)
- Writing style analysis

Coverage Details and Benefits:
- Evaluation of medical coverage, trip cancellation, baggage, etc.
- Feedback: Assess the comprehensiveness of coverage and clarity in benefit descriptions. Suggest improvements to enhance the understanding of coverage details. 
- status: Are there any gaps or missing information in coverage details and benefits? (Yes/No)
- Writing style analysis

Exclusions and Limitations:
- Examination of scenarios not covered and coverage limits.
- Feedback: Evaluate the clarity and fairness of exclusions, ensuring precise definitions. Suggest clarifications or additions for a more transparent policy. 
- status: Are there any gaps or ambiguities in exclusions or coverage limits? (Yes/No)
- Writing style analysis

Claims Process and Requirements:
- Review of steps to file a claim and required documentation.
- Feedback: Ensure a straightforward and well-explained claims process. Suggest improvements to simplify the steps and enhance clarity in documentation requirements. 
- status: Are there any missing steps or unclear documentation requirements? (Yes/No)
- Writing style analysis

Premiums and Payment Terms:
- Inspection of payment methods and the refund policy.
- Feedback: Review for transparency and simplicity in payment terms. Suggest enhancements to improve understanding of payment methods and streamline the refund policy. 
- status: Are there any ambiguities or missing details in payment terms? (Yes/No)
- Writing style analysis

Policy Modifications and Extensions:
- Investigation into procedures for changes and renewals.
- Feedback: Check for flexibility and ease of making policy modifications. Suggest improvements to streamline procedures for changes and renewals. 
- status: Are there any gaps or complexities in policy modification procedures? (Yes/No)
- Writing style analysis

General Terms and Conditions:
- Assessment of rights and responsibilities and cancellation terms.
- Feedback: Ensure that terms are fair, clearly stated, and easily understood. Suggest modifications for clarity and precision in presenting rights, responsibilities, and cancellation terms. 
- status: Are there any unclear or missing terms in this section? (Yes/No)
- Writing style analysis

Contact Information and Assistance:
- Verification of contact details for support and emergencies.
- Feedback: Confirm the accuracy and accessibility of contact information. Suggest improvements for better visibility and ease of access to support and emergency contacts. 
- status: Are there any inaccuracies or missing contacts? (Yes/No)
- Writing style analysis

Legal and Regulatory Compliance:
- Examination of jurisdiction and regulatory adherence.
- Feedback: Ensure compliance with legal and industry standards. Suggest modifications for clearer alignment with jurisdiction and regulatory requirements. 
- status: Is the document compliant with legal and industry standards, or are there any gaps? (Yes/No)
- Writing style analysis

Definitions and Key Terms:
- Analysis of clear definitions of terms used.
- Feedback: Assess for clarity and consistency in terminology. Suggest enhancements to ensure that definitions are clear and concise. 
- status: Are there any unclear or missing definitions? (Yes/No)
- Writing style analysis

COVID-19 Specific Coverage (if applicable):
- Review of coverage related to the pandemic.
- Feedback: Check for relevance, clarity, and adequacy of COVID-19 coverage. Suggest modifications to align with current guidelines and enhance clarity. 
- status: Is the COVID-19 coverage relevant and clear, or are there any gaps? (Yes/No)
- Writing style analysis

Additional Benefits and Services:
- Evaluation of extra offerings such as 24-hour assistance.
- Feedback: Assess the added value and relevance of these services. Suggest improvements to enhance the value proposition and relevance of additional benefits. 
- status: Are there any additional benefits or services missing or unclear? (Yes/No)
- Writing style analysis

Frequently Asked Questions (FAQs):
- Examination of common queries and answers.
- Feedback: Ensure FAQs address common concerns and are easy to understand. Suggest additions or clarifications to cover a broader range of questions. 
- status: Are there any common queries or answers missing or unclear? (Yes/No)
- Writing style analysis

For the writing style analysis you must check the following points:
 - Clarity and Precision: Use clear, unambiguous language to avoid misunderstandings. Legal and insurance documents should be precise in their wording to prevent ambiguities.
 - Professional Tone: Maintain a professional, formal tone throughout the document. This instills confidence and reflects the seriousness of the subject matter.
 - Conciseness: Be succinct yet comprehensive. Avoid unnecessary complexity or verbosity.
 - Neutral Sentiment: Keep the sentiment neutral. Insurance policies are factual and informative documents, not persuasive or emotional in nature.
 - Consistent Terminology: Use consistent terminology throughout the document to avoid confusion.
 - Legally Sound: Ensure that the language is legally sound and compliant with relevant laws and regulations.
 - Reader-Friendly Structure: Structure the document in a way that is easy to navigate, with clear headings and subheadings.
 - Empathetic Understanding: While maintaining professionalism, acknowledge the reader's need for clear understanding, especially in sections explaining coverage and exclusions.

*** INSTRUCTIONS ***
The context to use to extract the data is provided below. \n
------------
DOCUMENT:
{{context}}
------------
"""


refine_prompt_gap_analysis = """
You currently have an existing analysis up to a specific point:
------------
PREVIOUS CONTEXT:
{{prev_response}}
------------

Now, an opportunity has emerged to refine certain aspects of the existing analysis with the introduction of additional context.
Keep the original analysis and update only the relevant sections (feedback and status)covered by the additional context. 
If a section is not affected by the additional context, retain the previous results (feedback, status and Writing style analysis).

------------
ADDITIONAL CONTEXT:
{{context}}
------------

Return the whole structure of the original analysis with the newly refined sections (if applicable).
The status (Yes/No) and feed back of all the sections must be returned.
"""

########### Ambiguities ############

refine_prompt_ambiguities_first = """

*** INSTRUCTIONS ***

Role of Travel Insurance Tender Analysis Agent:

Objective: Your primary objective is to meticulously review the tender document section provided, focusing particularly on key elements. These include but are not limited to traveler information, offer targets, forecasts, deliverables, timelines, technology requirements, business data, strategy, insurance plans, implementation technology, requirements, and company results.

Focus: Your attention should be directed primarily towards the data and information specified in the 'Questions' and 'Example of Data' columns within the guidance table. While reviewing, prioritize the mentioned data over minor details such as formatting. Your task is to verify the presence of data outlined in the guidance table within the section under review.

Goal: The main goal is to identify and highlight any sections of the tender that lack information or are unclear, aligning with the specifications provided in the guidance table. For each section under review, ensure it contains the information described in the guidance table. If discrepancies or missing information are found, they should be clearly noted, and relevant questions must be raised. Questions should either originate from the Guidance Table or be similar in nature.

Analysis Guidelines:

Section Reference: Specify the name of the sub-section within the document that lacks information or requires more details as per the Guidance Table.
Statement Clarity: Identify statements or aspects that appear unclear, ambiguous, or incomplete.
Questions Raised: Formulate questions that pertain to the missing information, as delineated in the Guidance Table. Endeavor to ask comprehensive questions. In cases where the Guidance Table doesn't offer specific questions, base your inquiries on your understanding of the business context.
Explanation: Provide a rationale, based on the guidance table, elucidating the necessity for these additional details.
Utilization of the Guidance Table:

Purpose: Employ the table as a comprehensive checklist to confirm the presence of all essential as described in the Guidance Table.
Contents: The table includes Tender Segment, Section, Sub-section, relevant questions, their significance, and typical partner responses.
Task: Assess the tender information against the Guidance Table. Compare the tender's details and information with the necessary details and information from Guidance Table. 
Action on Discrepancies: If the tender lacks information outlined in the guidance table (typical partner responses) or according to your expertise, raise the pertinent question along with its justification as per the table's guidance.

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

***Output Overview***

This section focuses on areas within the document that require further attention due to missing information or the need for additional details based on the Guidance Table.

*Identifying Section References* : Locate sections of the document that lack necessary information or require more comprehensive details, as indicated by the Guidance Table.

*Clarifying Statements* : Highlight and address any statements or aspects within the document that are unclear, ambiguous, or incomplete.

*Question Generation* : Create a comprehensive list of questions pertaining to missing information outlined in the guidance table. It's crucial to ask a wide array of questions to ensure comprehensive coverage.

*Providing Explanations* : Offer a rationale derived from the guidance table to justify the necessity for additional details in these specific sections. This explanation serves as a guideline to enrich and refine the content.
"""
refine_prompt_ambiguities_iteration = """

*** INSTRUCTIONS ***

Role: Traveling Insurance Tender Analysis Agent

Objective: Your role entails a comprehensive review of a designated section within the tender document. Emphasize critical areas such as traveler information, offer targets, forecasts, deliverables, timelines, technology requirements, business data, strategy, insurance plans, implementation technology, requirements, and company results. This analysis should complement the previous one without altering it, but by enriching it.

Focus: Prioritize data and information outlined in the 'Questions' and 'Example of Data' columns within the guidance table. While formatting details are secondary, your primary goal is to confirm the presence of specified data from the guidance table within the tender section under evaluation.

Begin with the existing analysis:
{{prev_response}}.
Retain this analysis intact and enhance it with the additional context provided below.

Goal: Expand upon the existing analysis by incorporating new aspects for additional context evaluation. Focus on identifying and highlighting sections within the additional context that lack information or clarity, as outlined in the Guidance Table. Ensure each section contains the required information per the Guidance Table. Take note of any discrepancies or missing details, and formulate relevant questions based on the table or your understanding of the business.

Analysis Guidelines:

Section Reference: Specify the name of the subsection within the document that lacks information or requires more details according to the Guidance Table.
Statement Clarity: Recognize statements or aspects that lack clarity, are ambiguous, or incomplete.
Raised Questions: Create questions related to the missing information, following the guidelines in the Table. Generate multiple questions. If specific questions aren't available in the Table Guidance, base your queries on your understanding of the business.
Explanation: Provide reasoning, based on the guidance table, justifying the necessity of these additional details.


**How to Utilize the Guidance Table**

The Guidance Table serves as a comprehensive checklist, ensuring that all crucial details outlined within it are present and accounted for in the tender document. Its purpose is to guide the thorough examination of the tender against predefined criteria.

*Key Components of the Guidance Table* : This table encompasses essential elements, including the Tender Segment, various Sections, Sub-sections, pertinent questions, their significance within the context of the tender, and typical partner responses.

*Tasks Involved* : Your primary task involves a meticulous comparison between the information provided in the tender and the corresponding requirements detailed within the Guidance Table. This thorough scrutiny is pivotal in ensuring alignment and completeness.

*Dealing with Discrepancies* : Should discrepancies arise where the tender lacks necessary information as outlined in the Guidance Table, or where your expertise deems further clarification essential, the process involves raising pertinent questions. These questions should be substantiated with justifications as per the guidelines provided in the table.

Guidance Table:

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

                   
*** ADDITIONNAL CONTEXT *** 

{{context}}

*** OUTPUT *** 

Section Reference:
Specify the particular segment of the document that requires additional information or further elucidation, as per the provided Guidance Table.

Statement Clarity:
Identify any statements or elements within the document that lack precision, contain ambiguity, or are incomplete.

Questions Raised:
Compile a comprehensive list of inquiries pertaining to missing information as outlined in the guidance table. Generate a thorough set of questions to address any gaps in understanding.

Explanation:
Present a rationale based on the guidance table, justifying the necessity for incorporating these supplementary details into the document.
"""




#Used by Kristian
v2_refine_prompt_summary_summarize_by_section = """
Task: Analyze the provided document and extract detailed summaries for the following predefined topics. 
For each topic, focus exclusively on key points and statements relevant to that specific topic.

Task: Analyze the following text from a document and extract detailed summaries for predefined topic list.
The detailed summary for each topic should focus on all key points and statement which relevant to the topic itself.
The predefined topic list are listed below, containing the topic title and the expectation of summary inside the topic.
The final result should be list of topic summaries in JSON format without narration or any additional formatting or code block syntax, 
mentioning 2 information for each summary:
1. title: The topics title of summaries which based on the predefined topic list.
2. content: The summary of related topic which extracted from the document

DOCUMENT: 
{{context}}

TOPIC LIST:
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

#Used by Kristian
# As a tender agent for Ancileo, your task is to analyze take the section-wise summary and return it in a JSON format for post-processing. 
# The refined list will be crucial for preparing a targeted and precise response to the tender.

v2_refine_prompt_summary_refine_by_section = """
Task: Analyze the provided text and extract detailed summaries for the following predefined topics. 
For each topic, focus exclusively on key points and statements relevant to that specific topic.

- If the current document does not contain new information relevant to a topic, retain the existing summary for that topic from the previously provided summaries.
- If new and relevant information for a topic is found in the document, refine and update the existing summary for that topic. Include any new key points or details that enhance the understanding of the topic.

Please format the final result as a list of topic summaries in JSON format. Each summary should contain two pieces of information:
1. "title": The topic's title, as listed in the predefined topic list.
2. "content": The extracted summary for that topic, based on the analysis of the document.

Note: The output should be a clean JSON string without any additional narration, formatting, or code block syntax.


PREVIOUS SUMMARIES:
{{prev_response}}


DOCUMENT: 
{{context}}


PREDEFINED TOPIC LIST:
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

v2_refine_prompt_requirements_first = """
Task: Analyze the following text chunk from a tender proposal document and identify any requirements stated by the client.
The requirements represent all of the client's expectations for our response to the proposal.
List these requirements in JSON format, adhering to the provided JSON schema.
-----
Text Chunk: {context}
-----
JSON Schema:
{{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {{
    "documentInfo": {{
      "type": "object",
      "properties": {{
        "title": {{"type": "string"}},
        "author": {{"type": "string"}},
        "date": {{"type": "string"}},
        "filename": {{"type": "string"}}
      }},
      "required": ["title", "author", "date", "source"]
    }},
    "requirements": {{
      "type": "array",
      "items": {{
        "type": "object",
        "properties": {{
          "requirement": {{"type": "string"}},
          "mandatoryLevel": {{
            "type": "string",
            "enum": ["Mandatory", "Nice to Have", "Not Mandatory"]
          }},
          "details": {{"type": "string"}}
        }},
        "required": ["requirement", "mandatoryLevel"]
      }}
    }}
  }},
  "required": ["requirements"]
}}
-----
Please generate a JSON-formatted list of requirements based on this text chunk, following the JSON schema provided.
Your answer should only contain JSON without any narration
"""

v2_refine_prompt_requirements_iteration = """
Task: Refine the existing list of requirements by analyzing the next text chunk from the tender proposal document.
The requirements represent all of the client's expectations for our response to the proposal.
Add any new requirements or update the existing ones as necessary.
Use the provided JSON schema for structuring the output.
-----
Previous JSON Results: {prev_response}
-----
Next Text Chunk: {context}
-----
JSON Schema:
{{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {{
    "documentInfo": {{
      "type": "object",
      "properties": {{
        "title": {{"type": "string"}},
        "author": {{"type": "string"}},
        "date": {{"type": "string"}},
        "filename": {{"type": "string"}}
      }},
      "required": ["title", "author", "date", "source"]
    }},
    "requirements": {{
      "type": "array",
      "items": {{
        "type": "object",
        "properties": {{
          "requirement": {{"type": "string"}},
          "mandatoryLevel": {{
            "type": "string",
            "enum": ["Mandatory", "Nice to Have", "Not Mandatory"]
          }},
          "details": {{"type": "string"}}
        }},
        "required": ["requirement", "mandatoryLevel"]
      }}
    }}
  }},
  "required": ["requirements"]
}}
-----
Please update the JSON-formatted list of requirements by incorporating information from the new text chunk.
Ensure the updated list continues to follow the JSON schema provided.
Your answer should only contain JSON without any narration
"""
