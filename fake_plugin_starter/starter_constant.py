from kedro.framework.cli.starters import KedroStarterSpec

starters = [
    KedroStarterSpec(
        "test_plugin_starter",
        "https://github.com/kedro-org/kedro-starters/",
        "pandas-iris",
    ),
    KedroStarterSpec(
        "test_plugin_starter", "https://github.com/kedro-org/kedro-starters/"
    ),
]


[
    KedroStarterSpec(
        name="astro-airflow-iris",
        template_path="git+https://github.com/kedro-org/kedro-starters.git",
        directory=None,

    ),
    KedroStarterSpec(
        name="astro-iris",
        template_path="git+https://github.com/kedro-org/kedro-starters.git",
        directory="astro-airflow-iris",
    ),
]
