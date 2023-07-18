from .skeletonDoc import createDoc
import os

os.system("clear")

def initDoc():
    testQuery = input("Test mode? (Y/N) : ")
    if testQuery.lower() == "y" : 
        parameters = createDoc(
            "Redpeak",
            "Redpeak is a design agency (and so much more), that makes innovative brands appealing",
            "UX Design Meet",
            "Redpeak is hosting a UX design meet at their headquarters on the 21st Floor of the Taipei 101 at 3:00PM, Monday July 17th",
            "Design, UX",
            "Friendly, inviting, knowledgable",
            "UX/Design Professionals Looking To Expand Their Skills",
            "Knowledgable, friendly, and a leader",
            "We want the viewer to book a spot.",
            "Length should be somewhat concise.",
            "It's a free, fun event.",
            """
            Post #1: Our NYC office is now part of the Sid Lee family! Our colleagues are excited to be part of this new creative collective and to deliver work that matters. Follow at @sidlee_official to keep up with their work.
            Post #2: In partnership with the Taipei city government, #RedPeakAsia launched the identity that helped to transform the city into a testing ground for innovation. We’re happy to announce that #SmartTaipei just won the #iFDesignAward in the Brand Identity and Applications category #BrandsThatBond #DesignforGood
            Post #3: We opened our doors with @Intel as our inaugural client and we're proud of we’ve done together to continually evolve this brand. Happy 50th Anniversary #Intel! #Intel50years #BrandsThatBond
            Post #4: After today's shortsightedness from the Whitehouse, it seemed fitting to repost our poster from the @ideoorg design contest. A simple, universal warning about the dangers of climate change and the communities it will affect. #resist #designofdissent #designagency #design #posterdesign
            """
        )
    else:
        name = input("\nName? ")
        desc = input("Company description? ")
        subject = input("What's the post about? ")
        details = input("What're the details? ")
        industry = input("What's the industry of the company? ")
        tone = input("How do you want to sound in the post? ")
        targetAudience = input("What's your target demographic for this post? ")
        brandPersonality = input("What's the personality of your brand? ")
        cta = input("What do you want the person to do after viewing your post? ")
        length = input("Do you want to customize your post length? (Y/N) ")
        if length == "Y" : length = input("How many words should your post be around? ")
        else: length = "Whatever is best."
        uniqueAdvantage = input("What is the unique advantage of this event? ")
        examples = input("What are some example posts? ")
        parameters = createDoc(name, desc, subject, details, industry, tone, targetAudience, brandPersonality, cta, length, uniqueAdvantage, examples)
    
    print("\nParameters generated successfully.")

    return parameters