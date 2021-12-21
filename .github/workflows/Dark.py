name: MrDarkPrince

on: [push, pull_request]

jobs:
  PEP8:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v1
        with:
          python-version: 3.9

      - name: Install Python lint libraries
        run: |
          pip install autopep8 autoflake isort black
      - name: Check for showstoppers
        run: |
          autopep8 --verbose --in-place --recursive --aggressive --aggressive --ignore=W605. *.py
      - name: Remove unused imports and variables
        run: |
          autoflake --in-place --recursive --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports .
      - name: lint with isort and black
        run: |
          isort .
          black .
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: '`🥳EvaMaria🍀`'
          commit_options: '--no-verify'
          repository: .
          commit_user_name: Mr-Dark-Prince
          commit_user_email: 73339924+Mr-Dark-Prince@users.noreply.github.com
          commit_author: Mr-Dark-Prince <73339924+Mr-Dark-Prince@users.noreply.github.com>
