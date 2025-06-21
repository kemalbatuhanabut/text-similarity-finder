import os
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def read_text_files(folder):
    files = []
    contents = []
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if os.path.isfile(full_path) and filename.endswith(('.txt', '.md')):
            with open(full_path, encoding='utf-8') as f:
                content = f.read()
                files.append(filename)
                contents.append(content)
    return files, contents

def compute_similarity_matrix(docs):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(docs)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

def find_similar_pairs(files, similarity_matrix, threshold):
    n = len(files)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            similarity = similarity_matrix[i, j]
            if similarity >= threshold:
                pairs.append((files[i], files[j], similarity))
    return sorted(pairs, key=lambda x: -x[2])

def main():
    parser = argparse.ArgumentParser(description="Find near-duplicate text files in a folder using TF-IDF & Cosine Similarity.")
    parser.add_argument("folder", help="Path to the folder containing text files (.txt or .md)")
    parser.add_argument("--threshold", type=float, default=0.8, help="Similarity threshold (default: 0.8)")
    args = parser.parse_args()

    print(f"Scanning folder: {args.folder}")
    files, contents = read_text_files(args.folder)

    if len(files) < 2:
        print("Not enough text files to compare.")
        return

    print(f"Found {len(files)} text files. Calculating similarities...")

    similarity_matrix = compute_similarity_matrix(contents)
    similar_pairs = find_similar_pairs(files, similarity_matrix, args.threshold)

    if similar_pairs:
        print("\nSimilar file pairs (above threshold):\n")
        for file1, file2, score in similar_pairs:
            print(f"{file1} <--> {file2} | Similarity: {score:.3f}")
    else:
        print("No similar file pairs found above the given threshold.")

if __name__ == "__main__":
    main()
