from __future__ import division
from preprocessing import text_preprocessing
from feature_extraction import tf_idf
from xlsx_handling import read_dataset
import math
import numpy as np



def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


def main():
    # locate and load the dataset
    dataset_loc = "./Dataset AlQuran Multilabel.xlsx"
    dataset = read_dataset(dataset_loc)[:200]

    # select coloumn terjemahan from dataset
    en_verses = [row[3] for row in dataset]

    # preprocessing phase
    preprocessed_text = [text_preprocessing(verse) for verse in en_verses]

    # tfidf phase
    tfidf_matrix, vocab = tf_idf(preprocessed_text[:200])

    k_fold = 5
    pnn = 4

    tfidf_matrix_split = chunkIt(tfidf_matrix, k_fold)
    print tfidf_matrix_split
    print len(tfidf_matrix_split)

    akurasi = []
    count_all_hamming = 0

    for i in range(k_fold) :

        print ( "Fold -", i + 1 )
        selisih = 0
        count_test = 0
        for i_label in range(4,20) :
            test = []
            train = []

            target_train = []
            target_test = []
            target_actual = []

            label = [row[i_label] for row in dataset]
            label_split = chunkIt(label, k_fold)


            for j in range(len(tfidf_matrix_split)) :
                if j == i :
                    test.extend(tfidf_matrix_split[j])
                    target_test.extend(label_split[j])
                else :
                    train.extend(tfidf_matrix_split[j])
                    target_train.extend(label_split[j])


    #
            count_test = len(test)
            print ( "Label -", i_label -3)
            target_output = []

            for a in range(len(test)):
                jarak = []
                for b in range(len(train)) :

                    jarak.append(math.sqrt(sum(np.subtract(np.array(test[a]), np.array(train[b]))**2)))

                print len(jarak)

                jarakKlas = []
                for b in range(2) : #[0,1]
                    tmp_jarakKlas = []
                    value_a = []
                    for c in range(len(jarak)) :
                        if target_train[c] == b :
                            tmp_jarakKlas.append(jarak[c])
                    tmp_jarakKlas.sort()
                    value_a.sort()
                    for line in tmp_jarakKlas[:pnn]:
                        jarakKlas.append([b, line])

                b = {}
                for x in jarakKlas: b.setdefault(x[0], []).append(x[1])



                avgDict = {}
                x = 1
                for k, v in b.items():
                    avgDict[k] = sum((1.0 / i) * g for i, g in enumerate(v, 1))
                    x += 1


                min_index, min_value = min(avgDict.items(), key=lambda x: x[1]) #untuk mendapatkan min. index
                target_actual.append(min_index)


            for y in range(len(target_test)):
                if target_actual[y]!= target_test[y]:
                    selisih+=1



        print selisih
        print count_test
        nilai = count_test*16
        hamming_loss = (float(1/(nilai)) * selisih)
        print("hamming_loss :",hamming_loss)
        count_all_hamming += hamming_loss
        print("")


    print "hasil Hamming Keseluruhan"
    avg_hamming = count_all_hamming/k_fold
    print avg_hamming
main()

