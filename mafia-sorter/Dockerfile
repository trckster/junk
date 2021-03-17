FROM golang

WORKDIR /mafia

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o mafia main.go

CMD ["./mafia"]