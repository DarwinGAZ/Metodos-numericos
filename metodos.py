"""Implementações próprias dos métodos. Cada função retorna (raiz, historico),
onde historico é uma lista de dicionários (uma entrada por iteração).

Critério de parada: |x_{k+1} - x_k| < tol  (ou b - a < tol nos intervalares)
limitado a max_iter iterações.
"""


def bissecao(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos.")
    hist = []
    for k in range(1, max_iter + 1):
        x = (a + b) / 2
        fx = f(x)
        hist.append({"k": k, "a": a, "b": b, "x": x, "f(x)": fx, "erro": b - a})
        if (b - a) / 2 < tol:
            break
        if f(a) * fx < 0:
            b = x
        else:
            a = x
    return x, hist


def posicao_falsa(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos.")
    hist, x_ant = [], a
    for k in range(1, max_iter + 1):
        fa, fb = f(a), f(b)
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)
        erro = abs(x - x_ant)
        hist.append({"k": k, "a": a, "b": b, "x": x, "f(x)": fx, "erro": erro})
        if erro < tol:
            break
        if fa * fx < 0:
            b = x
        else:
            a = x
        x_ant = x
    return x, hist


def ponto_fixo(g, x0, tol=1e-6, max_iter=100):
    hist, x = [], x0
    for k in range(1, max_iter + 1):
        x_novo = g(x)
        erro = abs(x_novo - x)
        hist.append({"k": k, "x": x_novo, "erro": erro})
        x = x_novo
        if erro < tol:
            break
    return x, hist


def secante(f, x0, x1, tol=1e-6, max_iter=100):
    hist = []
    for k in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)
        if f1 == f0:
            raise ZeroDivisionError("f(x_k) = f(x_{k-1}); método falhou.")
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        erro = abs(x2 - x1)
        hist.append({"k": k, "x": x2, "f(x)": f(x2), "erro": erro})
        x0, x1 = x1, x2
        if erro < tol:
            break
    return x1, hist


def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    hist, x = [], x0
    for k in range(1, max_iter + 1):
        d = df(x)
        if d == 0:
            raise ZeroDivisionError("Derivada nula.")
        x_novo = x - f(x) / d
        erro = abs(x_novo - x)
        hist.append({"k": k, "x": x_novo, "f(x)": f(x_novo), "erro": erro})
        x = x_novo
        if erro < tol:
            break
    return x, hist
