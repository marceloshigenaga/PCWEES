from django.db import models
from stdimage.models import StdImageField
from django.conf import settings

class Topico_swebook_1(models.Model):
    nome = models.CharField('Tópico 1', max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tópico SWEBOOK 1'
        verbose_name_plural = 'Tópicos SWEBOOK 1'

class Topico_swebook_2(models.Model):
    nome = models.CharField('Tópico 2', max_length=200)
    associacao = models.ForeignKey(Topico_swebook_1, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tópico SWEBOOK 2'
        verbose_name_plural = 'Tópicos SWEBOOK 2'

class Topico_swebook_3(models.Model):
    nome = models.CharField('Tópico 3', max_length=200)
    associacao = models.ForeignKey(Topico_swebook_2, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tópico SWEBOOK 3'
        verbose_name_plural = 'Tópicos SWEBOOK 3'


class Exemplo(models.Model):
    titulo = models.CharField('Título', max_length=200)
    topico_swebook_1 = models.ForeignKey(Topico_swebook_1, on_delete=models.RESTRICT)
    topico_swebook_2 = models.ForeignKey(Topico_swebook_2, on_delete=models.RESTRICT)
    topico_swebook_3 = models.ForeignKey(Topico_swebook_3, on_delete=models.RESTRICT)
    outros_topicos = models.CharField('Outros Tópicos', max_length=200, null=True, blank=True)
    tag_1 = models.CharField('Tag 1', max_length=200, null=True, blank=True)
    tag_2 = models.CharField('Tag 2', max_length=200, null=True, blank=True)
    tag_3 = models.CharField('Tag 3', max_length=200, null=True, blank=True)
    conhecimento_previo_ou_restricoes = models.TextField('Conhecimento Prévio e Restrições de Uso')
    sugestores_de_uso = models.TextField('Sugestões de Uso')

    projeto_nome = models.CharField('Nome do projeto', max_length=200)
    projeto_descricao = models.TextField('Descrição do Projeto')
    projeto_linguagem_programacao = models.CharField('Linguagem de Programação', max_length=200)
    projeto_link = models.CharField('Link do Projeto', max_length=200)
    projeto_link_exemplo = models.CharField('Link do Exemplo', max_length=200)
    projeto_data_extracao_exemplo = models.DateField()

    exemplo_descicao_conceitual_problema = models.TextField('Descrição Conceitual do Problema')
    exemplo_ocorrencia_problema = models.TextField('Ocorrência do Problema no Projeto')
    exemplo_imagem_problema = StdImageField('Imagem para demonstrar o contexto', upload_to='IMG-exemplos', null=True, blank=True)
    exemplo_descricao_solucao = models.TextField('Descrição da Solução e Etapas da Solução')
    exemplo_imagem_solucao = StdImageField('Imagem para demonstrar as etapas de solução', upload_to='IMG-exemplos', null=True, blank=True)
    exemplo_resultado = models.TextField('Resultado')
    exemplo_imagem_resultado = StdImageField('Imagem para demonstrar um resultado', upload_to='IMG-exemplos', null=True, blank=True)
    exemplo_material_complementar = models.TextField('Material Complementar', null=True, blank=True)

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return self.titulo

class Avaliacao(models.Model):
    NOTAS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    avaliacao = models.PositiveIntegerField(choices=NOTAS)
    comentario = models.TextField('Comentário', null=True, blank=True)
    exemplo = models.ForeignKey(Exemplo, on_delete=models.CASCADE)
    avaliador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'