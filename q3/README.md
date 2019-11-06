# Questão 3

# 1
## Command
`-c IP_SERVIDOR`

## Response
Nesse comando iniciamos o iperf3 no modo `client` e especificamos um host através do seu hostname. No nosso caso `localhost`.

```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62417 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec  2.91 GBytes  25.0 Gbits/sec
[  8]   1.00-2.00   sec  2.95 GBytes  25.3 Gbits/sec
[  8]   2.00-3.00   sec  2.97 GBytes  25.6 Gbits/sec
[  8]   3.00-4.00   sec  2.36 GBytes  20.3 Gbits/sec
[  8]   4.00-5.00   sec  2.48 GBytes  21.4 Gbits/sec
[  8]   5.00-6.00   sec  2.85 GBytes  24.5 Gbits/sec
[  8]   6.00-7.00   sec  2.99 GBytes  25.7 Gbits/sec
[  8]   7.00-8.00   sec  2.91 GBytes  25.0 Gbits/sec
[  8]   8.00-9.00   sec  2.75 GBytes  23.6 Gbits/sec
[  8]   9.00-10.00  sec  2.94 GBytes  25.2 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  28.1 GBytes  24.2 Gbits/sec                  sender
[  8]   0.00-10.00  sec  28.1 GBytes  24.2 Gbits/sec                  receiver

iperf Done.
```

# 2

`-c IP_SERVIDOR -w 1 | 2.000 | 10.000 | 50.000 | 100.000`

## Response
Nesse comando definimos o tamanho da **window** para os dados. Podemos perceber que quanto maior a *window*, maior o a taxa de *Bitrate*.

### -w 1
```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62421 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec  35.8 KBytes   294 Kbits/sec
[  8]   1.00-2.00   sec  30.1 KBytes   247 Kbits/sec
[  8]   2.00-3.00   sec  38.4 KBytes   315 Kbits/sec
[  8]   3.00-4.00   sec  39.7 KBytes   325 Kbits/sec
[  8]   4.00-5.00   sec  40.1 KBytes   328 Kbits/sec
[  8]   5.00-6.00   sec  38.0 KBytes   311 Kbits/sec
[  8]   6.00-7.00   sec  39.9 KBytes   327 Kbits/sec
[  8]   7.00-8.00   sec  34.0 KBytes   279 Kbits/sec
[  8]   8.00-9.00   sec  39.4 KBytes   323 Kbits/sec
[  8]   9.00-10.00  sec  40.0 KBytes   328 Kbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec   375 KBytes   308 Kbits/sec                  sender
[  8]   0.00-10.00  sec   375 KBytes   308 Kbits/sec                  receiver

iperf Done.
```

### -w 2.000
```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62425 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec  83.7 KBytes   686 Kbits/sec
[  8]   1.00-2.00   sec  77.1 KBytes   632 Kbits/sec
[  8]   2.00-3.00   sec  56.7 KBytes   464 Kbits/sec
[  8]   3.00-4.00   sec  78.8 KBytes   645 Kbits/sec
[  8]   4.00-5.00   sec  78.8 KBytes   645 Kbits/sec
[  8]   5.00-6.00   sec  77.1 KBytes   631 Kbits/sec
[  8]   6.00-7.00   sec  78.2 KBytes   641 Kbits/sec
[  8]   7.00-8.00   sec  71.0 KBytes   582 Kbits/sec
[  8]   8.00-9.00   sec  68.1 KBytes   558 Kbits/sec
[  8]   9.00-10.00  sec  77.8 KBytes   637 Kbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec   747 KBytes   612 Kbits/sec                  sender
[  8]   0.00-10.00  sec   747 KBytes   612 Kbits/sec                  receiver

iperf Done.
```

### -w 10.000
```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62432 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec   367 KBytes  3.01 Mbits/sec
[  8]   1.00-2.00   sec   411 KBytes  3.37 Mbits/sec
[  8]   2.00-3.00   sec   337 KBytes  2.76 Mbits/sec
[  8]   3.00-4.00   sec   297 KBytes  2.44 Mbits/sec
[  8]   4.00-5.00   sec   394 KBytes  3.23 Mbits/sec
[  8]   5.00-6.00   sec   427 KBytes  3.50 Mbits/sec
[  8]   6.00-7.00   sec   360 KBytes  2.95 Mbits/sec
[  8]   7.00-8.00   sec   378 KBytes  3.10 Mbits/sec
[  8]   8.00-9.00   sec   409 KBytes  3.35 Mbits/sec
[  8]   9.00-10.00  sec   426 KBytes  3.49 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  3.72 MBytes  3.12 Mbits/sec                  sender
[  8]   0.00-10.01  sec  3.72 MBytes  3.12 Mbits/sec                  receiver

iperf Done.
```

