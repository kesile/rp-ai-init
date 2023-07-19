def campaignPost(parameters):
    name = parameters["name"]
    industry = parameters["industry"]
    subject = parameters["subject"]
    details = parameters["details"]
    tone = parameters["tone"]
    brandPosition = parameters["brandPersonality"]
    targetAudience = parameters["targetAudience"]
    cta = parameters["cta"]
    length = parameters["length"]
    examples = parameters["examples"]

    postType_options = {
        "1": "Product Detail",
        "2": "Product Use Scenarios",
        "3": "Follower Engagement",
        "4": "Event Announcement"
    }
    postType = input("""\nWhat type of campaign post are you creating?" \n1.Product Detail  -  2.Product Use Scenarios  -  3.Follower Engagement  -  4.Event Announcement""")
    postType = postType_options.get(postType, "Unknown")

    output = f"""
    Our company is launching a new product. We would like to create some posts that focuses on {postType}.
    As our social media manager, we need your help in creating engaging and compelling social media posts. 
    Please generate a series of posts that align with the brand's tone and target our audience effectively.
    Only use details mentioned below, and do not add anything irrelevant to the posts. 

    To ensure the posts align with the brand's public image, please carefully study the tone and structure of these
    example posts: 
    {examples}
    
    Here are some details to guide you:

    Brand Information:
    Name: {name}
    Industry/Niche: {industry}
    Brand Personality: {brandPosition}
    
    Target Audience:
    Interests/Hobbies: {targetAudience}
    Social Media Platforms: Instagram
    
    Content Guidelines:
    Tone: {tone}
    Length: {length}
    Content Themes: {subject}
    Details About the Post: {details}
    Call-to-Action: {cta}

    Please generate a set of 3 social media posts. 
    Ensure that the posts are creative, engaging, and tailored to the platform's requirements. 
    Use appropriate hashtags, mentions, and media (images, videos) where necessary. 
    """

    return output
