from __future__ import division
from xlsx_handling import loadCsv, read_dataset
from Classifier import *
import math
import numpy as np

def main():
    matrix_loc = "Output/tfidf_matrix.csv"
    label_loc = "Dataset/Dataset AlQuran Multilabel.xlsx"
    dataset_matrix = loadCsv(matrix_loc)[:100]
    dataset_label = read_dataset(label_loc)[:100]

    k_fold = 5
    pnn = 10


    matrix_split = validation(dataset_matrix, k_fold)
    count_all_hamming = 0
    hamming = []

    for x in range(k_fold):
        print ("Fold -", x + 1)
        selisih = 0
        count_test = 0
        for i in range(4,20):

            test = []
            train = []
            target_train = []
            target_test = []
            target_actual = []

            label = [row[i] for row in dataset_label]
            label_split = validation(label, k_fold)


            for j in range(len(matrix_split)):
                if j == x :
                    test.extend(matrix_split[j])
                    target_test.extend(label_split[j])
                else :
                    train.extend(matrix_split[j])
                    target_train.extend(label_split[j])

            count_test = len(test)
            print ("Label -", i - 3)

            length = len(train)

            for a in range(len(test)):
                simm_euclid = []
                for b in range(len(train)):
                    simm_euclid.append(pearson_correlation(test[a], train[b]))


                neighbour = get_neighbourhood(simm_euclid, target_train, pnn)
                target_actual.append(neighbour[0])

                if neighbour[0] != target_test[a]:
                    selisih += 1

        hamming_fold = hammingloss(selisih, len(test))
        print hamming_fold
        hamming.append(hamming_fold)

    print "sistem secara keseluruhan"
    count_all_hamming = float(sum(hamming)/k_fold)
    print count_all_hamming
main()