### -w 50.000
```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62434 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec  1.42 MBytes  11.9 Mbits/sec
[  8]   1.00-2.00   sec  1.64 MBytes  13.8 Mbits/sec
[  8]   2.00-3.00   sec  1.90 MBytes  15.9 Mbits/sec
[  8]   3.00-4.00   sec  1.63 MBytes  13.7 Mbits/sec
[  8]   4.00-5.00   sec  1.79 MBytes  15.0 Mbits/sec
[  8]   5.00-6.00   sec  1.80 MBytes  15.1 Mbits/sec
[  8]   6.00-7.00   sec  1.93 MBytes  16.2 Mbits/sec
[  8]   7.00-8.00   sec  2.01 MBytes  16.9 Mbits/sec
[  8]   8.00-9.00   sec  1.94 MBytes  16.3 Mbits/sec
[  8]   9.00-10.00  sec  1.99 MBytes  16.7 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  18.1 MBytes  15.1 Mbits/sec                  sender
[  8]   0.00-10.01  sec  18.1 MBytes  15.1 Mbits/sec                  receiver

iperf Done.
```

### -w 100.000

```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62439 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec  2.91 MBytes  24.4 Mbits/sec
[  8]   1.00-2.00   sec  3.62 MBytes  30.4 Mbits/sec
[  8]   2.00-3.00   sec  4.21 MBytes  35.3 Mbits/sec
[  8]   3.00-4.00   sec  4.02 MBytes  33.8 Mbits/sec
[  8]   4.00-5.00   sec  4.19 MBytes  35.2 Mbits/sec
[  8]   5.00-6.00   sec  4.11 MBytes  34.5 Mbits/sec
[  8]   6.00-7.00   sec  3.85 MBytes  32.3 Mbits/sec
[  8]   7.00-8.00   sec  3.50 MBytes  29.4 Mbits/sec
[  8]   8.00-9.00   sec  3.98 MBytes  33.4 Mbits/sec
[  8]   9.00-10.00  sec  2.72 MBytes  22.8 Mbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  37.1 MBytes  31.1 Mbits/sec                  sender
[  8]   0.00-10.00  sec  37.1 MBytes  31.1 Mbits/sec                  receiver

iperf Done.
```

# 3
## Command
`-c IP_SERVIDOR -M 100 | 250 | 500 | 1000 | 1500`

## Response
Esse comando configura o *Maximum Segment Size*, que é a especificação a quantidade máxima de dado que um computador pode receber em um único segmento TCP.

### -M 100
```sh
Connecting to host localhost, port 5201
[  4] local 127.0.0.1 port 38012 connected to 127.0.0.1 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  4]   0.00-1.00   sec  4.87 GBytes  41.9 Gbits/sec    0    312 KBytes       
[  4]   1.00-2.00   sec  4.63 GBytes  39.7 Gbits/sec    0    312 KBytes       
[  4]   2.00-3.00   sec  4.14 GBytes  35.5 Gbits/sec    0    705 KBytes       
[  4]   3.00-4.00   sec  3.04 GBytes  26.1 Gbits/sec    0    804 KBytes       
[  4]   4.00-5.00   sec  4.18 GBytes  35.9 Gbits/sec    0    804 KBytes       
[  4]   5.00-6.00   sec  3.06 GBytes  26.3 Gbits/sec    0    804 KBytes       
[  4]   6.00-7.00   sec  3.31 GBytes  28.4 Gbits/sec    0    804 KBytes       
[  4]   7.00-8.00   sec  3.38 GBytes  29.0 Gbits/sec    0    804 KBytes       
[  4]   8.00-9.00   sec  3.11 GBytes  26.7 Gbits/sec    0    804 KBytes       
[  4]   9.00-10.00  sec  3.41 GBytes  29.3 Gbits/sec    0    804 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-10.00  sec  37.1 GBytes  31.9 Gbits/sec    0             sender
[  4]   0.00-10.00  sec  37.1 GBytes  31.9 Gbits/sec                  receiver

iperf Done.
```

