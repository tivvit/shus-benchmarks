FROM golang:1.17

WORKDIR /app
ADD go-http/main.go /app/
ADD go-shush go-shush/

RUN go mod init github.com/tivvit/shush
RUN go mod tidy
RUN go get .
RUN go build -o main main.go

CMD ["./main"]