# ask-about
Ask about details that are embedded in a web.
This project was hatched as a final project for my AI training course.
My goal is to extend a web crawler / semantic search lesson, https://platform.openai.com/docs/tutorials/web-qa-embeddings,
to deal with a 
website that I know well, https://hackathon.slalom.com/.
This website has Slalom hackathon results for 2019 through 2023, with wonderful details of 
themes, teams, and accomplishments.  I'd like to scrape all the text from the site, and
then answer questions like these:
1. "Who can I ask about a healthcare solution built on AWS?"
1. "Are there any teams that built something about renewable energy?"
1. "Anyone who created a blockchain game?"
1. "What's an example application focused on sustainability, and built against Azure?"
1. "Any mobile applications related to the energy industry?"

# Status
1. I cloned the lesson repo, https://github.com/openai/web-crawl-q-and-a-example, and copied the Jupyter notebook here.
2. The crawler as is just scrapes the text of a page.  I started to extend the crawler using Selenium to scrape the source of a page, after Javascript has been rendered.
3. My current crawler fails on the first recursive call to a sub-page of the initial URL with ConnectionRefusedError, and therefore I'm stopping the recursive calls for now just to see what happens with the rest of the code.


## Setup
1. `pip install requests bs4 pandas tiktoken openai numpy`
2. `pip install selenium`
3. `nuget install selenium.webdriver.chromedriver -Version 130.0.6723.6900`
4. Modify the Chromedrive URL in the code.

