from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user
from .. import db
from ..models import Product, Comment

shop = Blueprint('shop', __name__)

@shop.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@shop.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        if not current_user.is_authenticated:
            flash('请先登录后再评论', 'warning')
            return redirect(url_for('auth.login'))

        content = request.form.get('content')
        if content:
            comment = Comment(content=content, user_id=current_user.id, product_id=product.id)
            db.session.add(comment)
            db.session.commit()
            flash('评论发表成功！', 'success')
            return redirect(url_for('shop.product_detail', product_id=product.id))

    return render_template('product.html', product=product)
