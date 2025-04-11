import codecs

from sklearn.feature_extraction.text import TfidfVectorizer


def get_tf_idf(file_path):
    try:
        with codecs.open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except UnicodeDecodeError:
        with codecs.open(file_path, 'r', encoding='cp1251') as file:
            text = file.read()

    vectorizer = TfidfVectorizer(
        use_idf=True,
        norm=None,
        smooth_idf=False
    )

    tfidf_matrix = vectorizer.fit_transform([text])

    terms = vectorizer.get_feature_names_out()

    tf = vectorizer.transform([text]).toarray()[0]
    idf = vectorizer.idf_
    tfidf = tfidf_matrix.toarray()[0]

    tf_dict = {term: tf_val for term, tf_val in zip(terms, tf)}
    idf_dict = {term: idf_val for term, idf_val in zip(terms, idf)}
    tfidf_dict = {term: tfidf_val for term, tfidf_val in zip(terms, tfidf)}

    return tf_dict, idf_dict, tfidf_dict
