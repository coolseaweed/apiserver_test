## K6 + Prometheus + Grafana test env setup.


## Env. setup
```bash
docker-compose up -d
```

## Run test

```yaml
version: '3.9'

services:

  k6:
    image: loadimpact/k6:0.42.0
    # ports:
    #   - "6565:6565"
    environment:
      - K6_PROMETHEUS_RW_SERVER_URL=http://prometheus:9090/api/v1/write
      - K6_PROMETHEUS_RW_TREND_AS_NATIVE_HISTOGRAM=true
    volumes:
      - ./scripts:/scripts/

    command: "run /scripts/test_grpc.js -o experimental-prometheus-rw" # << change script file based on protocols

```

```bash
docker-compose -f docker-compose-test.yaml up

```

## Monitor via Grafana
Check Grafana via port `3000` (default).   
![grafana image](/asset/grafana.png)

Get [dashboard template of k6+prometheus](https://grafana.com/grafana/dashboards/18030-official-k6-test-result/) and apply through:

`Home > Dashboards > Import dashboard > Import via grafana.com`

