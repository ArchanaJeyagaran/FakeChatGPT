from transformers import pipeline, set_seed

answer_generator = pipeline('question-answering', model = 'distilbert-base-uncased-distilled-squad')

def generate_answer(context: str,question: str):
    
    result = answer_generator(question=question, context=context)

    return (result['answer'], round(result['score'], 4))
