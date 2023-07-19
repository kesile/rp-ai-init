def upd(post, feedback, parameters):
  name = parameters["name"]
  industry = parameters["industry"]
  subject = parameters["subject"]
  details = parameters["details"]
  platform = parameters["platform"]
  tone = parameters["tone"]
  brandPosition = parameters["brandPersonality"]
  targetAudience = parameters["targetAudience"]
  length = parameters["length"]
  examples = parameters["examples"]
  
  output = f"""
  Hello, your job is now to design {platform} posts for {name}. {name} is a company, working in the {industry} industry.
  We would like you to design a post for {subject}. {details}.
  You are creating content for a {brandPosition} brand targeting {targetAudience}.
  Keep the tone {tone}. You have previously generated a post, which is here:
  {post}

  However, you have received some feedback. Here is the feedback you received:

  {feedback}

  Please integrate this feedback into a new, better post. Here are some example posts from {name} to help you out:
  {examples}

  Make sure the post structure is aligned with the {platform} standard, and keep your post length in check 
  so it doesn't become too long, as described in the following: {length}.
  """
  return output