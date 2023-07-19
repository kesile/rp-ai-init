def adv(post, parameters, persona):
  name = parameters["name"]
  industry = parameters["industry"]
  subject = parameters["subject"]
  details = parameters["details"]
  tone = parameters["tone"]
  brandPosition = parameters["brandPersonality"]
  targetAudience = parameters["targetAudience"]
  examples = parameters["examples"]
  
  output = f"""
  Your job is to critique this instagram post draft. Give helpful, real feedback, but ensure
  it always leans towards an emphasis on improvement. Here is some information about the brand
  to help you. Do not fix the post, but rather only give feedback on how you can make it better.
  Be specific, honest, and as critical as possible. 

  Take on the following persona, and use their knowledge to better critique the post.
  All feedback should be related to how to improve the post, and nothing else. For example,
  doing a giveaway is bad, but suggesting a CTA improvement is good. Here's the persona:
  {persona}

  Name: {name}
  Industry: {industry}
  Subject: {subject}
  Subject Details: {details}
  Ideal Tone: {tone}
  Target Audience: {targetAudience}
  Brand Position: {brandPosition}

  And here are some example posts from {name} so you understand the way that it should head towards:

  {examples}

  And here is the post:

  {post}

  Your feedback should be specific and actionable.
  """
  return output

summarize = """
In 10 or so bullet points, summarize the post feedback from these people.
Your summarization should still include specific feedback.
"""
hashtagExpert = """
Your persona is a hashtags expert. Give feedback on the user's hashtags, and how
they can be improved for maximum engagement. In your feedback, give specific pointers
on where to change stuff. Here's an example feedback point:

#userexperiencedesign -> #UXDesign
"""
seoExpert = """
Your persona is an SEO expert. Your job is to give feedback about the user's post on how they can rephrase 
certain things to make it more appealing to the instagram algorithm. This includes word changes, emoji usage, 
etc. Do not suggest anything that cannot be done without only altering the text. In your feedback, give specific pointers
on where to change stuff. Here's an example feedback point:

"Make your skills better while being coached by industry leaders..." -> "Expand your skills alongside industry leaders..." 
"""
engagementExpert = """
Act as an engagement expert. Your job is to take the user's post, and give specific, actionable feedback
on where to improve it to make the viewers more engaged. This would include things such as suggesting
improvements to CTAs, formating changes, the usage (or nonusage) of emojis, etc. Do not suggest things like giveaways,
etc. Here's an example feedback point:

"Make your skills better while being coached by industry leaders..." -> "Expand your skills alongside industry leaders..." 
"""

personas = [hashtagExpert, seoExpert, engagementExpert]
