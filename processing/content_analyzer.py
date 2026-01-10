
def seperate_content_types(chunk):
    """
    Separates text, tables, and images from a given chunk.

    Args:
        chunk: The chunk object containing text and metadata.

    Returns:
        A dictionary with keys 'text', 'tables', 'images', and 'types'.
    """

    content_data = {
        "text": chunk.text,
        "tables": [],
        "images": [],
        "types": ["text"]
    }

    if hasattr(chunk, "metadata") and hasattr(chunk.metadata, "orig_elements"):
        for element in chunk.metadata.orig_elements:
            element_type = type(element).__name__

            if element_type == "Table":
                content_data["types"].append("table")
                table_html = getattr(element.metadata, "text_as_html", element.text)
                content_data["tables"].append(table_html)

            elif element_type == "Image":
                if hasattr(element.metadata, "image_base64"):
                    content_data["types"].append("image")
                    content_data["images"].append(element.metadata.image_base64)

    content_data["types"] = list(set(content_data["types"]))
    return content_data
