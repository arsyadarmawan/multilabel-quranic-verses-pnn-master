from preprocessing import text_preprocessing
from feature_extraction import tf_idf
from xlsx_handling import read_dataset, write_data

# It is only preprocessing and feature extraction! (temporary)
def main():
    # locate and load the dataset
    dataset_loc = "Dataset/Dataset AlQuran Multilabel.xlsx"
    dataset = read_dataset(dataset_loc)[:100]

    # select coloumn terjemahan from dataset
    en_verses = [row[3] for row in dataset]

    # preprocessing phase
    preprocessed_text = [text_preprocessing(verse) for verse in en_verses]

    # tfidf phase
    tfidf_matrix = tf_idf(preprocessed_text)

    # locate and write tfidf matrix
    output_loc = "Output/test_output.xlsx"
    write_data(output_loc, tfidf_matrix)

if __name__ == "__main__":
    main()