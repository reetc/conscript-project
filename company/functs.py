import gensim
#print(dir(gensim))
from nltk import tokenize
import os
from conscript import settings


def answer_relevance(request):
    file_path = os.path.join(settings.BASE_DIR, 'company', 'static','modelanswer.txt')

    # file1 = open("static/modelanswer.txt","r")
    file1 = open(file_path,"r")
    p=file1.read()
    # print("****************Model Answer******************")
    # print(p)

    #p="Web development broadly refers to the tasks associated with developing websites for hosting via intranet or internet. The web development process includes web design, web content development, client-side/server-side scripting and network security configuration, among other tasks."
    raw_documents=tokenize.sent_tokenize(p)
    #print(raw_documents)



    #print("Number of documents:",len(raw_documents))
    from nltk.tokenize import word_tokenize
    gen_docs = [[w.lower() for w in word_tokenize(text)]
                for text in raw_documents]
    #print(gen_docs)

    dictionary = gensim.corpora.Dictionary(gen_docs)
    """
    print(dictionary[5])
    #print(dictionary.token2id['web'])
    #print("Number of words in dictionary:",len(dictionary))
    for i in range(len(dictionary)):
        print(i, dictionary[i])
    """
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    #print(corpus)

    tf_idf = gensim.models.TfidfModel(corpus)
    #print(tf_idf)
    s = 0
    for i in corpus:
        s += len(i)
    #print(s)


    sims = gensim.similarities.Similarity('static',tf_idf[corpus],
                                          num_features=len(dictionary))
    #print(sims)
    #print(type(sims))


    file_path = os.path.join(settings.BASE_DIR, 'company', 'static','answer1.txt')

    file2 = open(file_path,"r")
    p2=file2.read()
    print("****************  Given Answer 1  ******************")
    print(p2)



    query_doc = [w.lower() for w in word_tokenize(p2)]
    #print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    #print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    #print(query_doc_tf_idf)
    array=sims[query_doc_tf_idf]
    sum=0.0

    for i in array:
        print(i)
        sum=sum+i

    print("Final Similarity Index: ",(sum/(len(raw_documents))))





    file_path = os.path.join(settings.BASE_DIR, 'company', 'static','answer2.txt')

    file3 = open(file_path,"r")
    p3=file3.read()
    print("****************  Given Answer 2   ******************")
    print(p3)



    query_doc2 = [w.lower() for w in word_tokenize(p3)]
    #print(query_doc)
    query_doc_bow2 = dictionary.doc2bow(query_doc2)
    #print(query_doc_bow)
    query_doc_tf_idf2 = tf_idf[query_doc_bow2]
    #print(query_doc_tf_idf)
    array2=sims[query_doc_tf_idf2]
    sum=0.0

    for i in array2:
        print(i)
        sum=sum+i

    print("Final Similarity Index: ",(sum/(len(raw_documents))))
    file1.close()
    file2.close()
    file3.close()
    return((sum/(len(raw_documents))))
