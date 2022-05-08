import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


#fixture para ser usada nas classes abaixo
@pytest.fixture
def home_response(client):
    return client.get(reverse("pages:home"))


@pytest.fixture
def about_response(client):
    return client.get(reverse("pages:about"))

#Classe TestHomePageView: verifica o vai e vem das urls.#
#definindo as funções, test_reverse_resolve: verifica se a view #pages:home retorna "/" (pagina da raiz) e se quando acessamos a raiz"/"" teremos a pages:home, e função test_status_code passando como argumento a fixture home_response mostra o código retornado pelo servidor que deverá ser 200, e função test_template que verifica se o acesso ao template está correto.  

#Classe TestAboutView: tem a mesma operação da classe TestHomePageView para a url home e template home.html.#

class TestHomePageView:
    def test_reverse_resolve(self):
        assert reverse("pages:home") == "/"
        assert resolve("/").view_name == "pages:home"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, "home.html")


class TestAboutView:
    def test_reverse_resolve(self):
        assert reverse("pages:about") == "/about/"
        assert resolve("/about/").view_name == "pages:about"

    def test_status_code(self, about_response):
        assert about_response.status_code == 200

    def test_template(self, about_response):
        assertTemplateUsed(about_response, "about.html")