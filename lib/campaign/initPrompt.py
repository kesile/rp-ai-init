def generateInitialPrompt(platform, data, count):
    initPrompt = f"""
    Hello. Your job is to brain storm a series of {platform} posts for an advertising campaign.
    You should define the post types, quantity, etc.

    Each post should have... 
    - A type (IE: Teaser, Launch, Feature Highlight)
    - A theme (IE: Mystery/excitement, Introduction, Showcase)
    - An objective (IE: Generate anticipation, introduce the product, showcase the product)

    Campaigns should be cohesive and flow well with each other. Here is the data to make a campaign about:

    {data}

    Do not repeat posts or post types. Also, do not actually put the post. Just the structure.

    It should be separated by line breaks. Here's hot it should look.

    Type: x
    Theme: y
    Objective: z
    $%$
    Type: x
    Theme: y
    Objective: z

    Make {count} posts. All posts must flow together. There shouldn't be multiple launches, or 4 teasers in a row, etc. Include the $%$ for splitting purposes. 
    """
    return initPrompt