FROM golang:1.13

WORKDIR /app
ADD go.mod /
ADD go-http/main.go /app/
ADD go-shus /go-shus/

RUN go build -o main main.go

CMD ["./main"]