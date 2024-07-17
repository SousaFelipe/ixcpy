import math
from typing import Callable
from ixcpy import Connection, Query


def load_source(connection: Connection, args: list[str]) -> list:
    source: list = []

    for arg in args:
        query = Query(arg=arg)
        connection.where(query=query)

    page_number: int = 1
    page_source = connection.many(page=page_number)

    if page_source.total() > 0:
        page_total = math.ceil(page_source.total() / 20)

        for record in page_source.records():
            source.append(record)

        while page_number < page_total:
            page_source = connection.many(page=page_number + 1)
            for record in page_source.records():
                source.append(record)
            page_number += 1

    return source


def append_source(
        src: list,
        new_key: str,
        parser: Callable[[int], str]) -> list:
    
    for i, s in enumerate(src):
        s[new_key] = parser(i)
    
    return src


def merge_source(
        src: list,
        merge: list,
        search: str,
        replace: str) -> list:
    
    for i, s in enumerate(src):
        for m in merge:
            if 'id' in m and m['id'] == s[search]:
                s[replace] = m[replace]
                break

    return src
