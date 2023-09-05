# Build the k6 binary with the extension
FROM golang:1.17-alpine as builder
WORKDIR "$GOPATH"/src/go.k6.io/k6
COPY . .
RUN apk --no-cache add git &&\
    go install -trimpath go.k6.io/xk6/cmd/xk6@latest &&\
    xk6 build --with github.com/grafana/xk6-output-prometheus-remote@latest &&\
    cp k6 "$GOPATH"/bin/k6
# Use the operator's base image and override the k6 binary
FROM grafana/k6:latest
COPY --from=builder /k6 /usr/bin/k6