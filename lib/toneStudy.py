from axns.tc import text

company = "Google"
posts = ["""How do Dooglers tell their teams they’re going on vacation?
         They set their out of paw-ffice. 📧🐾 #InternationalJokeDay""",
         """Googlers at our Google Korea office recently got their coffees from a surprise barista: giant penguin Pengsoo from the YouTube channel Giant Peng TV, run by a major South Korean educational public broadcaster.
         For those who don’t know Pengsoo, he beat out BTS in 2019 for South Korea’s “Person of the Year”.
         Waddle you waiting for? Check out this fun video (English subtitles available) to watch him attempt to find the secret behind YouTube’s trending videos.""",
         """Meet Ido Frankel, a Tel Aviv-based software engineering intern studying computer science at Technion - Israel Institute of Technology! This summer, Ido is working on a team responsible for improving Google's ability to accurately categorize entities, people, and organizations in our search results.
         When asked how he became interested in this work, Ido spoke about the power of machine learning (ML). “Since the first courses I took about numerical algorithms and ML, I was amazed by the endless possibilities of these fields,” Ido explained. “Uncovering hidden information from data can help us solve very difficult problems. Having the opportunity to do this at Google's scale is all the more exciting!”
         Thank you for all of your hard work this summer, Ido!
         """]

def get_style(company_name, post):

    styles = []

    prompt = f""" 
        Please carefully read the following post by {company_name} and provide an in-depth analysis of the writing style, formatting, and key details:
    
        {post}
                
        In your response, please discuss:
                
        - The overall tone and voice of the writing. Is it formal, conversational, academic etc?
        - What writing techniques are used? Descriptive language, humor, rhetorical questions etc. Provide examples.
        - How is the content structured and organized? Chronicle format, problem-solution, compare-contrast etc.
        - The intended audience based on the language and approach. Is it aimed at experts, general public etc?
        - Any formatting used like headers, lists, images etc and how they enhance the content.
        - Your assessment of what works well in the writing and what could be improved.
        - Please provide a detailed analysis covering all these aspects of the article's style, formatting, and content. 
        - Focus your response on an objective, in-depth review of how effectively the information is presented to the reader.
        """

    styles.append(text(prompt))

    print(styles) # will work on using the styles directly in post generation

get_style(company, posts) # for testing
