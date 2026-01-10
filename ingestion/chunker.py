from unstructured.chunking.title import chunk_by_title

def create_chunks_by_title(elements):
    chunks = chunk_by_title(
        elements=elements,
        max_characters=3000,
        new_after_n_chars=2400,
        combine_text_under_n_chars=500
    )

    print(f"Number of chunks: {len(chunks)}")
    return chunks