### -M 250

```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 51132 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec  2.90 GBytes  24.9 Gbits/sec
[  8]   1.00-2.00   sec  2.81 GBytes  24.2 Gbits/sec
[  8]   2.00-3.00   sec  1.26 GBytes  10.8 Gbits/sec
[  8]   3.00-4.00   sec  1.86 GBytes  16.0 Gbits/sec
[  8]   4.00-5.00   sec  2.79 GBytes  24.0 Gbits/sec
[  8]   5.00-6.00   sec  3.16 GBytes  27.2 Gbits/sec
[  8]   6.00-7.00   sec  2.66 GBytes  22.8 Gbits/sec
[  8]   7.00-8.00   sec  3.05 GBytes  26.2 Gbits/sec
[  8]   8.00-9.00   sec  3.05 GBytes  26.2 Gbits/sec
[  8]   9.00-10.00  sec  3.03 GBytes  26.0 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  26.6 GBytes  22.8 Gbits/sec                  sender
[  8]   0.00-10.00  sec  26.6 GBytes  22.8 Gbits/sec                  receiver

iperf Done.
```
### -M 500
```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 51135 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.03   sec  1.54 GBytes  12.8 Gbits/sec
[  8]   1.03-2.00   sec  1.13 GBytes  10.0 Gbits/sec
[  8]   2.00-3.00   sec  2.33 GBytes  20.1 Gbits/sec
[  8]   3.00-4.00   sec  2.91 GBytes  25.0 Gbits/sec
[  8]   4.00-5.00   sec  2.12 GBytes  18.2 Gbits/sec
[  8]   5.00-6.00   sec  2.42 GBytes  20.8 Gbits/sec
[  8]   6.00-7.00   sec  2.79 GBytes  24.0 Gbits/sec
[  8]   7.00-8.00   sec  2.62 GBytes  22.4 Gbits/sec
[  8]   8.00-9.00   sec  1.82 GBytes  15.7 Gbits/sec
[  8]   9.00-10.00  sec  2.79 GBytes  23.9 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  22.5 GBytes  19.3 Gbits/sec                  sender
[  8]   0.00-10.00  sec  22.5 GBytes  19.3 Gbits/sec                  receiver

iperf Done.
```

### -M 1000

```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 51139 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec  1.83 GBytes  15.7 Gbits/sec
[  8]   1.00-2.00   sec  2.84 GBytes  24.4 Gbits/sec
[  8]   2.00-3.00   sec  2.19 GBytes  18.8 Gbits/sec
[  8]   3.00-4.01   sec  1.66 GBytes  14.3 Gbits/sec
[  8]   4.01-5.00   sec  1.27 GBytes  11.0 Gbits/sec
[  8]   5.00-6.01   sec  1.70 GBytes  14.4 Gbits/sec
[  8]   6.01-7.00   sec  1.07 GBytes  9.30 Gbits/sec
[  8]   7.00-8.00   sec  1.38 GBytes  11.8 Gbits/sec
[  8]   8.00-9.00   sec  2.46 GBytes  21.1 Gbits/sec
[  8]   9.00-10.00  sec  1.41 GBytes  12.1 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  17.8 GBytes  15.3 Gbits/sec                  sender
[  8]   0.00-10.00  sec  17.8 GBytes  15.3 Gbits/sec                  receiver

iperf Done.
```

