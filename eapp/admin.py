from flask_admin import Admin
from eapp import app, db
from flask_admin.contrib.sqla import ModelView
from eapp.models import Category, Product


admin = Admin(app=app, name='eCommerce Admin')

class ProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['id', 'name', 'price']
    edit_modal = True
    column_editable_list = ['name']
    can_view_details = True
    details_modal = True

admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))