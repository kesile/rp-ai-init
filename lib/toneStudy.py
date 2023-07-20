from axns.tc import text

company = "Google"
posts = ["""How do Dooglers tell their teams they’re going on vacation?
         They set their out of paw-ffice. 📧🐾 #InternationalJokeDay""",
         """Googlers at our Google Korea office recently got their coffees from a surprise barista: giant penguin Pengsoo from the YouTube channel Giant Peng TV, run by a major South Korean educational public broadcaster.
         For those who don’t know Pengsoo, he beat out BTS in 2019 for South Korea’s “Person of the Year”.
         Waddle you waiting for? Check out this fun video (English subtitles available) to watch him attempt to find the secret behind YouTube’s trending videos.""",
         """Meet Ido Frankel, a Tel Aviv-based software engineering intern studying computer science at Technion - Israel Institute of Technology! This summer, Ido is working on a team responsible for improving Google's ability to accurately categorize entities, people, and organizations in our search results.
         When asked how he became interested in this work, Ido spoke about the power of machine learning (ML). “Since the first courses I took about numerical algorithms and ML, I was amazed by the endless possibilities of these fields,” Ido explained. “Uncovering hidden information from data can help us solve very difficult problems. Having the opportunity to do this at Google's scale is all the more exciting!”
         Thank you for all of your hard work this summer, Ido!"""]

company2 = "Morgan Stanley"
posts2 = ["""Morgan Stanley reports second quarter 2023 net revenues of $13.5 billion, net income of $2.2 billion, EPS of $1.24 and ROTCE of 12.1%.
        Institutional Securities net revenues of $5.7 billion reflect continued muted activity in Investment Banking and declines in Equity and Fixed Income driven by lower client activity in a less favorable market environment compared to a year ago.
        Wealth Management delivered strong net new client assets of $90 billion and record net revenues of $6.7 billion, which reflect higher net interest income and the positive impact of DCP.
        Investment Management results reflect net revenues of $1.3 billion on AUM of $1.4 trillion and positive net flows. https://mgstn.ly/3Kqg37x""",
        """We are proud to have been recognized by the 2023 Euromoney Awards for Excellence as the World's Best Investment Bank, World's Best Bank for Advisory and World's Best Bank for Financial Institutions. Euromoney Editor Louise Bowman, Euromoney Editorial Director Peter Lee and TV presenter Jon Sopel presented the awards to Morgan Stanley’s Simon Smith, Guillaume Gabaix, Jan Weber and Clare Woodman on behalf of our global team whose grit and vision made this possible.""",
        """“Montréal is a key strategic location given its world-class talent, investment in tech innovation and proximity to our headquarters,” says Mike Pizzi, Head of Technology & U.S. Banks at Morgan Stanley, in conversation with Montréal Regional Head, Sophia Bennaceur. “Morgan Stanley Montréal has established itself as an employer of choice in the city’s vibrant technology landscape. We look forward to continuing to invest in our people’s growth and our city’s future,” added Sophia.
        Find out more about life in our Canada offices: https://lnkd.in/dtWU_iuT"""]

postTesting = """
We're pleased to share an update on Morgan Stanley's financial results for the third quarter of 2022.

In Q3, we delivered:

Net revenues of $13.6 billion, up 12% compared to Q3 2021
Net income of $3.2 billion, up 24% from the prior year quarter
EPS of $1.89 compared to $1.54 in Q3 2021
ROTCE of 20%, reflecting stable capital deployment
These results showcase the balanced performance across our integrated Investment Banking and Investment Management divisions.

Despite the challenging macroeconomic environment, we continue executing on our long-term vision: providing best-in-class advice and solutions to help our clients - institutions, governments, and individuals - achieve their strategic goals.

Thank you to our talented employees for your hard work serving our clients and communities around the world each day.

There's incredible potential ahead and we're just getting started! Read the full report for details on our Q3 2022 performance. #ProgressHappensHere

Let me know if you need any clarification on our latest quarterly results. Looking forward to continued success in Q4 and 2023.
"""


def get_style(company_name, post):
    prompt = f""" 
        Please carefully read the following post by {company_name} and provide an in-depth analysis of the writing style, formatting, use of punctuations, and key details:
    
        {post}
                
        In your response, please discuss:
                
        - The overall tone and voice of the writing. Is it formal, conversational, academic etc?
        - What writing techniques are used? Descriptive language, humor, rhetorical questions etc. Provide examples.
        - How is the content structured and organized? Chronicle format, problem-solution, compare-contrast etc.
        - Any special use of punctuations? 
        - The intended audience based on the language and approach. Is it aimed at experts, general public etc?
        - Any formatting used like headers, lists, images etc and how they enhance the content.
        - Please provide a detailed analysis covering all these aspects of the article's style, formatting, and content. 
        - Focus your response on an objective, in-depth review of how effectively the information is presented to the reader.
        """

    styles = text(prompt)
    # print(styles) # will work on using the styles directly in post generation
    # print("\n -Analysis Done- \n")

    prompt2 = f"""
        Please carefully review the provided analysis of a company's writing style:
        
        {styles}
        
        Extract and summarize the main points into a bulleted list covering the following aspects:
        - Overall tone and voice of the writing
        - Writing techniques used such as imagery, rhetoric, humor etc and examples
        - Structure and organization of content
        - Special use of punctuation
        - Intended audience based on language
        - Use of headers, lists, or other formatting
        - Any other notable observations about writing style and effectiveness
        Do not copy verbatim from the analysis. Synthesize the main points into clear, concise phrases in a bulleted list format. The goal is to extract the essence of the observations made about the company's writing style into a simplified summary. Please focus the response only on the summarized list.
        """

    summary = text(prompt2)
    #print(summary)
    #print("\n -Summary Complete- \n")

    prompt3 = f"""
        I will provide you with a bulleted list summarizing the key aspects of a writing style analysis conducted on a company's post. 
        Your task is to take this bulleted list and transform it into a clear set of step-by-step instructions that would allow a social media manager to replicate the same writing style.
        The instructions should be numbered and cover each of the elements outlined in the bulleted list in a straightforward manner. 
        Write the instructions as clear imperatives that guide the social media manager in employing the same techniques observed in the original post's writing style.
        The goal is to synthesize the writing style summary into an easy-to-follow set of techniques that can be implemented by a social media manager on a new post.
        Please read the provided summary carefully before composing the numbered list of instructions:

        {summary}

        Now please write out the instructions in a numbered list format based on this summary. Focus just on producing the clear, actionable instructions. Let me know if you have any other questions!
        """

    instructions = text(prompt3)
    return instructions
    #print(instructions)

def applyStyle():
    instructions = get_style(company2, posts2)

    prompt = f"""
        I now have a list of instructions on how to adjust the writing style of this post:
        
        {instructions}
        
        Afterwards, Please carefully review the following post:
        
        {postTesting}
        
        Then, follow the provided instructions step-by-step to make adjustments to the tone, techniques, structure, and formatting of the post. 
        The goal is to edit the post to align it with the desired writing style defined in the instructions.
        Make changes directly in the post itself - do not just describe the adjustments. 
        The end result should be an edited version of the initial post that implements each of the techniques outlined in the instructions, transforming the writing style appropriately.
        Only focus on styling and content changes that match the instructions. Do not add any new information beyond editing the existing text. 
        Please read through the instructions and the original post carefully before making any revisions.
        Once you have finished adjusting the post by following all steps in the instructions, please provide the revised post with the new writing style applied
        """

    resultPost = text(prompt)

    print(resultPost)
    #return resultPost

applyStyle() # testing
