# from preprocessing import text_preprocessing
# from feature_extraction import tf_idf
from xlsx_handling import read_dataset, write_data

def main():
    # locate and load the dataset
    dataset_loc = "Dataset/Dataset AlQuran Multilabel.xlsx"
    dataset = read_dataset(dataset_loc)

    # select coloumn terjemahan from dataset
    en_verses = [row[4] for row in dataset]
    return en_verses

    # preprocessing phase
    preprocessed_text = [text_preprocessing(verse) for verse in en_verses]

    # tfidf phase
    tfidf_matrix = tf_idf(preprocessed_text)

    # locate and write tfidf matrix
    output_loc = "Output/tfidf_matrix.xlsx"
    write_data(output_loc, tfidf_matrix)
    #
    dataset = read_dataset(output_loc)



if __name__ == "__main__":
    main()
