FROM rustlang/rust:nightly

WORKDIR /app
COPY rust-rocket .
RUN cargo install --path .

ENV ROCKET_PORT=80
ENV ROCKET_ADDRESS=0.0.0.0

CMD ["rust-rocket"]