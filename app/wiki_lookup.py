import wikipediaapi


def wiki_finder(entities: list):
    full_context = ""
    for entity in entities:
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )
        
        p_wiki = wiki_wiki.page(entity[0])
        
        full_context +=  ("\n\n" + p_wiki.text)

    return full_context