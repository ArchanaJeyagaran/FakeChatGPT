from .answer import generate_answer
from .classification import entity_categorizer
from .wiki_lookup import wiki_finder


def faker_response(question: str):
    
    entities = entity_categorizer(question=question)
    
    context = wiki_finder(entities)
    
    answer = generate_answer(
        context,
        question
    )
    
    return(answer)
