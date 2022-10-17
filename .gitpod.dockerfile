FROM gitpod/workspace-full-vnc

RUN sudo apt-get update \
 && curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - \
 && sudo apt-get install -y nodejs \
 && corepack enable \
 && sudo apt-get update \
 && sudo apt-get install -y \
  libasound2-dev \
  libgtk-3-dev \
  libnss3-dev \
 && sudo apt-get install fonts-noto-color-emoji -y \
 && sudo apt-get upgrade -y --allow-downgrades \
 && curl https://sh.rustup.rs -sSf | sudo sh -s -- --default-toolchain stable -y
