from transformers import pipeline, set_seed

def entity_categorizer(question: str):
    classifier = pipeline('ner', model = 'stevhliu/my_awesome_wnut_model')
    result = classifier(question)
    output = []
    for i in range(len(result)):
        output.append((result[i]['word'], result[i]['score']))
    return output