### -M 1500
```sh
Connecting to host localhost, port 5201
[  4] local 127.0.0.1 port 38050 connected to 127.0.0.1 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  4]   0.00-1.00   sec  3.26 GBytes  28.0 Gbits/sec    0    501 KBytes       
[  4]   1.00-2.00   sec  3.22 GBytes  27.7 Gbits/sec    0    612 KBytes       
[  4]   2.00-3.00   sec  4.47 GBytes  38.4 Gbits/sec    0    658 KBytes       
[  4]   3.00-4.00   sec  4.48 GBytes  38.5 Gbits/sec    0    658 KBytes       
[  4]   4.00-5.00   sec  4.53 GBytes  38.9 Gbits/sec    0    658 KBytes       
[  4]   5.00-6.00   sec  4.43 GBytes  38.1 Gbits/sec    0    695 KBytes       
[  4]   6.00-7.00   sec  2.82 GBytes  24.3 Gbits/sec    0   2.01 MBytes       
[  4]   7.00-8.00   sec  2.99 GBytes  25.7 Gbits/sec    0   2.12 MBytes       
[  4]   8.00-9.00   sec  3.04 GBytes  26.1 Gbits/sec   86   1.48 MBytes       
[  4]   9.00-10.00  sec  2.99 GBytes  25.7 Gbits/sec    0   1.48 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-10.00  sec  36.2 GBytes  31.1 Gbits/sec   86             sender
[  4]   0.00-10.00  sec  36.2 GBytes  31.1 Gbits/sec                  receiver

iperf Done.
```

# 4

## Command
`-s -c IP_SERVIDOR -P 1 | 2 | 4 | 8`

## Response
Nesse comando definimos o número de clientes paralelos que irão rodar.

### -P 1
```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62514 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec  2.85 GBytes  24.5 Gbits/sec
[  8]   1.00-2.00   sec  2.84 GBytes  24.4 Gbits/sec
[  8]   2.00-3.00   sec  2.47 GBytes  21.2 Gbits/sec
[  8]   3.00-4.00   sec  1.55 GBytes  13.4 Gbits/sec
[  8]   4.00-5.00   sec  1.96 GBytes  16.8 Gbits/sec
[  8]   5.00-6.00   sec  1.88 GBytes  16.1 Gbits/sec
[  8]   6.00-7.00   sec  2.88 GBytes  24.7 Gbits/sec
[  8]   7.00-8.00   sec  2.75 GBytes  23.6 Gbits/sec
[  8]   8.00-9.00   sec  2.47 GBytes  21.3 Gbits/sec
[  8]   9.00-10.00  sec  2.94 GBytes  25.3 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  24.6 GBytes  21.1 Gbits/sec                  sender
[  8]   0.00-10.00  sec  24.6 GBytes  21.1 Gbits/sec                  receiver

iperf Done.
```

### -P 2
```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62521 connected to ::1 port 5201
[ 10] local ::1 port 62522 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec  1.93 GBytes  16.6 Gbits/sec
[ 10]   0.00-1.00   sec   941 MBytes  7.89 Gbits/sec
[SUM]   0.00-1.00   sec  2.85 GBytes  24.5 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   1.00-2.00   sec  1.88 GBytes  16.1 Gbits/sec
[ 10]   1.00-2.00   sec  1.12 GBytes  9.58 Gbits/sec
[SUM]   1.00-2.00   sec  2.99 GBytes  25.7 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   2.00-3.00   sec  1.72 GBytes  14.8 Gbits/sec
[ 10]   2.00-3.00   sec  1.12 GBytes  9.65 Gbits/sec
[SUM]   2.00-3.00   sec  2.84 GBytes  24.4 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   3.00-4.00   sec  1.91 GBytes  16.4 Gbits/sec
[ 10]   3.00-4.00   sec  1.10 GBytes  9.47 Gbits/sec
[SUM]   3.00-4.00   sec  3.01 GBytes  25.8 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   4.00-5.00   sec  1.90 GBytes  16.4 Gbits/sec
[ 10]   4.00-5.00   sec  1.13 GBytes  9.71 Gbits/sec
[SUM]   4.00-5.00   sec  3.03 GBytes  26.1 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   5.00-6.00   sec  1.75 GBytes  15.1 Gbits/sec
[ 10]   5.00-6.00   sec  1.27 GBytes  10.9 Gbits/sec
[SUM]   5.00-6.00   sec  3.02 GBytes  26.0 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   6.00-7.00   sec  1.58 GBytes  13.6 Gbits/sec
[ 10]   6.00-7.00   sec  1.42 GBytes  12.2 Gbits/sec
[SUM]   6.00-7.00   sec  3.00 GBytes  25.8 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   7.00-8.00   sec  1.56 GBytes  13.4 Gbits/sec
[ 10]   7.00-8.00   sec  1.54 GBytes  13.2 Gbits/sec
[SUM]   7.00-8.00   sec  3.09 GBytes  26.5 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   8.00-9.00   sec  1.53 GBytes  13.1 Gbits/sec
[ 10]   8.00-9.00   sec  1.51 GBytes  13.0 Gbits/sec
[SUM]   8.00-9.00   sec  3.04 GBytes  26.1 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   9.00-10.00  sec  1.26 GBytes  10.8 Gbits/sec
[ 10]   9.00-10.00  sec  1.25 GBytes  10.8 Gbits/sec
[SUM]   9.00-10.00  sec  2.51 GBytes  21.6 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  17.0 GBytes  14.6 Gbits/sec                  sender
[  8]   0.00-10.00  sec  17.0 GBytes  14.6 Gbits/sec                  receiver
[ 10]   0.00-10.00  sec  12.4 GBytes  10.6 Gbits/sec                  sender
[ 10]   0.00-10.00  sec  12.4 GBytes  10.6 Gbits/sec                  receiver
[SUM]   0.00-10.00  sec  29.4 GBytes  25.3 Gbits/sec                  sender
[SUM]   0.00-10.00  sec  29.4 GBytes  25.3 Gbits/sec                  receiver

iperf Done.
```

