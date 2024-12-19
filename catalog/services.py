from catalog.models import Product


def get_products_from_category(category_id):
    """
    Получает список продуктов заданной категории.
    """
    products = Product.objects.filter(category=category_id)
    return products
