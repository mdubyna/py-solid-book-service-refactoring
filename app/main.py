from app.book_service.book import Book
from app.book_service.display_types import (
    DisplayProcessor,
    ConsoleDisplayProcessor,
    ReverseDisplayProcessor

)
from app.book_service.print_book_types import (
    PrintProcessor,
    ConsolePrintProcessor,
    ReversePrintProcessor
)
from app.book_service.serializers import (
    SerializeProcessor,
    JSONSerializeProcessor,
    XMLSerializeProcessor
)


def create_display_processor(display_type: str) -> DisplayProcessor:
    if display_type == "console":
        return ConsoleDisplayProcessor()
    elif display_type == "reverse":
        return ReverseDisplayProcessor()
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def create_print_processor(print_type: str) -> PrintProcessor:
    if print_type == "console":
        return ConsolePrintProcessor()
    elif print_type == "reverse":
        return ReversePrintProcessor()
    else:
        raise ValueError(f"Unknown print type: {print_type}")


def create_serialize_processor(serialize_type: str) -> SerializeProcessor:
    if serialize_type == "json":
        return JSONSerializeProcessor()
    elif serialize_type == "xml":
        return XMLSerializeProcessor()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_processor = create_display_processor(method_type)
            display_processor.display(
                content=book.content
            )
        elif cmd == "print":
            print_processor = create_print_processor(method_type)
            print_processor.print_book(
                title=book.title,
                content=book.content
            )
        elif cmd == "serialize":
            serialize_processor = create_serialize_processor(method_type)
            return serialize_processor.serialize(
                title=book.title,
                content=book.content
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
