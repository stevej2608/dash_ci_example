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