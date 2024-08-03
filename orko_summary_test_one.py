import os
#from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == '__main__':
    #load_dotenv()

    print('hello LangChain!')
    #print(os.environ['OPENAI_API_KEY'])

    information = """
        The next figure in Mondo's MASTERS OF THE UNIVERSE 1/6 scale line is the heroic court magician Orko! 
        The Orko 1/6 Scale Figure comes complete with a scepter and fabric robe as well as a slew of swappable 
        hands and portraits, including the never-before-produced unmasked Orko. The figure also provides a first 
        glimpse at Orko’s legs (yes, Orko has legs), and Mondo is honored that Mattel gave them a chance to 
        debut these expanded features. As an added bonus, in addition to the main figure, our deluxe Timed Edition 
        also features Orko Classic and Dree Elle mini figures and stands, plus Orko’s playmate Daimar the Demon.

        For our next trick ... the newest figure in our #MOTU 1/6 scale line is the heroic court magician Orko! 
        Our Orko 1/6 Scale Figure comes complete with a scepter and fabric robe as well as a slew of swappable hands and portraits, including the never-before-produced unmasked Orko. The figure also provides a first glimpse at Orko’s legs (yes, Orko has legs), and we’re honored that Mattel gave Mondo a chance to debut these expanded features. 
        The pre-order for the #Orko - Timed Edition will be available from Tuesday, Jan. 23 at 12 NOON CT until Tuesday, Jan. 30 at 11:59 AM CT … only at MondoShop.com. 
        Free shipping to the United States, Canada, UK and the EU. Payment plans available. 
        See more at https://mondoshop.com/.../motu-orko-1-6-scale-figure....
        #mastersoftheuniverse #mastersoftheuniversetoys #mastersoftheuniversecollector #mastersoftheuniversecollection

        Mondo Masters of the Universe 1/6 scale Orko Timed Edition goes up for preorder tomorrow (1/23) at 1 PM EST ($235.00).

        Includes unmasked Orko head and legs.
    """


    summary_template = """
        given the information {information} about product, I want you to create:
        1. A short summary. Ensure you include pricing and release details if provided.
        2. two interesting facts about the product
    """

    summary_prompt_template = PromptTemplate(input_variables=['information'], template=summary_template)

    #gpt-3.5-turbo
    llm = ChatOpenAI(temperature=0, model_name='gpt-4-turbo-preview')

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    rest = chain.invoke(input={'information': information})

    print(rest)