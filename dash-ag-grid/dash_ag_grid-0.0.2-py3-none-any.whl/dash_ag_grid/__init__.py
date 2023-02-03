raise Exception("""

    Thank you for your interest in Dash AG Grid open source!
    The 1.x series of this package is commercially distributed on
    instances of Dash Enterprise https://plotly.com/dash/.

    You have installed a non-functional stub version of the package.
    This probably means you ran `pip install dash-ag-grid` and we
    haven't yet released the final v2.0.0 open-source version.

    To install an alpha release, you need to specify the version
    exactly, for example `pip install dash-ag-grid==2.0.0a1`
    See https://pypi.org/project/dash-ag-grid/#history
    for the list of available versions.

    !! Be aware there will likely be breaking changes before the
    final v2.0.0 open-source release.

    If you are a Dash Enterprise customer and you want to continue
    using the v1.x series, please ensure you've installed dash-ag-grid
    with the `--extra-index-url` argument, either in your requirements.txt
    file or in the command line, so that the package is installed from
    Dash Enterprise's private, commercial package repository instead of from
    pypi.org. Visit the docs for your Dash Enterprise installation at:
    https://<your-dash-enterprise-instance>/Docs
    for details.

""")
