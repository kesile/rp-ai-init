def gp(parameters):
    name = parameters["name"]
    desc = parameters["desc"]
    industry = parameters["industry"]
    subject = parameters["subject"]
    details = parameters["details"]
    tone = parameters["tone"]
    targetAudience = parameters["targetAudience"]
    brandPosition = parameters["brandPersonality"]
    length = parameters["length"]
    examples = parameters["examples"]

    output = f"""
    Hello, your job is now to design instagram posts for {name}. {name} is a company, working in the {industry} industry.
    More about the company: {desc}.
    We would like you to design a post about {subject}. Details: {details}. 
    You are creating content for a {brandPosition} brand targeting {targetAudience}.
    Keep the tone {tone}.

    Ensure that the post incorporates an eye-catching image or video related to the content.
    Here are some things to keep in mind. Format it like an instagram post.

    Objective: Your goal is to entertain and inspire your audience with this post.
    Target Audience: Consider {targetAudience}.
    Headline: Create a catchy headline that captures attention and hints at the content.
    Introduction: Begin the post with an engaging introduction to pique the interest of your followers.
    Value: Offer value by sharing tips, insights, or a captivating story that resonates with your audience's interests.
    Visual Elements: Include an image or video that complements the content and attracts attention while maintaining relevance.
    Tone: Keep the tone {tone}.
    Post Length: the length of the post should be {length}.
    Call-to-Action (CTA): End the post with a CTA that encourages interaction. Ask a question, invite comments, or suggest sharing with friends.
    Hashtags: Suggest 3-5 relevant and popular hashtags to increase visibility and reach.
    Review and Edit: Before posting, review the content for coherence, grammar, and overall appeal. Edit as needed to ensure a polished final version.

    Here are some example posts from {name} to help you out:

    {examples}

    Only copy formatting and styling from posts, and do not integrate any of the content from the posts as they are not relevant.
    Format the posts, exactly as you would an instagram post. Do not say something like "Headline:" or "Value:", just put the post.
    Do not output anything other than the post.
    """
    return output

def lin(parameters):
    name = parameters["name"]
    desc = parameters["desc"]
    industry = parameters["industry"]
    subject = parameters["subject"]
    details = parameters["details"]
    tone = parameters["tone"]
    targetAudience = parameters["targetAudience"]
    brandPosition = parameters["brandPersonality"]
    length = parameters["length"]
    examples = parameters["examples"]

    output = f"""
    Hello, your job is now to design LinkedIn posts for {name}. {name} is a company, working in the {industry} industry.
    More about the company: {desc}.
    We would like you to design a post about {subject}. Details: {details}. 
    You are creating content for a {brandPosition} brand targeting {targetAudience}.
    Keep the tone {tone}.

    Ensure that the post incorporates an eye-catching image or video related to the content.
    Here are some things to keep in mind. Format it like an LinkedIn post.

    Objective: Your goal is to entertain and inspire your audience with this post.
    Target Audience: Consider {targetAudience}.
    Headline: Create an eye-catching headline that will capture attention and hint at what the post is about.
    Introduction: Write an introduction that introduces the post in an engaging way to pique interest.
    Value: Provide value to the reader such as tips, insights, or an interesting story relevant to the target audience.
    Visual Elements: Include an image or video that complements the content and attracts attention while maintaining relevance.
    Tone: Keep the tone {tone}. In addition, use an enthusiastic yet professional tone aligned with {name}'s brand: {brandPosition}.
    Post Length: the length of the post should be {length}.
    Call-to-Action (CTA): End with a strong call-to-action to encourage comments, sharing, asking questions, or another desired interaction.
    Hashtags: Suggest 3-5 relevant and popular hashtags to increase visibility and reach.
    Review and Edit: Before posting, review the content for coherence, grammar, and overall appeal. Edit as needed to ensure a polished final version.

    Here are some example posts from {name} to help you learn more about the company's tone:

    {examples}

    Most importantly, consider the following points to create an effective LinkedIn post:
    - More text-heavy long form posts - articles, blog styles work well.
    - Keep it simple, use plain text, no fancy imagery.
    - Professional tone, avoid slang. Well-written and insightful.
    - Thought leadership content performs best - tips, advice, insights.
    - Use hashtags strategically. No more than 2-3 max typically.
    - Call to actions should encourage engagement, sharing, comments.
    - Native video works well - interviews, presentations, tutorials etc.
    - Headlines and introductions are important to draw readers in.
    - End the post by asking a question to engage readers.

    Only copy formatting and styling from posts, and do not integrate any of the content from the posts as they are not relevant.
    Format the posts, exactly as you would an LinkedIn post. Do not say something like "Headline:" or "Value:", just put the post.
    Do not output anything other than the post.
    """
    return output