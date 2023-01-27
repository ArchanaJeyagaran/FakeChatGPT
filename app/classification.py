from transformers import pipeline, set_seed

classifier = pipeline('ner', model = 'stevhliu/my_awesome_wnut_model')

def entity_categorizer(question: str):
    result = classifier(question)
    output = []
    for i in range(len(result)):
        output.append((result[i]['word'], result[i]['score']))
    return output

