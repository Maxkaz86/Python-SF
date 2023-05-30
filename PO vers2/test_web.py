from pages.catalog_page import Catalog
from pages.product_page import ProductPage


def test_view_product_card(browser):
    catalog = Catalog(browser)
    products = ProductPage(browser)
    catalog.go_to_site()
    name_prod = catalog.get_product_name()
    catalog.click_to_product_name()
    name_prod2 = products.get_product_name()
    assert name_prod == name_prod2

