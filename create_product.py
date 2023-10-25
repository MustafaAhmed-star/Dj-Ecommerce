def main():
    fake: Faker = Faker() 
    
    product_names = ["T-shirt", "Jeans", "Sneakers", "Jacket", "Hat", "Socks", "Backpack", "Sweater", "Dress", "Skirt"]
    for _ in range(5):
        products =Product.objects.create(
            name=random.choice(product_names),
            price=random.uniform(100, 1000)
        )
        print(f"Created product. Name: {products.name}")
    task_count = Product.objects.count()

    print(f"There are {task_count} todos in the database")

    
 
if __name__ == "__main__":
    import os
 
    from django.core.wsgi import get_wsgi_application
 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    application = get_wsgi_application()
    import random
    from faker import Faker
    from store.models import Product
 
    main()