from django.urls import path
from .views import PolishBankListCreateView
from .views import PolishBankPredictView

urlpatterns = [
    path('polishbank/', PolishBankListCreateView.as_view(), name='polish-bank-list-create'),
    path('predict/', PolishBankPredictView.as_view(), name='polishbank-predict'),
    # Add more URLs as needed
]
