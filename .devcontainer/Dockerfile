FROM ubuntu:22.04

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates \
    && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    tzdata \
    && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && echo 'Asia/Tokyo' >/etc/timezone

RUN apt-get update \
    && apt-get install -y \
    git vim bash-completion rsync wget curl \
    && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN groupadd --gid 1000 vscode \
    && useradd --uid 1000 --gid 1000 -m vscode

RUN apt-get update \
    && apt-get install -y \
    build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev libgdbm-dev libbz2-dev liblzma-dev zlib1g-dev uuid-dev libffi-dev libdb-dev tk-dev \
    && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
    && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | tee /etc/apt/sources.list.d/ngrok.list \
    && apt update \
    && apt install ngrok \
    && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

USER vscode
ENV HOME /home/vscode

ENV PYTHON_VERSION 3.10.2
ENV PYTHON_ROOT $HOME/local/python-$PYTHON_VERSION
ENV PATH $PYTHON_ROOT/bin:$HOME/.poetry/bin:$PATH

RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv \
    && cd ~/.pyenv/plugins/python-build \
    && PREFIX=~/local ./install.sh \
    && ~/local/bin/python-build -v ${PYTHON_VERSION} ~/local/python-${PYTHON_VERSION}

ENV PATH "$PATH:/home/vscode/local/python-${PYTHON_VERSION}/bin"

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "$PATH:/home/vscode/.local/bin"
RUN source ~/.bashrc && mkdir -p ~/.local/share/bash-completion/ \
    && poetry completions bash > ~/.local/share/bash-completion/poetry.bash-completion

RUN poetry config virtualenvs.in-project true
