import faker

fake = faker.Faker()

class Data:
    base_url = "http://localhost:8080"
    user_login = {
        "email": fake.email(),
        "password": fake.password(),
    }
    user_put = {
        "firstName": "Петр",
        "lastName": "Петров",
        "companyName": "ООО Рекламные технологии",
        "phoneNumber": "+79991234588"
    }
    db_config = {
        "host": "localhost",
        "database": "ad_aggregator_dev",
        "user": "postgres",
        "password": "postgres",
    }
    resource_data = {
        "name": "Мой блог",
        "type": "BLOG",
        "url": fake.url(),
        "description": "Блог о технологиях и программировании",
        "monthlyVisitors": 5000,
        "primaryLanguage": "ru",
        "primaryCountry": "RU",
        "contentCategories": ["Technology", "Programming", "Web"]
    }
    resource_put = {
        "name": "Обновленный блог",
        "description": "Блог о технологиях, программировании и дизайне",
        "monthlyVisitors": 7500,
        "primaryLanguage": "ru",
        "primaryCountry": "RU",
        "contentCategories": ["Technology", "Programming", "Web", "Design"]
    }
    integration_patch = {
        "status": "PAUSED",
        "isActive": 'false'
    }
    statistics_date = {
        "startDate": "2025-03-01",
        "endDate": "2025-03-01",
    }
    payment_withdrawal = {
        "amount": 50.00,
        "currency": "USD",
        "paymentMethod": "bank_transfer"
    }


