from unstructured.partition.pdf import partition_pdf

def partition_documents(file_path: str):
    print(f"Partitioning document: {file_path}")

    elements = partition_pdf(
        filename=file_path,
        strategy="hi_res",
        infer_table_structure=True,
        extract_image_block_types=["Image"],
        extract_image_block_to_payload=True,    # convert image to base64 format
    )

    print(f"✅ Extracted {len(elements)} elements")
    return elements
