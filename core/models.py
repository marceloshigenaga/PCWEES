from django.db import models

from stdimage.models import StdImageField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.contrib.auth.models import User

class Topico_swebook_1(models.Model):
    nome = models.CharField('Tópico 1', max_length=200)

    def __str__(self):
        return self.nome

class Topico_swebook_2(models.Model):
    nome = models.CharField('Tópico 2', max_length=200)
    associacao = models.ForeignKey(Topico_swebook_1, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Topico_swebook_3(models.Model):
    nome = models.CharField('Tópico 3', max_length=200)
    associacao = models.ForeignKey(Topico_swebook_2, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Exemplo(models.Model):

    titulo = models.CharField('Título', max_length=200)
    topico_swebook_1 = models.ForeignKey(Topico_swebook_1, on_delete=models.SET_NULL, blank=True, null=True)
    topico_swebook_2 = models.ForeignKey(Topico_swebook_2, on_delete=models.SET_NULL, blank=True, null=True)
    topico_swebook_3 = models.ForeignKey(Topico_swebook_3, on_delete=models.SET_NULL, blank=True, null=True)
    outros_topicos = models.CharField('Outros Tópicos', max_length=200, null=True, blank=True)
    tag_1 = models.CharField('Tag 1', max_length=200, null=True, blank=True)
    tag_2 = models.CharField('Tag 2', max_length=200, null=True, blank=True)
    tag_3 = models.CharField('Tag 3', max_length=200, null=True, blank=True)
    conhecimento_previo_ou_restricoes = models.TextField('Conhecimento Prévio e Restrições de Uso', null=True, blank=True)
    sugestores_de_uso = models.TextField('Sugestões de Uso', null=True, blank=True)

    projeto_nome = models.CharField('Nome do projeto', max_length=200, null=True, blank=True)
    projeto_descricao = models.TextField('Descrição do Projeto', null=True, blank=True)
    projeto_linguagem_programacao = models.CharField('Linguagem de Programação', max_length=200, null=True, blank=True)
    projeto_link = models.CharField('Link do Projeto', max_length=200, null=True, blank=True)
    projeto_link_exemplo = models.CharField('Link do Exemplo', max_length=200, null=True, blank=True)
    projeto_data_extracao_exemplo = models.DateField(null=True, blank=True)

    exemplo_descicao_conceitual_problema = models.TextField('Descrição Conceitual do Problema', null=True, blank=True)
    exemplo_ocorrencia_problema = models.TextField('Ocorrência do Problema no Projeto', null=True, blank=True)
    exemplo_imagem_problema = StdImageField('Imagem para demonstrar o contexto', upload_to='IMG-exemplos', null=True, blank=True)
    exemplo_descricao_solucao = models.TextField('Descrição da Solução e Etapas da Solução')
    exemplo_imagem_solucao = StdImageField('Imagem para demonstrar as etapas de solução', upload_to='IMG-exemplos', null=True, blank=True)
    exemplo_resultado = models.TextField('Resultado', null=True, blank=True)
    exemplo_imagem_resultado = StdImageField('Imagem para demonstrar um resultado', upload_to='IMG-exemplos', null=True, blank=True)
    exemplo_material_complementar = models.TextField('Material Complementar', null=True, blank=True)

class Avaliacao(models.Model):
    avaliacao = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField('Comentário', null=True, blank=True)
    exemplo = models.ForeignKey(Exemplo, on_delete=models.CASCADE)
    avaliador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'