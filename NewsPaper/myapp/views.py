# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # импортируем класс получения деталей объекта
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.shortcuts import render
from django.views import View # импортируем простую вьюшку
from .models import Post
from .filters import PostFilter # импортируем недавно написанный фильтр
from .forms import PostForm # импортируем нашу форму
 
class PostList(ListView):

    model = Post  
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-creation_date']
    paginate_by = 10 # поставим постраничный вывод в один элемент
    form_class = PostForm

    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        return context    

# # создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'article.html' # название шаблона будет product.html
    context_object_name = 'article' # название объекта

class SearchList(ListView):

    model = Post  
    template_name = 'search.html'
    context_object_name = 'search'
    ordering = ['-creation_date']

    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        return context 

class Search(View):

    def get(self, request):
        search = Post.objects.order_by('-creation_date')
        p = Paginator(search, 1) # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы

        search = p.get_page(request.GET.get('page', 1)) # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами

        data = {
            'search': search,
        }
        return render(request, 'search.html', data)

class PostAdd(CreateView):
    template_name = 'add.html'
    form_class = PostForm

class PostEdit(UpdateView):
    model = Post
    template_name = 'edit.html'
    form_class = PostForm

class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url ="/news"