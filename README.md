[![Build Status][build_status_badge]][build_status_link]


## dash_ci_example

Initial effort to use gitHUB actions CI/UI workflow working on a Dash project.

### Objectives

* Use pytest and standard [dash_duo] test harness.
* Create GH [action.yaml] that creates headless test environment.
* Use snapshots and [Percy].

[dash_duo]: https://dash.plotly.com/testing
[action.yaml]: https://github.blog/2022-06-03-a-beginners-guide-to-ci-cd-and-automation-on-github/
[Percy]: https://percy.io/

### Usage

    pip install -r requirements.txt
    python usage.py

### Testing

    pytest

### Links

* [GitHub Actions]
  * [Adding a workflow status badge]

[GitHub Actions]: https://docs.github.com/en/actions
[Adding a workflow status badge]: https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge
[build_status_badge]: https://github.com/stevej2608/dash_ci_example/actions/workflows/test.yml/badge.svg
[build_status_link]: https://github.com/stevej2608/dash_ci_example/actions/workflows/test.yml