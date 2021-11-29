from django import forms
from .models import Exemplo, Avaliacao
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class ExemploForm(forms.ModelForm):
    class Meta:
        model = Exemplo
        fields = '__all__'
        exclude = ('autor',)
        labels = {
            "tag_1": "Tags - Atributos técnicos ou pedagógicos (Opcional)<hr>Tag 1",
            "topico_swebook_1": "Tópicos SWEBOOK<hr>Tópico 1",
            "topico_swebook_2": "Tópico 2",
            "topico_swebook_3": "Tópico 3",
            "exemplo_imagem_problema":
                "Você pode adicionar uma imagem para demonstrar o contexto do problema abordado, e citá-la no texto, caso seja necessário.",
            "exemplo_imagem_solucao": "Você pode adicionar uma imagem para demonstrar as etapas de solução, e citá-la no texto, caso necessário.",
            "exemplo_imagem_resultado" : "Você pode adicionar uma imagem para demonstrar um resultado, e citá-la no texto, caso necessário."

        }

    def __init__(self, *args, **kwargs):
        super(ExemploForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs['placeholder'] = 'Título do exemplo'
        self.fields['outros_topicos'].widget.attrs[
            'placeholder'] = 'Informe outras subareas nas quais o exemplo possa estar contido, caso existam.'
        self.fields['conhecimento_previo_ou_restricoes'].widget.attrs[
            'placeholder'] = 'Informe pré-requisitos necessários para o entendimento do worked example, ou possíveis restrições de uso.'
        self.fields['titulo'].widget.attrs[
            'placeholder'] = 'Apresentar informações sobre como usar, quando usar, e com quem usar o worked example.'
        self.fields['sugestores_de_uso'].widget.attrs[
            'placeholder'] = 'Apresentar informações sobre como usar, quando usar, e com quem usar o worked example.'
        self.fields['projeto_nome'].widget.attrs['placeholder'] = 'Nome do projeto de software livre do qual o exemplo foi extraído'
        self.fields['projeto_descricao'].widget.attrs[
            'placeholder'] = 'Breve descrição do escopo do projeto'
        self.fields['projeto_linguagem_programacao'].widget.attrs[
            'placeholder'] = 'Linguagem de programação na qual o projeto foi implementado'
        self.fields['projeto_link'].widget.attrs[
            'placeholder'] = 'Link para o repositório do projeto'
        self.fields['projeto_link_exemplo'].widget.attrs[
            'placeholder'] = 'Link para o local de onde o exemplo foi retirado do projeto'
        self.fields['projeto_data_extracao_exemplo'].widget.attrs[
            'placeholder'] = 'dd/mm/aaaa'
        self.fields['exemplo_descicao_conceitual_problema'].widget.attrs[
            'placeholder'] = 'Explicar conceitualmente o problema que será abordado no exemplo.'
        self.fields['exemplo_ocorrencia_problema'].widget.attrs[
            'placeholder'] = 'Explicar o contexto no qual o problema abordado no exemplo está aplicado no projeto.'
        self.fields['exemplo_descricao_solucao'].widget.attrs[
            'placeholder'] = 'Passos para a resolução do problema'
        self.fields['exemplo_resultado'].widget.attrs[
            'placeholder'] = 'Resultado gerado a partir etapas de solução do problema.'
        self.fields['exemplo_material_complementar'].widget.attrs[
            'placeholder'] = 'Indicar materiais que possam ser complementares ao estudo do exemplo, caso existam.'

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = '__all__'
        exclude = ('exemplo','avaliador')

        labels = {
            "avaliacao": "Nota da avaliação:",
        }

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=150)
    group = forms.ModelChoiceField(queryset=Group.objects.exclude(name='Professor Validado'),
                                   required=True, label='Tipo de usuário')

    class Meta:
        model = User
        fields = ['username','first_name','last_name','group', 'email', 'password1', 'password2']















