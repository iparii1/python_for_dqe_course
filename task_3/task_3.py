import re


def count_whitespaces(text: str) -> int:
    whitespace = sum(1 for i in text if i.isspace())
    return whitespace


def normalize_text(text: str) -> str:
    lines = [i for i in text.replace('\xa0', ' ').split('\n') if i != '']
    sentences = [i.strip().split('. ') for i in lines]
    normalized = '\n'.join(
        ['. '.join(item.capitalize() for item in sublist) for sublist in sentences]
    )
    normalized = re.sub(r'\biz\b', 'is', normalized)
    return normalized


def create_sentence(text: str) -> str:
    sentence = ' '.join([item[:-1] for item in re.findall(r'\b\w+\.', text)]).capitalize() + '.'
    return sentence


def insert_sentence(text: str, sentence: str, target_word: str) -> str:
    index = text.find(target_word)
    insert_index = index + len(target_word)
    final_text = text[:insert_index] + ' ' + sentence + text[insert_index:]
    return final_text


if __name__ == '__main__':
    my_text = '''  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



      it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



      last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

    whitespaces = count_whitespaces(my_text)
    normalized_text = normalize_text(my_text)
    new_sentence = create_sentence(normalized_text)
    final_text = insert_sentence(normalized_text, new_sentence, 'paragraph.')

    print(f'Number of whitespaces: {whitespaces}.\n')
    print(f'Normalized text:\n{normalized_text}\n')
    print(f'New sentence from last words is: {new_sentence}\n')
    print(f'The final output text is:\n{final_text}\n')
