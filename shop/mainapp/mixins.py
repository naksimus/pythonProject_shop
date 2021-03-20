from django.views.generic import View

from .models import Cart, Customer, Product, Category


class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                customer = Customer.objects.create(
                    user=request.user
                )
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
        else:
            cart = Cart.objects.filter(for_anonymous_user=True).first()
            if not cart:
                cart = Cart.objects.create(for_anonymous_user=True)
        self.cart = cart

        return super().dispatch(request, *args, **kwargs)




class ProductMixin(View):

    def dispatch(self, request, *args, **kwargs):
        product  = Product.objects.all().order_by('-id')
        self.product = product
        return super().dispatch(request, *args, **kwargs)

class ProductCategoryMixin(View):

    def dispatch(self, request, *args, **kwargs):
        category = Category.objects.all()
        self.category = category
        return super().dispatch(request, *args, **kwargs)


