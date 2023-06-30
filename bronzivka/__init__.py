from pathlib import Path
from sphinx.application import Sphinx

from importlib.metadata import version

__version__ = version(__package__)


def get_html_theme_path():
    """Return list of HTML theme paths."""
    parent = Path(__file__).parent.resolve()
    theme_path = parent / "theme"
    return theme_path


def setup(app: Sphinx):
    # Register theme
    theme_dir = get_html_theme_path()

    app.add_html_theme("bronzivka", theme_dir)
    app.setup_extension("sphinx_copybutton")
    app.setup_extension("sphinx.ext.autodoc")
    app.setup_extension("sphinx.ext.napoleon")
    app.setup_extension("sphinx.ext.autosummary")
    app.setup_extension("sphinx_design")
    app.setup_extension("myst_nb")

    app.config["exclude_patterns"].append("_build")
    app.config["exclude_patterns"].append("**/.ipynb_checkpoints")
    app.config["source_suffix"].update(
        {
            ".rst": "restructuredtext",
            ".ipynb": "myst-nb",
            ".myst": "myst-nb",
        }
    )
    app.add_css_file(str(theme_dir / "bronzivka.css"))

    # other options
    app.config["nb_render_image_options"] = {"align": "center"}

    app.config.templates_path.append(str(theme_dir))

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
