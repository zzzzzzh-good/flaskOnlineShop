import json
import os
from app import create_app, db
from app.models import Product

app = create_app()

def create_fake_data():
    if Product.query.first() is None:
        json_path = os.path.join(os.path.dirname(__file__), 'data', 'products.json')
        with open(json_path, encoding='utf-8') as f:
            items = json.load(f)
        products = [Product(**item) for item in items]
        db.session.add_all(products)
        db.session.commit()
        print(f"初始化测试商品数据完成，共 {len(products)} 件。")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_fake_data()
    app.run(debug=True, host='0.0.0.0', port=5000)
