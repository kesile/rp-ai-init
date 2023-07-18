def upd(post, feedback, parameters):

  name = parameters["name"]
  industry = parameters["industry"]
  subject = parameters["subject"]
  details = parameters["details"]
  tone = parameters["tone"]
  brandPosition = parameters["brandPersonality"]
  targetAudience = parameters["targetAudience"]
  examples = parameters["examples"]
  
  output = f"""
  Hello, your job is now to design instagram posts for {name}. {name} is a company, working in the {industry} industry.
  We would like you to design a post advertising their product, {subject}. {details}.
  You are creating content for a {brandPosition} brand targeting {targetAudience}.
  Keep the tone {tone}. You have previously generated a post, which is here:
  {post}

  However, you have recieved some feedback. Here is the feedback you recieved:

  {feedback}

  Please integrate this feedback into a new, better post. Here are some example posts from {name} to help you out:
  {examples}

  Make sure you keep your post length in check so it doesn't become too long.
  """
  return output