from django.shortcuts import render
from django.http import Http404

ALUNOS = [
    {
        "slug": "pedro-niob",
        "nome": "Pedro Niob",
        "curso": "Engenharia de Materiais",
        "descricao": "Alienígena infiltrado. Veio de outro planeta estudar a espécie humana e já entendeu tudo, menos por que a gente faz prova e almoça às 11h da manhã.",
    },
    {
        "slug": "luiza-dracula",
        "nome": "Luiza Drácula",
        "curso": "Engenharia Elétrica",
        "descricao": "Vampira de intercâmbio. Só assiste aula noturna e já virou cinza na terceira aula de laboratório com janela. Mesmo assim, sempre tira nota alta.",
    },
    {
        "slug": "carlos-do-futuro",
        "nome": "Carlos do Futuro",
        "curso": "Ciência da Computação",
        "descricao": "Viajante do tempo. Voltou de 2087 só para entregar o trabalho que esqueceu. Diz que o futuro é bom, mas que a mensalidade continua cara.",
    },
    {
        "slug": "bia-poltergeist",
        "nome": "Bia Poltergeist",
        "curso": "Arquitetura e Urbanismo",
        "descricao": "Fantasma com matrícula ativa. Morreu em 1987, mas se recusa a trancar o curso. Assombra a biblioteca e derruba o Wi-Fi dos colegas durante a prova.",
    },
    {
        "slug": "mario-fire",
        "nome": "Mario Fire",
        "curso": "Engenharia Química",
        "descricao": "Dragão disfarçado de gente. Usa casaco e chapéu para esconder as asas, e cada espirro queima um trabalho em grupo. Os professores fingem que não percebem.",
    },
]


def inicio(request):
    return render(request, "alunos/inicio.html")


def lista(request):
    return render(request, "alunos/lista.html", {"alunos": ALUNOS})


def detalhe(request, slug):
    for a in ALUNOS:
        if a["slug"] == slug:
            return render(request, "alunos/detalhe.html", {"aluno": a})
    raise Http404("Aluno não encontrado")