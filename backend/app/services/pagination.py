from sqlalchemy.orm import Query


def paginate(query: Query, page: int = 1, page_size: int = 10):
    if page < 1:
        page = 1

    if page_size < 1 or page_size > 100:
        page_size = 10

    total = query.count()

    items = (
        query
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return items, total