### -P 4
```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62525 connected to ::1 port 5201
[ 10] local ::1 port 62526 connected to ::1 port 5201
[ 14] local ::1 port 62527 connected to ::1 port 5201
[ 16] local ::1 port 62528 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec   457 MBytes  3.82 Gbits/sec
[ 10]   0.00-1.00   sec   273 MBytes  2.28 Gbits/sec
[ 14]   0.00-1.00   sec   455 MBytes  3.81 Gbits/sec
[ 16]   0.00-1.00   sec   477 MBytes  4.00 Gbits/sec
[SUM]   0.00-1.00   sec  1.62 GBytes  13.9 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   1.00-2.00   sec   373 MBytes  3.13 Gbits/sec
[ 10]   1.00-2.00   sec  68.3 MBytes   573 Mbits/sec
[ 14]   1.00-2.00   sec   374 MBytes  3.14 Gbits/sec
[ 16]   1.00-2.00   sec   408 MBytes  3.43 Gbits/sec
[SUM]   1.00-2.00   sec  1.19 GBytes  10.3 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   2.00-3.00   sec   585 MBytes  4.90 Gbits/sec
[ 10]   2.00-3.00   sec  72.0 MBytes   603 Mbits/sec
[ 14]   2.00-3.00   sec   583 MBytes  4.89 Gbits/sec
[ 16]   2.00-3.00   sec   662 MBytes  5.54 Gbits/sec
[SUM]   2.00-3.00   sec  1.86 GBytes  15.9 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   3.00-4.03   sec   373 MBytes  3.05 Gbits/sec
[ 10]   3.00-4.03   sec  91.3 MBytes   747 Mbits/sec
[ 14]   3.00-4.03   sec   375 MBytes  3.07 Gbits/sec
[ 16]   3.00-4.03   sec   379 MBytes  3.10 Gbits/sec
[SUM]   3.00-4.03   sec  1.19 GBytes  9.97 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   4.03-5.00   sec   421 MBytes  3.62 Gbits/sec
[ 10]   4.03-5.00   sec   305 MBytes  2.62 Gbits/sec
[ 14]   4.03-5.00   sec   443 MBytes  3.81 Gbits/sec
[ 16]   4.03-5.00   sec   543 MBytes  4.67 Gbits/sec
[SUM]   4.03-5.00   sec  1.67 GBytes  14.7 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   5.00-6.00   sec   546 MBytes  4.59 Gbits/sec
[ 10]   5.00-6.00   sec   469 MBytes  3.94 Gbits/sec
[ 14]   5.00-6.00   sec   550 MBytes  4.62 Gbits/sec
[ 16]   5.00-6.00   sec   718 MBytes  6.03 Gbits/sec
[SUM]   5.00-6.00   sec  2.23 GBytes  19.2 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   6.00-7.00   sec   654 MBytes  5.48 Gbits/sec
[ 10]   6.00-7.00   sec   670 MBytes  5.61 Gbits/sec
[ 14]   6.00-7.00   sec   701 MBytes  5.88 Gbits/sec
[ 16]   6.00-7.00   sec   871 MBytes  7.30 Gbits/sec
[SUM]   6.00-7.00   sec  2.83 GBytes  24.3 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   7.00-8.00   sec   615 MBytes  5.17 Gbits/sec
[ 10]   7.00-8.00   sec   646 MBytes  5.43 Gbits/sec
[ 14]   7.00-8.00   sec   626 MBytes  5.26 Gbits/sec
[ 16]   7.00-8.00   sec   637 MBytes  5.35 Gbits/sec
[SUM]   7.00-8.00   sec  2.47 GBytes  21.2 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   8.00-9.00   sec   291 MBytes  2.44 Gbits/sec
[ 10]   8.00-9.00   sec   290 MBytes  2.43 Gbits/sec
[ 14]   8.00-9.00   sec   290 MBytes  2.43 Gbits/sec
[ 16]   8.00-9.00   sec   289 MBytes  2.42 Gbits/sec
[SUM]   8.00-9.00   sec  1.13 GBytes  9.73 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   9.00-10.00  sec   330 MBytes  2.75 Gbits/sec
[ 10]   9.00-10.00  sec   330 MBytes  2.76 Gbits/sec
[ 14]   9.00-10.00  sec   330 MBytes  2.76 Gbits/sec
[ 16]   9.00-10.00  sec   330 MBytes  2.76 Gbits/sec
[SUM]   9.00-10.00  sec  1.29 GBytes  11.0 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  4.53 GBytes  3.89 Gbits/sec                  sender
[  8]   0.00-10.01  sec  4.53 GBytes  3.89 Gbits/sec                  receiver
[ 10]   0.00-10.00  sec  3.14 GBytes  2.69 Gbits/sec                  sender
[ 10]   0.00-10.01  sec  3.14 GBytes  2.69 Gbits/sec                  receiver
[ 14]   0.00-10.00  sec  4.62 GBytes  3.96 Gbits/sec                  sender
[ 14]   0.00-10.01  sec  4.62 GBytes  3.96 Gbits/sec                  receiver
[ 16]   0.00-10.00  sec  5.19 GBytes  4.46 Gbits/sec                  sender
[ 16]   0.00-10.01  sec  5.19 GBytes  4.45 Gbits/sec                  receiver
[SUM]   0.00-10.00  sec  17.5 GBytes  15.0 Gbits/sec                  sender
[SUM]   0.00-10.01  sec  17.5 GBytes  15.0 Gbits/sec                  receiver

iperf Done.
```

