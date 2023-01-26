from transformers import pipeline, set_seed


def generate_answer(context: str,question: str):
    answer_generator = pipeline('question-answering', model = 'distilbert-base-uncased-distilled-squad')
    
    result = answer_generator(question=question, context=context)

    return (result['answer'], round(result['score'], 4))
