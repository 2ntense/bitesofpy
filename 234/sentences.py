import io


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""

    with io.StringIO() as stream:
        first_letter = True
        for c in text:
            to_write = c
            if c in ".?!":
                first_letter = True
            elif first_letter and c.isalpha():
                to_write = c.upper()
                first_letter = False
            stream.write(to_write)
        return stream.getvalue()