### -P 8
```sh
Connecting to host localhost, port 5201
[  8] local ::1 port 62531 connected to ::1 port 5201
[ 10] local ::1 port 62532 connected to ::1 port 5201
[ 14] local ::1 port 62533 connected to ::1 port 5201
[ 16] local ::1 port 62534 connected to ::1 port 5201
[ 18] local ::1 port 62535 connected to ::1 port 5201
[ 20] local ::1 port 62536 connected to ::1 port 5201
[ 22] local ::1 port 62537 connected to ::1 port 5201
[ 24] local ::1 port 62538 connected to ::1 port 5201
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-1.00   sec   360 MBytes  3.01 Gbits/sec
[ 10]   0.00-1.00   sec   358 MBytes  3.00 Gbits/sec
[ 14]   0.00-1.00   sec   354 MBytes  2.97 Gbits/sec
[ 16]   0.00-1.00   sec   355 MBytes  2.97 Gbits/sec
[ 18]   0.00-1.00   sec   351 MBytes  2.94 Gbits/sec
[ 20]   0.00-1.00   sec   354 MBytes  2.96 Gbits/sec
[ 22]   0.00-1.00   sec   358 MBytes  2.99 Gbits/sec
[ 24]   0.00-1.00   sec   357 MBytes  2.99 Gbits/sec
[SUM]   0.00-1.00   sec  2.78 GBytes  23.8 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   1.00-2.00   sec   369 MBytes  3.10 Gbits/sec
[ 10]   1.00-2.00   sec   367 MBytes  3.08 Gbits/sec
[ 14]   1.00-2.00   sec   364 MBytes  3.06 Gbits/sec
[ 16]   1.00-2.00   sec   366 MBytes  3.07 Gbits/sec
[ 18]   1.00-2.00   sec   364 MBytes  3.05 Gbits/sec
[ 20]   1.00-2.00   sec   362 MBytes  3.04 Gbits/sec
[ 22]   1.00-2.00   sec   362 MBytes  3.04 Gbits/sec
[ 24]   1.00-2.00   sec   360 MBytes  3.02 Gbits/sec
[SUM]   1.00-2.00   sec  2.85 GBytes  24.5 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   2.00-3.00   sec   367 MBytes  3.09 Gbits/sec
[ 10]   2.00-3.00   sec   364 MBytes  3.05 Gbits/sec
[ 14]   2.00-3.00   sec   366 MBytes  3.08 Gbits/sec
[ 16]   2.00-3.00   sec   289 MBytes  2.42 Gbits/sec
[ 18]   2.00-3.00   sec   365 MBytes  3.06 Gbits/sec
[ 20]   2.00-3.00   sec   362 MBytes  3.04 Gbits/sec
[ 22]   2.00-3.00   sec   361 MBytes  3.03 Gbits/sec
[ 24]   2.00-3.00   sec   358 MBytes  3.01 Gbits/sec
[SUM]   2.00-3.00   sec  2.77 GBytes  23.8 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   3.00-4.00   sec   379 MBytes  3.18 Gbits/sec
[ 10]   3.00-4.00   sec   374 MBytes  3.14 Gbits/sec
[ 14]   3.00-4.00   sec   375 MBytes  3.14 Gbits/sec
[ 16]   3.00-4.00   sec   264 MBytes  2.22 Gbits/sec
[ 18]   3.00-4.00   sec   378 MBytes  3.17 Gbits/sec
[ 20]   3.00-4.00   sec   376 MBytes  3.15 Gbits/sec
[ 22]   3.00-4.00   sec   378 MBytes  3.17 Gbits/sec
[ 24]   3.00-4.00   sec   377 MBytes  3.17 Gbits/sec
[SUM]   3.00-4.00   sec  2.83 GBytes  24.3 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   4.00-5.00   sec   393 MBytes  3.29 Gbits/sec
[ 10]   4.00-5.00   sec   389 MBytes  3.26 Gbits/sec
[ 14]   4.00-5.00   sec   385 MBytes  3.23 Gbits/sec
[ 16]   4.00-5.00   sec   259 MBytes  2.17 Gbits/sec
[ 18]   4.00-5.00   sec   388 MBytes  3.26 Gbits/sec
[ 20]   4.00-5.00   sec   387 MBytes  3.24 Gbits/sec
[ 22]   4.00-5.00   sec   387 MBytes  3.24 Gbits/sec
[ 24]   4.00-5.00   sec   384 MBytes  3.22 Gbits/sec
[SUM]   4.00-5.00   sec  2.90 GBytes  24.9 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   5.00-6.00   sec   376 MBytes  3.16 Gbits/sec
[ 10]   5.00-6.00   sec   379 MBytes  3.18 Gbits/sec
[ 14]   5.00-6.00   sec   374 MBytes  3.14 Gbits/sec
[ 16]   5.00-6.00   sec   265 MBytes  2.22 Gbits/sec
[ 18]   5.00-6.00   sec   378 MBytes  3.18 Gbits/sec
[ 20]   5.00-6.00   sec   375 MBytes  3.15 Gbits/sec
[ 22]   5.00-6.00   sec   372 MBytes  3.12 Gbits/sec
[ 24]   5.00-6.00   sec   375 MBytes  3.15 Gbits/sec
[SUM]   5.00-6.00   sec  2.83 GBytes  24.3 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   6.00-7.00   sec   390 MBytes  3.26 Gbits/sec
[ 10]   6.00-7.00   sec   390 MBytes  3.26 Gbits/sec
[ 14]   6.00-7.00   sec   389 MBytes  3.25 Gbits/sec
[ 16]   6.00-7.00   sec   274 MBytes  2.29 Gbits/sec
[ 18]   6.00-7.00   sec   388 MBytes  3.24 Gbits/sec
[ 20]   6.00-7.00   sec   387 MBytes  3.23 Gbits/sec
[ 22]   6.00-7.00   sec   386 MBytes  3.22 Gbits/sec
[ 24]   6.00-7.00   sec   377 MBytes  3.15 Gbits/sec
[SUM]   6.00-7.00   sec  2.91 GBytes  24.9 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   7.00-8.00   sec   375 MBytes  3.15 Gbits/sec
[ 10]   7.00-8.00   sec   375 MBytes  3.15 Gbits/sec
[ 14]   7.00-8.00   sec   375 MBytes  3.14 Gbits/sec
[ 16]   7.00-8.00   sec   315 MBytes  2.65 Gbits/sec
[ 18]   7.00-8.00   sec   373 MBytes  3.13 Gbits/sec
[ 20]   7.00-8.00   sec   372 MBytes  3.12 Gbits/sec
[ 22]   7.00-8.00   sec   369 MBytes  3.10 Gbits/sec
[ 24]   7.00-8.00   sec   367 MBytes  3.08 Gbits/sec
[SUM]   7.00-8.00   sec  2.85 GBytes  24.5 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   8.00-9.00   sec   376 MBytes  3.16 Gbits/sec
[ 10]   8.00-9.00   sec   375 MBytes  3.15 Gbits/sec
[ 14]   8.00-9.00   sec   374 MBytes  3.14 Gbits/sec
[ 16]   8.00-9.00   sec   347 MBytes  2.92 Gbits/sec
[ 18]   8.00-9.00   sec   371 MBytes  3.11 Gbits/sec
[ 20]   8.00-9.00   sec   371 MBytes  3.12 Gbits/sec
[ 22]   8.00-9.00   sec   365 MBytes  3.07 Gbits/sec
[ 24]   8.00-9.00   sec   369 MBytes  3.10 Gbits/sec
[SUM]   8.00-9.00   sec  2.88 GBytes  24.8 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[  8]   9.00-10.00  sec   369 MBytes  3.10 Gbits/sec
[ 10]   9.00-10.00  sec   371 MBytes  3.11 Gbits/sec
[ 14]   9.00-10.00  sec   370 MBytes  3.10 Gbits/sec
[ 16]   9.00-10.00  sec   365 MBytes  3.06 Gbits/sec
[ 18]   9.00-10.00  sec   368 MBytes  3.09 Gbits/sec
[ 20]   9.00-10.00  sec   369 MBytes  3.10 Gbits/sec
[ 22]   9.00-10.00  sec   368 MBytes  3.09 Gbits/sec
[ 24]   9.00-10.00  sec   369 MBytes  3.10 Gbits/sec
[SUM]   9.00-10.00  sec  2.88 GBytes  24.7 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec  3.67 GBytes  3.15 Gbits/sec                  sender
[  8]   0.00-10.01  sec  3.67 GBytes  3.15 Gbits/sec                  receiver
[ 10]   0.00-10.00  sec  3.65 GBytes  3.14 Gbits/sec                  sender
[ 10]   0.00-10.01  sec  3.65 GBytes  3.14 Gbits/sec                  receiver
[ 14]   0.00-10.00  sec  3.64 GBytes  3.13 Gbits/sec                  sender
[ 14]   0.00-10.01  sec  3.64 GBytes  3.12 Gbits/sec                  receiver
[ 16]   0.00-10.00  sec  3.03 GBytes  2.60 Gbits/sec                  sender
[ 16]   0.00-10.01  sec  3.03 GBytes  2.60 Gbits/sec                  receiver
[ 18]   0.00-10.00  sec  3.64 GBytes  3.12 Gbits/sec                  sender
[ 18]   0.00-10.01  sec  3.64 GBytes  3.12 Gbits/sec                  receiver
[ 20]   0.00-10.00  sec  3.63 GBytes  3.12 Gbits/sec                  sender
[ 20]   0.00-10.01  sec  3.63 GBytes  3.11 Gbits/sec                  receiver
[ 22]   0.00-10.00  sec  3.62 GBytes  3.11 Gbits/sec                  sender
[ 22]   0.00-10.01  sec  3.62 GBytes  3.11 Gbits/sec                  receiver
[ 24]   0.00-10.00  sec  3.61 GBytes  3.10 Gbits/sec                  sender
[ 24]   0.00-10.01  sec  3.61 GBytes  3.09 Gbits/sec                  receiver
[SUM]   0.00-10.00  sec  28.5 GBytes  24.5 Gbits/sec                  sender
[SUM]   0.00-10.01  sec  28.5 GBytes  24.4 Gbits/sec                  receiver

iperf Done.
```