from django.urls import pathfrom .views.cart import ShowCartView, AddItemCartView, RemoveItemCartViewfrom .views.item import ItemViewfrom .views.payment import (	CreateCheckoutSessionView, SuccessView, CancelView, StripeWebHook, CreateCheckoutCartView,	StripeIntentView, )urlpatterns = [	path('cart/', ShowCartView.as_view(), name='cart'),	path('cart/checkout/', CreateCheckoutCartView.as_view(), name='checkout-cart'),	path('cart/remove/<int:pk>', RemoveItemCartView.as_view(), name='remove-cart'),	path('cart/add/<int:pk>', AddItemCartView.as_view(), name='add-cart'),	path('item/<int:pk>/', ItemView.as_view(), name='item'),	path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy-item'),	path('buy/success/', SuccessView.as_view(), name='buy-success'),	path('buy/cancel/', CancelView.as_view(), name='buy-cancel'),	path('buy/intent/<int:pk>', StripeIntentView.as_view(), name='buy-intent'),	path('webhooks/stripe/', StripeWebHook.as_view(), name='stripe-webhook'),]