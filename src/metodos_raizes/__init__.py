"""Pacote com métodos numéricos para determinação de raízes."""
from .metodos import bissecao, posicao_falsa, ponto_fixo, secante, newton_raphson
from .problema import f, df, g

__all__ = ["bissecao", "posicao_falsa", "ponto_fixo", "secante",
           "newton_raphson", "f", "df", "g"]
