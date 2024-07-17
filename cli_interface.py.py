from create_database import create_tables, insert_products, insert_customers, insert_orders
from sql_queries import (get_total_sales, get_order_count_per_customer,
                         get_average_order_value, get_most_popular_category,
                         get_product_count_per_category, update_smartphone_prices)


def user_interface():
    while True:
        print("\n1. Додати продукти")
        print("2. Додати клієнтів")
        print("3. Додати замовлення")
        print("4. Показати сумарний обсяг продажів")
        print("5. Показати кількість замовлень на кожного клієнта")
        print("6. Розрахувати середній чек замовлення")
        print("7. Знайти найбільш популярну категорію товарів")
        print("8. Показати загальну кількість товарів кожної категорії")
        print("9. Оновити ціни на смартфони")
        print("10. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            insert_products()
            print("Продукти додані.")
        elif choice == '2':
            insert_customers()
            print("Клієнти додані.")
        elif choice == '3':
            insert_orders()
            print("Замовлення додані.")
        elif choice == '4':
            total_sales = get_total_sales()
            print(f"Сумарний обсяг продажів: {total_sales}")
        elif choice == '5':
            orders_per_customer = get_order_count_per_customer()
            for customer in orders_per_customer:
                print(f"{customer[0]} {customer[1]}: {customer[2]} замовлень")
        elif choice == '6':
            avg_order_value = get_average_order_value()
            print(f"Середній чек замовлення: {avg_order_value}")
        elif choice == '7':
            most_popular_category = get_most_popular_category()
            print(f"Найбільш популярна категорія товарів: {most_popular_category}")
        elif choice == '8':
            product_count_per_category = get_product_count_per_category()
            for category in product_count_per_category:
                print(f"{category[0]}: {category[1]} товарів")
        elif choice == '9':
            update_smartphone_prices()
            print("Ціни на смартфони оновлені.")
        elif choice == '10':
            break
        else:
            print("Невідома опція, спробуйте ще раз.")


if __name__ == '__main__':
    create_tables()
    user_interface()
