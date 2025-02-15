import nox
from pathlib import Path


@nox.session(python=["3.12"])
def test(session):
    session.install(".[dev]")
    try:
        session.run("coverage", "run", "-m", "pytest", *session.posargs)
    finally:
        session.notify("coverage")


@nox.session
def coverage(session):
    session.install("coverage[toml]")
    if any(Path().glob(".coverage.*")):
        session.run("coverage", "combine", "--omit", "tests/*")
    session.run("coverage", "report")


@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", ".")


@nox.session
def coverage_html(session):
    session.install("coverage[toml]")
    session.run("coverage", "html")
